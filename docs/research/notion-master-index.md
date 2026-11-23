# Danh mục 207 đề mục của nhật ký nghiên cứu H01

> **INDEXED / CHƯA PHẢI BẢN CÔNG BỐ TOÀN VĂN.** Trích **tiêu đề cấp 2 בלבד** từ trang Notion tổng “H01 – Nghiên cứu firmware GlocalMe K1 / Qualcomm MSM8909”, kiểm kê 23/11/2026. Không chứa nội dung log, ảnh, firmware, mã khóa, đường dẫn riêng hoặc dữ liệu nhận dạng thiết bị.

## Cách dùng

- Mã **H001–H207** là số thứ tự do bản kiểm kê GitHub gán, **không phải ID trong Notion**.
- Tiêu đề có số trùng hoặc số chạy lại vì nhật ký chứa các đợt ghi chép bổ sung; **không tự sửa số mốc gốc**.
- Mỗi dòng mới chỉ được **đánh chỉ mục**. Chỉ những chủ đề đã có trang [đối chiếu Notion → GitHub](notion-coverage.md) mới được gọi là **DOCUMENTED**.
- Trước khi đưa nội dung của mục vào GitHub: đọc lại nguồn, tách mốc lịch sử khỏi trạng thái mới, ẩn danh, kiểm tra quyền tác giả và trạng thái PASS/FAIL/PROPOSED.
- Không công bố APK/IMG/VDEX OEM, dữ liệu SIM, secret, log gốc hoặc token.

## Tóm tắt nguồn

- **Tổng số tiêu đề H2:** 207, trích theo đúng thứ tự ghi trong trang nguồn.
- **Đánh dấu thuật ngữ để định tuyến:** 16 mục liên quan OTA/firmware; 43 mục liên quan lưu trữ/EDL; 36 mục liên quan boot/root. Những nhóm này có thể chồng lấp; **không cộng lại thành tổng**.

## Danh mục theo thứ tự nguồn


### Đề mục 1–50

