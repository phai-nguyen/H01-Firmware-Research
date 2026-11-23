# Nghiên cứu OTA H01 (mốc 22/11/2026)

**Nguồn:** ghi chép Notion "H01 — Nghiên cứu OTA, cách lấy firmware gốc và kiểm chứng bản sao (22/11/2026)". Đây là tóm tắt kết quả của máy thử; không công bố gói tải hay thông tin xác thực.

## Kết quả được ghi nhận

- Đã lấy được **gói OTA incremental block-based** từ dịch vụ cập nhật được ứng dụng FOTA sử dụng.
- Gói có dung lượng **44.118.207 byte** (~42,1 MiB), nguồn **build 81**, đích **build 87**.
- Build đích được ghi: `K1_TSV3.1.005.001.240116_20240116-1930`.
- Báo cáo ghi nhận kiểm tra chữ ký CMS toàn gói, khóa signer khớp khóa trong Recovery gốc; nhiều phân vùng và các block đích system/vendor đối chiếu được với bản sao tương ứng.
- Trong quá trình lấy gói, **không cài firmware lên máy** và không thay `ro.fota.version` thực trên thiết bị.

## Giới hạn

- OTA **không** phải ảnh eMMC đầy đủ hay factory ROM có thể phục hồi tùy ý.
- Không có chứng cứ khẳng định gói tương thích với tất cả các revision/biến thể H01.
- Mã xác thực/định danh thiết bị, token/secret và liên kết tải gói gốc **không được công khai**.
- Phần xử lý tương thích chứng chỉ hết hạn trong bộ công cụ thử nghiệm không phải mô hình bảo mật khuyến nghị cho sản phẩm; không xuất bản script vượt kiểm tra TLS hoặc thông tin đăng ký thiết bị trong phiên bản tài liệu này.

## Hướng nghiên cứu tiếp

1. Chuẩn hóa báo cáo kiểm tra chữ ký và danh sách block theo dạng không tiết lộ firmware.
2. Viết trình kiểm tra OTA **ngoại tuyến**, với đầu vào là gói do người sử dụng có quyền truy cập cung cấp.
3. So sánh GPT/boot chain theo phiên bản và xác định tính đầy đủ của đường khôi phục.
