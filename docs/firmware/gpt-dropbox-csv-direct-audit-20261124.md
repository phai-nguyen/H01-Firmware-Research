# H01 — đối chiếu trực tiếp GPT trên Dropbox với CSV GitHub

**Nguồn:** Dropbox `H01-GPT-map-20261111.txt` (báo cáo GPT ngày 11/11/2026) và [bảng CSV đã lược định danh](partition-layout-sanitized.csv) trong repository. **Đối chiếu metadata trong hai báo cáo**, không phải đọc eMMC hoặc xác minh IMG mới.

## Kiểm tra 42 phân vùng

Đọc toàn bộ **42 dòng PARTITION MAP** từ báo cáo GPT, so với 42 dòng CSV ở cùng thứ tự. Các trường được đối chiếu: số thứ tự, tên phân vùng, Start LBA, End LBA, sector count và `size_bytes = sectors × 512`. **Kết quả: 42/42 khớp đầy đủ, 0 trường sai khác.**

| Phép kiểm nội bộ báo cáo GPT gốc | Kết quả |
| --- | --- |
| Primary header CRC32 | PASS, `AF6A17BB` |
| Primary entry-array CRC32 | PASS, `328365AD` |
| Backup header CRC32 | PASS, `68C2E96F` |
| Backup entry-array CRC32 | PASS, `328365AD` |
| Primary/backup reciprocal LBA pointers | PASS |
| Primary/backup entry-array content | Báo cáo ghi **byte-identical** |
| Số entry GPT | 44, có 42 entry được sử dụng |
| User Area | 15.269.888 sector × 512 = **7.818.182.656 byte** |

## Các khoảng không thuộc phân vùng, trong usable range

| Khoảng LBA | Sector | Dung lượng byte |
| --- | ---: | ---: |
| 34–131071 | 131.038 | 67.091.456 |
| 284768–393215 | 108.448 | 55.525.376 |
| 3467880–3538943 | 71.064 | 36.384.768 |
| **Tổng ba gap** | **310.550** | **159.001.600** |

Các gap là vùng **không có entry GPT**, không chứng minh chúng trống, bằng zero hay an toàn để ghi. Kết quả trên không bao gồm vùng Boot0/Boot1/RPMB ngoài User Area.

## Mức độ chứng cứ

- **VERIFIED IN TWO REPORTS:** dữ liệu metadata 42 entry khớp tại thời điểm đọc hai tài liệu và các phép CRC được ghi PASS.
- **NOT VERIFIED:** từng ảnh IMG đọc đúng byte từ LBA, restore thực địa, tính nguyên bản OEM, khả năng dùng bảng này trên mọi H01.
- **PRIVATE:** Disk GUID/Unique GUID/Type GUID, raw IMG, SHA-256 thiết bị, dữ liệu SIM/NV và userdata không được sao chép sang GitHub.

Xem [GPT tổng quan](gpt-layout.md), [bản đồ các khoảng trống](gpt-unallocated-regions-and-integrity.md) và [kiểm toán iPhone](emmc-iphone-gpt-integrity-timeline.md).