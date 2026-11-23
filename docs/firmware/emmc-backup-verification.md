# eMMC H01: kiểm tra 42 phân vùng, nhiều thế hệ ảnh sao lưu

**Nguồn:** nhật ký Notion H01 mục 95 và 98 (11/11/2026) cùng bảng GPT công khai. **Trạng thái: BACKUP COPY INTEGRITY REPORTED PASS, chưa xác minh restore.**

## Phải phân biệt hai mốc báo cáo

| Báo cáo | ZIP đọc hoàn chỉnh | IMG trong ZIP | IMG ngoài ZIP | MATCH |
| --- | ---: | ---: | ---: | ---: |
| Kiểm tra ban đầu, mục 95 | 18 | 41 | 1 userdata | 42/42 |
| Báo cáo mới hơn, mục 98 | 19 | 45 | 1 userdata | **46/46** |

**Giải thích số đếm:** Lần 98 đã bổ sung dữ liệu thiếu và chứa các IMG khác thế hệ cùng hai ảnh GPT metadata; do đó **46 đối tượng IMG được kiểm tra không có nghĩa GPT có 46 phân vùng**. Bản đồ GPT vẫn chứa **42 phân vùng được sử dụng**. Báo cáo cuối ghi **42/42 tên phân vùng GPT có ảnh sao lưu tương ứng**, đồng thời giữ những thế hệ boot/recovery cũ.

Công cụ xác minh trên iPhone đọc ZIP member đến EOF để kiểm tra CRC và tính SHA-256 so với sidecar; bản userdata độc lập cũng được kiểm tra hash. Nội dung userdata/partition **không được đưa vào GitHub**.

## Chứng cứ chứng minh điều gì?

**Được ghi nhận:** bản sao IMG ở vị trí kiểm tra khớp với checksum đi kèm; ZIP đọc được không lỗi; kiểm kê đủ ảnh theo tên 42 phân vùng.

**Không được chứng minh chỉ bằng kiểm tra này:** mọi lần đọc trên H01 đúng tuyệt đối dải LBA, nguồn dump có chữ ký OEM, mọi thành phần ngoài User Area đã được sao lưu hoặc có thể ghi lại ảnh để cứu hộ. Sidecar tự sinh khi sao lưu xác nhận **tính nhất quán bản sao**, không tự xác nhận **tính xác thực firmware**.

## Chuẩn xử lý kỹ thuật khi tiếp tục

1. Bảo toàn ảnh gốc và hash gốc bất biến, không xóa các thế hệ dump trùng tên/khác thời điểm.
2. Đối chiếu từng ảnh với [partition layout](gpt-layout.md): thứ tự, LBA bắt đầu/kết thúc, size byte, thời gian, phương pháp đọc, checksum.
3. Phân tích riêng boot, system, vendor, recovery và chain `sbl1 → aboot → kernel`; kiểm tra dependency.
4. **Tách dữ liệu đặc thù máy** (`userdata`, `modemst*`, `fsg*`, `persist`, `productinfo`, `keystore`, `ssd`, SoftSIM) khỏi mọi bản public.
5. Không gọi tập IMG hiện có là factory firmware phục hồi chính thức khi chưa có quy trình restore đầu-cuối được kiểm nghiệm.

**Xem thêm:** [bản đồ GPT](gpt-layout.md), [kế hoạch ghép firmware](backup-and-reconstruction.md), [Boot1/Boot2](emmc-boot-areas.md).