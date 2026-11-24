# H01 — phân tích vendor init RC: HAL và cấu hình hostapd

**Nguồn:** Dropbox `H01-vendor-init-rc.txt` và `H01-vendor-init-rc 2.txt`. Hai kết quả đọc trả **cùng nội dung text 5.442 ký tự**. **Đã xem trực tiếp nội dung init**, chưa chạy lại service nào.

## Các service đã thấy

Bản text có **26 dòng bắt đầu bằng `service `**. Đây là số stanza nhận ra được trong bản text ghép, không phải số service của toàn hệ thống Android.

| Nhóm | Dịch vụ khai báo | Giới hạn kết luận |
| --- | --- | --- |
| Audio | `audio-hal-2-0` | Khai báo HAL không chứng minh PCM/audio output hoạt động |
| Security | `gatekeeper-1-0`, `keymaster-3-0`, `qteeconnector-hal-1-0` | Chưa chứng minh các nghiệp vụ keystore/attestation |
| Graphics | `gralloc-2-0`, `hwcomposer-2-1`, `display-color-hal-1-0` | Có khai báo dịch vụ đồ họa |
| Radio/GNSS | `ril-daemon`, `qti_gnss_service` | Không chứng minh mọi kênh radio/GPS đều hoạt động |
| Wi-Fi | `wifi_hal_legacy`, `hostapd`, `hostapd_dual` | Có hai cấu hình hostapd, chưa chứng minh Wi-Fi hai băng tần |
| Khác | `sensors-hal-1-0`, `vibrator-1-0`, `light-hal-2-0`, `factory-hal-1-0`, `perf-hal-1-0` | Service tồn tại không phải xác minh linh kiện phần cứng |

**Lỗi giới hạn của nguồn:** hai fragment trong bản TXT ở ranh giới `light-hal-2-0` và `mediacodec` bị nối thành một dòng, khiến `service mediacodec` không còn là dòng `^service`. Không suy rằng firmware không có media codec service và không tự sửa văn bản gốc để lấy con số stanza khác.

## Phân biệt hai cấu hình hostapd

- `hostapd` tham chiếu `/data/misc/wifi/hostapd.conf`.
- `hostapd_dual` tham chiếu `hostapd_dual2g.conf` và `hostapd_dual5g.conf`.
- Cả hai stanza có `disabled` và `oneshot`, user `wifi`. Thuộc tính **disabled** nghĩa không tự chạy chỉ vì class đã được khởi chạy; không có trong nguồn này bằng chứng cả hai mode chạy đồng thời.
- **Tên 5g trong config không chứng minh radio H01 hỗ trợ phát 5 GHz**, tương tự tên `sensors-hal` không chứng minh bo có cảm biến.
- `hostapd_dual` **không liên quan đến Dual SIM**. RIL thứ hai được khai báo trong `init.qcom.rc`, không có trong bản vendor text này.

Bằng chứng khác ngày 21/11 đã ghi Audio HAL process tồn tại nhưng **ALSA không có card/PCM và /soc/sound/status=disabled**; hai kết quả không mâu thuẫn.

Không công bố nguyên văn vendor RC của hãng, cấu hình chứa Wi-Fi password, firmware OEM hoặc lệnh start/stop service.

Xem [init service map](init-service-map.md), [âm thanh](audio.md), [Dual SIM](../network/dual-sim-ril-pcb-evidence.md).
