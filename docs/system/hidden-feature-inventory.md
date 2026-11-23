# Kiểm kê chức năng ẩn — APK/ODEX/VDEX H01

**Mốc phân tích tĩnh 19/11/2026; chưa chạy hàng loạt các Activity.**

H01 Hidden Feature Scanner v1.1 đã thu **8 APK, 7 ODEX và 7 VDEX**; parser cũ có 22 cảnh báo, trong đó `VBArray expected`, nên phân tích độc lập đọc Manifest/DEX thay cho kết quả parser lỗi.

| Package | Activity | Alias | DEX class |
| --- | ---: | ---: | ---: |
| `com.android.settings` | 220 | 20 | 3.826 |
| `com.android.systemui` | 19 | 1 | 3.830 |
| `com.glocalme.g4home` | 55 | 0 | 17.932 |
| `com.ukelink.dusk.mmi` | 44 | 0 | 2.790 |
| `com.android.phone` | 29 | 3 | 1.322 |
| `com.android.providers.settings` | 0 | 0 | 31 |
| `com.android.provision` | 1 | 0 | 1 |
| `com.ukl.factory` | 1 | 0 | 3 |
| **Tổng** | **369** | **24** | **29.735** |

Báo cáo nhận diện **473 component** (trong đó 393 Activity/Activity Alias). **Đây không phải 473 tính năng có thể dùng**.

### Ứng viên

- Settings: RunningServices, AppMemoryUsage, SpecialAccess, WifiP2p; RadioInfo, BandMode và chỉnh APN là nhóm nguy cơ cao.
- SystemUI: `TunerActivity` có trong manifest nhưng `enabled=false`.
- GlocalmeHome: BatteryProtect, UsbShare, Optimize, Display, Assistant, LockSet, LockScreen.
- Cờ OEM: `show_passwordLock`, `show_simManager`, `show_localSim`, `show_hotspotManager`, `show_push_message`, v.v. Chỉ `show_passwordLock="false"` đã được ghi nhận trong productinfo; **không biết giá trị runtime các cờ còn lại**.
- MMI có 30 bài kiểm tra trong tài nguyên; không đồng nghĩa H01 có mọi cảm biến/phần cứng đó. Xem [MMI](mmi-factory-tests.md).

Không tự bật radio/factory/ADB ROOT/USB Test Mode/AutoReboot/AgingTest. Không commit 8 APK/7 ODEX/7 VDEX hoặc dữ liệu nhận dạng của máy.

**Nguồn:** Notion “H01 – Phân tích chức năng ẩn từ APK, ODEX, VDEX (19-11-2026)”.