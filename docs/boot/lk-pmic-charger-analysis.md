# H01 — phân tích LK/PMIC và lựa chọn Charger Mode

**Nguồn:** [Notion Auto Power-On](https://app.notion.com/p/41ec5d5277a9815799c4d61fba41a3ea), mục 1–7, đặc biệt mục 7 (20/11/2026). Biên soạn 24/11/2026. **STATIC VERIFIED trong ảnh ABOOT/ramdisk**, không đồng nhất với kết quả tự bật nguồn của các mốc sau.

## Vì sao cờ Fastboot chưa đủ?

Trong phép thử ban đầu, `off-mode-charge` và `charger-screen-enabled` đều bằng `1`. Lệnh OEM chỉnh `off-mode-charge 0` trả `OKAY`, đọc lại ngay được `0`, nhưng sau khi tắt/cắm nguồn H01 vẫn mở giao diện sạc và giá trị quay về `1`. Lệnh tắt màn hình sạc cũng trả OKAY nhưng không có bằng chứng cờ được lưu. **OKAY không đồng nghĩa thay đổi có hiệu lực qua reboot**.

## Những nhánh ARM được khảo sát

| Địa chỉ trong ABOOT | Kết quả phân tích tĩnh |
| --- | --- |
| `0x8F630720` | Kiểm tra nguyên nhân nguồn; chuỗi `uc_8909_check_charge_poweron yes/no` |
| `0x8F638154` | Truy xuất thanh ghi `0x808`, phù hợp PMIC PON reason |
| `0x8F6382C4` | Xét `0x80A/0x80B`, phù hợp warm-reset reason |
| `0x8F630754` và `0x8F63078C` | Hai nhánh kết luận no/yes |
| `0x8F62B3E8–0x8F62B434` | Logic gắn `androidboot.mode=charger` vào kernel cmdline |
| `0x8F600BE8` | Đánh giá PON reason trước khi quyết định charger mode |

Báo cáo nhận diện mask `0x58` liên quan DC/USB/CBL, phân biệt reset và Power Key. Đây là cách diễn giải mã ARM dựa trên các định nghĩa PMIC phù hợp, **chưa đo thanh ghi H01 tại thời điểm cắm sạc**. Một nhánh hàm trả `1` được OR với cờ charger-screen trong đường LK, vì vậy đặt cờ 0 đơn lẻ chưa đủ kết luận sẽ bỏ charger mode.

## Ramdisk charger

Ảnh boot gốc chứa `/sbin/charger` (ELF ARM), `/charger` liên kết tới nó, cùng giao diện pin 240×320. `init.rc` có:

```text
on charger
    class_start charger
on property:sys.boot_from_charger_mode=1
    class_stop charger
    trigger late-init
```

Đường init này **có khả năng chuyển** từ charger sang Android khi property phù hợp, nhưng cấu trúc mã không tự chứng minh trigger đã chạy trong một phiên cấp USB-C. Log ADB sau khi Android đã khởi động thường không phản ánh trạng thái lúc hiển thị pin sạc.

Kết quả **Auto Power-On v0.6 PASS** là mốc sau, xem [bằng chứng boot lạnh](auto-power-on-cold-boot-evidence.md). Không đưa ABOOT/boot IMG, ramdisk OEM hoặc script flash lên GitHub.