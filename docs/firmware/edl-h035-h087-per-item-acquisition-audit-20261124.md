# ZEUS H01 — truy vết 53 mục EDL/eMMC H035–H087 theo từng bước (10–11/11/2026)

**Nguồn:** [Notion tổng H01, H035–H087](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), đối chiếu với [nhật ký batch đã công bố](edl-partition-backup-batches-20261110-11.md), [báo cáo GPT](gpt-dropbox-csv-direct-audit-20261124.md) và [kiểm tra ZIP/iPhone](emmc-iphone-gpt-integrity-timeline.md). **Trạng thái:** biên soạn lịch sử từ ảnh/log và xác nhận trong nguồn, **không thực hiện READ, WRITE, FLASH hoặc tính checksum mới**.

Bảng này tách **53 mục** thành bốn loại chứng cứ quan trọng: `PLAN` (chưa làm ở thời điểm đó), `READ REPORTED` (công cụ báo đọc đủ), `INTEGRITY REPORTED` (hash/ZIP được ghi nhận PASS) và `TRANSFER REPORTED` (bản sao xuất hiện ở iPhone). Các loại này **không thay thế nhau**: 100% progress không chứng minh SHA; SHA khớp không chứng minh đọc đúng LBA; file lên iPhone không chứng minh restore.

## H035–H052 — từng phân vùng boot-chain và chuyển bản sao

| ID | Điều được ghi nhận | Phân loại |
| --- | --- | --- |
| H035 | Đọc `splash` qua Firehose đủ 10.485.760 byte | READ REPORTED |
| H036 | Gói sao lưu splash được người dùng xác nhận chuyển tới iPhone | TRANSFER REPORTED |
| H037 | Gói sao lưu `boot` được xác nhận chuyển tới iPhone | TRANSFER REPORTED |
| H038 | Gói sao lưu `recovery` được xác nhận chuyển tới iPhone | TRANSFER REPORTED |
| H039 | Chốt kế hoạch đọc lần lượt `sbl1/sbl1bak` | PLAN |
| H040 | Đọc `sbl1` qua Firehose | READ REPORTED |
| H041 | Gói `sbl1` được chuyển sang iPhone | TRANSFER REPORTED |
| H042 | Đọc và chuyển `sbl1bak` | READ + TRANSFER REPORTED |
| H043 | Đọc `aboot` và chuyển bản sao | READ + TRANSFER REPORTED |
| H044 | Đọc `abootbak` và chuyển bản sao | READ + TRANSFER REPORTED |
| H045 | Lập kế hoạch đọc `rpm` | PLAN |
| H046 | Đọc `rpm` và chuyển bản sao | READ + TRANSFER REPORTED |
| H047 | Lập kế hoạch đọc `rpmbak` | PLAN |
| H048 | Đọc `rpmbak` và chuyển bản sao | READ + TRANSFER REPORTED |
| H049 | Lập kế hoạch đọc `tz` | PLAN |
| H050 | Đọc `tz` và chuyển bản sao | READ + TRANSFER REPORTED |
| H051 | Lập kế hoạch đọc `tzbak` | PLAN |
| H052 | Đọc `tzbak` và chuyển bản sao đầu 11/11 | READ + TRANSFER REPORTED |

## H053–H060 — công cụ multi-read và batch boot-security

| ID | Điều được ghi nhận | Phân loại |
| --- | --- | --- |
| H053 | Lập kế hoạch đọc `devcfg` từ GPT | PLAN |
| H054 | Đọc nguồn EDL upstream, kiểm khả năng nhận danh sách phân vùng | SOURCE ANALYSIS |
| H055 | Ảnh terminal xác nhận EDL v3.62 hỗ trợ đọc tuần tự nhiều mục | TOOL BEHAVIOR REPORTED |
| H056 | Batch `devcfg/cmnlib/cmnlibbak/keymaster/keymasterbak` đọc đủ 5 phân vùng | 5 READ REPORTED |
| H057 | Kiểm SHA-256 và đóng ZIP batch boot-security | INTEGRITY REPORTED |
| H058 | Gói boot-security được chuyển tới iPhone | TRANSFER REPORTED |
| H059 | Đối chiếu GPT, lập kế hoạch `apdp/pad/misc` | PLAN |
| H060 | Batch `apdp/pad/misc` được đọc, kiểm và chuyển | READ + INTEGRITY + TRANSFER REPORTED |

