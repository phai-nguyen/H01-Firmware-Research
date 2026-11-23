# Firmware, boot chain và phân vùng

## Phạm vi

Thiết bị thử sử dụng Android 8.1 và sơ đồ GPT được ghi nhận có **42 phân vùng**. Danh sách có `modem`, `boot`, `system`, `recovery`, `vendor`, `userdata`, `splash`, `aboot`, `sbl1`, `rpm`, `tz`, `misc` và nhiều vùng OEM/bảo mật. Đối chiếu bảng GPT thực tế của đúng thiết bị trước mọi thao tác khôi phục.

| Thành phần | Trạng thái nghiên cứu |
| --- | --- |
| eMMC/GPT | Đã có báo cáo bản đồ GPT và tệp sao lưu; cần công khai bảng đã khử thông tin nhạy cảm |
| Bootloader/EDL | Đã ghi nhận các phiên thử trên máy thật; xem tài liệu boot |
| `system.img` / `vendor.img` | Có bản sao riêng trong kho lưu trữ; **không phát hành ở đây** |
| `userdata.img` | Bản sao riêng, **không công khai** |
| OTA | Đã nghiên cứu gói incremental 81→87, không phải factory image |
| Full factory firmware | Chưa có gói cứu hộ chính thức được công bố/kiểm chứng trong repository |

## Không đăng firmware OEM

Không commit ảnh phân vùng, boot image Magisk đã patch, modem, NV, phần mềm/driver OEM, khóa ký hoặc URL tải firmware có thông tin xác thực. Chỉ đưa hướng dẫn phân tích, các phát hiện phi nhạy cảm và công cụ do dự án tự viết.

## Kế hoạch công khai bản đồ phân vùng

Dùng CSV **đã làm sạch**, ghi tên phân vùng, thứ tự, kích thước, bản build nguồn, thời gian quan sát và mức độ chắc chắn. Không sao chép nội dung `modemst*`, `fsg*`, `userdata`, `persist`, `keystore`, `productinfo` hay dữ liệu nhận dạng thiết bị vào kho công khai.
