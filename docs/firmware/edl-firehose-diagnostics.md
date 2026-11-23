# EDL 9008, Sahara và Firehose — phân biệt READ với ghi flash

**Nguồn:** nhật ký Notion H01 các mốc 10/11 và 14/11/2026, đặc biệt mục 32, 115–123, 132. **Trạng thái: Firehose handshake/read/GPT đã được kiểm chứng trong log trên H01 thử nghiệm.**

## Chứng cứ theo thời gian

| Bước | Bằng chứng |
| --- | --- |
| USB EDL | Thiết bị nhận diện ở chế độ Qualcomm `05c6:9008` |
| Sahara | Host/device handshake, gửi programmer tới RAM và `END_TRANSFER SUCCESS` trong log 14/11 |
| Firehose | `configure` ACK, `MemoryName=eMMC`, `TargetName=8909` |
| Đọc GPT | Truy vấn sector LBA 1 của physical partition 0 (512 byte) có magic `EFI PART` |
| StorageInfo | User Area: **15.269.888 sector × 512 byte = 7.818.182.656 byte** |
| NOP | Firehose trả ACK; client báo `Nop succeeded` |
| GPT | 42 phân vùng được nhận diện; bảng riêng đã [lược bỏ GUID](gpt-layout.md) |

Rà XML TX của **phiên log 14/11/2026** ghi nhận đúng các loại command: `configure`, `read`, `getstorageinfo`, `nop`. Không thấy TX `program`, `erase`, `patch`, `poke` trong phiên **được phân tích đó**. Dữ liệu ELF programmer được truyền ở giai đoạn Sahara là **nạp vào RAM**, không phải lệnh Firehose ghi eMMC.

## Cảnh báo bắt buộc

- Programmer có dấu vết tĩnh cho `program`, `erase`, `patch`, `poke`, `read`...; **không được gọi là chỉ đọc** vì tên file có chữ `peek`.
- Firehose `SkipWrite=0` trong cấu hình đã ghi: **không có khóa write-protect ở tầng giao thức**. Việc một phiên không gửi lệnh ghi không chứng minh những phiên khác cũng an toàn.
- Trường `num_physical_partitions=3` không tự chứng minh ánh xạ Boot1/Boot2/RPMB; cần xét đặc thù programmer và kết quả trực tiếp.
- Một số phiên NOP ban đầu treo hoặc gặp lỗi cleanup USB sau ACK. Không nhầm lỗi cleanup ở host với thất bại đọc GPT/handshake; phải đọc trình tự đầy đủ.
- Đã có cảnh báo SELinux AVC từ Android shell khi đọc MMC sysfs/debugfs. Không tắt SELinux hay đổi `EXT_CSD` để vượt hạn chế.

Không đăng programmer ELF, serial/HWID/PK_HASH đầy đủ, token, full log hoặc trích dữ liệu định danh. Không cung cấp XML ghi/erase hoặc flash hàng loạt vào kho công khai.

**Xem thêm:** [sao lưu và kiểm tra 42 ảnh](emmc-backup-verification.md), [Boot1/Boot2](emmc-boot-areas.md), [bản đồ GPT](gpt-layout.md).