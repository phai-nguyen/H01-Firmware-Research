# Launcher3 AutoHotspot v0.4

**Nguồn:** ghi chép Notion 20–21/11/2026 và báo cáo kiểm thử người dùng.

## Mục tiêu

Sử dụng Launcher3 thay cho giao diện OEM mà vẫn khởi động hotspot tự động sau Android boot bằng module Magisk, không cần mở GlocalmeHome.

## Mốc kết quả

- v0.3.2: có lỗi gọi sai chữ ký API; nguyên nhân được ghi là `NoSuchMethodError`.
- v0.3.3: xác định chữ ký `IConnectivityManager.startTethering(int, ResultReceiver, boolean, String)` cho firmware thử.
- v0.3.4: người dùng báo PASS bật hotspot thủ công bằng API phù hợp.
- v0.4: báo cáo PASS module Magisk tự bật SoftAP sau reboot; người dùng cũng xác nhận hoạt động trong một lần cấp nguồn USB-C từ trạng thái tắt và vào Android.

## Chưa kết luận

Chưa có thống kê chu kỳ boot lặp lại, không pin, vận hành 24/7, độ ổn định sau mất điện bất ngờ hay tương thích mọi revision H01. Không khẳng định các thành phần OEM đều an toàn để vô hiệu hóa.

Hiện mới công bố **tài liệu tổng quan**. Bộ cài/modul gốc và mã liên quan sẽ được rà soát quyền phân phối và dữ liệu riêng trước khi tạo Release.
