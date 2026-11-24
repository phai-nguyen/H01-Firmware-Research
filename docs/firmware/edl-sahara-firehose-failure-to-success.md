# H01 EDL 9008 — từ lỗi đường dẫn, treo Sahara tới Firehose NOP/GPT PASS

**Nguồn trực tiếp:** [Notion H01 H119–H127, 14/11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). Tài liệu **lịch sử chẩn đoán**, không phải quy trình flash, không chạy lại lệnh trên H01.

## Trình tự sự kiện

| Giai đoạn | Biểu hiện / kết quả | Cách đọc đúng |
| --- | --- | --- |
| H117–H119 | Thiết bị ở USB Qualcomm **05c6:9008**; host không tìm thấy tệp programmer vì **đường dẫn sai** | Lỗi file cục bộ, chưa có Firehose |
| H120–H121 | Client NOP dừng khoảng **30 phút** ở Sahara; Ctrl+C trên host; chưa thấy ACK Firehose | Treo trong giao thức nạp/host, **không chứng minh eMMC đã đổi** |
| H122 | Debug log mới có **Sahara END_TRANSFER SUCCESS + DONE_RSP**, loader đã nạp RAM | Bằng chứng nạp programmer vào RAM thành công |
| H122–H123 | Firehose `configure` **ACK**, nhận `MemoryName=eMMC`, `TargetName=8909` | Nền tảng đọc eMMC đã sẵn sàng |
| H122 | `getstorageinfo` trả **15.269.888 sector × 512 byte** ở User Area | Dung lượng ghi nhận **7.818.182.656 byte** |
| H122 | READ GPT sector LBA 1 có magic `EFI PART`; NOP ACK | **READ/GPT/NOP đã PASS trong log** |
| H123 | Phía host có `TypeError`/USB cleanup sau phản hồi; USB 9008 còn enumerate | Lỗi cleanup **sau ACK** không hủy kết quả ACK đã có |

Log debug chủ yếu phân tích USB XML TX `configure`, `read`, `getstorageinfo`, `nop`; trong **phiên này** không thấy host gửi `program`, `erase`, `patch` hoặc `poke`. Câu “không có lệnh ghi trong log” chỉ áp dụng **phiên đã đọc**, không bảo đảm Firehose/ELF không có khả năng ghi. Programmer nhận diện được cả chức năng write; cấu hình `SkipWrite=0` **không cưỡng chế read-only**.

## Vì sao không diễn giải nhầm trạng thái?

- **Sahara handshake thành công** chưa đồng nghĩa Firehose configured; cần `END_TRANSFER` và Firehose ACK để chốt.
- **NOP ACK** là kết quả cụ thể; dòng client “đang chờ” ở 30 phút trước đó là mốc FAIL khác, không được lấy kết quả sau để sửa lịch sử.
- Probe khách hàng từng đoán UFS/4.096 byte sector, H01 **NAK** và sau đó nhận dạng đúng eMMC **512 byte/sector**. NAK của probe sai geometry **không chứng minh thiết bị không đọc được eMMC**.
- `num_physical_partitions=3` chưa tự xác nhận map Boot1/Boot2/RPMB; xem [PPN và EXT_CSD](mmc-extcsd-access-investigation.md).

## Phạm vi khôi phục

Đã đọc được GPT và backup sector trong log, **chưa chứng minh khả năng restore từ thiết bị hỏng boot**. Không công khai programmer ELF, serial/HWID/PK_HASH, XML ghi/xóa, raw USB trace hoặc file chứa NV/SIM.

Tham khảo [EDL Firehose core](edl-firehose-diagnostics.md) và [recovery readiness](../boot/recovery-readiness.md).