- **H001** — 1. Thiết bị và môi trường nghiên cứu
- **H002** — 2. Mục tiêu và phạm vi
- **H003** — 3. ADB và giới hạn quyền
- **H004** — 4. Nhánh FOTA / ABUP
- **H005** — 5. Nhánh UCloudlink native libraries
- **H006** — 6. Nhánh UService
- **H007** — 7. Daemon UCloudlink và tiến trình runtime
- **H008** — 8. Ứng dụng và hệ thống khác đã nhận diện
- **H009** — 9. Những điều chưa được xác minh
- **H010** — 10. Kế hoạch tiếp theo
- **H011** — 11. Tệp và dữ liệu đã thu thập
- **H012** — 12. Quy tắc vận hành và an toàn
- **H013** — 13. Nhật ký các kết luận chính
- **H014** — 14. Bổ sung ngày 10/11/2026 – Khôi phục DEX UService và phân tích loader
- **H015** — 15. Bổ sung ngày 10/11/2026 – Phân tích socket runtime
- **H016** — 16. Bổ sung – Snapshot PID daemon đối chiếu socket (ảnh CMD mới)
- **H017** — 17. Bổ sung – Không đọc được file descriptor của daemon root
- **H018** — 18. Bổ sung – Danh sách init RC và kết quả netstat -anp (ảnh ngày 10/11/2026)
- **H019** — 19. Phân tích trực tiếp hai file init RC
- **H020** — 20. Bổ sung – Qualcomm init files và giới hạn kiểm tra kernel modules
- **H021** — 21. Bổ sung – Xác minh sysfs uknet và quyền đọc init
- **H022** — 22. Bổ sung – Phân tích trực tiếp H01-uknet.ko và cấu hình init Qualcomm
- **H023** — 23. Bổ sung – Đối chiếu kernel runtime, firmware mount và Qualcomm DLOAD
- **H024** — 24. Bổ sung – Quyền thực tế của /firmware và nguyên nhân Permission denied
- **H025** — 25. Hướng A – Kiểm tra OTA ABUP thực tế và nguồn firmware OEM
- **H026** — 26. Hướng A – Kết quả rà soát web công khai firmware GlocalMe K1 (10/11/2026)
- **H027** — 27. Kết quả kiểm tra OTA hiện tại ngày 10/11/2026
- **H028** — 28. Rà soát sâu H01 – xác nhận mối liên hệ ZEUS WiFi Nhật Bản / uCloudlink và các nguồn firmware (10/11/2026)
- **H029** — 29. Tiếp tục truy vết firmware H01 – xác minh nhà phân phối ZEUS/HUMAN LIFE và kênh kỹ thuật (10/11/2026)
- **H030** — 30. Phản hồi chính thức từ uCloudlink về yêu cầu firmware H01 (10/11/2026)
- **H031** — 30. Phản hồi chính thức từ uCloudlink về yêu cầu firmware H01 (10/11/2026)
- **H032** — 31. Bootloader, Recovery và Qualcomm EDL – kết quả xác minh trực tiếp (10/11/2026)
- **H033** — 32. Firehose hoạt động và đọc GPT eMMC thành công (10/11/2026)
- **H034** — 33. Phân tích cấu trúc GPT và chuẩn bị sao lưu phân vùng chỉ đọc (10/11/2026)
- **H035** — 34. Sao lưu phân vùng splash thành công qua Firehose (10/11/2026)
- **H036** — 35. Chuyển bản sao splash sang iPhone (10/11/2026)
- **H037** — 36. Chuyển bản sao boot sang iPhone (10/11/2026)
- **H038** — 37. Chuyển bản sao recovery sang iPhone (10/11/2026)
- **H039** — 38. Kế hoạch sao lưu boot chain – bắt đầu với sbl1 (10/11/2026)
- **H040** — 39. Sao lưu phân vùng sbl1 thành công qua Firehose (10/11/2026)
- **H041** — 40. Chuyển bản sao sbl1 sang iPhone (10/11/2026)
- **H042** — 41. Sao lưu và chuyển sbl1bak sang iPhone (10/11/2026)
- **H043** — 42. Sao lưu aboot thành công và chuyển sang iPhone (10/11/2026)
- **H044** — 43. Sao lưu abootbak thành công và chuyển sang iPhone (10/11/2026)
- **H045** — 44. Kế hoạch sao lưu RPM boot-chain (10/11/2026)
- **H046** — 45. Sao lưu rpm thành công và chuyển sang iPhone (10/11/2026)
- **H047** — 46. Kế hoạch sao lưu RPM backup (10/11/2026)
- **H048** — 47. Sao lưu rpmbak thành công và chuyển sang iPhone (10/11/2026)
- **H049** — 48. Kế hoạch sao lưu TZ (10/11/2026)
- **H050** — 49. Sao lưu tz thành công và chuyển sang iPhone (10/11/2026)

### Đề mục 51–100

