# Auto Power-On khi cấp USB-C (H01 v0.6)

**Trạng thái: REPORTED PASS — 20–21/11/2026, trên chiếc H01 thử nghiệm.**

Nhật ký Notion “Tự khởi động khi cắm sạc: Fastboot, LK và kernel” xác nhận người dùng đã tắt hẳn H01, rút/cấp lại USB-C và **Android tự khởi động mà không bấm Power** sau khi thử ảnh boot v0.6. Fastboot từng báo ghi boot OKAY; sau reboot, `sys.boot_completed=1` và Magisk trả `uid=0`.

### Kết quả tích hợp

| Hạng mục | Bản | Kết quả |
| --- | --- | --- |
| Tự bật nguồn từ USB-C | Auto Power-On v0.6 | PASS theo người dùng |
| Tự bật Wi-Fi khi Android lên | Launcher3 AutoHotspot v0.4 | PASS |
| Tự hiển thị 4G và cột sóng | Magisk AutoShow v1.1 One-Shot | PASS |
| Tổ hợp ba chức năng | 21/11/2026 | PASS trong một chu kỳ cấp nguồn lạnh |

Phân tích LK/ramdisk đã xem nhánh xử lý lý do cấp nguồn và `androidboot.mode=charger`. Bằng chứng từ **một cấu hình H01** không đồng nghĩa patch boot phù hợp cho mọi phiên bản.

**Chưa xác nhận:** thử tháo pin, nhiều chu kỳ mất điện, nguồn 5V kém ổn định, chạy liên tục 24/7 hoặc đường phục hồi đầy đủ trên một máy khác. Không phát hành ảnh boot đã vá, boot OEM hay script flash không có rollback.

Đối chiếu chỉ đọc sau khởi động: `adb shell getprop sys.boot_completed` và `adb shell getprop uservice.control.slot0`. Hai lệnh **không tự kiểm thử** chức năng bật nguồn. Xem [AutoHotspot](../projects/autohotspot.md) và [4G AutoShow](../system/4g-status-icon.md).

**Nguồn:** trang Notion “H01 – Tự khởi động khi cắm sạc” (20/11, cập nhật 21/11/2026).