# GPT 42 phân vùng H01 không phải bản sao full eMMC — các khoảng ngoài GPT

**Nguồn trực tiếp:** [Notion H01 H087, H095–H099, H118 và H135](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), 11–14/11/2026. **Trạng thái: GPT và tính nhất quán dữ liệu sao lưu đã được ghi PASS; khả năng phục hồi toàn bộ eMMC CHƯA KIỂM CHỨNG.**

## Geometry và bảng GPT

Firehose báo User Area **15.269.888 sector × 512 byte**. GPT sao lưu cho **42 entry phân vùng được dùng**, cùng các metadata GPT; bản sao GPT dự phòng có **44 entry × 128 byte** (42 có dữ liệu + 2 trống).

Trong lần đọc lại ngày 14/11:
- Đọc **11 sector** GPT backup entries, đúng **5.632 byte**.
- Entry-array CRC32 tính lại **0x328365AD**, bằng trường lưu trong backup header.
- Backup header CRC32 tính lại **0x68C2E96F**, bằng trường lưu trong header.
- Không thấy entry phân vùng chồng lấn; 42 tên, LBA đầu/cuối và kích thước khớp CSV đã lược bỏ GUID.

## Ngoài 42 phân vùng còn có gì?

Hồ sơ đã chỉ ra các khoảng **không thuộc entry phân vùng GPT**, ví dụ:

| LBA khoảng trống | Số sector | Kích thước |
| --- | ---: | ---: |
| **34–131071** | 131.038 | 67.091.456 byte |
| **284768–393215** | 108.448 | 55.525.376 byte |
| **3467880–3538943** | 71.064 | 36.384.768 byte |

Các khoảng ví dụ này không bao quát tất cả gap trong eMMC. Không được suy toàn bộ các gap chứa dữ liệu, hay tất cả đều có thể ghi zero an toàn. **Sao lưu 42/42 ảnh partition không tương đương full User Area raw clone**, chưa kể PPN1/2 và RPMB.

## Đối chiếu các mốc backup

| Báo cáo | Phạm vi đã xác minh |
| --- | --- |
| Kiểm tra ban đầu | 18 ZIP, 41 IMG bên trong + 1 IMG độc lập → **42/42 MATCH** |
| Kiểm tra cập nhật | 19 ZIP, 45 IMG bên trong + 1 IMG độc lập → **46/46 MATCH** |
| Bảng mapping GPT | **42/42 tên phân vùng** có ảnh tương ứng; IMG thừa gồm metadata GPT, ảnh lịch sử |

Gói ảnh có sidecar SHA-256 khớp **là integrity của bản sao**, không chứng minh mọi dữ liệu gốc được EDL đọc đúng LBA. ZIP CRC không xác nhận ảnh có chữ ký OEM hoặc máy có thể boot sau restore. Nhóm dữ liệu `modemst*`, `fsg*`, `persist`, `userdata`, `devinfo`, `productinfo` và SoftSIM là **đặc thù từng máy**, không tạo firmware dùng chung.

## Kết luận công bố

- **PASS theo nguồn:** GPT header/entry-array CRC, 42 partition names, ZIP/IMG sidecar integrity theo mẫu đã kiểm.
- **CHƯA PASS:** full eMMC image, dữ liệu gaps, Boot Areas vật lý, xác thực factory ROM, restore end-to-end.
- **Không đưa lên GitHub:** IMG/ZIP/manifest riêng, GPT chứa Disk GUID và Unique GUID, số định danh, XML ghi, token, loader.

Xem [bảng GPT công khai](gpt-layout.md), [xác minh backup](emmc-backup-verification.md), [readiness](../boot/recovery-readiness.md).