# Màn hình, xoay, thanh điều hướng và bàn phím (IME)

**Nguồn:** nhật ký Notion nghiên cứu H01, các mốc ngày 18/11/2026. Phạm vi có thiết lập Magisk root, không phải chức năng chuẩn mọi Android.

- Snapshot UI H01: `240 × 320 px`, `160 dpi`.
- Thanh phím điều hướng Android: nhật ký ghi nhận đã bật được sau root; nhánh tự ẩn theo immersive gặp trường hợp ngoại lệ khi kéo bảng thông báo/mở bàn phím.
- IME v0.1/v0.2/v0.3: các phiên bản có hoàn tác, báo cáo v0.3 đã tự áp dụng sau reboot.
- Xoay dọc v0.1 và điều khiển hướng thủ công v0.2.1 có mốc PASS.
- **Xoay cố định v0.3.1:** báo cáo sau reboot có `H01_ROTATION_BOOT_MODE=PERSISTENT`, `BOOT_COMPLETED=1`, `ACCELEROMETER_ROTATION=0`, `USER_ROTATION=0`; người dùng xác nhận hướng dọc áp dụng khi khởi động lại.

**Chưa xác nhận:** chạy không pin/cạn pin, mọi app bên thứ ba, mọi trạng thái bàn phím/bảng thông báo, nhiều chu kỳ mất điện. Nhánh tự ẩn thanh trong bảng thông báo đã hoãn.

Không xuất bản `services.jar` OEM đã vá, boot image root, file ký hoặc gói thay hệ thống khi chưa rà soát quyền phân phối. Các script cộng đồng cần có snapshot, xác minh và hoàn tác riêng.

**Nguồn chi tiết:** trang Notion tổng, các mục “Thử bật thanh phím Android”, “Tự ẩn thanh điều hướng”, “Hướng xoay dọc” và “Hoàn tất khóa xoay v0.3.1”.