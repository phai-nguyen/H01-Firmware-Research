# H01 — kiểm toán 42 mục Notion H100–H141: boot, Secure World, EDL và MMC

**Nguồn duy nhất:** [Trang tổng Notion H01 — mục H100–H141](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), các ghi chép 11–14/11/2026. **Tình trạng:** tổng hợp theo mốc, không tái chạy phân tích nhị phân, không gửi lệnh mới tới H01 và không sử dụng nguồn chưa ghi trên Notion. Các con số/phát hiện được trình bày là kết quả **được lưu trong nhật ký**, không phải tái kiểm chứng trực tiếp ở lần công bố này.

Bốn nhánh dưới đây tách rõ **trạng thái thiết bị được quan sát**, **phân tích tĩnh**, **kế hoạch** và **lỗi host**. Đặc biệt, câu `secure:no` hay `OKAY` **không đủ** để kết luận fuse Secure Boot hoặc bootloader unlock thành công.

## H100–H105 — Boot image, ABOOT và Fastboot

| ID | Nội dung được Notion ghi nhận | Mức bằng chứng |
| --- | --- | --- |
| H100 | Tệp boot 32 MiB khớp GPT; đã khảo sát kernel/ramdisk, fstab, verity và các init riêng; chưa xác nhận restore | BINARY STATIC |
| H101 | Từ property và dump lúc đầu chỉ có dấu hiệu hỗ trợ OEM unlock; trạng thái thực tế khi đó vẫn khóa | BASELINE / NOT YET PASS |
| H102 | Bản ABOOT chứa callback OEM unlock/get_unlock_ability, nhưng sự hiện diện của mã không chứng minh mở khóa thực địa | BINARY STATIC |
| H103 | Đối chiếu ZIP CONFIG/DEVINFO và trạng thái metadata, phát hiện cần kiểm lại với snapshot Android không nhất quán thời điểm | BINARY STATIC / INFERENCE |
| H104 | Lần truy vấn Fastboot trực tiếp trên H01, trạng thái main unlock chưa thay đổi | DEVICE OBSERVED |
| H105 | Giải thích output getvar/secure/Verified Boot; secure:no không tự chứng minh Qualcomm fuse bị tắt | OBSERVED + ANALYSIS |

## H106–H116 — Boot verifier, Secure World và điều kiện unlock

| ID | Nội dung được Notion ghi nhận | Mức bằng chứng |
| --- | --- | --- |
| H106 | Rà sâu đường SCM secure-state, image validation và flash policy; chưa có UART/QFPROM bằng chứng fuse | STATIC / OPEN |
| H107 | Phân tích callback và nhánh boot_verifier; câu cảnh báo Continue không đồng nghĩa bỏ qua mọi xác minh | STATIC / LIMITED |
| H108 | Đối chiếu QSEE version và secure-state helper; chưa có raw response thực tế xác định fuse | STATIC / OPEN |
| H109 | Hiệu chỉnh call graph để tách boot verification khỏi Fastboot flash gate; kết luận cũ về nhánh bypass được thu hẹp | CORRECTED STATIC |
| H110 | Tìm cấu trúc keystore trong ABOOT; Secure World software-fuse API không phải chứng minh burn fuse QFPROM vật lý | STATIC / SENSITIVE OMITTED |
| H111 | Rà Root of Trust/keystore và thông báo tamper; log bootloader chưa đủ để chốt chính sách runtime | STATIC / OPEN |
| H112 | Mô hình chữ ký image SHA-256 + RSA; GREEN/OEM key, YELLOW/embedded certificate, RED/failure; không suy YELLOW là vô xác minh | STATIC MODEL |
| H113 | Log Android ghi Keymaster TA 3.120, HAL 3.0, RPMB/SSD listener; không chứng minh bootloader verification state | RUNTIME SNAPSHOT |
| H114 | Phân biệt ro.boot.keymaster property, TA đang chạy và ABOOT Root-of-Trust call; không gộp làm một PASS | EVIDENCE CORRECTION |
| H115 | Đối chiếu ABOOT/DEVINFO với kết quả Fastboot; sửa lỗi diễn giải trường charger screen/critical status | CORRECTED STATIC |
| H116 | Từ disassembly ghi đường unlock yêu cầu xác nhận và wipe; ở mốc 13/11 chưa có phép thử PASS trên thiết bị | STATIC / PLAN |

## H117–H126 — Kho sao lưu và Firehose: từ lỗi host tới NOP ACK

