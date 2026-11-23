# H01 Share Server v0.1.4 — giao thức, PASS máy thật và test fixture

**Nguồn:** Notion trang tổng nghiên cứu H01, mục “Share Server H01 — chốt bản ổn định cuối v0.1.4” (18/11/2026). **REPORTED PASS trên máy H01 được thử**, nhưng kiểm chứng SHA-256 tệp 9 MiB là ở **server giả lập**.

## Kiến trúc

Server HTTP chạy **trên iPhone**; ứng dụng client Android `vn.h01.share` trên H01 kết nối qua Wi-Fi nội bộ, không cần PC hoặc root cho thao tác thường. Server không được nhúng vào firmware Android; địa chỉ/port server lấy từ UI iPhone, không hardcode theo một lần thử.

| Phiên bản | Mục đích và bằng chứng |
| --- | --- |
| v0.1 | Danh sách file hiện, tải timeout — FAIL |
| v0.1.1 | Hiển thị tiến trình, điều chỉnh HTTP đóng kết nối; tải xuống **PASS** theo người dùng |
| v0.1.2 | Giao diện gọn, danh sách cuộn, menu; tải file khoảng 9 MiB **PASS**, tốc độ chỉ là nhận xét |
| v0.1.3 | H01 chọn file rồi gửi iPhone, có tiến trình/hủy — **upload PASS** |
| v0.1.4 Final | Sửa icon/tên launcher, giữ lõi truyền v0.1.3 — **PASS** |

Việc thêm `Connection: close` ở v0.1.1 và hết timeout **chưa chứng minh** nguyên nhân timeout ban đầu chính xác là reuse kết nối.

## Giao thức tệp

- Danh sách: `GET /`, lấy liên kết tương đối `/files/...`, hỗ trợ tên UTF-8 và hạn chế link ngoài máy chủ; giới hạn trang danh sách **2 MiB**.
- Tải: `GET` với `Accept-Encoding: identity` và `Connection: close`; ghi `.part` ở `Download/ShareServer`, so `Content-Length` nếu có, hoàn tất mới đổi tên. File trùng tên được đổi tên tránh ghi đè.
- Gửi: `POST /upload`, `application/octet-stream`, `X-Filename` percent-encoded UTF-8, `Content-Length` xác định; gửi streaming **32 KiB/khối** để không giữ toàn file trong RAM.
- Chỉ báo gửi thành công khi nhận **HTTP 2xx**, không phải chỉ vì client gửi đủ byte. **Không auto retry** lúc lỗi vì có thể đã tạo file ở server. Khi hủy, cần đối chiếu tệp trên iPhone trước khi gửi lại.
- Chỉ truyền **một file mỗi lượt**: không có queue, multi-select hay resume, và chủ dự án chốt dừng phát triển ở v0.1.4.

## Độ tin cậy của bằng chứng

- Trên H01 thật: người dùng xác nhận tải, gửi, giao diện và icon. Không có thống kê MB/s/đối chiếu hash hai chiều trên đúng file H01↔iPhone.
- Trên host mô phỏng: **15 tình huống giao thức**, tệp 9 MiB đối chiếu SHA-256, các trường hợp chunked, HTTP 403, timeout, file rỗng, tên Unicode, hủy, trùng tên. **Không đồng nhất fixture PASS với mạng thật**.
- Hồ sơ H01 máy B về sau ghi đã chuyển **bộ cài Share Server v0.1.4** tới B, nhưng chưa xác nhận truyền tệp trên B.

Không công khai URL kho file cá nhân, server IP/port riêng, tên tệp/log truyền, APK/ZIP chưa rà bản quyền hoặc khóa ký. Xem [tổng quan](share-server.md), [hồ sơ A/B](../research/h01-device-b-comparison-20261124.md).