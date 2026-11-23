# Nghiên cứu OEM Unlock trên bootloader ZEUS H01

**Nguồn:** Notion H01 mục 99–113 và mục “60. Mở khóa bootloader H01 — PASS” (11–18/11/2026). **Mốc sau cùng: REPORTED PASS trên một H01 sau lần thử 18/11; các ghi chú khóa trước đó là lịch sử.**

## Diễn biến quan trọng

| Giai đoạn | Kết quả |
| --- | --- |
| 11/11: truy vấn khả năng | `fastboot flashing get_unlock_ability` trả `1`; trạng thái `Device unlocked: false`, critical-unlocked là trạng thái riêng |
| 14/11: thử lệnh OEM | Một số lệnh trả `OKAY` nhưng bootloader **vẫn báo khóa** sau reboot; không coi phản hồi OKAY là thành công |
| 17–18/11: phân tích sâu ABOOT và DEVINFO | Phát hiện nhánh trạng thái OEM riêng mang nhãn `GLOCALME-BOOT`, phân biệt với đường `ANDROID-BOOT!` |
| 18/11: thử nghiệm trên H01 | `ro.boot.flash.locked=0`, `ro.boot.verifiedbootstate=orange`, được ghi nhận cả sau một lần `adb reboot` — **REPORTED PASS** |

### Phân tích cơ chế

Trong dump ABOOT, hai nhãn metadata dẫn đến những nhánh khởi tạo cờ unlock khác nhau; kết quả mô phỏng ARM phù hợp với hiện tượng nhánh Android có thể đặt lại cờ unlock. Nhật ký cuối ghi người thử **đã đồng ý** thực hiện thay đổi chỉ trên ảnh DEVINFO nghiên cứu và xác nhận kết quả từ thuộc tính boot trên H01 thật.

Đây là nghiên cứu lịch sử về **một build thiết bị**, không phải hướng dẫn thay byte/flash DEVINFO cho cộng đồng. Không sao chép image DEVINFO, cấu trúc dữ liệu đặc thù máy, patch hoặc lệnh ghi vào bài public này.

### Cách đánh giá kết quả đúng

- `get_unlock_ability=1` chỉ nói điều kiện **cho phép yêu cầu** unlock, không phải `unlocked=true`.
- `fastboot OKAY` có thể chỉ xác nhận lệnh được nhận, không chứng minh thay đổi trạng thái bootloader.
- `ro.boot.flash.locked=0` và `orange` sau reboot là bằng chứng hệ điều hành đã quan sát; không tự chứng minh mọi loại flash hoặc mọi revision đều hoạt động.
- Nhánh OEM có thể yêu cầu xác nhận hoặc **wipe userdata**. Không chạy lại unlock/ghi metadata trên H01 đang hoạt động tốt khi không có backup và đường cứu hộ.

**Liên quan:** [root/recovery](root-and-recovery.md), [kiểm tra eMMC](../firmware/emmc-backup-verification.md), [Firehose](../firmware/edl-firehose-diagnostics.md).