| ID | Nội dung được Notion ghi nhận | Mức bằng chứng |
| --- | --- | --- |
| H117 | Kiểm kê Dropbox lúc đó có 42/42 ảnh phân vùng và userdata + sidecar, không phải full eMMC clone | FILE INVENTORY |
| H118 | Đọc đúng cơ chế Persistent Data Block; 42 ảnh không bao gồm mọi vùng ngoài User Area/RPMB; no restore PASS | SOURCE REVIEW |
| H119 | Lập kế hoạch chỉ đọc physical partitions; phân biệt GPT boot với eMMC Boot Area | PLAN |
| H120 | Sahara/EDL USB nhận thiết bị; phiên NOP lỗi thiếu đường dẫn programmer trước khi nạp | HOST FAILURE |
| H121 | Kiểm lại host: chưa có đúng tệp programmer tại đường dẫn; bước khắc phục không phải Firehose PASS | HOST DIAGNOSIS |
| H122 | Sau khi có programmer, lỗi missing file hết; ảnh lúc đó mới đến Sahara, chưa xác nhận nạp loader | PARTIAL HOST RECOVERY |
| H123 | Phiên NOP treo ở Sahara khoảng 30 phút; phải phân biệt timeout host với lỗi firmware | HANG REPORTED |
| H124 | Log đầu sau ngắt phiên còn chưa đủ chứng cứ nạp loader; EDL 9008 vẫn enumerate | LOG ANALYSIS |
| H125 | Log debug tiếp theo cho thấy nạp programmer, configure eMMC, READ LBA1, getstorageinfo và NOP ACK | FIREHOSE REPORTED PASS |
| H126 | Ảnh xác nhận Firehose NOP ACK trước lỗi TypeError trong giai đoạn cleanup USB; lsusb còn thấy EDL không chứng minh session cũ hoạt động | ACK + HOST CLEANUP ERROR |

## H127–H141 — EXT_CSD, MMC/SELinux, GPT dự phòng và PPN 1/2

| ID | Nội dung được Notion ghi nhận | Mức bằng chứng |
| --- | --- | --- |
| H127 | Phân tích giới hạn đọc EXT_CSD qua Firehose; không có giao thức raw EXT_CSD đã được xác nhận | RESEARCH / OPEN |
| H128 | Thử đọc debugfs trên Android: điều kiện kernel và quyền shell hạn chế, không xác minh EXT_CSD raw | RUNTIME LIMITED |
| H129 | Kernel hiện RPMB block node 512 KiB; không coi đây là phép đọc raw RPMB hay EXT_CSD | KERNEL OBSERVED |
| H130 | Có đường sysfs raw_rpmb_size_mult nhưng chưa đọc được giá trị do quyền; Boot Areas không thể kết luận từ việc thiếu node | PARTIAL |
| H131 | MMC sysfs/debugfs bị từ chối, không suy RPMB_SIZE_MULT là giá trị đã đọc trực tiếp | PERMISSION OBSERVED |
| H132 | Audit log xác nhận SELinux Enforcing chặn domain shell đọc các thuộc tính MMC; không cần thử lại bằng cách vượt quyền | SELINUX AVC VERIFIED IN REPORT |
| H133 | Đã rà đường liên hệ OEM để xin phương pháp chẩn đoán chỉ đọc; chưa có raw EXT_CSD hoặc loader OEM được xác minh | SUPPORT / OPEN |
| H134 | Phân tích USB/Firehose sau ACK, nguồn lỗi cleanup host; không suy GetStorageInfo là EXT_CSD | HOST DIAGNOSIS |
| H135 | Đọc entry/header GPT backup và khảo sát mapping physical partition tham chiếu; không nhầm Boot Area với GPT | GPT META |
| H136 | GetStorageInfo cho PPN1 trả metadata kích thước ứng viên Boot1; chưa phải IMG payload | METADATA ACK |
| H137 | GetStorageInfo cho PPN2 có cùng kích thước ứng viên Boot2; chưa chứng minh có nội dung bootloader | METADATA ACK |
| H138 | Kiểm kê kho riêng trước đọc, phân biệt `boot.img` GPT 32 MiB với Boot Area 4 MiB | INVENTORY / PLAN |
| H139 | Bản IMG/sidecar/log PPN1 có trong Dropbox, nhưng tại mốc đó nội dung log chưa được kiểm trực tiếp toàn bộ | FILE PRESENCE / OPEN |
| H140 | Log PPN1 cho biết READ đủ 4 MiB; payload trả về zero-filled, chưa xác nhận đúng Boot Area vật lý | READ REPORTED; CONTENT UNKNOWN |
| H141 | PPN2 cũng trả 4 MiB zero-filled, cùng kết quả PPN1; **không chứng minh hai Boot Areas thực sự trống** | READ REPORTED; CONTENT UNKNOWN |