- **H051** — 50. Kế hoạch sao lưu TZ backup (10/11/2026)
- **H052** — 51. Sao lưu tzbak thành công và chuyển sang iPhone (11/11/2026)
- **H053** — 52. Kế hoạch sao lưu devcfg (11/11/2026)
- **H054** — 53. Nghiên cứu đọc nhiều phân vùng trong một lần chạy EDL (11/11/2026)
- **H055** — 54. Xác nhận EDL V3.62 hỗ trợ đọc nhiều partition (11/11/2026)
- **H056** — 55. Batch đọc thành công 5 phân vùng devcfg / cmnlib / keymaster (11/11/2026)
- **H057** — 56. Xác minh checksum và đóng gói batch boot-security thành công (11/11/2026)
- **H058** — 57. Chuyển batch boot-security gồm 5 partition sang iPhone (11/11/2026)
- **H059** — 58. Nghiên cứu GPT và kế hoạch batch APDP / PAD / MISC (11/11/2026)
- **H060** — 59. Batch APDP / PAD / MISC đã sao lưu, kiểm tra và chuyển sang iPhone (11/11/2026)
- **H061** — 60. Bước tiếp theo sau batch APDP/PAD/MISC: kiểm tra lưu trữ và batch CONFIG/OEM (11/11/2026)
- **H062** — 61. Chuyển thư mục backup tạm từ overlay antiX sang ổ cứng DATA của laptop (11/11/2026)
- **H063** — 62. Người dùng xác nhận format /dev/sda6 làm kho H01 (11/11/2026)
- **H064** — 63. Đã format và mount kho H01DATA thành công (11/11/2026)
- **H065** — 64. Xác nhận quyền ghi kho H01DATA và sẵn sàng dump trực tiếp (11/11/2026)
- **H066** — 65. Batch OEM + CONFIG đã khởi chạy, đang chờ H01 vào EDL (11/11/2026)
- **H067** — 66. Batch OEM + CONFIG dump hoàn tất vào ổ H01DATA (11/11/2026)
- **H068** — 67. Batch OEM + CONFIG đã chuyển đủ 4 tệp sang iPhone (11/11/2026)
- **H069** — 68. Kế hoạch batch hai phân vùng lớn VENDOR + SYSTEM (11/11/2026)
- **H070** — 69. Batch VENDOR + SYSTEM đã dump đủ kích thước (11/11/2026)
- **H071** — 70. Batch VENDOR + SYSTEM đã chuyển 4 tệp sang iPhone (11/11/2026)
- **H072** — 71. Kế hoạch batch kế tiếp: PRODUCTINFO + BOOT + PERSIST + RECOVERY (11/11/2026)
- **H073** — 72. Batch PRODUCTINFO + BOOT + PERSIST + RECOVERY đã dump đủ kích thước (11/11/2026)
- **H074** — 73. Batch PRODUCTINFO + BOOT + PERSIST + RECOVERY đã chuyển sang iPhone (11/11/2026)
- **H075** — 74. Đối chiếu GPT và batch kế tiếp: MODEM / RADIO / SECURITY (11/11/2026)
- **H076** — 75. Batch MODEM + RADIO + SECURITY: đã dump đủ 15 phân vùng (11/11/2026)
- **H077** — 76. Batch MODEM + RADIO + SECURITY: checksum và ZIP đã xác minh (11/11/2026)
- **H078** — 77. Batch MODEM + RADIO + SECURITY đã chuyển sang iPhone (11/11/2026)
- **H079** — 78. Các phân vùng còn lại và thứ tự tiếp tục
- **H080** — 79. Phân vùng CACHE đã dump xong (11/11/2026)
- **H081** — 80. CACHE: checksum và ZIP đạt, các thành phần đã chuyển sang iPhone (11/11/2026)
- **H082** — 81. Chuẩn bị backup USERDATA (chưa chạy)
- **H083** — 82. Kiểm tra dung lượng trước khi sao lưu USERDATA (11/11/2026)
- **H084** — 83. USERDATA đã dump và SHA-256 xác minh thành công (11/11/2026)
- **H085** — 84. USERDATA đã chuyển sang iPhone (11/11/2026)
- **H086** — 85. Trạng thái tổng kết sao lưu H01
- **H087** — 86. Bảng kiểm kê đầy đủ 42 phân vùng GPT H01 (11/11/2026)
- **H088** — 87. Giai đoạn tiếp theo: xác minh SHA-256 trên iPhone và sao lưu raw GPT sectors (11/11/2026)
- **H089** — 88. Primary GPT raw dump hoàn tất (11/11/2026)
- **H090** — 89. Backup GPT raw dump hoàn tất (11/11/2026)
- **H091** — 90. GPT raw ZIP đóng gói và kiểm tra nguồn thành công (11/11/2026)
- **H092** — 91. Xác minh GPT raw ZIP trực tiếp trên iPhone – PASS (11/11/2026)
- **H093** — 92. Xác minh VENDOR + SYSTEM trực tiếp trên iPhone – PASS (11/11/2026)
- **H094** — 93. Thiết kế kiểm tra hàng loạt toàn bộ H01 backup – 11/11/2026
- **H095** — 94. Kiểm tra hàng loạt toàn bộ backup H01 trên iPhone – OVERALL PASS (11/11/2026)
- **H096** — 95. Phân tích đầy đủ H01-verify-all-report.txt – 42/42 MATCH (11/11/2026)
- **H097** — 96. Công cụ đọc bản đồ GPT H01 – script chuẩn bị (11/11/2026)
- **H098** — 97. GPT eMMC audit + reconciliation of 42 IMG verification report (11/11/2026)
- **H099** — 98. Hoàn tất xác minh độ bao phủ 42 phân vùng và kế hoạch xây dựng bộ firmware phục hồi (11/11/2026)
- **H100** — Phân tích tĩnh boot.img – 11/11/2026

