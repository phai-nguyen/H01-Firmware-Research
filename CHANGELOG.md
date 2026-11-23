# Changelog

## [H01 firmware deep-dive documentation] — 2026-11-23

- Bổ sung bảy báo cáo: ABUP/FOTA, UService loader, MQTT/UCloudlink daemons, EDL/Firehose, integrity 42/42 và 46/46 IMG, Boot1/Boot2 zero-filled, OEM Unlock.
- Đối chiếu mốc lịch sử và mốc cuối: UService dequickening đã hoàn thành trong ghi chép sau; Bootloader mở khóa PASS 18/11 là mốc sau các thử nghiệm khóa 14/11.
- Không đăng OEM firmware/APK/VDEX/DEVINFO, token, dữ liệu SIM hoặc log thô.



## [H01 research consolidation] — 2026-11-23
- Xuất bản thêm mục lục **207 đề mục H2 của trang Notion tổng** (chỉ tiêu đề đã lọc), tạo danh sách truy vết những nội dung chưa được chuyển thành báo cáo.


- Đối chiếu 15 trang Notion H01, bổ sung 12 tài liệu chuyên đề và 2 bảng kiểm kê/trạng thái (Notion coverage và publication backlog nằm trong 12 tài liệu).
- Ghi lại mốc Auto Power-On v0.6, AutoShow 4G v1.1, rotation v0.3.1 và Share Server v0.1.4 theo chứng cứ đã lưu.
- Phân biệt rõ kết quả thử máy, phân tích tĩnh và phần chưa xác minh; không đăng IMG/APK gốc, secret hoặc raw log.



## [0.2.0 + nghiên cứu 2846] — 2026-11-23

- Đối chiếu 4 bản sao GlocalmeHome gốc có cùng SHA-256; bản GlocalmeHome-VietHoa-Test.apk khác hash nhưng giữ chữ ký tham chiếu/opcode của 5 phương thức xử lý menu 2846.
- Đưa lên GitHub công cụ `compare_glocalmehome_2846.py`, tài liệu đối chiếu và 6 unit tests synthetic.
- Đánh dấu rõ **chưa có APK đã xác thực từ chiếc H01 thứ hai**, vì vậy chưa có so sánh giữa hai bản firmware OEM thực sự.


### Bổ sung nghiên cứu mã 2846 — 2026-11-23 (sau v0.2.0)

- Mở mã nguồn độc lập `tools/inspect_2846.py` (6/6 xác minh trên APK mẫu gốc).
- Mở mã nguồn `tools/inspect_mmi_vdex.py` cho VDEX 010: constructor và `onReceive`, 1/1 + 9/9 chỉ mục quickening; 8/8 kiểm tra ngữ nghĩa trên VDEX mẫu H01.
- Bổ sung 5 bài thử bằng dữ liệu VDEX tổng hợp, không kèm firmware gốc.
- Xác nhận hai nhánh sử dụng mã `2846` khác nhau: About → AssistantActivity và `MMI.MySecretCodeReceiver` qua Telephony secret-code broadcast.

## [0.2.0] — 2026-11-23

- Công khai bảng GPT 42 phân vùng từ snapshot ngày 11/11/2026, loại bỏ GUID/CRC riêng.
- Thêm script ADB chỉ đọc cho Windows 7 và Linux/antiX; không dùng root, flash hay cài APK.
- Thêm trình xác minh SHA-256 sidecar ngoại tuyến và năm bài kiểm thử Python dùng dữ liệu giả.
- Bổ sung hướng dẫn thu thập, ẩn danh kết quả và nguồn chứng cứ.
- Mở rộng CI để chạy kiểm thử CSV, kiểm thử checksum và rà soát nội dung công khai.

**Chưa xác minh thực địa:** script ADB chưa được thử chạy trên H01 sau khi phát hành. Tình trạng firmware, SIM và audio không thay đổi vì cập nhật repository.

## [0.1.0] — 2026-11-23 (công khai trên GitHub)

- README tiếng Việt/Anh, hướng dẫn đóng góp và bảo mật.
- Chính sách MIT cho mã nguồn tự viết, CC BY 4.0 cho tài liệu tự biên soạn.
- Biên soạn các ghi chép H01: phần cứng, OTA, EDL/root, Dual SIM, audio và AutoHotspot.
- Bảng trạng thái và nguồn bằng chứng; danh mục mẫu của các tệp sao lưu **không chứa binary hoặc checksum nhạy cảm**.
- Kiểm tra nội dung public cơ bản và mẫu issue.

**Đã tải lên GitHub Public ngày 23/11/2026.** Đây là bản khởi tạo gồm 26 tệp; chưa chuyển toàn bộ kết quả nghiên cứu trong Notion/Dropbox và chưa phát hành GitHub Release chính thức.