## Hiệu chỉnh cần giữ lại khi công bố

### H104–H116: Không suy kết quả boot từ nhãn đơn

1. `fastboot secure:no` không đồng nghĩa QFPROM secure-boot fuse đã tắt. Phân tích ABOOT ghi nhận các tình huống SCM trả lỗi hoặc trả response không thỏa điều kiện; **chưa có raw QFPROM**, UART bootloader hoặc SCM response để chốt trạng thái phần cứng.
2. Trạng thái `Device critical unlocked`, `Device unlocked` và `get_unlock_ability` có ý nghĩa khác nhau. Báo cáo này **chỉ mô tả baseline 11–14/11**; kết quả `unlocked` về sau được ghi tại [nghiên cứu 18/11](../boot/oem-unlock-research.md).
3. Nhánh `boot_verifier` và quyền flash Fastboot cần phân tích tách biệt: mã có bước kiểm tra image signature không tự mở tất cả cổng flash; `GREEN`, `YELLOW`, `RED` là **trạng thái xác minh**, không phải nhãn hiệu năng hoặc quyền root.
4. Runtime Keymaster/RPMB listeners trong Android **không chứng minh** bootloader đã xác thực tất cả keystore và không suy Secure World/QFPROM như nhau. Các sửa lỗi diễn giải đã ghi trong H109, H114 và H115 được ưu tiên so với nhận định cũ.

### H120–H126: NOP ACK khác lỗi cleanup USB

Một phiên cũ lỗi tìm file programmer; phiên khác dừng tại Sahara. Chỉ **log debug ở H125 và ảnh H126** mới cho phép ghi rõ loader được nạp, lệnh NOP nhận **ACK** và việc đọc LBA1 ở thời điểm đó được báo PASS. Lỗi Python `TypeError` ở giai đoạn cleanup host **không đảo ngược ACK** đã nhận; USB vẫn hiện diện ở 9008 **không chứng minh** phiên Firehose cũ còn đang mở.

### H127–H141: Trống dữ liệu trả về không đồng nghĩa chip trống

Theo Notion, **PPN1 và PPN2** đều trả các ảnh **4.194.304 byte (4 MiB)** gồm byte `0x00` trong lần READ qua generic programmer. Chưa có chứng cứ độc lập rằng loader ánh xạ chính xác hai eMMC Boot Areas vật lý hoặc rằng eMMC Boot Areas thực tế đều trống. Các ảnh này chỉ mang trạng thái **ZERO-FILLED / NOT VERIFIED FOR RESTORE**. Kernel xuất hiện RPMB 512 KiB nhưng đó là namespace lưu trữ có xác thực, không thuộc 42 GPT partitions của User Area. Không công bố phương án đọc/ghi RPMB, cấp khóa hoặc thay `PARTITION_CONFIG`.

## Những giới hạn chưa đóng

- **Không có** thử nghiệm phục hồi firmware end-to-end từ bộ ảnh sao lưu.
- **Không có** phép xác thực toàn bộ boot chain, fuse QFPROM hay Secure World trên mọi H01.
- **Không có** EXT_CSD raw đã được kiểm chứng từ H01 tại các mốc trên; việc ước tính thuộc tính từ kích thước node không tương đương đọc raw.
- Một số kết luận nguồn ban đầu là kế hoạch; báo cáo chỉ đưa nội dung **đã ghi nhận trong Notion**, không coi kế hoạch là công việc đã chạy.

**Tham khảo các báo cáo đã có:** [ABOOT/Verified Boot](../boot/boot-verification-chain.md), [QSEE](../boot/qsee-keymaster-rpmb-runtime-evidence.md), [Sahara/Firehose](../firmware/edl-sahara-firehose-failure-to-success.md), [MMC EXT_CSD](../firmware/mmc-extcsd-access-investigation.md), [Boot Areas](../firmware/emmc-boot-areas.md), [khôi phục](../boot/recovery-readiness.md).

**Chính sách công bố:** không đính kèm raw dump ABOOT/DEVINFO, file programmer OEM, log chứa định danh, địa chỉ/offset patch, thông tin khóa hoặc hướng dẫn ghi/xóa/thay đổi bảo mật eMMC. Đây là **42 dòng phân loại chứng cứ**, không chứng nhận mọi ảnh/log của 42 mục được đưa lên GitHub.
