# RAM và ứng dụng hệ thống H01 — báo cáo snapshot & giới hạn tối ưu

**Nguồn:** Notion H01, các mục “Đổi phạm vi: giữ disable, rà ứng dụng để giảm RAM” và “Kết quả đo RAM trên H01 thật và bước tối ưu tiếp theo”, nghiên cứu tháng 11/2026. **Trạng thái: ADB RAM SNAPSHOT OBSERVED; việc tắt ứng dụng được đề xuất nhưng chưa xác nhận thực hiện sau báo cáo.**

## Bộ nhớ theo snapshot H01

| Chỉ số từ `/proc/meminfo` | Giá trị |
| --- | --- |
| `MemTotal` | 929.480 kB ≈ 907,7 MiB |
| `MemAvailable` | 549.540 kB ≈ 536,7 MiB |
| `MemFree` | 128.320 kB ≈ 125,3 MiB |
| Uptime khi thu thập | Khoảng 2 giờ 21 phút |

**Cách đọc đúng:** `MemAvailable` bao gồm bộ nhớ có thể thu hồi, không phải lượng RAM trống hoàn toàn; snapshot này không chỉ ra tình trạng thiếu RAM vào thời điểm thu thập. Không dự báo mức tiết kiệm RAM bằng cách cộng RSS nhiều tiến trình.

## Kết quả PSS từ `dumpsys meminfo`

| Package/nhóm | PSS theo lần đo | Ý nghĩa |
| --- | ---: | --- |
| `com.googlecode.eyesfree.setorientation` | 11.573 kB ≈ 11,3 MiB | OrientationService foreground, có BootReceiver; ứng viên cân nhắc nếu không còn dùng |
| Launcher3 | 12.009 kB ≈ 11,7 MiB | Cache adj 900, có thể được thu hồi; không tự xóa vì đang quản lý HOME |
| `vn.h01.home` | 14.879 kB ≈ 14,5 MiB | Launcher đang sử dụng, **giữ** |
| `com.ucloudlink.uservice` | 38.108 kB ≈ 37,2 MiB | Dịch vụ mạng/SIM OEM, **giữ** |
| SystemUI | 42.030 kB | Thành phần giao diện quan trọng, **giữ** |
| Telephony/Phone | 28.450 kB | Thành phần radio/phone, **giữ** |
| `com.ukelink.dusk.mmi`, `com.ukl.factory` | Không thấy tiến trình trong snapshot | Chưa có bằng chứng tắt chúng giúp giảm RAM |

Tại snapshot, FOTA và Feedback còn installed, có `enabled=3` (disabled-user); không được giải thích việc còn thấy tiến trình system UID 1000 là “gỡ/tắt thất bại” nếu chưa phân tích dependency. Một số package cũ không có trong danh sách mới, nên không được tắt theo lịch sử.

## Nguyên tắc tối ưu hóa

1. Giữ `UService`, `InstallService`, `GlocalmeHome`, `vn.h01.home`, Magisk, SystemUI, Phone/TeleService, các dịch vụ Wi-Fi/RIL/QMI.
2. Chỉ xem xét tắt **ứng dụng thật sự đang chiếm PSS/giữ foreground service** khi không còn cần chức năng, và bảo đảm có đường bật lại.
3. Đo trước/sau cùng điều kiện uptime, hotspot, SIM, launcher; không coi giá trị của một ảnh CMD là mức RAM cố định.
4. Không `force-stop` hoặc `pm disable-user` hàng loạt; đặc biệt không tắt MMI/Factory chỉ vì APK tồn tại.
5. Ghi lại các thay đổi phiên bản module Magisk vì có thể thay cơ chế khởi động, icon 4G và tùy chỉnh UI.

## Kiểm tra chỉ đọc

```bat
adb shell cat /proc/meminfo
adb shell dumpsys meminfo
adb shell pm list packages -d
adb shell dumpsys activity processes
```

Báo cáo công khai không chứa serial, ID thiết bị, thông tin SIM, địa chỉ hotspot hoặc raw log. Đề xuất tắt SetOrientation trong nhật ký **không phải bằng chứng đã tắt hoặc xác nhận số RAM tăng sau đó**.

**Liên quan:** [App Control](../projects/app-control.md), [xoay màn hình](display-rotation-navigation.md), [init service map](init-service-map.md).