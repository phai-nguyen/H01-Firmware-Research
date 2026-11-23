# UCloudlink daemons, MQTT và socket runtime

**Nguồn:** trang tổng Notion H01, mục 7, 15, 19, 22 (10/11/2026); snapshot thời điểm khảo sát, không phải bản đồ port hiện tại. **Trạng thái: process/port OBSERVED; attribution ở một số cổng OPEN.**

## Tiến trình đã thấy

| Thành phần | Quan sát |
| --- | --- |
| `uc_MsgRouter` | Process với tham số dùng `/system/etc/mosquitto.conf` |
| `uC_WebServer` | Process UID root trong snapshot |
| `unet` | Process UID root |
| `uc_qmi_clnt` | Process từ `/vendor/bin`, UID root |
| `uc_netlink` | Process từ `/system/bin`, UID root |
| `uc_kglogd` | Process log của OEM |
| `com.ucloudlink.uservice` | Process UID radio |
| `com.abupdate.fota_demo_iot` | Process FOTA |

PID snapshot thay đổi sau boot. `init.qcom.rc` khai báo `uc_qmi_clnt` tạo socket `uc_qmi_clnt_socket`, `class late_start`; `uc_netlink` cũng ở `late_start`. Tìm thấy endpoint tương ứng trong `/proc/net/unix`. Không suy đoán toàn bộ process này được khai báo trong cùng một tệp RC.

## Kết quả từ /proc/net/tcp và tcp6

- Snapshot TCP IPv4: `0.0.0.0:1883` ở LISTEN, và một cặp kết nối `127.0.0.1:* ↔ 127.0.0.1:1883` ESTABLISHED. Port 1883 thường được sử dụng cho MQTT; kết hợp process `uc_MsgRouter` và cấu hình Mosquitto tạo **bằng chứng mạnh** về broker/router MQTT nội bộ, nhưng **chưa gán sở hữu socket tới PID bằng inode/FD**.
- Port 53 được thấy tại loopback và địa chỉ LAN hotspot; đây là snapshot DNS, không khẳng định daemon tên gì.
- TCP6 snapshot còn có các port 80, 443, 1883, 1989 và 8012. **Không khẳng định** HTTP(S) truy cập được từ Internet hoặc port được phơi ra WAN: cần xét network namespace, firewall, bind và định tuyến ở cùng thời điểm.
- Unix socket có `uc_qmi_clnt_socket`, `ucl_net_ns`, `ucl_net_dm` và các endpoint Qualcomm QMUX/RIL. Sự xuất hiện đường dẫn không chứng minh giao thức ứng dụng có thể tự ý gửi.

## Cấu hình và ranh giới nghiên cứu

Bản `mosquitto.conf` lưu trữ chưa cho thấy listener/password/topic/tài khoản cloud đang hoạt động ở các dòng cấu hình không comment. **Không dùng MQTT publish/subscribe tùy ý**, không quét/tấn công từ WAN, không chia sẻ IP WAN, password hotspot, account, token hoặc log network riêng.

Khảo sát tiếp theo ưu tiên **chỉ đọc**: `adb shell cat /proc/net/tcp`, `adb shell cat /proc/net/tcp6`, `adb shell cat /proc/net/unix`, `adb shell getprop init.svc.ril-daemon`. Trước khi đưa log lên công khai phải lọc địa chỉ, định danh và phiên kết nối.

**Liên quan:** [UService](../system/uservice-loader.md), [Dual SIM](dual-sim.md), [khảo sát phần cứng](../hardware/overview.md).