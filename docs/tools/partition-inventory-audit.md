# Kiểm kê 42 phân vùng từ các tên IMG và metadata ZIP

**Công cụ:** [audit_partition_inventory.py](../../tools/audit_partition_inventory.py). So sánh tên ảnh dạng H01-PARTITION-YYYYMMDD.img và kích thước IMG hoặc metadata ZIP với bảng [GPT CSV đã khử định danh](../firmware/partition-layout-sanitized.csv).

## Mục đích

Nhật ký firmware H01 ghi 42 phân vùng GPT, nhưng báo cáo kiểm tra kho backup có thể chứa 46 đối tượng ảnh vì các thế hệ dump cũ và metadata khác. Chương trình này chỉ tính **số tên phân vùng có ứng viên ảnh kích thước đúng**. Không đếm mỗi file IMG thành một phân vùng.

- Đọc một cấp thư mục, không thay đổi tệp và không giải nén ZIP.
- Bỏ qua ảnh có tên khác mẫu, ví dụ bản marker hoặc ảnh thử nghiệm đã vá.
- Khi một tên phân vùng xuất hiện nhiều bản, đếm một phân vùng và ghi số variants riêng.
- Chấp nhận tên ảnh từ ZIP theo metadata file size; không đọc payload, không tính CRC và không hash trong chương trình này.

Chạy CMD Windows 7 (Python 3):

    python tools\audit_partition_inventory.py C:\H01\backup --details

antiX Linux:

    python3 tools/audit_partition_inventory.py "/home/user/H01-backup" --details

Kết quả **Partition candidates of expected 42: 42** chỉ có nghĩa đã tìm thấy 42 ứng viên tên/kích thước; **không phải 42/42 integrity PASS**. Cần chạy thêm [ZIP/IMG CRC + SHA-256 auditor](backup-archive-audit.md) và giữ bằng chứng nguồn đọc eMMC.

Nếu tên ảnh không theo mẫu H01-PARTITION-YYYYMMDD.img, công cụ có thể đánh dấu thiếu dù file thực tế vẫn còn. Không đổi tên hoặc sửa bản gốc chỉ để đạt kết quả; nên ghi nhận tên và provenance đúng.

Không đưa dữ liệu SIM, userdata, ZIP IMG gốc, sidecar/checksum của thiết bị hoặc log vào repository công khai. Công cụ dùng dữ liệu tổng hợp trong 7 unit tests, chưa chạy trực tiếp với kho sao lưu H01 thực tế.
