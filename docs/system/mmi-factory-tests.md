# MMI — danh mục 30 bài kiểm tra trong tài nguyên APK

Dữ liệu tổng hợp từ báo cáo phân tích ngoại tuyến `H01_PhanTich_3APK_MenuAn_20261119.txt` ngày 19/11/2026. Tất cả tên Activity phía dưới thuộc namespace `com.ukelink.dusk.mmi.itemstest.`; tên cuối cùng được chép theo manifest/tài nguyên, kể cả lỗi chính tả gốc `MutiTouchActivity`.

`T` = cấu hình APK cho phép hiển thị mục; `F` = cấu hình APK không bật mục. **Không phải** kết quả test PASS/FAIL, cũng **không** chứng minh H01 có phần cứng đó. Chưa xác định runtime của GlocalMe K1 dùng cột nào.

| STT | Nội dung (dịch nghĩa) | Thường | DG4 | Tên Activity (hậu tố) |
| --- | --- | :---: | :---: | --- |
| 01 | Thông tin phần mềm | T | T | `SystemVersionActivity` |
| 02 | Thông tin phần cứng | T | T | `HardwareInfoActivity` |
| 03 | Màn hình / màu sắc | T | T | `ScreenColorActivity` |
| 04 | Đèn nền / độ sáng | T | T | `BackLightActivity` |
| 05 | Cảm ứng một điểm | T | T | `SingleTouchPointActivity` |
| 06 | Cảm ứng đa điểm | T | F | `MutiTouchActivity` |
| 07 | Phím cứng | T | T | `KeyActivity` |
| 08 | Hiệu chuẩn khuếch đại âm thanh | F | F | `SmartPaCalibrateActivity` |
| 09 | Loa ngoài | T | F | `SpeakerActivity` |
| 10 | Loa thoại | T | F | `HeadphoneActivity` |
| 11 | Tai nghe | T | F | `HeadsetActivity` |
| 12 | Mic chính/phụ | T | F | `MicActivity` |
| 13 | Rung | F | F | `VibrateActivity` |
| 14 | Đèn flash | F | F | `FlashLightActivity` |
| 15 | Camera sau | F | F | `BackCameraActivity` |
| 16 | Camera trước | F | F | `FrontCameraActivity` |
| 17 | Camera sau phụ | F | F | `AuxiliaryCameraActivity` |
| 18 | Lưu trữ | T | T | `SDCardActivity` |
| 19 | Gia tốc kế | T | F | `GsensorActivity` |
| 20 | Con quay hồi chuyển | F | F | `GyroscopeSensorActivity` |
| 21 | Cảm biến tiệm cận | T | F | `ProximitySensorActivity` |
| 22 | Cảm biến ánh sáng | T | F | `LightSensorActivity` |
| 23 | Pin | T | T | `BatteryActivity` |
| 24 | Bluetooth | F | F | `BluetoothActivity` |
| 25 | Wi-Fi | T | T | `WIFIListActivity` |
| 26 | GPS | T | F | `GPSActivity` |
| 27 | NFC | F | F | `nfc.TagViewer` |
| 28 | USB OTG | T | F | `OtgActivity` |
| 29 | Thẻ SIM | T | T | `SIMCardActivity` |
| 30 | Gọi điện | F | F | `PhoneCallActivity` |

**Đối chiếu:** 30 mục, cấu hình thường **20 bật**, cấu hình DG4 **10 bật**. Cột `F` không xác nhận chức năng bị cấm vĩnh viễn hay thực tế thiếu cảm biến.

## Ưu tiên kiểm chứng

- Chỉ quan sát giao diện và các mục **thông tin phần mềm/phần cứng** trước.
- Không chạy **hiệu chuẩn amplifier**, **Autoreboot**, **AgingTest**, **Charging/DisCharging** hoặc các bài có thể tác động hệ thống.
- Với GPS, Bluetooth, SIM và audio: sự hiện diện của Activity **không** chứng minh tính năng phần cứng đang hoạt động.
- Đối chiếu thực tế bằng [công cụ ADB chỉ đọc](../tools/secret-2846-readonly.md), không tự động gọi từng Activity.
