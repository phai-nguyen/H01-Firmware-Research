# Changelog

## [H01 secondary-device research and Share Server documentation] — 2026-11-24

- Bổ sung **5 báo cáo** từ trang Notion H01 23–24/11 và mục Share Server v0.1.4: đối chiếu máy A/B, EDL/unlock/root, DPI/Launcher3/IME, xoay persistent, giao thức truyền file.
- Phân biệt **bộ cài gửi** với **ứng dụng chạy PASS**, các mốc boot ID khác nhau, thử IME đang mở và lưu module qua reboot, kết quả root/boot của từng máy.
- Chỉ biên soạn tài liệu; không công bố ID máy, PK_HASH, serial, IMG, DEVINFO, module OEM, log, công cụ mới hay lệnh ghi flash.



## [H01 legacy power/SIM/hotspot research documentation] — 2026-11-24

- Đăng thêm 6 báo cáo lịch sử chi tiết từ Notion 19–21/11: LK/PMIC charger-mode, Auto Power-On v0.6 trên eMMC, AutoShow slot0, AutoHotspot API v0.3.1–v0.4, SMS Provider và giới hạn dùng lại ảnh boot trên máy khác.
- Phân biệt các mốc FAIL trước v0.6 với PASS sau đó; không khẳng định hoạt động không pin/24 giờ hoặc khả năng dùng hai SIM.
- Chỉ tài liệu: không tạo công cụ, không công bố firmware OEM hay dữ liệu riêng.



## [Keyguard and hidden component research] — 2026-11-23

- Bổ sung bốn chuyên đề H01 từ hồ sơ Notion 19–20/11: Android Keyguard + UCloud sleep, crash BackKeyManager, UI LockSet/High contrast, danh mục Activity/cờ OEM.
- Chỉ công bố tài liệu. Nhánh khóa PIN và các cờ OEM chưa kiểm thử tiếp; không đưa log riêng, APK/DEX hoặc patch lên repo.



## [OTA, UService, network and hardware research] — 2026-11-23

- Bảy báo cáo kỹ thuật từ Notion: OTA v1–v11, UService v12/v16, socket runtime v13/v14, Device Tree âm thanh K1 và DSDS/PCB.
- Chỉ lưu bằng chứng; phân biệt bản sao ngoại tuyến, thử runtime, lỗi/hạn chế còn mở và trạng thái được chứng minh.
- Không thêm code, tool, binary OEM hay dữ liệu SIM và bí mật backend.



## [Research-history consolidation only] — 2026-11-23

- Bổ sung 7 báo cáo kỹ thuật lịch sử từ hồ sơ H01: OTA ABUP, nguồn firmware và phản hồi OEM, timeline sao lưu eMMC, J2ME/KISS/H01 Home, chính sách APK và FOTA/Feedback, IME/nav, xoay/cảm biến.
- Đợt này **chỉ công bố tài liệu**. Không thêm script, công cụ, APK hoặc binary. Các mốc PASS gắn với bằng chứng lịch sử, không phải phép kiểm thử mới.
- Bảo vệ dữ liệu SIM, ID thiết bị, xác thực ABUP, thư riêng và firmware/driver OEM.



## [Partition inventory audit] — 2026-11-23

- Bổ sung công cụ metadata-only để tính số ứng viên 42 phân vùng GPT theo tên/kích thước IMG/ZIP, không trộn số ảnh và số partition.
- Kèm 7 unit tests dùng dữ liệu tổng hợp; không thay thế SHA-256/CRC hoặc khả năng phục hồi.



## [Backup archive integrity auditor] — 2026-11-23

- Đăng trình kiểm tra ZIP/IMG CRC + SHA-256 chỉ đọc, kèm 12 bài thử tổng hợp và tài liệu Windows 7/antiX.
- Phân biệt bản sao khớp checksum với độ bao phủ GPT, tính xác thực firmware và khả năng restore; không đăng ảnh OEM hoặc sidecar riêng.



## [Kernel/init/boot and recovery readiness documentation] — 2026-11-23

- Bổ sung bảy chuyên đề từ Notion: uknet.ko, init services Qualcomm/UCloudlink, /firmware DAC/mount, RAM/PSS, Verified Boot vs Fastboot flash, Magisk 30.7, readiness cứu hộ.
- Đính chính những mốc lịch sử theo báo cáo nguồn sau: /firmware thực sự mounted nhưng bị DAC chặn; 3.10.49 vermagic khác kernel 3.18.71 chưa kết luận compatibility; root cố định đã PASS sau boot RAM.
- Giữ giới hạn: chỉ tài liệu và lệnh đọc trạng thái, không kèm OEM .ko/IMG, log riêng, script flash, khóa hoặc dữ liệu SIM.



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
