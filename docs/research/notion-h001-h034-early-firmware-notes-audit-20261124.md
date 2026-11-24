# H01 — mục Notion H001–H034: hồ sơ khởi đầu, daemon, FOTA và EDL

**Nguồn duy nhất:** [Nhật ký tổng H01 trên Notion, H001–H034](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), các mốc thời gian ghi trong tài liệu từ giai đoạn đầu tháng 11/2026. Nội dung dưới đây là **bản tóm tắt nghiên cứu an toàn đã ghi trên Notion**, không pha thêm phép thử H01 mới chưa được ghi vào đó.

**Quy tắc hiệu lực:** mốc đầu “chưa có firmware”, “chưa unlock”, “chưa dequickening UService” đúng ở thời điểm nguồn; kết quả sau đó **không được sửa ngược lịch sử** mà phải giữ cả hai mốc và đường liên kết cập nhật.

## H001–H013 — nền tảng, FOTA, UService và snapshot đầu tiên

| Mục | Nội dung trong Notion | Mức bằng chứng |
| --- | --- | --- |
| H001 | Nhận dạng bo thiết bị, Android 8.1/Qualcomm MSM8909; ký hiệu pad trên PCB không phải pinout UART đã kiểm | HARDWARE OBSERVED |
| H002 | Mục tiêu nghiên cứu/giữ bản gốc; không phải một kết quả cài ROM khác | PROJECT SCOPE |
| H003 | ADB shell UID 2000, quyền root bị giới hạn ở mốc đầu, có thu thập thông tin hệ thống chỉ đọc | RUNTIME BASELINE |
| H004 | Khôi phục FOTA DEX từ VDEX010, phân tích ABUP/Recovery; kết quả dequickening không chứng minh có OTA tải được | STATIC VERIFIED |
| H005 | Kiểm kê 12 thư viện UCloudlink ELF ARM và symbol mạng/FOTA; symbol không chứng minh traffic live | BINARY STATIC |
| H006 | UService APK/ODEX/VDEX cùng các thư viện native; bản raw DEX ở mốc đầu chưa dequickening hoàn chỉnh | STATIC / INITIAL LIMIT |
| H007 | Nhận diện daemon UCloudlink/process và cấu hình Mosquitto; không gán chắc toàn bộ socket/PID | RUNTIME SNAPSHOT |
| H008 | Danh mục các APK OEM gồm FOTA, UService, GlocalmeHome, InstallService, UKL Factory, MMI | FILE/PACKAGE INVENTORY |
| H009 | Danh sách điều chưa xác minh ở đầu dự án, **không** đồng nghĩa kết luận còn đúng sau 18–24/11 | HISTORICAL OPEN |
| H010 | Định hướng phân tích DEX/IPC/firmware và Linux, ở thời điểm này chỉ là kế hoạch | PLAN |
| H011 | Danh mục file FOTA/UService/snapshot đã thu thập; không đồng nghĩa mọi binary được đính kèm Notion | FILE INVENTORY |
| H012 | Nguyên tắc chỉ đọc, dừng khi Permission denied và giữ dữ liệu SoftSIM/NV bí mật | PUBLICATION SAFETY |
| H013 | Bản tổng kết sớm: chưa có OTA/dump/unlock; các mốc đã thay đổi về sau được lưu riêng | HISTORICAL SUMMARY |

## H014–H024 — VDEX, MQTT, init và các giới hạn filesystem

| Mục | Nội dung trong Notion | Mức bằng chứng |
| --- | --- | --- |
| H014 | UService VDEX010 được báo xử lý quickening và kiểm checksum; thay kết luận thô của H006 | STATIC VERIFIED LATER |
| H015 | Thấy listener MQTT 1883 và socket loopback/DNS trong snapshot; không chứng minh truy cập WAN | NETWORK SNAPSHOT |
| H016 | Ảnh PID/UID daemon, nhưng chưa ghép socket inode với từng process | PROCESS SNAPSHOT |
| H017 | Không đọc được /proc/PID/fd của daemon root từ ADB shell; không đoán chủ listener | PERMISSION LIMITED |
| H018 | Danh sách RC và netstat, nhưng tên file init không chứng minh stanza thực tế | INVENTORY ONLY |
| H019 | Đọc trực tiếp một số init RC: unet/uc_kglogd/uc_tcpd và trigger riêng | INIT STATIC |
| H020 | Nhận diện các Qualcomm init file còn cần nội dung; /proc/modules có giới hạn quyền quan sát | PARTIAL |
| H021 | Thu thập init RC bổ sung và kiểm sysfs uknet; không suy nội dung file chỉ từ lệnh chạy | SOURCE COLLECTION |
| H022 | Phân tích uknet.ko, daemon uc_qmi_clnt/uc_netlink và socket; mount /firmware có nhưng nội dung chưa đọc | STATIC + RUNTIME |
| H023 | Đối chiếu module kernel runtime, /firmware và Qualcomm DLOAD; không biến đường debug thành công cụ cứu hộ đã PASS | PARTIAL / RISK |
| H024 | Quyền mount/dir khiến ADB shell không pull được /firmware; không phá quyền hoặc SELinux | PERMISSION OBSERVED |