## H061–H068 — bảo toàn dữ liệu trên antiX và batch OEM/CONFIG

| ID | Điều được ghi nhận | Phân loại |
| --- | --- | --- |
| H061 | Sau APDP/PAD/MISC, rà dung lượng trước khi đọc phân vùng lớn | STORAGE PRECHECK |
| H062 | Phát hiện `~/edl` trên overlay antiX Live khoảng 1,5 GiB, không bền khi reboot | HOST STORAGE OBSERVED |
| H063 | Chủ thiết bị chấp thuận dùng phân vùng HDD riêng làm kho sao lưu; đây là lịch sử | CONSENT/PLAN |
| H064 | Ảnh antiX cho thấy đã định dạng ext4 và mount kho H01DATA | HOST OPERATION REPORTED |
| H065 | Kiểm quyền ghi và đường dẫn thư mục lưu bền vững | HOST CHECK REPORTED |
| H066 | Khởi tạo batch `oem/config`, còn chờ H01 vào EDL tại mốc đó | IN PROGRESS HISTORICAL |
| H067 | Báo cáo Firehose hoàn tất đọc `oem/config` vào kho | READ REPORTED |
| H068 | Người dùng xác nhận chuyển đủ bộ IMG/sidecar OEM/CONFIG sang iPhone | TRANSFER REPORTED |

## H069–H078 — system/vendor, boot/product và radio/security

| ID | Điều được ghi nhận | Phân loại |
| --- | --- | --- |
| H069 | Lập kế hoạch batch `vendor/system` theo GPT gốc | PLAN |
| H070 | Firehose báo đọc đủ kích thước `vendor/system` | READ REPORTED |
| H071 | Bốn thành phần IMG/sidecar `vendor/system` được chuyển sang iPhone | TRANSFER REPORTED |
| H072 | Kế hoạch `productinfo/boot/persist/recovery` theo GPT | PLAN |
| H073 | Batch bốn phân vùng được đọc đủ sector/kích thước | 4 READ REPORTED |
| H074 | Tính checksum và chuyển batch bốn phân vùng | INTEGRITY + TRANSFER REPORTED |
| H075 | Lập danh sách 15 phân vùng modem/radio/security cần đọc | PLAN |
| H076 | Log Firehose báo hoàn tất 15 lượt READ | 15 READ REPORTED |
| H077 | Lệnh kiểm 15 sidecar SHA-256 và ZIP được ghi PASS | INTEGRITY REPORTED |
| H078 | Batch radio/security được chuyển tới iPhone | TRANSFER REPORTED |

## H079–H087 — cache, userdata và chốt 42 phân vùng GPT

| ID | Điều được ghi nhận | Phân loại |
| --- | --- | --- |
| H079 | Từ các batch trước xác định còn `cache` và `userdata` chưa thấy bản sao | INTERIM INVENTORY |
| H080 | Firehose báo đọc đủ `cache` | READ REPORTED |
| H081 | Cache đúng 115.343.360 byte, checksum/ZIP và chuyển file ghi PASS | INTEGRITY + TRANSFER REPORTED |
| H082 | Tại mốc này mới chuẩn bị đọc `userdata`, chưa chạy | PLAN |
| H083 | Kiểm dung lượng HDD trước khi đọc `userdata` | STORAGE PRECHECK |
| H084 | Log báo READ 100% và SHA-256 OK cho `userdata` | READ + INTEGRITY REPORTED |
| H085 | Người dùng xác nhận bản sao userdata xuất hiện trên iPhone | TRANSFER REPORTED |
| H086 | Báo cáo kết thúc loạt sao lưu phân vùng đã lên kế hoạch | HISTORICAL SUMMARY |
| H087 | Kiểm kê GPT: file đầu vào có 55 dòng văn bản nhưng **42 entry phân vùng** | GPT INVENTORY |

