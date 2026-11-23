# Điều kiện sẵn sàng cứu hộ firmware H01 — checklist đánh giá

**Trạng thái: READINESS CHECKLIST / NOT A VERIFIED RESTORE PROCEDURE.** Tổng hợp các ghi chép sao lưu eMMC, EDL/Firehose, root và boot trên H01 trong tháng 11/2026.

## Năng lực đã được ghi nhận

- EDL 9008, Sahara và Firehose: có log hoàn thành configure, đọc GPT, getstorageinfo, NOP và nhiều thao tác READ theo tên phân vùng.
- GPT eMMC User Area: **42 entry phân vùng được sử dụng**; bảng backup GPT đã đối chiếu CRC trong nhật ký.
- Integrity check của kho lưu trên iPhone: báo cáo mới hơn ghi **46/46 IMG đối tượng MATCH**, đại diện đủ tên **42/42 phân vùng GPT**, bao gồm các thế hệ dump/metadata bổ sung.
- Boot1/Boot2 phần cứng: programmer generic trả hai ảnh 4 MiB **zero-filled**, chưa xác minh là nội dung vật lý thực; không dùng làm bootloader rescue.
- Magisk root qua RAM và boot cố định đã PASS trên cấu hình thử; Auto Power-On v0.6 và module liên quan đã có thử nghiệm, nhưng không có phép đo endurance hoặc restore nguyên bộ.

## Điều kiện chưa được xác nhận

| Tiêu chí | Trạng thái |
| --- | --- |
| Bảng manifest từng image: source device/time/build/partition/LBA/size/hash | Cần chuẩn hóa và đối chiếu đầy đủ |
| Tính toàn vẹn bản sao chuyển kho | Có kết quả hash; cần giữ bản bất biến và kiểm tra định kỳ |
| Full physical storage gồm mọi vùng ngoài GPT | **Chưa chứng minh** |
| Phân biệt dữ liệu đặc thù thiết bị và firmware dùng chung | **Bắt buộc trước mọi thao tác restore** |
| Cơ chế EDL/Firehose chỉ đọc ở mức cưỡng chế | **Không có**: programmer có lệnh ghi, SkipWrite=0 |
| Quy trình phục hồi từ tình trạng hỏng boot thật | **Chưa kiểm nghiệm đầu-cuối** |
| Tương thích phiên bản phần cứng / OEM revision khác | **Chưa xác minh** |
| Bộ ảnh factory ROM chính thức có chữ ký | **Chưa có chứng cứ** |

## Phân vùng dữ liệu phải giữ riêng tư và không ghép chéo

`userdata`, `modemst1`, `modemst2`, `fsg*`, `persist`, `keystore`, `keymaster`, `productinfo`, `devinfo`, `fsc`, `ssd`, SoftSIM, cấu hình NV và định danh phần cứng. **Không dùng bản sao một H01 để ghi mù vào máy khác**.

## Quy trình đánh giá không can thiệp thiết bị

1. Xác minh checksum của những file bản sao đã lưu bằng [công cụ ngoại tuyến](../tools/backup-hashes.md); không tạo dump trùng không cần thiết.
2. Kiểm tra CSV GPT đã loại bỏ GUID và mapping theo tên/size, không thay GPT.
3. Đối chiếu source/target firmware và các generation của boot/recovery, giữ mọi bản gốc read-only.
4. Ghi rõ từng câu hỏi chưa giải quyết ở [backlog](../research/publication-backlog.md).
5. Chỉ xây dựng kịch bản phục hồi có khả năng ghi sau khi đã chứng minh đường rollback cho đúng thiết bị và có phê duyệt rõ.

**Đây là tài liệu quản lý rủi ro, không phải hướng dẫn flash**; không cung cấp rawprogram XML, patch DEVINFO hoặc lệnh format/erase phân vùng.

**Liên quan:** [Firehose](../firmware/edl-firehose-diagnostics.md), [42 phân vùng](../firmware/emmc-backup-verification.md), [PPN1/2](../firmware/emmc-boot-areas.md).