# H01 Share Server — truyền file giữa H01 và iPhone

**Trạng thái: v0.1.4 Final — người dùng xác nhận PASS (18/11/2026).**

Ứng dụng Android `vn.h01.share` trên H01 kết nối với Share Server **chạy trên iPhone**, truyền file hai chiều qua Wi-Fi nội bộ, không cần PC cho mỗi lần chuyển và không cần root trong luồng sử dụng. Không cài server iOS thành dịch vụ hệ thống H01.

| Bản | Kết quả ghi nhận |
| --- | --- |
| v0.1 | Liệt kê được nhưng tải timeout |
| v0.1.1 | Người dùng xác nhận tải file thành công |
| v0.1.2 | Giao diện gọn, danh sách cuộn, PASS |
| v0.1.3 | Gửi file từ H01 lên iPhone PASS |
| v0.1.4 | Thêm icon/tên trên launcher, người dùng PASS |

**Kỹ thuật:** GET tải file với `Connection: close`, lưu `.part` trước khi đổi tên; POST `/upload` theo khối 32 KiB, gửi `X-Filename` UTF-8 và kiểm tra phản hồi HTTP 2xx. Chỉ gửi/tải **một file một lượt**; chưa có resume, hàng đợi hay đa chọn.

Kiểm thử local có đối chiếu SHA-256 của file 9 MiB trên máy giả lập; **không** suy diễn thành hiệu suất/hàm băm đo trực tiếp giữa H01 và iPhone. Không công khai địa chỉ server thực, tên tệp riêng, log truyền hoặc APK/công cụ có giấy phép khác.

**Nguồn:** Notion trang tổng “H01 – Nghiên cứu firmware GlocalMe K1 / Qualcomm MSM8909”, mục “Share Server H01 — v0.1.4” (18/11/2026).