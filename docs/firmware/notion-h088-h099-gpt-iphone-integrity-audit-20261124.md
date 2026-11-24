# H01 — đối chiếu Notion H088–H099: GPT thô và kiểm SHA-256 trên iPhone (11/11/2026)

**Nguồn duy nhất:** [Nhật ký H01 trên Notion, mục H088–H099](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). Đây là bản **chuyển biên soạn lịch sử kiểm chứng**, không dùng các phép thử mới chưa có trong Notion, không tải thêm ảnh OEM và không thực thi thao tác trên thiết bị. Mức chứng cứ có chữ `REPORTED` dựa vào ảnh/báo cáo người dùng ghi trong Notion.

## 12 mục được đối chiếu theo mốc

| ID | Kết luận đúng tại thời điểm mục nguồn | Mức chứng cứ |
| --- | --- | --- |
| H88 | Kế hoạch kiểm SHA-256 ngay trên iPhone bằng a-Shell mini/pickFolder; đọc theo khối, không sao chép userdata dung lượng lớn | PLAN |
| H89 | Firehose đọc 128 sector GPT primary (LBA 0); ảnh 65.536 byte; **chưa có hash ở mốc này** | READ REPORTED |
| H90 | Firehose đọc thêm 128 sector GPT backup tại cuối LUN; hai ảnh 65.536 byte, chưa đóng ZIP | READ REPORTED |
| H91 | Hai hash `sha256sum -c` OK trên laptop; ZIP gồm 2 IMG và 2 sidecar kiểm tra cấu trúc PASS; **chưa kiểm iPhone** | LOCAL INTEGRITY REPORTED |
| H92 | ZIP GPT có trên iPhone; hai ảnh primary/backup SHA-256 MATCH; userdata độc lập cũng MATCH | CROSS-DEVICE COPY INTEGRITY REPORTED |
| H93 | VENDOR và SYSTEM trong ZIP đều MATCH trên a-Shell; không suy rộng sang mọi batch | CROSS-DEVICE COPY INTEGRITY REPORTED |
| H94 | Script kiểm theo khối 4 MiB, so IMG-sidecar và đọc ZIP tới EOF; thử bằng dữ liệu giả PASS, lúc đó chưa chạy thật | TOOL DESIGN / SYNTHETIC TEST |
| H95 | Ảnh a-Shell hiển thị 42 IMG được kiểm, 42 MATCH, 0 REVIEW, 0 ZIP lỗi | RUNTIME REPORT SUMMARY |
| H96 | Báo cáo chi tiết lượt đầu: 18 ZIP, 41 IMG trong ZIP, 1 userdata IMG độc lập, 42/42 MATCH | RUNTIME REPORT AUDITED |
| H97 | Script GPT-inspect đã dựng và thử trên GPT giả với CRC/LBA hợp lệ; khi đó chưa kiểm trên ảnh GPT H01 thật | TOOL DESIGN / SYNTHETIC TEST |
| H98 | Báo cáo GPT thật: header/entry CRC PASS, primary/backup khớp, 42 partition; đối chiếu file scanner lượt đầu chỉ **40/42 partition** vì 2 IMG còn thiếu | GPT RUNTIME AUDITED; INITIAL COVERAGE PARTIAL |
| H99 | Lượt kiểm sau: 19 ZIP + 1 userdata độc lập, 46/46 đối tượng IMG MATCH, có thêm productinfo/persist; đạt 42/42 tên phân vùng | LATER COPY INTEGRITY REPORTED |

## Sai khác quan trọng giữa ba bản kiểm

| Mốc | ZIP | IMG được kiểm | Số phân vùng GPT có ảnh tương ứng | Ý nghĩa |
| --- | ---: | ---: | ---: | --- |
| H095–H096 (lần đầu) | 18 | **42 MATCH** = 41 IMG trong ZIP + 1 userdata ngoài ZIP | **40/42** (hai IMG được đếm là metadata GPT) | 42/42 MATCH của các đối tượng đã quét **không** chứng minh đủ tên 42 phân vùng |
| H098 (kiểm tra GPT) | 18 theo báo cáo nguồn đã đọc | Vẫn là các IMG nói trên | **40/42**; còn thiếu `productinfo`, `persist` trong danh sách scanner khi đó | Phải phân biệt 42 populated partition GPT với 42 tệp đã hash |
| H099 (lần sau) | 19 | **46 MATCH** = 45 IMG ZIP + 1 userdata độc lập | **42/42** có ứng viên tương ứng | Batch `productinfo/boot/persist/recovery` đã được bổ sung; có boot/recovery nhiều thế hệ |

Các kết quả trên đúng **theo báo cáo trong Notion** và không cần chỉnh sửa lời kết luận lịch sử cũ. Không trộn thời điểm H098 với H099 khi đánh giá mức đầy đủ. [Tổng quan integrity](emmc-backup-verification.md) và [đối chiếu GPT với CSV](gpt-dropbox-csv-direct-audit-20261124.md).

## H098 — tính toàn vẹn GPT và khoảng trống chưa gán

Theo nội dung Notion, hai GPT header và partition entry-array đều kiểm **CRC32 PASS**, primary/backup tham chiếu LBA qua lại và entry arrays **byte-identical**. GPT có **44 ô entry, 42 entry được dùng**. User Area ghi **15.269.888 sector × 512 byte = 7.818.182.656 byte**. Bảng GPT không có partition overlap, nhưng có **3 khoảng không được gán**: LBA 34–131071; 284768–393215; 3467880–3538943. Không coi các vùng này là rỗng hoặc có thể ghi đè.

## Điều bằng chứng thực sự chứng minh

- Đọc hết ZIP và hash khớp sidecar hỗ trợ **tính toàn vẹn bản sao lưu** ở vị trí đã kiểm; với H092/H093 còn có đối chiếu qua thiết bị iPhone. Sidecar thường được tạo trong lúc sao lưu, **không tự chứng minh dữ liệu OEM chính hãng**.
- Kiểm CRC32 GPT và không chồng LBA chứng minh cấu trúc bảng phân vùng **trong hai ảnh đã ghi** tự nhất quán; **không** chứng minh mọi lệnh đọc IMG đi đúng địa chỉ.
- **Không** xác nhận restore trên máy mất boot, snapshot eMMC nguyên tử, đầy đủ các vùng ngoài partition, tính xác thực firmware hoặc khả năng dùng cho máy H01 khác.
- Ở H094/H097, phép kiểm dữ liệu giả (`synthetic test`) **không** được coi là thiết bị thật PASS; những lần chạy thật xuất hiện ở H095–H099.

## Tài liệu liên quan đã có trong repo

- [Kiểm integrity 42/46 IMG](emmc-backup-verification.md)
- [Nhật ký GPT và iPhone](emmc-iphone-gpt-integrity-timeline.md)
- [GPT 42 mục đã khử định danh](gpt-layout.md)
- [Các khoảng GPT không được gán](gpt-unallocated-regions-and-integrity.md)
- [Giới hạn ghép firmware](user-area-reconstruction-overlap-and-gaps.md)

**Ranh giới công bố:** tài liệu này **không** đăng `userdata.img`, ZIP firmware hãng, ảnh GPT chứa GUID của thiết bị, file `modemst*`/SoftSIM/NV, serial, đường dẫn Files riêng, hoặc checksum định danh. 12 mục có mô tả riêng **không đồng nghĩa** đã chuyển mọi ảnh, log và văn bản gốc của 12 mục.
