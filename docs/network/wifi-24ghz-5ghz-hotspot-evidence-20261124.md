# ZEUS H01 — Wi-Fi 2,4 GHz / 5 GHz: bằng chứng cấu hình và hiện tượng hotspot tắt

**Mốc tổng hợp:** 24/11/2026. **Phân loại:** `FIRMWARE CONFIG VERIFIED` + `USER-REPORTED FAILURE` + `HARDWARE CAPABILITY OPEN`. Đây là báo cáo giới hạn chứng cứ, **không xác nhận** H01 có hoặc không có radio 5 GHz. Chưa thực hiện phép thử phần cứng mới trong đợt công bố.

## 1. Triệu chứng do chủ thiết bị báo cáo

Giao diện H01 có tùy chọn **5 GHz**. Khi chọn, hotspot đang phát tự tắt, thay vì chuyển sang mạng 5 GHz hoạt động. Người thử quan sát tình trạng này trên H01 đang sử dụng; **chưa có log cùng thời điểm**, bảng tần số radio hoặc kết quả quét SSID từ máy khác được đưa vào báo cáo công khai. Không suy rằng chipset không hỗ trợ 5 GHz chỉ từ hiện tượng giao diện này.

**Khả năng giải thích chưa được phân định:** cấu hình giao diện được tái sử dụng từ nền tảng khác; thiếu hỗ trợ radio/firmware/driver; quốc gia/kênh không hợp lệ; quá trình khởi tạo AP trả lỗi; hoặc trạng thái SoftAP bị thay đổi bởi dịch vụ OEM. Đây là **giả thuyết**, không phải kết luận đã xác nhận.

## 2. Bằng chứng chắc chắn đã có trong firmware

Từ hai tệp báo cáo vendor init RC đã đối chiếu trên Dropbox, [báo cáo vendor init](../system/vendor-init-hals-hostapd-20261114.md) ghi:

| Mục quan sát | Dữ kiện | Không được suy ra |
| --- | --- | --- |
| `wifi_hal_legacy` | Có service trong vendor init | Radio hoạt động mọi băng tần |
| `hostapd` | Tham chiếu `/data/misc/wifi/hostapd.conf` | Băng 2,4 hoặc 5 GHz đang phát tại runtime |
| `hostapd_dual` | Tham chiếu `hostapd_dual2g.conf` và `hostapd_dual5g.conf` | H01 có hai radio hoạt động đồng thời |
| `disabled`, `oneshot` | Các stanza được khai báo với cờ này | Có service đang chạy, hay chuyển băng thành công |

Chữ **dual** ở `hostapd_dual` mô tả cấu hình dịch vụ Wi-Fi; không liên quan đến cấu hình **DSDS hai SIM** của modem.

## 3. Phép kiểm chỉ đọc có thể thực hiện trên chính H01

Chụp trạng thái **trước khi đổi băng** và **ngay sau khi hotspot tắt**, không cần flash hay root:

```sh
adb shell getprop init.svc.hostapd
adb shell getprop init.svc.hostapd_dual
adb shell dumpsys wifi
adb shell ls /sys/class/ieee80211
adb shell cat /proc/net/wireless
```

- `init.svc.*`: cho biết trạng thái dịch vụ nếu tên được đăng ký; property rỗng **không chứng minh** firmware thiếu Wi-Fi.
- `dumpsys wifi`: có thể cung cấp yêu cầu băng tần, trạng thái SoftAP và lỗi framework; tên trường tùy bản Android/OEM.
- `/sys/class/ieee80211`: nếu có `phy*`, có thể dùng để định vị thiết bị wireless; **không đủ** để khẳng định 5 GHz.
- `/proc/net/wireless`: thông tin wireless interface có thể rỗng tùy driver; không phải bảng supported bands.

Nếu firmware thực sự có công cụ `iw` và cho phép thao tác đọc, `iw phy` / `iw list` có thể cho danh sách tần số mà driver công bố. **Không giả định H01 cài sẵn `iw`**; driver báo khả năng cũng chưa bảo đảm SoftAP 5 GHz PASS. Phép thử xác nhận tiếp theo cần **thiết bị thu khác quét được SSID trên kênh 5 GHz** và log cho thấy SoftAP còn hoạt động.

**Bảo vệ dữ liệu:** `dumpsys wifi` có thể chứa SSID, BSSID/MAC, mật khẩu hoặc lịch sử mạng. Không đưa bản xuất raw lên issue công khai. Chỉ công bố trạng thái đã ẩn danh; không thay đổi country code, `setprop`, `svc wifi`, `start/stop hostapd`, file cấu hình hoặc driver để “ép” 5 GHz.

## 4. Kết luận và điều kiện đóng nhánh

- **Đã xác minh từ nguồn init:** tên dịch vụ và đường dẫn cấu hình `hostapd_dual5g.conf` tồn tại trong văn bản đã lưu.
- **Đã được người thử báo cáo:** bấm chọn 5 GHz làm hotspot tắt.
- **Chưa xác minh:** radio có 5 GHz hay không, khả năng SoftAP 5 GHz của driver, kênh/quốc gia đang áp dụng, nguyên nhân chính xác của lỗi, và Wi-Fi 5 GHz PASS trên thiết bị thật.
- **Điều kiện đánh dấu PASS 5 GHz:** có log cùng lần thử và một máy thu độc lập nhận SSID ở kênh 5 GHz khi hotspot vẫn hoạt động ổn định. Không thể thay bằng tên file cấu hình hay menu Settings.

**Liên quan:** [vendor init HAL/hostapd](../system/vendor-init-hals-hostapd-20261114.md), [init map](../system/init-service-map.md), [mạng/daemon](ucloud-daemons-and-sockets.md), [chính sách công bố](../security/publication-policy.md).
