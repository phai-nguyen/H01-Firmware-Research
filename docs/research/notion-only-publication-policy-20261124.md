# ZEUS H01 — phạm vi công bố chỉ từ Notion (chốt 24/11/2026)

**Yêu cầu của chủ dự án:** từ thời điểm chốt này, **chỉ đưa lên GitHub phần nghiên cứu H01 đã được ghi trong Notion**. Kết quả đang thử, ý tưởng mới, thông tin từ chat hoặc nguồn khác **chưa được ghi Notion** phải để chờ, không tự đưa vào nhánh công khai. Vẫn giữ quy định tách binary OEM và dữ liệu riêng.

## Điều kiện đủ để thêm một báo cáo mới

1. **Có trang Notion cụ thể** (URL/ID), tiêu đề/mục trong trang và mốc thời gian. Nguồn Notion là điều kiện **bắt buộc**; GitHub cũ, chat hoặc một file Dropbox chưa được biên soạn vào Notion **không đủ** để xuất bản nội dung nghiên cứu mới.
2. **Trích đúng mức chứng cứ:** `OBSERVED`, `STATIC VERIFIED`, `REPORTED PASS`, `FAIL`, `PAUSED`, `PLAN`, `OPEN`; khi kết luận mới thay thế kết luận trước, ghi rõ **mốc nào**.
3. **Chỉ công bố phần có quyền phân phối và đã làm sạch:** mô tả kỹ thuật do dự án tự viết, bảng kiểm chứng tổng hợp không định danh, số liệu phi nhạy cảm và mã nguồn do dự án tự sở hữu sau rà soát.
4. **Không xuất bản raw/private assets:** IMG/OTA/APK/ODEX/VDEX/ELF của hãng, dump GPT chứa GUID của máy, programmer, mật khẩu/token, IMEI/ICCID/IMSI, phone number, SoftSIM/định danh mạng, dữ liệu người dùng, private Dropbox, chứng từ tài khoản, patch bảo mật hay script ghi flash chưa kiểm chứng.
5. **Trạng thái hoàn thành** chỉ gắn sau khi đối chiếu nguồn, mốc thời gian, các phản chứng và các đính kèm **có thể công bố hợp pháp**. Một link trong bảng 207 mục chỉ là `MAPPED`, không phải `FULLY REVIEWED`.

## Phạm vi Notion đã kiểm kê ở lượt này

- [Một trang tổng H01, gồm 207 đề mục cấp 2](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd).
- [Bảng đối chiếu 16 trang chuyên đề H01](notion-16-specialist-pages-publication-audit-20261124.md).
- [Mục lục 207 đề mục có liên kết báo cáo chuyên sâu và báo cáo theo mốc](notion-207-routing-map.md).

Việc tìm Notion theo từ khóa **H01** tại thời điểm kiểm kê đưa về 17 trang có chủ đề H01 trong số các kết quả liên quan; **không chứng minh** các trang H01 không có từ H01 trong tiêu đề/nội dung, trang ẩn hoặc trang mới về sau đều đã được tìm thấy.

## Nội dung được giữ lại ở trạng thái chờ

- Phân tích **Wi-Fi hotspot 5 GHz bị tắt** khi đổi băng tần: trong 17 trang Notion đã kiểm, chưa tìm thấy một đoạn ghi nhận hiện tượng thử nghiệm đó. Đã rút báo cáo được soạn từ cuộc trò chuyện khỏi nhánh công khai chính của repository và gỡ liên kết trong các trang chỉ mục; Git vẫn có thể lưu lịch sử commit cũ, việc rút khỏi nhánh hiện tại **không** tương đương xóa khỏi lịch sử.
- Các nghiên cứu H01 phát sinh về sau hoặc chưa được ghi vào Notion **không tự nhập** vào tập báo cáo công khai.

## Chưa được chứng nhận

Tập tài liệu đã có báo cáo theo mục **207/207** của trang tổng và có tóm tắt từ **16/16** trang chuyên đề đã tìm thấy. Tuy nhiên việc công bố toàn văn của mỗi mục, rà toàn bộ TXT/ZIP/RAR/ảnh/video và kiểm tra quyền sở hữu từng asset chưa được thực hiện trọn vẹn. **Không công bố tiến độ 100% nội dung** nếu chưa có bảng kiểm toán cấp nguồn/đính kèm đầy đủ.

Xem thêm [Backlog](publication-backlog.md), [bảng nguồn](source-boundaries-and-coverage.md), [quy định công bố bảo mật](../security/publication-policy.md).
