# Kiểm chứng ZIP và IMG H01 bằng CRC + SHA-256

**Công cụ tự viết:** [audit_backup_archives.py](../../tools/audit_backup_archives.py). Chương trình chỉ đọc một thư mục, không giải nén ra đĩa, không can thiệp H01, không kết nối mạng, không yêu cầu quyền root.

## Mục đích và nguồn

Nhật ký H01 ngày 11/11/2026 (Notion mục 95, 98) ghi hai lượt kiểm tra: trước là 18 ZIP + 41 IMG bên trong ZIP + 1 standalone = 42/42 MATCH; sau là 19 ZIP + 45 IMG bên trong + 1 standalone = 46/46 MATCH. 46 đối tượng ảnh bao gồm cả lịch sử/metadata; bảng GPT vẫn có **42 phân vùng**.

Công cụ mới giúp chủ sở hữu kiểm tra bản sao riêng trên PC bằng dữ liệu/sidecar đang có. Chương trình không chứa hoặc tải các ảnh firmware OEM.

## Chạy trên Windows 7

Cần cài Python 3:

    python tools\audit_backup_archives.py C:\H01\backup

Trên antiX:

    python3 tools/audit_backup_archives.py /path/to/H01-backup

Tùy chọn --details chỉ hiển thị loại trạng thái, không in checksum hoặc dữ liệu nhị phân. Chương trình mặc định không tạo báo cáo tệp.

## Quy tắc

- Chỉ xét ZIP hoặc IMG ngay trong thư mục chọn, **không đệ quy**.
- Đọc hết từng member ZIP để kiểm tra CRC, không giải nén ra thư mục.
- Đối với member ZIP tên test.img, cần member test.img.sha256 trong **cùng thư mục bên trong ZIP**; với IMG bên ngoài ZIP cần sidecar cạnh IMG.
- Sidecar đúng định dạng sha256sum: 64 ký tự hex + 2 khoảng trắng (hoặc dấu *) + tên basename ảnh.
- MATCH: nội dung khớp SHA-256; REVIEW: thiếu sidecar, **không được tính PASS**; MISMATCH: checksum khác; ERROR: ZIP/CRC/sidecar không hợp lệ.
- Mã thoát: 0 = toàn bộ ảnh có MATCH; 1 = cần REVIEW; 2 = lỗi/mismatch hoặc không có ảnh.
- Giới hạn 4.096 member/ZIP và 24 GiB dữ liệu uncompressed/ZIP; từ chối đường dẫn traversal, member trùng, member mã hóa. Đây không phải sandbox cho ZIP không tin cậy tuyệt đối.

**Giới hạn quan trọng:** Nếu checksum sidecar lưu **bên ngoài** ZIP thay vì là member tương ứng trong ZIP, ảnh ZIP sẽ được đánh dấu REVIEW. Công cụ v1 chưa hỗ trợ ánh xạ manifest bên ngoài và chưa tự đối chiếu 42 partition GPT.

CRC/SHA-256 khớp **không chứng minh** đúng LBA eMMC, chữ ký OEM, nội dung firmware hợp pháp để phát tán hoặc khả năng phục hồi bằng flash. Không tải userdata, ảnh modemst, NV, profile SoftSIM, sidecar nhạy cảm hoặc log gốc lên GitHub.

Bộ 12 unit test dùng dữ liệu ZIP/IMG tổng hợp. **Chưa thử trên kho backup H01 nhiều GB thực tế.**

**Tài liệu liên quan:** [backup integrity](../firmware/emmc-backup-verification.md), [GPT](../firmware/gpt-layout.md), [hash từng ảnh](backup-hashes.md).

## Đối chiếu số phân vùng GPT

Dùng thêm [audit_partition_inventory.py](../../tools/audit_partition_inventory.py) và [hướng dẫn](partition-inventory-audit.md). Công cụ đó chỉ so sánh tên/kích thước IMG/ZIP với 42 mục trong GPT CSV, không tính hash hoặc CRC. Hai công cụ giải quyết hai câu hỏi độc lập: tính toàn vẹn bản sao và độ phủ tên phân vùng.
