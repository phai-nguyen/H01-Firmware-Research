# H01 init — dịch vụ Qualcomm, UCloudlink và điều kiện khởi tạo

**Nguồn:** Notion H01 mục 18–24 (10/11/2026), đối chiếu `H01-system-init-rc.txt`, `H01-vendor-init-rc.txt`, `H01-init-qcom-rc.txt`, `H01-init-target-rc.txt`. **Trạng thái: INIT STATIC VERIFIED; process/socket OBSERVED ở một số snapshot.**

## Các service đã nhận dạng

| Service | Nguồn khai báo | Executable | Kết luận |
| --- | --- | --- | --- |
| `unet` | System init | `/system/bin/unet` | Có socket `ucl_net_ns`, `ucl_net_dm`, đối chiếu được `/proc/net/unix` |
| `uc_kglogd` | System init | `/system/bin/uc_kglogd` | Có socket `kglogdSocket`; `disabled` trong stanza, start/stop theo property |
| `uc_tcpd` | System init | `/system/bin/uc_tcpd` | Có socket `tcpdumpService`; có trigger theo property; **chưa xác nhận process đang chạy** |
| `uc_qmi_clnt` | `init.qcom.rc` | `/vendor/bin/uc_qmi_clnt` | `late_start`, user root, socket `uc_qmi_clnt_socket` |
| `uc_netlink` | `init.qcom.rc` | `/system/bin/uc_netlink` | `late_start`, user root; chưa kết luận kênh IPC cụ thể |
| `ril-daemon` | Vendor init | `/vendor/bin/hw/rild` | Chạy với các quyền/nhóm radio được firmware cấu hình |
| `uknet.ko` | Action `on boot` trong system init | `insmod system/lib/modules/uknet.ko` | Có cấu hình nạp; xem [phân tích module](../hardware/uknet-kernel-module.md) |

**Chú ý về thời gian:** `uc_kglogd` có stanza mặc định disabled và trigger property, nhưng cũng đã thấy process trong một snapshot. Không suy luận nó luôn tắt hoặc luôn bật.

## Property triggers nhạy cảm

- `persist.vendor.uc_kglogd.enable` điều khiển `uc_kglogd`.
- `persist.vendor.uc_tcpd.enable` điều khiển `uc_tcpd`.

Hai tên trên được lấy từ cấu hình, **không phải khuyến nghị thay đổi**. Không bật logger/tcpdump ngầm hoặc dùng `setprop` để dò tác dụng.

## Firmware mount và các đường dẫn OEM

`init.target.rc` khai báo chờ partition `modem`, mount VFAT tại `/firmware` với `ro`; cũng tạo cấu trúc thư mục `/mnt/system/productinfo/server/softsim/...`. Tên đường dẫn chứng minh cấu trúc OEM có định nghĩa, **không cho phép công khai nội dung SoftSIM, profile, seed, khóa hay metadata thiết bị**. Chi tiết quyền truy cập: [Mount & Permissions](firmware-mount-permissions.md).

`init.qcom.rc` có lệnh `chown/chmod` cho các sysfs Qualcomm DLOAD. Trong snapshot sau đó `/sys/kernel/dload` **không tồn tại**; vì vậy không gọi đây là giao diện có thể vận hành trên H01 hiện tại. Không tạo node hay thao tác dump qua thử-sai.

## Giới hạn kiểm kê

Có lúc chỉ dump các file `/system/etc/init/*.rc` và `/vendor/etc/init/*.rc` ở một cấp thư mục; thiếu `/init*.rc`, `/vendor/etc/init/hw/*.rc` hoặc RC import khác. Bước sau đã lấy `init.qcom.rc` và `init.target.rc`, sửa thiếu sót cho `uc_qmi_clnt` và `uc_netlink`. Vẫn **chưa có bản đồ toàn bộ init graph** được xác minh.

## Lệnh khảo sát không làm thay đổi hệ thống

```bat
adb shell getprop init.svc.uc_qmi_clnt
adb shell getprop init.svc.uc_netlink
adb shell getprop persist.vendor.uc_kglogd.enable
adb shell getprop persist.vendor.uc_tcpd.enable
adb shell ls /vendor/etc/init/hw
```

Không `start`, `stop`, `setprop`, `chmod`, `chcon`, `insmod`, `remount`, phát broadcast hoặc truy cập socket điều khiển.

**Liên quan:** [UCloudlink daemons](../network/ucloud-daemons-and-sockets.md), [UService](uservice-loader.md), [kernel uknet](../hardware/uknet-kernel-module.md).