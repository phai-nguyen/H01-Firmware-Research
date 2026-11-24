# Ranh giới nguồn đã khảo sát và tiến độ chuyển nghiên cứu H01

**Mốc kiểm toán: 24/11/2026.** Đây là kiểm kê phạm vi biên soạn cho kho GitHub công khai, không công bố dữ liệu nguyên bản.

## Các nhóm nguồn

| Nguồn | Đã tiếp cận | Điều được đưa lên GitHub |
| --- | --- | --- |
| Notion, trang tổng H01 | **207 đề mục cấp 2** được đọc, có mục lục | Báo cáo kỹ thuật đã lọc, sơ đồ [207 mục → báo cáo liên quan](notion-207-routing-map.md) |
| Notion, các trang chuyên đề | Tìm được **16 trang chủ đề H01** ngoài trang tổng khi tìm từ khóa H01 (một kết quả tìm kiếm, không xác nhận toàn bộ workspace) | Các nghiên cứu FOTA/OTA, modem/SIM, MMI, Keyguard, root, UI, hotpot/4G, audio, máy B |
| Dropbox, tệp H01 | Có nhiều ảnh phân vùng và một số báo cáo TXT; đã đọc riêng các báo cáo chọn lọc ngày 14/11 | Hai báo cáo kết luận về [USB EDL](../firmware/edl-usb-host-endpoint-diagnostics-20261114.md) và [MMC/sysfs](../hardware/mmc-hosts-sysfs-dac-evidence-20261114.md) |
| GitHub nguồn trước đó | Repository có cả tài liệu và công cụ Python đã được đăng trước | Đối chiếu tên báo cáo, cập nhật README, không chép lại binary hoặc dữ liệu nhạy cảm |

## Phần chưa thể gọi là 100%

- Bảng [207/207 mục](notion-207-routing-map.md) là **truy vết tiêu đề đến báo cáo liên quan**; không có cột chứng nhận đã trích hết từng đoạn, hình, tệp đính kèm, log, lần thử hoặc diễn biến thay đổi.
- Những báo cáo TXT/ZIP, ảnh/video và ZIP phân vùng còn lại trên kho lưu riêng **chưa được đánh giá từng tệp** về quyền phân phối, mức độ liên quan và thông tin nhạy cảm.
- Các binary hãng/ảnh phân vùng không có giấy phép phân phối công khai hoặc chứa dữ liệu người dùng **không thuộc phạm vi upload GitHub công khai**.
- Mỗi mốc PASS chỉ phản ánh kết quả từng thử nghiệm được ghi rõ; không tự suy ra chạy với mọi H01, mọi firmware hay đủ điều kiện flash cứu hộ.

## Quy tắc về niềm tin

**Đã chuyển thành tài liệu** không đồng nghĩa **đã tái kiểm chứng trên H01**; **hash bản sao khớp** không đồng nghĩa **factory ROM chính hãng**; **đã có báo cáo liên quan** không đồng nghĩa **đã chuyển toàn văn**. Khi nguồn lịch sử bị kết quả mới thay thế, cần giữ cả mốc trước và sau (ví dụ OEM Unlock, UService DEX, socket-to-PID, AutoHotspot và boot root).

Báo cáo này không chứa liên kết tới kho dữ liệu riêng hoặc thông tin định danh thiết bị.