## 6. Những số đếm không thể hoán đổi

| Con số | Đúng nghĩa của mốc nguồn | Không chứng minh |
| --- | --- | --- |
| **42/42 tên phân vùng** | Danh mục GPT 42 entry có bản sao ứng viên tương ứng | Đầy đủ mọi vùng eMMC, OEM factory ROM, flash/restore PASS |
| **42/42 MATCH** ở lượt đầu | Lần kiểm ZIP/iPhone trước đó kiểm 41 ảnh ZIP + userdata riêng | Có 42 ảnh không trùng thời điểm/không lỗi nguồn |
| **46/46 đối tượng IMG MATCH** ở lượt sau | Các ảnh bổ sung và phiên bản lịch sử/gói GPT làm tổng IMG tăng | GPT có 46 phân vùng |
| **48 IMG và 48 sidecar** trong kiểm kê 18/11 | Danh mục gồm ảnh GPT, Boot Areas và nhiều thế hệ | Tất cả 48 được băm lại tại lượt 18/11 |

Nguồn từng số: [integrity](emmc-backup-verification.md) và [phân tích gap/overlap](user-area-reconstruction-overlap-and-gaps.md). Dải dữ liệu chưa có snapshot trong danh sách mốc 18/11 là **158.953.472 byte** sau khi loại phần GPT primary đã bao phủ, cộng với giới hạn Boot Areas/RPMB và ảnh không đồng thời. Không có bản User Area raw clone đầy đủ được công bố.

## 7. Các bẫy khi tái sử dụng nhật ký

1. **Không coi `PLAN` là PASS:** ví dụ H082 chưa đọc userdata, nhưng H084 đã ghi READ/SHA thành công ở thời điểm sau.
2. **Không phát lại thao tác format HDD** ở H063–H064: đó là quyết định được chấp thuận trong phiên antiX 11/11, không phải bước cần chạy lại để xem báo cáo.
3. **Đọc nhiều phân vùng không phải snapshot nguyên tử:** dữ liệu `devinfo`, `boot`, `recovery` hoặc phân vùng modem ở các thời điểm có thể đã thay đổi.
4. **Vùng riêng cần bảo vệ:** `userdata`, `modemst*`, `fsg*`, `persist`, `productinfo`, `keystore`, `config`, `devinfo`, boot chain/firmware OEM và định danh thiết bị không được đăng lên repository công khai.
5. **Không suy ra có factory ROM:** thiếu đọc/xác minh đầy đủ Boot Areas, RPMB, các khoảng ngoài partition, bộ ảnh nguyên tử và quy trình rescue end-to-end.

## 8. Đầu việc chứng cứ còn mở

- Rà lại từng ảnh CMD/TXT/ZIP theo mức độ nhạy cảm, phiên bản và thời điểm; bảng trên chỉ phản ánh **ý chính của 53 mục nguồn**.
- Đối chiếu từng IMG với đúng `partition name + Start LBA + End LBA + size`; công cụ [audit partition](../tools/partition-inventory-audit.md) hiện chỉ đối chiếu tên/kích thước bằng metadata, **chưa kiểm dữ liệu từng LBA**.
- Chưa có thử nghiệm phục hồi thực địa trên H01 mất boot hoặc kiểm chứng full User Area và Boot Areas. Không đăng programmer OEM, partition IMG, ZIP userdata, key hoặc XML ghi eMMC.

**Kết luận:** 53/53 đề mục H035–H087 nay có một dòng truy vết riêng. Đây là **kiểm kê độ phủ kết luận**, tuyệt đối **không** có nghĩa 53/53 file đính kèm đã được công bố hoặc toàn bộ sao lưu đủ để flash cứu hộ.
