# Changelog

## [Magisk compatibility, mksh hash fix, navbar persistence and package-state history] — 2026-11-24

- Từ các mục Notion H179–H187 và H190–H191, công bố **4 báo cáo** về Magisk 31.1/30.7, Root Control v1.1, thanh điều hướng Android và trạng thái FOTA/Feedback.
- Tách `fastboot boot` thử RAM và root cố định sau flash; không suy Magisk được OEM ký lại.
- Ghi lỗi tên hàm `hash` trong mksh và phép kiểm 12 fixture host, không suy false negative thành mismatch ảnh.
- Ghi rõ người dùng quyết định **giữ hai package disabled-user, không uninstall**, dù có giai đoạn đề xuất gỡ.
- Cập nhật 8 tuyến trong mục lục Notion 207 mục tới báo cáo chuyên sâu hơn; không đăng IMG/JAR/OEM binaries hay log chứa ID thiết bị.



## [FOTA filesystem metadata, hidden Activity risk and UService v16] — 2026-11-24

- Đọc trực tiếp file `H01-FOTA-files.txt` trên Dropbox: `FOTA.apk` 577.817 byte, `FOTA.odex` 74.208 byte, `FOTA.vdex` 2.865.228 byte; mtime 2008 không được diễn giải thành ngày build.
- Đối chiếu trang Notion 19/11 để lập ma trận Activity, OEM flags, feature declarations và rủi ro thử nghiệm; không kích hoạt chức năng ẩn.
- Từ nghiên cứu UService v16, phân biệt ba cơ chế update và các trigger nguồn tĩnh với mode runtime chưa được đo.
- Chỉ bổ sung Markdown; không phát hành binary OEM, request credentials hoặc dữ liệu máy.



## [Detailed firmware reconstruction, launcher and UI regression evidence] — 2026-11-24

- Công bố 6 nghiên cứu chi tiết từ các mục H173–H178, H188–H189, H192–H206 của Notion.
- Đính chính rõ khoảng GPT không phân vùng 159.001.600 byte so với phần dữ liệu chưa nằm trong bộ ảnh đã lưu 158.953.472 byte; cửa sổ backup GPT chồng 95 sector với cuối userdata.
- Tách kết quả emulator và H01 thật của J2ME/KISS/H01 Home; phân biệt lỗi không cấp root với PASS cài APK ở bản 0.4.
- Lưu riêng các mốc lỗi JNI preflight, lỗi Binder khi boot và PASS persistent; không đưa bytecode OEM/JAR/modules lên GitHub.



## [Direct Dropbox evidence: GPT, vendor init and FOTA] — 2026-11-24

- Đọc lại GPT TXT ngày 11/11 và so từng dòng với CSV GitHub: 42/42 partition metadata trùng ở index, name, LBA, sector count, bytes.
- Đối chiếu hai bản text vendor init RC giống nhau; ghi 26 service stanza nhận dạng được, HAL và cấu hình hostapd_dual với lưu ý file nối dòng.
- Đọc `H01-ota-check-current.txt`: FOTA 10/11/2026 hai lần trả status 2101; không sao chép raw URL định danh/signature.
- Chỉ nghiên cứu, không ghi firmware hoặc công bố OEM binaries.



## [H01 LockSet and OTA recovery-source clarifications] — 2026-11-24

- Công bố hai báo cáo chi tiết: LockSet/High Contrast UI và lịch sử bản OTA cũ trong Recovery, phân biệt HTTP/TLS với chữ ký CMS OTA.
- Cập nhật đường dẫn bảng Notion chuyên đề và tình trạng: **giao diện khóa PASS, PIN chưa thử; incremental 81→87 không phải ROM factory**.



## [Notion specialist sources and FOTA/UService archival reports] — 2026-11-24

- Xuất bản bảng 17 trang Notion H01 (trang tổng + 16 trang chuyên đề) tới các báo cáo liên quan; không suy 100% nội dung đã hoàn thành.
- Bổ sung báo cáo OTA cache v15 chưa chạy trên thiết bị, ma trận AudioTrack/ALSA, lỗi parser scanner, menu 2846 Log Tools, FOTA/UService VDEX dequickening và UCloudlink ELF library.
- Chỉnh tuyến H004/H005/H006/H014 trong bản đồ 207 đề mục tới tài liệu chuyên sâu hơn; vẫn giữ tư liệu OEM và thông tin riêng ngoài repository.



## [H01 board, ADB, Fastboot and Dropbox evidence] — 2026-11-24

- Bổ sung 5 báo cáo: nhận dạng PCB/pad, ADB trước root, Fastboot/GPT baseline, PyUSB 9008 endpoint, MMC/sysfs/DAC.
- Chỉnh đường định tuyến các mục H001–H003, H016–H017 và H104–H105 tới tài liệu chi tiết hơn.
- Có thêm bảng ranh giới các nguồn Notion/Dropbox đã đọc; không đăng log gốc chứa serial, APK/IMG OEM hoặc khóa.



## [H01 207-section routing map and backup evidence] — 2026-11-24

- Xuất bản bảng 207 mục gốc → tài liệu GitHub liên quan, chỉ để truy vết nguồn, **không báo cáo đã chuyển đủ 100%**.
- Bổ sung nhật ký batch EDL và kiểm chứng sao lưu trên iPhone/GPT; không phát hành dump OEM.



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
