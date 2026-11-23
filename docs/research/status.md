# Bảng trạng thái nghiên cứu — mốc 23/11/2026

| Chủ đề | Trạng thái | Ghi chú |
| --- | --- | --- |
| Android 8.1 / MSM8909 | OBSERVED | Thuộc tính và snapshot từ máy thử |
| GPT / eMMC | OBSERVED | Có báo cáo 42 phân vùng; công bố bản map đã khử dữ liệu còn PENDING |
| Bootloader unlock + Magisk root | REPORTED PASS | Ghi chép thử nghiệm 18/11; không bảo đảm trên máy khác |
| OTA incremental 81→87 | REPORTED VERIFIED | Có báo cáo kiểm tra chữ ký và block; chưa có factory ROM đầy đủ |
| Dual SIM firmware DSDS | OBSERVED | Chưa xác minh hai SIM vật lý hoạt động đồng thời |
| Launcher3 AutoHotspot v0.4 | REPORTED PASS | Sau reboot; chưa có kiểm tra tải lâu dài |
| AudioTrack / ALSA output | FAIL / PAUSED | Không phát AAC; nhánh sửa audio tạm dừng |
| Ứng dụng Hidden Settings | PARTIAL | Đã có mã/build; một số màn hình OEM có lỗi/giới hạn |
| Điều chỉnh DPI | PARTIAL | Có mã công cụ; kiểm thử hoàn tác thực tế cần thận trọng |
| Logo boot Nokia C3-00 | RESEARCH | Chưa phát hành patch boot/splash đã xác minh |
| H01 App Control | PROPOSED | Kiến trúc quản lý tiến trình/ứng dụng cần nghiên cứu thêm |
| Bộ firmware phục hồi đầy đủ | OPEN | Chưa có bản phục hồi đầu-cuối công khai được xác nhận |

**Định nghĩa:** `OBSERVED` = dữ liệu đo/ghi nhận; `REPORTED PASS` = người thử báo thành công; `REPORTED VERIFIED` = kết quả đối chiếu theo báo cáo nguồn; `PARTIAL` = một phần hoàn thành; `FAIL` = phát hiện lỗi; `PAUSED` = tạm dừng; `RESEARCH`/`PROPOSED`/`OPEN` = chưa hoàn tất.

## Ưu tiên tiếp theo (không ghi flash)

1. Chuẩn hóa bản đồ GPT không có thông tin nhận dạng.
2. Bổ sung bảng phiên bản OTA đã nghiên cứu, không xuất gói OTA gốc.
3. Hoàn thiện bộ test read-only Windows 7 và Linux chống lộ dữ liệu.
4. Chia nhỏ Issues dựa trên các mục `OPEN`/`PARTIAL`; không tự động khôi phục nhánh `PAUSED`.
