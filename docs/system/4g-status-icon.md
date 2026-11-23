# Khôi phục biểu tượng 4G và cột sóng trên Launcher3

**Trạng thái: REPORTED PASS — AutoShow v1.1 One-Shot, 21/11/2026.**

### Hiện tượng và nguyên nhân

Thiết bị vẫn lên LTE, vẫn phát hotspot và iPhone truy cập Internet được nhưng không hiển thị chữ 4G/cột sóng. Snapshot SystemUI có `isShowSlot0:false` dù Telephony trả dữ liệu LTE `IN_SERVICE` và thanh trạng thái có nhóm icon 4G. Thuộc tính OEM `uservice.control.slot0` đang `false`.

Ngày 20/11/2026 người dùng đặt cờ runtime thành `true` qua Magisk, đọc lại giá trị và xác nhận **4G/cột sóng xuất hiện**. Sau reboot cờ có thể trở về `false`; mô-đun `h01_mobile_4g_autoshow` v1.1.0 chạy **một lần khi Android boot hoàn tất**, đặt lại `true` rồi thoát, không kiểm tra mỗi 30 giây.

Ngày 21/11/2026 người dùng xác nhận biểu tượng vẫn trở lại trong chuỗi Auto Power-On v0.6 → AutoHotspot v0.4 → AutoShow v1.1.

### Giới hạn

Đây là lỗi **hiển thị icon**, không phải bằng chứng modem hỏng hoặc sửa chất lượng sóng. Chưa kiểm thử nhiều chu kỳ mất điện, hoạt động 24/7, tháo pin hoặc tất cả phiên bản H01. Giữ nguyên SystemUI gốc, tránh patch APK/modem khi chỉ cần điều chỉnh hành vi giao diện.

Lệnh đọc trạng thái:

```bat
adb shell getprop sys.boot_completed
adb shell getprop uservice.control.slot0
```

**Nguồn:** Notion “H01 — Phân tích SystemUI: ẩn biểu tượng sóng 4G SIM 1” (20/11, cập nhật 21/11/2026).