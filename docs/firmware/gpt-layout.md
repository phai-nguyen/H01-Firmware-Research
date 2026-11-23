# Bảng GPT/eMMC H01 đã lược bỏ định danh

**Bản quan sát:** 11/11/2026 · ZEUS H01 / GlocalMe K1 · chỉ dùng cho nghiên cứu.

[Tải bảng CSV gồm 42 phân vùng](partition-layout-sanitized.csv). Bảng đã loại bỏ `unique_guid`, `type_guid`, DiskGUID, CRC chi tiết và mọi byte dữ liệu phân vùng. Nó giữ lại **thứ tự phân vùng, tên, LBA đầu/cuối, số sector và kích thước** để so sánh cấu trúc, không phải tập tin phân vùng để flash.

## Bằng chứng và phương pháp

- Nguồn riêng: `/H01/EMMC/H01-partitions-20261111.csv`, đối chiếu `/H01/EMMC/H01-GPT-map-20261111.txt` trên Dropbox.
- Sector size của bản thu thập: **512 byte**; GPT báo **44 entry**, trong đó **42 entry được dùng**.
- GPT chính và dự phòng trong bản chụp đã được báo cáo **CRC32 PASS**, mảng entry byte-identical.
- Dung lượng phương tiện suy từ backup GPT: **7.818.182.656 byte** (xấp xỉ **7,281 GiB**).
- Bảng được tái cấu trúc từ file báo cáo đã phân tích; phép kiểm tra trong CI xác minh kích thước/tính không chồng lấn trên **CSV này**, không xác minh lại ảnh GPT binary gốc.

## Các phân vùng đáng chú ý

| Tên | Kích thước | Ý nghĩa khái quát |
| --- | ---: | --- |
| `boot` | 32 MiB | Ảnh khởi động Android |
| `recovery` | 32 MiB | Ảnh môi trường Recovery |
| `system` | 1.228,8 MiB | Phân vùng Android system |
| `vendor` | 500 MiB | Thành phần riêng của nhà cung cấp |
| `splash` | 10 MiB | Dữ liệu màn hình khởi động cần nghiên cứu thêm |
| `userdata` | ≈ 5.188,48 MiB | Dữ liệu cá nhân, tuyệt đối không công khai |

Các vị trí được trích từ một thiết bị và một phiên bản. **Không dùng CSV này làm rawprogram, lệnh `dd`, thông số QFIL hoặc cấu hình flash**. Các máy H01 khác có thể sử dụng partition layout khác. Việc GPT PASS không chứng minh mọi ảnh `.img` được sao lưu đúng vùng hay có khả năng phục hồi.

## Đối chiếu an toàn

Không dùng lệnh ghi đè eMMC. Chỉ đọc metadata/partition list trên thiết bị khác bằng bộ [ADB read-only](../tools/read-only-report.md) và so sánh tên, kích thước; nếu khác, ghi nhận là biến thể mới thay vì cố ép lại bản đồ này.
