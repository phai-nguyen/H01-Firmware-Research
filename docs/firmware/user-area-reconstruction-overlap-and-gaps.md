# H01 — đánh giá khả năng tái dựng eMMC User Area từ các ảnh đã sao lưu

**Nguồn:** [Nhật ký Notion H01, H178 — “Phương án ghép toàn bộ firmware H01 — đối chiếu ngày 18/11/2026”](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Chỉ phân tích độ phủ dữ liệu và sự chồng lấn địa chỉ**, không tạo, ghi hay phát hành ảnh 7,8 GB.

## Các đối tượng đã kiểm trong kho riêng ở mốc 18/11

| Nội dung kho | Kết quả báo cáo |
| --- | --- |
| Tổng đối tượng IMG và sidecar | **48 IMG + 48 sidecar** |
| 42 phân vùng GPT | Có **42 IMG ứng viên**, kích thước khớp CSV GPT |
| Hai ảnh GPT | GPT primary và GPT backup, mỗi bản đọc **128 sector** |
| Hai ảnh lịch sử | Hai bản boot/recovery từ các thời điểm khác |
| Hai ảnh PPN | Boot-area candidates PPN 1/2, mỗi ảnh **4 MiB** được programmer trả toàn zero |
| Hash referential | Đọc 48 sidecar; 42 IMG có hash tham chiếu |
| Kiểm binary tại lượt 18/11 | Chỉ trực tiếp băm lại GPT và một số ảnh boot/recovery/aboot/sbl1; **chưa băm lại tất cả 42 IMG** |

**Phân biệt:** Kết quả **46/46 IMG SHA-256 MATCH** được ghi ở lượt kiểm ZIP trên iPhone **ngày 11/11** là một mốc trước, không được gộp thành “đã băm lại 48 ảnh ngày 18/11”.

## Vì sao 159.001.600 byte gap không đồng nghĩa 159.001.600 byte còn thiếu?

Đối chiếu [GPT 42 partition](gpt-dropbox-csv-direct-audit-20261124.md), usable LBA có ba khoảng không thuộc phân vùng:

| Khoảng trống GPT | Toàn khoảng | Đã được snapshot GPT bao phủ | Còn thiếu theo bản rà 18/11 |
| --- | ---: | --- | ---: |
| `34–131071` | 131.038 sector | `34–127` (**94 sector**) trong ảnh GPT primary `LBA 0–127` | `128–131071`: **130.944 sector**, **67.043.328 byte** |
| `284768–393215` | 108.448 sector | Chưa thấy trong danh sách | **55.525.376 byte** |
| `3467880–3538943` | 71.064 sector | Chưa thấy trong danh sách | **36.384.768 byte** |
| **Tổng** | **310.550 sector = 159.001.600 byte** | **94 sector = 48.128 byte** | **310.456 sector = 158.953.472 byte** |

Đây là tính **độ phủ theo địa chỉ** từ những đối tượng đã liệt kê, không chứng minh các gap chứa dữ liệu quan trọng, bằng zero hay đã thực sự đọc đúng byte ở mọi sector.

## Vấn đề GPT backup 128 sector chồng lấn userdata

Theo bảng GPT, `userdata` kết thúc tại LBA **15269854**, backup GPT entry-array bắt đầu **15269855**, header cuối tại **15269887**. Ảnh `GPT-backup` đã đọc **128 sector cuối**, tức cửa sổ `LBA 15269760–15269887`, nên **95 sector đầu của cửa sổ là vùng cuối userdata**.

Báo cáo nguồn chọn cách mô hình hóa không chồng byte:

- Giữ **toàn bộ userdata** từ IMG riêng của nó.
- Xem **33 sector cuối** của ảnh GPT backup (từ **offset byte 48.640**, chiều dài **16.896 byte**) là vùng sau userdata `LBA 15269855–15269887`.
- Không nối đuôi các IMG như một file ZIP sequence: vị trí logic phải dựa vào **Start LBA × 512** của đúng GPT.

Đây chỉ là **cách phân tích metadata và dự định xử lý trùng vùng khi tái dựng ngoại tuyến**, không phải công cụ tạo IMG đã chạy PASS hay hướng dẫn ghi image trở lại máy.

## Những trường hợp chưa thể gọi là firmware gốc đầy đủ

- **Chưa có** ba gap được thu và kiểm độc lập trong danh sách tại lượt 18/11.
- **Chưa có** bản User Area raw clone kiểm toàn dải 15.269.888 sector, hoặc so từng byte giữa ảnh ghép với chip.
- **Chưa có** đường khôi phục end-to-end trên thiết bị mất boot.
- PPN1/2 payload toàn zero **không chứng minh Boot Areas vật lý trống**. RPMB và EXT_CSD không thuộc vùng User Area.
- Ảnh ở nhiều thời điểm, gồm **DEVINFO trước và sau unlock**, có trạng thái khác nhau. Không thể gọi bộ ảnh ghép là **snapshot nguyên tử duy nhất** hay factory ROM chính hãng.

**Kết luận:** Có dữ liệu **theo tên/kích thước cho 42/42 partition** nhưng **chưa có bằng chứng đầy đủ để tạo bản firmware phục hồi tin cậy**. Không phát hành các IMG riêng, dữ liệu SIM/NV/SoftSIM, GPT GUID, lệnh/ XML ghi eMMC.

Xem [backup readiness](../boot/recovery-readiness.md), [mốc kiểm ZIP](emmc-iphone-gpt-integrity-timeline.md), [Boot Areas](emmc-boot-areas.md).