# Chính sách mở nguồn an toàn

**Mở mã nguồn của công cụ, không mở bí mật hoặc phần mềm OEM của thiết bị.** Repository phải chỉ chứa tư liệu và mã do dự án có quyền phân phối.

## Được công bố

- Tài liệu tự biên soạn, mô tả phần cứng và kiến trúc hệ thống.
- Kết quả kiểm tra đã khử dữ liệu riêng tư, bảng kích thước và trạng thái tổng hợp.
- Script tự phát triển chỉ đọc có mã nguồn rõ ràng.
- Mẫu output giả lập (synthetic) không lấy từ danh tính thiết bị thực.

## Không được công bố nếu chưa có cơ sở pháp lý và quy trình bảo vệ thích hợp

- Firmware OEM, APK/ODEX/VDEX/ELF gốc, ảnh eMMC/boot/system/vendor/userdata/OTA nguyên bản.
- File `modemst*`, `fsg*`, `persist`, NV, khóa ký, keybox, root token, `deviceSecret`, SoftSIM, mã định danh thuê bao.
- Log có IMEI/MEID, ICCID/IMSI, số điện thoại, SSID/mật khẩu, địa chỉ MAC và thông tin tài khoản.
- Bản vá chưa được kiểm thử gắn nhãn `PASS` hoặc hướng dẫn flash không có đường cứu hộ.

## Checklist trước commit

1. Kiểm tra `git diff --cached` và toàn bộ nội dung được stage.
2. Chạy `python tools/check_public_content.py` (chỉ kiểm tra mẫu, **không bảo đảm an toàn**).
3. Nếu nghi ngờ đã đưa bí mật lên Git: **không tiếp tục push**, kiểm tra lịch sử Git, thu hồi khóa liên quan và chuyển sang cơ chế báo cáo bảo mật.
4. Đọc lại ảnh, log, file CSV được trích từ thiết bị và quyền sở hữu nội dung trước khi xuất bản.