## H025–H034 — OTA, kênh hỗ trợ OEM, Fastboot và GPT

| Mục | Nội dung trong Notion | Mức bằng chứng |
| --- | --- | --- |
| H025 | Hai lần kiểm FOTA lịch sử không tải payload; log cũ không phải kiểm OTA hiện tại | FOTA LOG SNAPSHOT |
| H026 | Chưa tìm thấy public factory H01 đúng board/build tại thời điểm khảo sát 10/11 | WEB SEARCH HISTORY |
| H027 | Hai phản hồi kiểm OTA 10/11 status 2101, data=null; không có cập nhật mới được trả lúc đó | FOTA RUNTIME SNAPSHOT |
| H028 | Báo cáo lịch sử ZEUS/uCloudlink và ngừng dịch vụ H01 cũ; không biến tin dịch vụ thành khả năng flash firmware | SOURCE RESEARCH |
| H029 | Truy vết nhà phân phối/board liên quan ZEUS, nhưng chưa xác nhận chính xác mọi revision phần cứng | SOURCE RESEARCH |
| H030 | Phản hồi uCloudlink chưa cung cấp firmware hay recovery; yêu cầu định danh phải xử lý riêng tư | SUPPORT STATUS |
| H031 | Ghi thêm nguồn phản hồi và các hạn chế chia sẻ IMEI; không có gói phục hồi chính thức | SUPPORT STATUS |
| H032 | Fastboot báo cho phép **yêu cầu** unlock nhưng main vẫn locked; EDL/Recovery có kết quả thăm dò riêng | DEVICE SNAPSHOT |
| H033 | Firehose đã được báo đọc được GPT LUN0 sau handshake; không suy từ một lần READ là restore đã PASS | EDL/GPT REPORTED PASS |
| H034 | Phân tích GPT 42 mục, kích thước config 512 KiB khác oem 8 MiB; chuẩn bị đọc từng partition chỉ đọc | GPT STATIC / PLAN |

## Ba hiệu chỉnh lịch sử quan trọng

1. **UService H006 vs H014:** ở H006 mới có DEX raw quickened/checksum không hợp lệ; H014 báo xử lý VDEX010 và phục hồi checksum. Không gắn nhãn “UService DEX chưa giải được” như trạng thái muộn nhất, cũng không suy toàn bộ mã bị obfuscate đã giải.
2. **OTA H025–H027 vs đợt 22/11:** những lần check status 2101 ngày 10/11 chỉ là **không có cập nhật mới tại thời điểm check**, không phủ định báo cáo sau về việc thu và phân tích offline incremental 81→87. [Báo cáo OTA](../firmware/ota-delta-validation-v10.md).
3. **EDL H032–H034 vs lịch sử unlock/backup sau:** ở H032 Fastboot vẫn báo main locked, dù cho phép yêu cầu unlock. H033–H034 mới có GPT/Firehose READ, chưa có bộ phục hồi. Về sau mới xuất hiện [42/42 partition IMG](../firmware/emmc-backup-verification.md) và [OEM unlock reported PASS](../boot/oem-unlock-research.md). Không ghép các thử nghiệm khác ngày thành một phiên thống nhất.

## Các chuyên đề chi tiết đã có trong kho

- [VDEX FOTA](../firmware/fota-vdex010-dequickening-evidence.md) và [UService VDEX](../system/uservice-vdex010-recovery-progression.md)
- [UCloudlink ELF](../network/ucloudlink-elf-library-symbol-inventory.md), [MQTT/socket](../network/ucloud-daemons-and-sockets.md), [init](../system/init-service-map.md), [uknet.ko](../hardware/uknet-kernel-module.md)
- [OTA FOTA cũ](../firmware/fota-update-history.md), [hỗ trợ OEM](../firmware/oem-firmware-sources-and-support.md), [EDL](../firmware/edl-firehose-diagnostics.md), [GPT](../firmware/gpt-layout.md)
- [Đối chiếu chi tiết H007–H013](h007-h013-initial-baseline-reconciliation-20261124.md)

**Phạm vi công bố:** không chép binary OEM (APK, VDEX, ELF, firmware), configuration có credential, địa chỉ máy chủ có thông tin xác thực, IMEI/serial, SoftSIM/NV, file private Dropbox hoặc log nguyên văn. Các báo cáo này **chỉ xác nhận độ phủ chủ đề**, không phải chứng nhận đính kèm được kiểm duyệt hết.
