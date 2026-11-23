# H01 — danh mục Activity và cờ hiển thị OEM trong APK/DEX

**Nguồn:** [Notion phân tích 8 APK/7 ODEX/7 VDEX ngày 19/11/2026](https://app.notion.com/p/41dc5d5277a981db8ad1fff1aca10bc5). **Trạng thái: phần lớn STATIC VERIFIED, runtime chỉ xác nhận các trường hợp có bằng chứng riêng.**

## Quy mô dữ liệu

Scanner v1.1 thu được **8 APK, 7 ODEX, 7 VDEX**. Parser v1.0 trước đó lỗi khởi tạo CLR trên Windows 7; parser v1.1 còn lỗi `VBArray expected`, vì vậy báo cáo dùng phân tích độc lập `AndroidManifest.xml`/DEX. Tổng trong bảng nguồn: **369 Activity + 24 Alias = 393**, **473 component** khi gồm service/receiver/provider, **29.735 class DEX**. Những con số này **không phải số tính năng H01 chạy được**.

## Những nhóm màn hình đã nhận diện

| Package | Màn hình hoặc mã được thấy | Độ chắc chắn |
| --- | --- | --- |
| Android Settings | RunningServices, AppMemoryUsage, SpecialAccess, WifiP2p, Development, VPN, SimSettings, DataUsage, NightDisplay, NotificationAccess | Manifest/DEX; chưa thử tất cả |
| Android Settings OEM | `UcApnSettingsActivity`, `UcApnEditorActivity` | Manifest/DEX; sửa APN chưa được chứng minh an toàn |
| SystemUI | `TunerActivity` | Manifest ghi **enabled=false** |
| GlocalmeHome | `UsbShareActivity`, `BatteryProtectActivity`, `DisplayActivity`, `AssistantActivity`, `OptimizeActivity`, `LocationActivity`, `LockSetActivity`, `LockScreenActivity` | Có thành phần; runtime chỉ xác nhận các màn đã thử riêng |
| MMI | 44 Activity, gồm GPS, USB OTG, sensor, Bluetooth, display và AutoReboot | Bộ test nhiều model; không chứng minh H01 có tất cả phần cứng |
| UklFactory | Một Activity | Manifest, không khẳng định quyền truy cập |

## Các cờ OEM trong DEX

Nhóm string ghi nhận: `show_battery_protect`, `show_display`, `show_location_mode`, `show_passwordLock`, `show_push_message`, `show_slide_unlock`, `show_netOptimize`, `show_localSim`, `show_simManager`, `show_hotspotManager`, `show_qrCode`, `show_language`, `usbShareEnable`, `show_blackList`, `show_whitelist`, `show_recover`, `show_update`.

**Chỉ `show_passwordLock="false"` đã được quan sát trong productinfo** ở các nghiên cứu trước. Các string khác chỉ chứng minh đường mã biết tên cờ, không biết giá trị hiệu lực runtime; `show_push_message` cũng không tương đương inbox SMS đã chạy.

Bản feature Android khai báo GPS, BLE, USB host, Wi-Fi Direct, cảm biến và SIP/VoIP, nhưng có thể là khai báo chung từ OEM. Ví dụ báo cáo cảm biến khác thấy `No Sensors on the device`; không được quảng bá các feature từ `pm list features` thành phần cứng thật.

## Rủi ro

Xem trạng thái ứng dụng/RAM thường ít tác động; SIM settings/APN, USB Share, RadioInfo/BandMode, Factory Reset, AutoReboot và SystemUI Tuner `enabled=false` là các luồng có thể thay trạng thái. **Không tự kích hoạt** chỉ vì được tìm thấy trong manifest.

Xem [bảng kiểm kê đầy đủ](hidden-feature-inventory.md), [menu 2846](glocalmehome-about-secret-code-2846.md) và [keyguard](keyguard-framework-vdex-ucloud-sleep.md).