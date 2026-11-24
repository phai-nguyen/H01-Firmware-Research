# H01/K1 — cấu hình recovery, Android Treble và giới hạn lựa chọn ROM/GSI

**Nguồn:** [Notion tổng H01, H175 — “Chọn hướng mở rộng H01: mod firmware gốc hay thay Android”](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Đây là snapshot property từ ramdisk Recovery và đánh giá phương án**, không phải bản ROM đã được port.

## Các thuộc tính trong Recovery ramdisk gốc

Snapshot `prop.default` được giải từ **ảnh Recovery của đúng H01**, cùng họ build `K1_TSV3.1.005.001.240116`:

| Property | Giá trị tại nguồn |
| --- | --- |
| `ro.build.version.sdk` | `27` — Android 8.1 |
| `ro.build.version.security_patch` | `2019-04-05` |
| `ro.product.cpu.abilist` | `armeabi-v7a,armeabi` |
| `ro.treble.enabled` | `true` |
| `config.disable_cameraservice` | `true` |
| `config.disable_searchmanager` | `true` |
| `config.disable_vibrator` | `true` |
| `config.disable_noncore_mifi` | `true` |
| `config.disable_mediaproj` | `true` |
| `config.disable_vrmanager` | `true` |
| `config.disable_consumerir` | `true` |
| `config.disable_pinner` | `true` |

**Không nhầm:** đây là **prop.default của Recovery image**, chưa phải `getprop` runtime trên mọi lần boot H01. Một property `config.disable_...` không tự chứng minh chức năng đó đang disable ở một process cụ thể; phải truy xem nơi đọc cờ và tình trạng HAL/phần cứng.

## Vì sao Treble=true chưa đủ để chọn GSI?

Trên H01 hiện có:
- SoC **MSM8909**, Android **8.1/API 27**, ABI **ARM32**, kernel **3.18.71**.
- Bảng GPT có `system` và `vendor` riêng, nhưng **tách phân vùng không đồng nghĩa mọi hợp đồng vendor/system tương thích GSI bất kỳ**.
- UService, các thư viện OEM và các dịch vụ modem/SIM/hotspot hiện diện **cả trong /system**, không chỉ `vendor`. Thay system có nguy cơ mất dependency hãng ngay cả khi giữ nguyên vendor.
- Chưa có bằng chứng nghiệm thu VNDK/linker namespaces, VINTF manifest/matrix, fstab/verity, kích thước ảnh và boot chain cho một GSI mới cụ thể.
- Mã/ảnh Android cùng chip Qualcomm không tự tương thích đúng **DTB, màn hình, cảm ứng, sạc, WLAN, RIL, audio và phím**.

| Hướng trong nhật ký | Đánh giá tại nguồn |
| --- | --- |
| **Mod từng tính năng trên firmware gốc** | **Ưu tiên**, vì đã cài được J2ME Loader và KISS mà không thay system |
| Port ROM MSM8909 khác | **Chưa có bản H01/K1 được kiểm chứng**, cùng chip không đủ |
| GSI | **Còn nghiên cứu**, không có ảnh GSI nào được nghiệm thu cho H01 |

Các bản GSI hiện đại thường giả định hợp đồng Android 9+; không mặc nhiên chạy trên vendor Android 8.1 chỉ vì có chữ `Treble`.

## Quy tắc không suy diễn

Một APK chỉ có thư viện native ARM64 không chạy ARM32 chỉ bằng thay minSdk. Sửa launcher không nâng SDK 27. Bật cờ disable không tự tạo camera/mic/sensor. **Không có ROM/GSI thay thế đã PASS ở mục nguồn** và không tự flash/overwrite system trong nhiệm vụ công bố này.

Xem [firmware overview](overview.md), [UService](../system/uservice-loader.md), [root/recovery](../boot/root-and-recovery.md).