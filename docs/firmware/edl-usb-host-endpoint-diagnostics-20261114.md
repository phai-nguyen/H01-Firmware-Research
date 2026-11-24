# H01 — cấu hình USB 9008 và chẩn đoán host Firehose (14/11/2026)

**Nguồn:** Dropbox `H01-firehose-usb-diagnostic-20261114.txt` và `H01-firehose-source-check-20261114.txt`. Hai tệp chứa kết quả lệnh host Linux/antiX và trích mã nguồn EDL, **không phải trace phát sinh lỗi trên một phiên mới**. Nội dung ở đây đã bỏ các đường dẫn/nhận dạng máy và chi tiết riêng.

## Descriptor USB thực tế

| Trường | Kết quả |
| --- | --- |
| USB vendor:product | **05c6:9008** (Qualcomm QDL/EDL) |
| Configuration | 1 |
| Interface | **0** |
| Alternate setting | **0** |
| Endpoints | **2** |
| EP IN | **0x81**, Bulk, max packet **512 byte** |
| EP OUT | **0x01**, Bulk, max packet **512 byte** |

Các descriptor này cho biết host nhìn thấy giao diện USB Bulk; **không chứng minh** Firehose command/READ/WRITE đã chạy được trong chính lần lấy descriptor.

## Phiên bản và cách client xử lý USB

- Host có **Python 3.13.5**, **PyUSB 1.3.1**; lệnh truy vấn package không tìm thấy package pip `libusb1`. **Không suy libusb backend hệ thống không có**, vì PyUSB có thể sử dụng một backend khác.
- Mã `usblib.py` trong EDL client liệt kê thiết bị bằng PyUSB, khớp VID/PID, chọn interface theo class và chọn endpoint theo hướng IN/OUT.
- Client dùng `wMaxPacketSize` từ endpoint IN để xác định kích thước gói ở tầng USB và xử lý `usbread()`/`usbreadwrite()`.
- Trích mã nguồn còn có nhánh xét lỗi permission, cấu hình USB hoặc kernel driver. **Đó là những nhánh code khả dụng**, chưa chứng minh lỗi cleanup USB thực tế của H01 bắt nguồn từ đúng một nhánh.

## Liên hệ với lỗi Firehose/NOP

Các log ngày 14/11 ở hồ sơ khác đã ghi **Sahara/Firehose ACK, GPT READ và NOP ACK** trong một phiên, rồi có TypeError/USB cleanup phía host. Việc đọc source USB giúp định vị **các điểm host xử lý endpoint**, nhưng không tự chẩn đoán nguyên nhân lỗi cleanup cuối phiên. Không kết luận nên đổi timeout, nạp programmer khác hoặc buộc reset máy.

## Giới hạn công bố

Chỉ đăng thông số USB không nhạy cảm và giải thích hành vi host. Không đăng serial USB/ADB, đường dẫn riêng, full debug trace, bộ programmer ELF hoặc file chứa thông số định danh máy. Không cấp quyền USB rộng hoặc chỉnh udev rule chỉ dựa trên bản báo cáo lịch sử.

Xem [nhật ký EDL](edl-sahara-firehose-failure-to-success.md), [Firehose diagnostics](edl-firehose-diagnostics.md).