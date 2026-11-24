# H01 — đối chiếu Fastboot getvar/device-info với GPT, CONFIG và DEVINFO

**Nguồn:** [Nhật ký H01, H101–H105, 11/11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Trạng thái: quan sát trên thiết bị ở mốc còn locked, chưa phải kết quả unlock sau ngày 18/11.**

## Fastboot được ghi ở phiên ban đầu

| Trường | Dữ liệu nguồn | Diễn giải |
| --- | --- | --- |
| `version` | `0.5` | Phiên bản giao thức báo |
| `variant` | `MTP eMMC` | Hình thái thiết bị |
| `product` | `MSM8909` | SoC |
| `kernel` | `lk` | Bootloader |
| `unlocked` | `no` | **Chưa mở khóa main** |
| `secure` | `no` | **Không chứng minh fuses Secure Boot đã tắt** |
| `max-download-size` | `0x0FA00000` (**250 MiB**) | Giới hạn tải do Fastboot công bố |
| `get_unlock_ability` | `1` | **Được phép yêu cầu**, không phải unlocked |
| `Device critical unlocked` | `true` | Trạng thái riêng, **không tương đương main unlocked** |
| `Device tampered` | `false` | Cờ báo lúc đó |
| `Charger screen enabled` | `true` | Cờ giao diện sạc |

Trong `getvar all`, bootloader công bố đúng **42 giá trị partition-size** tương ứng 42 entry GPT. Chỉ ba partition-type `userdata`, `cache`, `system` được in rõ là ext4; 39 trường type để trống **không nghĩa các phân vùng đó không tồn tại**.

## CONFIG và DEVINFO — hai vai trò khác nhau

- `config` thuộc Persistent Data Block/FRP: Android 8.1 dùng vùng cuối cho **cờ cho phép OEM unlock** và digest nội bộ. ABOOT đọc bit liên quan để trả `get_unlock_ability`.
- `devinfo` chứa thông tin trạng thái device unlocked, tampered, critical unlocked và cờ charger. **Chúng là những trường khác biệt**.
- Hai ZIP nguồn chứa CONFIG/DEVINFO và các ảnh liên quan được ghi nhận ZIP CRC đạt và **17/17 IMG-sidecar MATCH**; không đăng các ảnh radio/security đi kèm.
- Hash của ảnh backup chỉ chứng minh **bản sao integrity**. Digest Persistent Data Block bên trong CONFIG là tầng khác; không được sửa byte/cập nhật checksum thủ công theo báo cáo này.

Những lần thử ngày 14/11 có `unlock-go OKAY` nhưng main bootloader vẫn **locked**. Mốc ngày 17–18/11 có kết quả **unlocked/orange** sau thay đổi được chủ thiết bị chấp thuận. Xem [lịch sử fail → PASS](oem-unlock-failed-attempts.md), không lấy snapshot 11/11 làm trạng thái mới nhất.

**Không công khai** DEVINFO, CONFIG, FRP credential handle, token, hình CMD chứa serial, byte patch, lệnh ghi flash hoặc thao tác vượt khóa.