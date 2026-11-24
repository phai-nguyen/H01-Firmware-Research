# H01 — 12 thư viện UCloudlink ELF32 và phạm vi chứng cứ symbols

**Nguồn:** [Notion H01, mục 5–7 (10/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **STATIC SYMBOL/ELF VERIFIED**, chức năng runtime từng daemon chưa kiểm thử đầy đủ.

## Danh mục đã thu từ firmware mẫu

| Thư viện | Kích thước ghi trong nguồn | Nhóm symbol/chức năng nhận diện |
| --- | ---: | --- |
| `libucore.so` | 91.992 byte | network policy, QoS, whitelist, DNS, flow statistics |
| `libucos.so` | 24.628 | timer, factory/power/GPIO helpers |
| `libucprotobuf.so` | 262.836 | protobuf cho FOTA, VSIM, thiết bị |
| `libmosquitto.so` | 45.756 | MQTT connect/publish/subscribe và TLS APIs |
| `libghttp.so` | 33.176 | HTTP request/response |
| `libcurl.so` | 226.080 | HTTP(S), TLS, range/resume |
| `libuclog.so` | 24.588 | logging |
| `libucjson.so` | 24.740 | JSON parse/build |
| `libutools.so` | 37.092 | task/thread pool, socket server/client |
| `libuitface.so` | 24.388 | interface/app registration |
| `libudns.so` | 32.680 | DNS requests |
| `libprotobuf-c-1.1.1.so` | 28.700 | protobuf-c runtime |

Đây là **12 ELF32 ARM little-endian** của bộ phân tích. `libucprotobuf.so` có **1.385 symbols export** trong hồ sơ. Các tên message như `fota_upg_info`, `fota_upgrade_board`, `m2at_fota_update_start`, `ter_fota_file_download`, `ter_fota_upgrade_succ/fail` là **định nghĩa protobuf/serializer**, không chứng minh một gói OTA đã tải hoặc modem đã nhận lệnh.

## Ranh giới kết luận

- **Có thể khẳng định:** tệp chứa metadata/symbol phù hợp lớp giao tiếp HTTP/MQTT, protobuf, policy và log UCloudlink.
- **Chưa khẳng định:** thư viện nào sở hữu MQTT listener ở một snapshot cụ thể, dependency graph runtime hoàn chỉnh, chuỗi API phát message FOTA, cấu hình endpoint hiện có hoặc chức năng SoftSIM đã chạy.
- Mốc network 10/11 từng chưa ghép socket inode tới PID; kết quả snapshot v14 ngày 22/11 **đã bổ sung attribution** cho một số port, không tự chứng minh toàn bộ symbol của từng thư viện được gọi.

Mọi binary OEM, protobuf payload có thông tin khách hàng, SoftSIM profile, certificate private và log máy đều giữ riêng. **Không phát hành thư viện gốc**.

Xem [daemon/socket](ucloud-daemons-and-sockets.md), [network v13–v14](ucloud-live-sockets-v13-v14.md), [UService](../system/uservice-loader.md).