### Đề mục 101–150

- **H101** — 99. Nghiên cứu khả năng mở khóa bootloader H01 (11/11/2026)
- **H102** — 100. Phân tích nhị phân ABOOT và ABOOTBAK – xác định cổng OEM Unlock của H01 (11/11/2026)
- **H103** — 101. Xác minh CONFIG và DEVINFO từ hai ZIP người dùng gửi (11/11/2026)
- **H104** — 102. Xác minh Fastboot trực tiếp trên H01 – 11/11/2026
- **H105** — 103. Phân tích Fastboot getvar, cờ secure và mô hình phân vùng (11/11/2026)
- **H106** — 104. Phân tích sâu ABOOT: SCM secure-state, image verification và Fastboot flash gates (11/11/2026)
- **H107** — 105. Giải mã sâu response SCM và luồng boot_verifier trong ABOOT H01 (11/11/2026)
- **H108** — 106. Xác định ý nghĩa field QSEE version và ngưỡng 0x01000000 (11/11/2026)
- **H109** — 107. Hiệu chỉnh và hoàn tất call graph của boot_verifier – phân biệt Verified Boot với Fastboot flash (11/11/2026)
- **H110** — 108. Phân tích keystore tích hợp ABOOT, Root of Trust và SCM Secure Storage (11/11/2026)
- **H111** — 108. Root of Trust, OEM keystore và các software-tamper marker trong ABOOT H01 (11/11/2026)
- **H112** — 109. Xác định thuật toán chữ ký image: SHA-256 + RSA PKCS#1 v1.5 và quy tắc GREEN/YELLOW (11/11/2026)
- **H113** — 110. Đối chiếu runtime QSEE / Keymaster / RPMB / SSD từ logcat H01 (11/11/2026)
- **H114** — 111. Hiệu chỉnh ý nghĩa ro.boot.keymaster=1 và tách biệt với trạng thái TA (11/11/2026)
- **H115** — 112. Đối chiếu trực tiếp ABOOT H01 với DEVINFO: sơ đồ trường và trạng thái Critical (12/11/2026)
- **H116** — 113. Kết luận quy trình OEM Unlock chuẩn H01 và điều kiện trước khi kích hoạt (13/11/2026)
- **H117** — 114. Hoàn tất đưa H01-userdata lên Dropbox – kiểm tra độ bao phủ bản sao lưu (14/11/2026)
- **H118** — 115. Kiểm tra sâu Persistent Data Block, năng lực Firehose và giới hạn phục hồi toàn bộ eMMC (14/11/2026)
- **H119** — 116. Bước tiếp theo: thăm dò Firehose NOP chỉ đọc và kiểm kê eMMC hardware partitions (14/11/2026)
- **H120** — 117. Kiểm tra phiên EDL NOP ngày 14/11/2026 – Sahara thành công, lỗi đường dẫn programmer
- **H121** — 118. Ảnh xác nhận không tìm thấy programmer trong HOME; phương án tải lại đúng đường dẫn (14/11/2026)
- **H122** — 119. Programmer đã tải đúng và NOP đã qua lỗi đường dẫn (14/11/2026)
- **H123** — 120. EDL NOP bị treo 30 phút tại Sahara – dừng host client và thu thập log (14/11/2026)
- **H124** — 121. Phân tích log NOP sau Ctrl+C và xác định vị trí treo trong Sahara (14/11/2026)
- **H125** — 122. Firehose đã hoạt động trên H01 – phân tích log debug ngày 14/11/2026
- **H126** — 123. Xác nhận ảnh sau phiên Firehose – NOP ACK, lỗi cleanup USB và trạng thái EDL còn enumerate (14/11/2026)
- **H127** — 124. Nghiên cứu đường đọc EXT_CSD an toàn và xác minh giới hạn Firehose H01 (14/11/2026)
- **H128** — 125. Kết quả thử đọc EXT_CSD qua debugfs trên Android H01 (14/11/2026)
- **H129** — 126. Phân tích báo cáo MMC: xác nhận eMMC host, RPMB node và chặn quyền đọc debugfs (14/11/2026)
- **H130** — 127. Phân tích báo cáo MMC NODE: RPMB node, sysfs raw_rpmb_size_mult và Boot Area (14/11/2026)
- **H131** — 128. Phân tích quyền SELinux đối với MMC sysfs và kết quả SYSFS ATTRIBUTES (14/11/2026)
- **H132** — 129. Xác nhận SELinux AVC chặn đọc MMC sysfs/debugfs trên H01 (14/11/2026)
- **H133** — 130. Triển khai Hướng A – yêu cầu GlocalMe/uCloudlink hỗ trợ chẩn đoán eMMC chỉ đọc (14/11/2026)
- **H134** — 131. Hướng B – phân tích Firehose và xử lý lỗi đọc USB sau ACK (14/11/2026)
- **H135** — 132. Xác minh GPT dự phòng và khảo sát các vùng eMMC ngoài User Area (14/11/2026)
- **H136** — 133. Kết quả GetStorageInfo của eMMC physical partition 1 (14/11/2026)
- **H137** — 134. Kết quả GetStorageInfo của eMMC physical partition 2 (14/11/2026)
- **H138** — 135. Kiểm tra Dropbox và chuẩn bị đọc eMMC Boot1 (14/11/2026)
- **H139** — 136. Xác minh ba tệp Boot1 đã tải lên Dropbox (14/11/2026)
- **H140** — 137. Phân tích đầy đủ log đọc PPN 1 / Boot1 (14/11/2026)
- **H141** — 138. Phân tích log đọc eMMC PPN 2 / Boot2 và đối chiếu PPN 1 (14/11/2026)
- **H142** — 139. Điều tra lần OEM Unlock ngày 14/11/2026: lệnh OKAY nhưng trạng thái vẫn khóa
- **H143** — 32. Cập nhật 14/11/2026 – Nghiên cứu mở khóa OEM sau khi reset
- **H144** — 33. Nghiên cứu các đường mở khóa khác – 14/11/2026
- **H145** — 34. Phân tích trực tiếp bootloader H01 và cập nhật đường unlock – 14/11/2026
- **H146** — 35. Xác nhận unlock khi phím âm lượng không hoạt động – 14/11/2026
- **H147** — 36. Kết quả thử lệnh mở khóa Fastboot – 14/11/2026
- **H148** — 37. Không xuất hiện prompt sau lệnh chuẩn – 14/11/2026
- **H149** — 38. Kết quả thử alias OEM – 14/11/2026
- **H150** — 39. Kết quả kiểm tra sau oem unlock-go – 14/11/2026

