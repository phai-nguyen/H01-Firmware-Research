# H01 — ứng dụng hệ thống, tiến trình nền và ma trận rủi ro trước tối ưu

**Nguồn:** [Notion tổng H01, H007–H008 và H187–H191](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), đối chiếu với [init map](init-service-map.md), [RAM/PSS](ram-and-package-audit.md) và [FOTA/Feedback](fota-feedback-disable-vs-uninstall-final-state.md). **Mốc 24/11/2026**; `PACKAGE/PROCESS OBSERVED`, `DEPENDENCIES PARTIAL`. Đây là tài liệu kiểm kê, **không có thử nghiệm tắt/gỡ mới**.

## 1. Ba lớp khác nhau cần tách riêng

1. **APK/package:** có trong `/system/app` hay `/system/priv-app` không đồng nghĩa đã chạy. `installed=true`, `enabled=3` và trạng thái process là các thuộc tính khác nhau.
2. **Android process/service:** `dumpsys activity`, `ps` và PSS phản ánh một snapshot. Cùng UID hoặc service persistent có thể tồn tại dù một package user 0 bị disable.
3. **Native init service:** `uc_qmi_clnt`, `uc_netlink`, `unet`, `hostapd`, `rild` không phải package APK thông thường; `pm disable-user` không phải công cụ để quản lý dependency của init.

## 2. Danh mục nguồn và quyết định can thiệp

| Thành phần | Nguồn/ghi nhận | Mức rủi ro nếu vô hiệu hóa mù | Kết luận hiện có |
| --- | --- | --- | --- |
| GlocalmeHome, Launcher3, `vn.h01.home` | Tệp APK OEM và các launcher tùy biến; H01 Home PSS đã đo | **Cao**: mất giao diện HOME, đường cài đặt hoặc thao tác thiết bị | Giữ đường quay lại launcher đang dùng |
| `com.ucloudlink.uservice` | Dịch vụ OEM, UID radio trong snapshot, PSS ~38.108 kB | **Rất cao**: có thể ảnh hưởng chức năng SIM/mạng | Không có phép thử tắt an toàn |
| Android Phone/SystemUI, `ril-daemon`, `uc_qmi_clnt`, `uc_netlink`, `unet` | Mạng, radio, OEM native runtime | **Rất cao**: có thể mất LTE/hotspot/điều khiển | Không tắt trong đợt nghiên cứu |
| InstallService (`com.ucloudlink.base.installservice` trong báo cáo PackageManager) | Liên quan đường cài APK được OEM cho phép | **Cao**: có thể ảnh hưởng khả năng cài/khôi phục app | Cần khảo sát phụ thuộc trước |
| `com.abupdate.fota_demo_iot` | FOTA; trạng thái cuối của user 0: `installed=true, enabled=3` | **Không xác định**: có thể ảnh hưởng cập nhật | Chủ thiết bị đã chọn **giữ disabled-user, không uninstall** |
| `com.ucloudlink.feedback` | Feedback, cùng trạng thái `installed=true, enabled=3` | **Không xác định**: còn dấu vết process system UID | Không suy có thể xóa an toàn |
| MMI / UKL Factory | APK/bộ chức năng kiểm tra OEM, không thấy process trong một snapshot RAM | **Chưa xác định**: mất khả năng chẩn đoán | Không coi “không thấy process” là ứng viên gỡ |
| `com.googlecode.eyesfree.setorientation` | PSS ~11.573 kB, foreground service tại lần đo | **Phụ thuộc cấu hình**: xoay màn hình có thể chịu tác động | Chỉ xem xét nếu xác minh không còn dùng và có rollback |

**Mức rủi ro là đánh giá thận trọng theo vai trò**, không phải thử nghiệm thực tế rằng thao tác tắt chắc chắn gây lỗi.

## 3. Snapshot RAM không phải dự báo mức tiết kiệm

Trong một lần đo, `MemTotal=929.480 kB`, `MemAvailable=549.540 kB`, uptime khoảng 2 giờ 21 phút. `MemAvailable` **không phải** RAM chưa được cấp phát; PSS của vài process **không cộng** thành RAM chắc chắn có thể giải phóng nếu gỡ APK. FOTA không xuất hiện trong danh sách process đang chạy tại một mốc; Feedback vẫn xuất hiện với PSS khoảng **3.070 kB** dù `enabled=3`. Sự khác biệt này cần được ghi nhận như trạng thái nguồn, không coi đó là lỗi disable.

## 4. Tiêu chuẩn để nâng từ `PARTIAL` lên `VERIFIED`

Một kết luận “ứng dụng X có thể tắt an toàn” phải có: (a) package name được xác nhận trên đúng máy/build; (b) trạng thái trước thay đổi; (c) sơ đồ phụ thuộc quan trọng và phương án hồi phục; (d) kiểm tra 4G, hotspot, launcher, cài APK và boot trước/sau; (e) kết quả qua reboot khi cần; (f) đánh giá dữ liệu riêng đã che. **Hiện báo cáo này không có bộ kiểm chứng đầy đủ đó.**

Các lệnh **chỉ đọc** có thể dùng để lập snapshot tại chỗ, nhưng output phải được xử lý ẩn danh trước khi chia sẻ:

```sh
adb shell pm list packages -d
adb shell dumpsys activity processes
adb shell dumpsys meminfo
adb shell getprop init.svc.uc_qmi_clnt
adb shell getprop init.svc.uc_netlink
```

Không tự chạy `pm uninstall`, `pm disable-user`, `stop`, `setprop`, thao tác Magisk hoặc `rm` để làm báo cáo trông như đã PASS. Những thay đổi đã có từ lịch sử phải được mô tả như lịch sử, không tái thực hiện khi chưa có yêu cầu và rollback.

## 5. Giới hạn công bố

Không đăng APK OEM, file `init.rc` nguyên bản nếu chưa đủ quyền phân phối, ảnh launcher chứa thông tin cá nhân, serial, IMEI/IMSI, token, địa chỉ Wi-Fi và log hệ thống thô. Không có xác minh an toàn riêng cho mọi build H01. Tài liệu là **ma trận ưu tiên nghiên cứu**, không phải danh sách package nên gỡ.

**Liên quan:** [H01 App Control](../projects/app-control.md), [lịch sử cài APK](package-install-and-fota-feedback.md), [RAM](ram-and-package-audit.md), [vendor HAL](vendor-init-hals-hostapd-20261114.md), [chính sách công bố](../security/publication-policy.md).
