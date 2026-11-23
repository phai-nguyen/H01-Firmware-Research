# H01 máy B — khóa xoay thủ công và module tích hợp IME + xoay

**Nguồn:** Notion “H01 MÁY MỚI #2”, mục 10, nhật ký 23–24/11/2026. **REPORTED PASS theo hai boot và phản hồi người dùng; chưa kiểm chứng mọi ứng dụng.**

Bản ứng dụng `vn.h01.rotation` đã nghiên cứu trên máy A được dùng ở B. Vì IME đã có module framework persistent, thiết kế trên B dùng **một module tích hợp IME + xoay**, tránh hai module cùng ghi đè services.jar. Controller giữ lựa chọn root-private; dịch vụ sau boot áp lựa chọn một lần rồi thoát.

| Mốc từ log | Kết quả |
| --- | --- |
| 23:36 — cài | APK Success và trạng thái `REBOOT_REQUIRED` |
| 23:38 — reboot thử | `BOOT_COMPLETED=1`, `MODE=awaiting_boot_confirmation`, `NEXT_BOOT_ENABLED=true`, **ngang 320×240**, `choice3/user_rotation3` |
| Người dùng xác nhận | **Chuyển hướng dọc/ngang PASS** |
| 23:48 — reboot mới sau lưu cố định | `MODE=persistent`, `NEXT_BOOT_ENABLED=true`, `boot.log PERSISTENT`; lúc báo cáo **dọc 240×320**, `choice0/user_rotation0`, thanh phím ẩn |

Có sự khác nhau giữa service log **áp ngang 3 ở đầu boot** và trạng thái **dọc 0** lúc đọc báo cáo cuối: đây là **hai thời điểm**, không mâu thuẫn. Chưa có log một lần reboot tiếp để xác nhận **chính lựa chọn dọc 0** sẽ vẫn giữ qua reboot nữa. Cũng chưa chứng minh tự xoay bằng cảm biến, tương thích mọi game/Activity hay sửa nhánh bảng thông báo.

Báo cáo cũ có watchdog thử boot; ở trạng thái persistent không tự suy watchdog vẫn chạy. Không phát hành APK/JAR OEM, module có mã sở hữu, script cài/restore hoặc log riêng.

Xem [IME B](device-b-launcher-ime-evidence.md), [xoay A](rotation-and-sensors-timeline.md), [A/B](../research/h01-device-b-comparison-20261124.md).