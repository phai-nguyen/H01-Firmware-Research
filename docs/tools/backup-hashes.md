# Kiểm tra SHA-256 của bản sao cục bộ — ngoại tuyến

Tệp `*.sha256` của các bản sao trong kho H01 dùng dạng `sha256sum` (`64 ký tự hex`, hai khoảng trắng, tên tệp). Script [`verify_sha256.py`](../../tools/verify_sha256.py) xác minh **một hoặc nhiều sidecar** ngay trên máy tính và không mở kết nối mạng hay chỉnh sửa file nguồn.

Ví dụ trên Windows 7 với Python 3 tương thích:

```cmd
python tools\verify_sha256.py C:\H01\H01-boot-20261111.sha256
```

Ví dụ antiX:

```sh
python3 tools/verify_sha256.py /path/to/H01-boot-20261111.sha256
python3 tools/verify_sha256.py /path/to/H01-boot-20261111.sha256 /path/to/H01-vendor-20261111.sha256
```

- Tệp `.img` được tham chiếu phải ở **cùng thư mục** với sidecar. Không chấp nhận đường dẫn tuyệt đối, `..`, phân cách thư mục hay symlink.
- Script đọc theo luồng 1 MiB; xác minh `userdata.img` sẽ mất thời gian tương ứng dung lượng.
- `PASS`: checksum trùng khớp với sidecar. `MISMATCH`: nội dung khác, dừng sử dụng bản sao đó. `ERROR`: thiếu tệp hoặc sidecar sai định dạng.
- **Không xác minh** bản sao đến đúng từ một vùng eMMC, chưa xác nhận chữ ký OEM, chưa chứng minh ảnh an toàn để flash.
- Không chia sẻ cả sidecar của `userdata` nếu giá trị hash có thể tiết lộ hoặc liên kết một bản sao dữ liệu riêng cụ thể; không đưa ảnh `.img` vào repository.
