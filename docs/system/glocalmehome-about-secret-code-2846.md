# Mã 2846 — menu kỹ thuật ẩn trong About của GlocalmeHome

> **Trạng thái:** Ghi nhận từ người thử thiết bị H01; chưa phân tích xác nhận đầy đủ điều kiện kích hoạt trên từng bản launcher. Đây **không phải** ứng dụng [H01 Hidden Settings](https://github.com/phai-nguyen/H01-Hidden-Settings).

## Mục đích và vị trí

- Thiết bị: ZEUS H01 / nền tảng GlocalMe K1, Android 8.1.
- Launcher OEM: `GlocalmeHome`, package `com.glocalme.g4home`.
- **Mã được chủ thiết bị xác nhận: `2846`.**
- **Vị trí được mô tả:** mục **About / Giới thiệu** trong launcher GlocalmeHome, để vào **menu bí mật / menu kỹ thuật**.
- Phải phân biệt menu OEM này với các trang Android Settings mở qua ứng dụng H01 Hidden Settings.

Các bước chạm chính xác để xuất hiện ô nhập mã (nhấn nhiều lần vào phiên bản, giữ lâu hay lựa chọn khác) **chưa được xác minh bằng bản ghi thao tác**. Không suy diễn rằng mọi firmware đều mở bằng cách giống nhau.

## Bằng chứng và giới hạn

Ghi chép nghiên cứu H01 ngày 19/11/2026 trong Notion ghi nhận mã `2846` xuất hiện trong thành phần **MMI**, được người dùng đánh giá có liên quan đến các mốc nghiên cứu mở khóa bootloader và root. Ghi chép đó **chưa chứng minh** kiểm tra mã nằm trong `GlocalmeHome.apk` hay chỉ do launcher gọi Activity/Service của MMI.

Vì vậy cần tách ba vấn đề:

1. **Trải nghiệm người dùng:** nhập mã `2846` từ mục About của GlocalmeHome để truy cập menu OEM — ghi nhận từ người thử.
2. **Nơi xử lý mã:** `GlocalmeHome.apk`, `MMI.apk`, `UklFactory.apk` hay IPC giữa chúng — **đang điều tra**.
3. **Tác dụng từng mục trong menu:** chưa kiểm kê đủ và chưa bảo đảm các thao tác an toàn.

## Hướng phân tích tiếp theo (chỉ đọc)

- Ghi lại phiên bản launcher và tên màn hình About, ảnh màn hình trước/sau khi nhập mã (loại bỏ IMEI, số SIM và dữ liệu tài khoản).
- Thu thập `dumpsys package` cho `com.glocalme.g4home` và package của MMI/UklFactory, so sánh Activity được mở khi nhập mã.
- Phân tích tĩnh tài nguyên/DEX từ bản APK **đang sở hữu hợp pháp** để xác định nơi so sánh mã và đường chuyển sang Activity kỹ thuật.
- Chỉ công khai **mô tả, tên lớp/hàm, mã nguồn công cụ tự viết**; không đăng APK/DEX, khóa ký OEM hay bản dump firmware có bản quyền.

## An toàn

Menu OEM có thể chứa **factory reset, thử phần cứng, cài firmware hoặc cấu hình modem**. Chỉ xem và ghi nhận ban đầu. Không nhấn các nút ghi NV, xóa dữ liệu, đổi IMEI, flash hoặc đặt lại thiết bị nếu chưa có phương án khôi phục và hiểu rõ tác dụng.

**Nguồn ghi chép nội bộ:** “H01 – Mốc khóa màn hình PIN: mở menu PASS, tương phản cao PASS” (19/11/2026). Xác nhận vị trí *About* và mã 2846 do chủ thiết bị cung cấp trong cuộc trao đổi ngày 23/11/2026.
