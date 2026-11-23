# UCloudlink UService — loader DEX, native libraries và binary update

**Nguồn:** Notion H01 mục 5, 6, 14 (10/11/2026). **Trạng thái: phân tích tĩnh; không giải mã SoftSIM/payload có thể chứa khóa.**

## APK và mã bytecode

| Hạng mục | Kết quả được ghi nhận |
| --- | --- |
| UService APK | 23.449.980 byte |
| VDEX | 8.853.712 byte, `vdex010`, có một DEX `035` |
| Method IDs | 64.209 |
| Class definitions | 7.291 |
| Bản DEX raw ban đầu | Có quickening và checksum không khớp |
| Bản DEX dequickened sau đó | 37.008/37.008 quickening records được xử lý; SHA-1/Adler-32 sau phục hồi khớp |

**Đính chính theo thời gian:** kết luận “chưa dequickening hoàn chỉnh” trong mục 6 chỉ mô tả bản raw giai đoạn đầu; mục 14 ghi nhận việc khôi phục DEX có kiểm tra checksum ở mức cấu trúc. Điều này **chưa chứng minh** giải mã được toàn bộ logic obfuscation hoặc mọi payload nạp động.

## Thành phần loader đã tìm thấy

- `com.ucloudlink.uservice.UServiceApplication`: `onCreate`, `loadJars`, `loadLibraries`, `overrideUcAssetFile`, `getUcAssetsDir`.
- `com.ucloudlink.framework.remoteuim.LibDexload.loadUcClasses(Context)`: điểm vào native.
- `UcConnectCtrl`: `loadDex()`, `loadLibraries()`, `init()`.
- `BinaryUpdateHelper`: tham chiếu `binary_update.json`, `currentVersion`, `lastVersion`, `binaryPath`, `md5`.
- Các đường dẫn/chuỗi `assets/uc-asset0.bin`, `/files/code`, `mini.dex`, `mini.odex`, `loadDex` phù hợp cơ chế loader mã động. **Không khẳng định tất cả đều tồn tại trên máy tại runtime.**

Phân tích native `libdexload.so` tìm thấy tham chiếu Android AssetManager, ART/Dalvik `DexFile`, routine mang tên RC4 và kỹ thuật ELF hooking. **Chưa xác minh** `uc-asset0.bin` thực sự dùng khóa/thuật toán cụ thể nào, cũng chưa xác định hook nào được chạy.

## Lớp UCloudlink native

12 ELF ARM đã khảo sát bao gồm các chức năng: MQTT, HTTP/HTTPS, DNS, JSON, Protobuf, quản lý socket, policy Wi-Fi và FOTA. Thư viện Protobuf có message liên quan update, VSIM và quản lý thiết bị. Có symbol/message **không đồng nghĩa** daemon thực sự gửi lệnh đó.

`TestReceiver` tham chiếu nhiều action `com.ucloudlink.cmd.*` (trạng thái SIM, cấu hình log, mạng, PLMN, dữ liệu đo). Chưa xác định permission, sender hoặc tác động đầy đủ: **không phát broadcast thử nghiệm**.

## Dữ liệu cần bảo vệ

- Asset `uc-asset0.bin` có cấu trúc/entropy bất thường; chưa giải nghĩa hoàn chỉnh.
- Các asset SoftSIM và native `SoftSimNative_*` liên quan IMSI, ICCID, KI/OPC và APDU: **không mở khóa, đăng, giải mã hoặc chia sẻ**.
- `mcfg_hw.mbn` và `mcfg_sw.mbn` là cấu hình modem được ghi nhận, **không phải full baseband firmware**.

**Nguồn liên quan:** [FOTA](../firmware/fota-abup-internals.md), [daemon/socket](../network/ucloud-daemons-and-sockets.md), [chính sách công bố](../security/publication-policy.md).