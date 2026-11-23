# Nghiên cứu thanh điều hướng và IME của H01

**Nguồn:** nhật ký Notion H01 từ “Nghiên cứu tự ẩn thanh điều hướng sau 5 giây” đến “v0.3 đã PASS: giữ cố định và nạp lại sau khởi động”. **Phân loại: static/ADB evidence và REPORTED PASS theo từng phiên bản, không bao gồm binary vá.**

## Vấn đề cần giải quyết

Mục tiêu ban đầu: thanh Back/Home/Recents tự ẩn khi không dùng và vuốt từ cạnh để gọi lại. Cấu hình `immersive.navigation=*` có thể giữ thanh ẩn khi ở ứng dụng bình thường nhưng các trạng thái **bàn phím IME** và **bảng thông báo** làm thanh hiện trở lại.

Phân tích `StatusBar.scheduleAutohide()` và chính sách `PhoneWindowManager` của bản firmware H01 cho thấy hai nhánh xử lý khác nhau; không thể suy ra một lệnh immersive duy nhất giải quyết tất cả.

## Diễn tiến thử nghiệm

| Giai đoạn | Quan sát chính | Kết luận tại thời điểm đó |
| --- | --- | --- |
| Phân tích ban đầu | Khi mở bàn phím, `mForcingShowNavBar=true`, hệ thống xóa cờ ẩn navigation; thanh hiện lên | Có nhánh riêng của IME |
| v0.1 preflight | Probe so sánh baseline/candidate PASS trong tiến trình riêng, không nạp vào system_server | **Chỉ preflight, chưa PASS giao diện** |
| v0.2 thử tạm | Nạp services JAR đã kiểm chứng qua cơ chế thử có rollback, `DEX2OAT_EXIT=0`; log bàn phím mở nhưng thanh ẩn; người dùng báo PASS | **IME exception PASS** trong lượt thử |
| v0.3 cố định | Module Magisk kiểm tra hash/manifest trước khi nạp, báo `MODE=persistent`, `NEXT_BOOT_ENABLED=true` sau boot mới | **Cơ chế cố định sau reboot PASS** trong snapshot |

Snapshot v0.3 có Launcher3 ở foreground, thanh navigation ẩn và thanh trạng thái vẫn hiện. **Không ghi snapshot này là ảnh đo lúc bàn phím đang mở**; phép thử IME dựa vào log v0.2 và phản hồi trực tiếp của người dùng.

## Điều chưa hoàn tất

Nhánh **bảng thông báo** làm thay đổi chính sách hiển thị thanh điều hướng vẫn chưa có bản sửa chạy trên H01 được ghi nhận PASS trong các mục này. Cũng chưa chứng minh tiêu chí chính xác “ẩn sau 5 giây” được đảm bảo trong mọi Activity/cửa sổ.

Không công bố `services.jar` OEM đã vá, ODEX/VDEX, boot image hoặc gói Magisk chứa mã sở hữu không có quyền phân phối. Tài liệu chỉ lưu các phát hiện về cơ chế và kết quả thử nghiệm.