# Khảo sát eMMC physical partition 1 và 2 (Boot1/Boot2)

**Nguồn:** nhật ký Notion H01 mục 132, 137 và 138 (14/11/2026). **Trạng thái: READ ACK + payload ZERO-FILLED, ý nghĩa Boot Area chưa xác nhận.**

## Dữ liệu thu thập từ Firehose

| Thông số | Physical partition 1 | Physical partition 2 |
| --- | --- | --- |
| Sector bắt đầu | 0 | 0 |
| Số sector | 8.192 | 8.192 |
| Sector size | 512 byte | 512 byte |
| Payload đọc | 4.194.304 byte | 4.194.304 byte |
| Nội dung tái dựng từ log | Toàn `0x00` | Toàn `0x00` |
| Giao thức | `rawmode=true` ACK → payload → `rawmode=false` ACK | Tương tự |
| Đối chiếu sidecar | SHA-256 khớp | SHA-256 khớp |

**Kết luận chính xác:** generic Firehose programmer đã trả **hai payload 4 MiB toàn số 0** và tiến trình đọc đạt 100% cho cả PPN 1 và PPN 2. Báo cáo còn đối chiếu byte được tái dựng từ log với ảnh lưu trong kho riêng. **Không được suy ra Boot Area vật lý trên chip chắc chắn trống**; có thể là vùng chưa sử dụng, hoặc cơ chế ánh xạ/đọc của programmer không phản ánh Boot Area thực.

Không nhầm phân vùng `boot` trong GPT của User Area với Boot Area phần cứng PPN 1/2. Hai ảnh zero-filled này **không phải bộ bootloader có thể phục hồi**.

## RPMB / EXT_CSD

SELinux AVC của `u:r:shell:s0` trong firmware đang Enforcing đã chặn đọc sysfs MMC và debugfs. Giá trị `EXT_CSD` thực tế (boot selection, multiplier) **chưa đọc được**. RPMB không được thăm dò, provision key hoặc ghi; không đọc/ghi raw RPMB qua các lệnh block thông thường.

**Hướng tiếp theo:** so sánh tài liệu/mã nguồn programmer thật với kết quả từ một cơ chế chẩn đoán đọc chính thức, nếu có; không thay đổi boot selection, `EXT_CSD`, SELinux hay chạy `program/erase/patch/poke`.

**Liên quan:** [Firehose](edl-firehose-diagnostics.md), [kiểm tra sao lưu](emmc-backup-verification.md).