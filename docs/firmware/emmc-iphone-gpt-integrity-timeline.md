# H01 — kiểm tra ZIP/IMG trên iPhone và GPT CRC (11–14/11/2026)

**Nguồn:** [Notion H087–H099, H117 và H135](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Kiểm tra tính nhất quán bản sao**, chưa phải thử phục hồi.

| Mốc | Kết quả được ghi trong nhật ký |
| --- | --- |
| AntiX sau READ | Sidecar SHA-256 của các batch hoàn tất báo `OK`; ZIP được kiểm CRC |
| iPhone: GPT raw | Hai ảnh primary/backup trong ZIP được kiểm SHA-256: **MATCH** |
| iPhone: system/vendor | Hai ảnh trong ZIP được tính SHA-256 theo luồng: **MATCH** |
| Kiểm toàn bộ lần đầu | **18 ZIP, 41 IMG trong ZIP, 1 userdata riêng = 42/42 MATCH**, REVIEW 0, ZIP errors 0 |
| Kiểm cập nhật | **19 ZIP, 45 IMG trong ZIP, 1 userdata riêng = 46/46 MATCH**, REVIEW 0 |
| Đối chiếu tên GPT | **42/42 tên phân vùng** có ảnh ứng viên đúng kích thước |

**46 IMG không phải 46 partition**: một số ảnh là metadata GPT hoặc bản boot/recovery khác thế hệ.

## GPT raw và CRC

Hai bản raw GPT primary và backup được đọc từ **128 sector × 512 byte = 65.536 byte mỗi bản**, kiểm hash và đóng gói riêng. Các kiểm tra đã PASS: header CRC32, entry-array CRC32 của primary/backup, pointer trỏ qua lại, phạm vi usable LBA, Disk GUID đối chiếu và hai bảng entry phù hợp.

Trong lượt đọc backup entries độc lập 14/11, **11 sector = 5.632 byte**, 42 entry có dữ liệu và 2 entry trống. CRC32 entry array **0x328365AD** và backup header **0x68C2E96F** khớp trường ghi trên disk tại thời điểm thu.

## Kết luận với giới hạn

- **PASS:** cấu trúc GPT, checksum bản sao và ZIP CRC tại lần kiểm đã ghi.
- **Chưa PASS:** chứng minh đúng tuyệt đối các LBA gốc, xác thực chữ ký OEM, raw clone cả eMMC (kể cả gaps/Boot Area) hay quy trình cứu hộ đầu-cuối.
- **Giữ riêng:** IMG/ZIP, userdata, Disk GUID/Unique GUID, serial, dữ liệu SIM/SoftSIM và log kiểm tra.

Xem [nhật ký batch](edl-partition-backup-batches-20261110-11.md), [GPT gaps](gpt-unallocated-regions-and-integrity.md).