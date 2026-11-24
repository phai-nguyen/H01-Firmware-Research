# H01 — ma trận Activity, cấu hình ẩn OEM và mức rủi ro từ APK/ODEX/VDEX

**Nguồn:** [Notion “Phân tích chức năng ẩn từ APK, ODEX, VDEX” ngày 19/11/2026](https://app.notion.com/p/41dc5d5277a981db8ad1fff1aca10bc5), mục 3–7. **STATIC VERIFIED cho tên component/chuỗi/manifest; không phải kiểm thử tất cả Activity trên máy H01.**

## Khả năng nhìn thấy ≠ quyền mở ≠ tính năng hoạt động

Một lớp Activity hoặc tên flag trong DEX chỉ cho biết mã **có mặt trong mẫu firmware**. Để hiển thị/chạy còn phụ thuộc khai báo `exported`, `enabled`, quyền gọi, user state, dependency service, kiểm tra OEM flag và thiết bị thật. Lỗi scanner v1.1 **22 cảnh báo** không được diễn giải là không có DEX; [parser độc lập](hidden-scanner-parser-failure-and-recovery.md) đã kiểm 8 APK + 7 ODEX + 7 VDEX.

## Ma trận các màn hình được nhận diện

| Gói | Màn hình / chức năng tìm thấy | Mức đánh giá từ nguồn | Điều chưa được xác minh |
| --- | --- | --- | --- |
| Android Settings | `RunningServicesActivity`, `AppMemoryUsageActivity`, `SpecialAccessSettingsActivity`, `WifiP2pSettingsActivity` | **Thấp nếu chỉ xem** | Mỗi màn mở được trên H01 và có dữ liệu hợp lệ |
| Android Settings | `DevelopmentSettingsActivity`, `VpnSettingsActivity`, `SimSettingsActivity`, `DataUsageSummaryActivity`, `NightDisplaySettingsActivity` | **Vừa hoặc phụ thuộc cấu hình** | Quyền, khả năng áp dụng, phần cứng và màn hình runtime |
| Android Settings | `UcApnSettingsActivity`, `UcApnEditorActivity`, `RadioInfo`, `BandMode`, `TestingSettingsActivity` | **Cao** | Không tự mở/sửa radio, band, APN |
| SystemUI | `TunerActivity` | **Không bật thử** | Manifest ghi `enabled=false` |
| GlocalmeHome | `MiniLauncherActivity`, `UsbShareActivity`, `BatteryProtectActivity`, `DisplayActivity`, `AssistantActivity`, `OptimizeActivity` | **Ứng viên UI**, phải xác minh từng màn | Không suy tất cả Activity đều mở được hoặc có đầy đủ backend |
| GlocalmeHome | `LocationActivity`, `LockSetActivity`, `LockScreenActivity` | **Cần giới hạn bằng chứng** | Mục LockSet có **UI PASS**, còn PIN thực và khóa vuốt chưa PASS |
| MMI | Nhánh kiểm tra GPS, Bluetooth, NFC, USB OTG, cảm biến, vân tay, `AutoRebootActivity` | **Factory/rủi ro cao** | MMI có thể chung nhiều model; không chứng minh linh kiện H01 có đủ |

## Những chuỗi cờ GlocalMe được tìm thấy

Nhóm UI/thiết bị:

`show_battery_protect`, `show_display`, `show_location_mode`, `show_passwordLock`, `show_slide_unlock`, `show_netOptimize`, `usbShareEnable`, `batteryProtectDefaultClose`.

Nhóm SIM/mạng/cập nhật:

`show_localSim`, `show_simManager`, `show_hotspotManager`, `show_push_message`, `show_qrCode`, `show_language`, `show_blackList`, `show_whitelist`, `show_recover`, `show_update`.

**Chỉ có** `show_passwordLock="false"` được trích rõ trong bản `productinfo` tại nguồn liên quan. **Không biết giá trị runtime của các cờ còn lại** từ danh sách string. `show_push_message` không chứng minh gửi/nhận SMS; `show_simManager` không chứng minh hai SIM vật lý đã hoạt động.

## Lưu ý các feature hệ thống

Bản `features.txt` khai báo GPS, Bluetooth/BLE, một số cảm biến, USB Host, Wi‑Fi Direct, GSM/CDMA và SIP/VoIP. Nhưng [báo cáo cảm biến](rotation-and-sensors-timeline.md) có `No Sensors on the device` trong snapshot Android. **Feature khai báo không thay cho sensorservice, sysfs, driver hay thử nghiệm phần cứng.**

**Tổng kiểm kê:** 369 Activity, 24 alias, 29.735 lớp DEX trong tám gói, và 473 component được đếm tổng hợp. Những con số này **không** phải số tính năng người dùng có thể sử dụng.

Không đăng APK/VDEX/ODEX nguyên bản hoặc script tự khởi chạy Factory Test, APN/radio, AutoReboot, secret-code. Không tự thay cờ OEM hoặc profile SIM để “mở” chức năng. Xem [inventory](hidden-feature-inventory.md), [khảo sát menu 2846](assistant-2846-log-tools-safety-evidence.md) và [PIN UI](lockset-high-contrast-ui-validation.md).