### Đề mục 151–200

- **H151** — 40. Phân tích tĩnh bước đầu về phản hồi OKAY – 14/11/2026
- **H152** — 41. Đối chiếu sâu hơn handler OEM unlock với source Qualcomm LK công khai – 14/11/2026
- **H153** — 42. Lần theo bảng lệnh và handler bằng giải mã ARM ngoại tuyến – 14/11/2026
- **H154** — 43. Đối chiếu handler getvar/device-info với cờ trong unlock-go – 14/11/2026
- **H155** — 44. Cờ get_unlock_ability lấy từ FRP và rà lại chuỗi ảnh – 14/11/2026
- **H156** — 45. Đối chiếu ảnh mới: ADB sau unlock-go và build ID – 14/11/2026
- **H157** — 46. Đọc bootmode đúng cú pháp – ảnh mới
- **H158** — 47. Thuộc tính boot bổ sung từ ADB
- **H159** — 48. Toàn bộ property ro.boot từ ảnh mới
- **H160** — 49. Xác nhận nguồn dump aboot và ảnh thử truy vấn Fastboot
- **H161** — 50. Kết quả truy vấn Fastboot có mục tiêu
- **H162** — 51. Hoàn tất truy vấn Fastboot – trạng thái vẫn khóa
- **H163** — 52. Trạng thái thiết bị hiện tại
- **H164** — 53. Kiểm kê baseline EDL trên Dropbox cho phương án tiếp theo
- **H165** — 54. Bước thao tác tiếp theo đã chốt: đọc mới devinfo và misc
- **H166** — 55. Đối chiếu lần thử QFIL trên Windows và hướng quay lại antiX
- **H167** — 56. Đối chiếu cơ chế Fastboot với chuẩn Android – tiếp tục nghiên cứu, chưa dùng antiX
- **H168** — 57. Rà nguồn gốc dump aboot và giới hạn bằng chứng EDL
- **H169** — 58. Phân tích trực tiếp dump aboot đính kèm – 14/11/2026
- **H170** — 59. Lần theo luồng mã của fastboot unlock – xác nhận UI và giới hạn phím cứng
- **H171** — 60. Mở khóa bootloader H01 — PASS trên thiết bị thật
- **H172** — 61. Phương án tiếp theo: kiểm chứng boot qua RAM, rồi nghiên cứu root/cứu hộ
- **H173** — 62. Cài J2ME Loader: xác định danh sách nguồn cài được phép
- **H174** — 63. Nghiên cứu launcher hiển thị danh sách ứng dụng trên H01
- **H175** — 64. Chọn hướng mở rộng H01: mod firmware gốc hay thay Android
- **H176** — 65. Bản thử H01 Home 0.1: launcher, cử chỉ và quản lý tệp
- **H177** — 66. H01 Home 0.2 — mở giao diện GlocalMe và tìm HOME-only
- **H178** — 67. Phương án ghép toàn bộ firmware H01 — đối chiếu ngày 18/11/2026
- **H179** — Nghiên cứu root H01 — chọn Magisk và thử boot RAM
- **H180** — H01 thật: thử boot RAM ảnh gốc và marker đã đạt
- **H181** — H01: user_rotation không vượt được yêu cầu ngang — chuẩn bị thử lớp phủ
- **H182** — Mốc mới: root Magisk 30.7 qua boot RAM đã PASS trên H01 thật
- **H183** — Thử bật thanh phím Android gốc sau khi có root
- **H184** — Chuẩn bị root cố định và tự bật thanh phím
- **H185** — Root cố định đã PASS sau lần ghi boot và khởi động bình thường
- **H186** — Module tự bật thanh phím đã nạp sau reboot
- **H187** — Nghiên cứu gỡ FOTA và GlocalMe Feedback
- **H188** — H01 Home 0.4: bản thử cài APK trực tiếp bằng root
- **H189** — Cài APK trực tiếp bằng H01 Home 0.4 đã PASS trên H01 thật
- **H190** — Đổi phạm vi: giữ disable, rà ứng dụng để giảm RAM
- **H191** — Kết quả đo RAM trên H01 thật và bước tối ưu tiếp theo
- **H192** — Nghiên cứu tự ẩn thanh điều hướng sau 5 giây
- **H193** — Xác nhận bằng hai báo cáo cửa sổ và thiết kế sửa từng phần
- **H194** — Đã dựng bản IME v0.1 và gói kiểm tra trước khi cài
- **H195** — v0.1 PASS trên H01; đã chuẩn bị v0.2 thử tạm toàn hệ thống
- **H196** — v0.2 đã PASS thực tế; v0.3 nạp qua Magisk lúc khởi động đã đóng gói
- **H197** — v0.3 đã PASS: giữ cố định và nạp lại sau khởi động
- **H198** — Hướng xoay dọc: xác định khóa trong firmware
- **H199** — Bộ thử xoay dọc v0.1 đã dựng, chờ kiểm tra H01
- **H200** — Xoay dọc v0.1 PASS thực tế; nghiên cứu cảm biến và khóa hướng

### Đề mục 201–207

- **H201** — Chuyển dọc/ngang thủ công v0.2: đã dựng gói thử
- **H202** — Sửa lỗi bộ kiểm tra xoay tay: v0.2.1
- **H203** — Xoay thủ công v0.2.1 đã PASS trên H01
- **H204** — Gói giữ hướng qua khởi động v0.3 đã tạo
- **H205** — Sửa gói cố định v0.3.1: hai trạng thái lỗi đã được phân biệt
- **H206** — Hoàn tất kiểm chứng khóa xoay v0.3.1 sau khởi động lại
- **H207** — Share Server H01 — chốt bản ổn định cuối v0.1.4

## Trạng thái chuyển tiếp

[Chuyên đề đã công khai](notion-coverage.md) · [Backlog](publication-backlog.md) · [Chính sách an toàn](../security/publication-policy.md)

Danh mục là **thước đo độ bao phủ nội dung**, không là xác nhận 207 kết quả độc lập hay 207 thử nghiệm PASS. Kết quả H01 thật và các giả thuyết phải kiểm tra trong từng báo cáo riêng.
