# H01 — SystemUI ẩn biểu tượng 4G của slot 0, AutoShow v1.1

**Nguồn:** [Notion phân tích SystemUI 4G](https://app.notion.com/p/41ec5d5277a9813fbeebe77a1c3617f2), 20–21/11/2026. Biên soạn 24/11/2026. **STATIC + RUNTIME REPORTED PASS** trên cấu hình đã thử.

## Triệu chứng và dữ liệu phân biệt modem/UI

Trong Launcher3, chữ 4G và vạch sóng biến mất dù LTE vẫn dùng được; Telephony snapshot ghi `mDataRegState=0` (IN_SERVICE), `mRilDataRadioTechnology=14` (LTE), `mDataConnectionState=2`. SystemUI báo `connected=true`, `level=4`, `IconGroup(4G)` nhưng `isShowSlot0:false`. Snapshot màn hình `240x320`, density `160`, `icon_blacklist=null`.

## Bằng chứng DEX

Trong `MobileSignalController.notifyListeners()` có:

```java
SystemProperties.getBoolean("uservice.control.slot0", false)
```

`NetworkControllerImpl` đăng ký action `action.g4.systemui.show.slot0` và đọc cùng thuộc tính. Việc tìm được action không chứng minh broadcast được dùng ở lần PASS; ảnh lệnh thực tế cho thấy **thay property**.

## Các mốc đã kiểm thử

| Thời điểm | Bằng chứng | Kết quả |
| --- | --- | --- |
| 20/11 | Đặt `uservice.control.slot0` từ false → true; đọc lại và thấy chữ 4G/vạch sóng | **PASS trong phiên** |
| Sau reboot | Property có thể trở về false | **Cách đặt thủ công chưa bền** |
| 21/11 | Magisk `h01_mobile_4g_autoshow` v1.1.0 dùng service.sh sau Android boot, đặt true **một lần** rồi thoát | **PASS sau reboot** |
| 21/11 cấp USB-C lạnh | Auto Power-On v0.6 + AutoHotspot v0.4 + AutoShow v1.1 | **REPORTED PASS tích hợp** |

V1.1 là **one-shot**, không polling 30 giây/lần. Chưa tìm được daemon cụ thể đặt lại property và chưa đo độ ổn định liên tục; không ghi nhận là lỗi sóng LTE/driver modem.

SystemUI.apk/ODEX/VDEX chỉ được đọc để phân tích, không cần sửa APK trong phép thử. Không công bố các binary OEM, địa chỉ và dữ liệu SIM. Xem [tổng quan](4g-status-icon.md) và [Auto Power-On](../boot/auto-power-on-cold-boot-evidence.md).