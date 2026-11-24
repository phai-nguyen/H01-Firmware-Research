# Bootloader, Fastboot, EDL, Magisk và khôi phục

## Trạng thái từ nhật ký thử nghiệm

- **18/11/2026:** ghi nhận `ro.boot.flash.locked=0` và `ro.boot.verifiedbootstate=orange` trên máy thử sau thao tác mở khóa; trạng thái vẫn được báo cáo sau `adb reboot`.
- `fastboot boot` ảnh boot có Magisk từng PASS trong phiên kiểm thử.
- Sau đó ảnh boot Magisk đã được flash và Android lên với quyền `uid=0` theo nhật ký nghiên cứu; đây là **báo cáo của thiết bị thử**, không phải bảo đảm cho mọi H01.
- EDL 9008, Firehose và GPT đã được nghiên cứu; cần đối chiếu đúng programmer/OEM, phiên bản và cơ chế bảo vệ trước bất kỳ thay đổi nào.

## Nguyên tắc khôi phục an toàn

- Sao lưu và kiểm tra SHA-256 **ngoài thiết bị** trước các thử nghiệm có thể ghi flash.
- Giữ nguyên bản gốc, tách biệt các bản vá và có khả năng đọc lại dữ liệu để xác minh.
- Ưu tiên lệnh **chỉ đọc**; không cung cấp lệnh flash đại trà không kèm kiểm thử/đường rollback đã được chứng minh.
- Không dùng Firehose/programmer không rõ nguồn, không ghi modem/NV hoặc phân vùng danh tính thiết bị.
- Cấu hình đã PASS của một máy **không** chứng minh an toàn cho máy khác.

Tài liệu thực hành chi tiết sẽ được bổ sung sau khi tẩy dữ liệu nhạy cảm khỏi log và xây dựng quy trình cứu hộ đã xác minh.

## Hướng dẫn theo trình tự đã ghi trong Notion

- [Mở khóa bootloader H01: cơ chế OEM/DEVINFO và cách xác minh](h01-bootloader-unlock-notion-procedure-20261124.md).
- [Root Magisk 30.7: vá boot đúng máy, boot RAM, root cố định](h01-magisk-root-notion-procedure-20261124.md).

Hai tài liệu mô tả kết quả từng bước và điều kiện dừng, **không** cung cấp script ghi DEVINFO/boot đại trà cho mọi H01.
