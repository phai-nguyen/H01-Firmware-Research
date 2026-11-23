# Bảng trạng thái nghiên cứu — mốc 23/11/2026

| Chủ đề | Trạng thái | Ghi chú |
| --- | --- | --- |
| Android 8.1 / MSM8909 | OBSERVED | Thuộc tính và snapshot từ máy thử |
| GPT / eMMC | OBSERVED | Có báo cáo 42 phân vùng; đã công bố bảng 42 mục loại bỏ GUID riêng của thiết bị |
| Bootloader unlock + Magisk root | REPORTED PASS | Ghi chép thử nghiệm 18/11; không bảo đảm trên máy khác |
| OTA incremental 81→87 | REPORTED VERIFIED | Có báo cáo kiểm tra chữ ký và block; chưa có factory ROM đầy đủ |
| Dual SIM firmware DSDS | OBSERVED | Chưa xác minh hai SIM vật lý hoạt động đồng thời |
| Launcher3 AutoHotspot v0.4 | REPORTED PASS | Sau reboot; chưa có kiểm tra tải lâu dài |
| AudioTrack / ALSA output | FAIL / PAUSED | Không phát AAC; nhánh sửa audio tạm dừng |
| Ứng dụng Hidden Settings | PARTIAL | Đã có mã/build; một số màn hình OEM có lỗi/giới hạn |
| Assistant Function / Log Tools | STATIC ROUTES VERIFIED | Đã đối chiếu 3 Intent và guard PackageUtil; Feedback APK chưa có để phân tích; không cần máy H01 thứ hai |
| Mã 2846 / MMI menu OEM | STATIC + RUNTIME VERIFIED | About → Assistant → MMI đã xác minh qua ADB; receiver 2846 khôi phục từ MMI VDEX; phương thức xử lý được phân tích ngoại tuyến |
| Điều chỉnh DPI | PARTIAL | Có mã công cụ; kiểm thử hoàn tác thực tế cần thận trọng |
| Logo boot Nokia C3-00 | RESEARCH | Chưa phát hành patch boot/splash đã xác minh |
| H01 App Control | PROPOSED | Kiến trúc quản lý tiến trình/ứng dụng cần nghiên cứu thêm |
| Bộ firmware phục hồi đầy đủ | OPEN | Chưa có bản phục hồi đầu-cuối công khai được xác nhận |

**Định nghĩa:** `OBSERVED` = dữ liệu đo/ghi nhận; `REPORTED PASS` = người thử báo thành công; `REPORTED VERIFIED` = kết quả đối chiếu theo báo cáo nguồn; `PARTIAL` = một phần hoàn thành; `FAIL` = phát hiện lỗi; `PAUSED` = tạm dừng; `RESEARCH`/`PROPOSED`/`OPEN` = chưa hoàn tất.

## Ưu tiên tiếp theo (không ghi flash)

1. Đối chiếu bảng GPT v0.2.0 với các biến thể H01 khác, chỉ đọc.
2. Bổ sung bảng phiên bản OTA đã nghiên cứu, không xuất gói OTA gốc.
3. Chạy thử bộ script ADB chỉ đọc Windows 7 và Linux trên H01, rà soát thủ công báo cáo trước khi gửi.
4. Chia nhỏ Issues dựa trên các mục `OPEN`/`PARTIAL`; không tự động khôi phục nhánh `PAUSED`.

## Mốc tài liệu được bổ sung — 23/11/2026

| Chủ đề | Trạng thái | Trang |
| --- | --- | --- |
| Auto Power-On USB-C v0.6 | REPORTED PASS | [Boot](../boot/auto-power-on-usb.md) |
| Hiển thị icon 4G v1.1 | REPORTED PASS | [SystemUI](../system/4g-status-icon.md) |
| Keyguard / khóa OEM | STATIC VERIFIED, PIN/Swipe PAUSED | [Keyguard](../system/keyguard-and-lockscreen.md) |
| SMS | SERVICE OBSERVED, SEND/RECEIVE OPEN | [SMS](../network/sms.md) |
| Hidden feature inventory | 473 COMPONENTS STATIC | [Inventory](../system/hidden-feature-inventory.md) |
| Rotate v0.3.1 | REPORTED PASS AFTER REBOOT | [Display](../system/display-rotation-navigation.md) |
| Share Server v0.1.4 | REPORTED PASS | [Share Server](../projects/share-server.md) |
| H01 Home installer v0.4 | REPORTED PASS | [Installer](../projects/h01-home-installer.md) |

Xem [bản đồ nguồn](notion-coverage.md) và [backlog công bố](publication-backlog.md).

## Chuyên đề bổ sung: FOTA/UService, EDL và eMMC (23/11/2026)

| Phân hệ | Trạng thái | Tài liệu |
| --- | --- | --- |
| FOTA/ABUP | STATIC VERIFIED; Recovery install path | [FOTA](../firmware/fota-abup-internals.md) |
| UService/Loader | STATIC VERIFIED; DEX dequickened theo báo cáo | [UService](../system/uservice-loader.md) |
| UCloud daemon/socket | SNAPSHOT OBSERVED; port-to-process PARTIAL | [Daemons](../network/ucloud-daemons-and-sockets.md) |
| Firehose | READ / GPT / NOP VERIFIED in source logs | [EDL](../firmware/edl-firehose-diagnostics.md) |
| eMMC backups | 42/42 partition IMG; 46/46 objects integrity match (latest) | [Verification](../firmware/emmc-backup-verification.md) |
| PPN1/PPN2 | Zero-filled READ; physical Boot Area NOT CONFIRMED | [Boot areas](../firmware/emmc-boot-areas.md) |
| Bootloader OEM | REPORTED PASS 18/11; không lặp unlock | [Unlock research](../boot/oem-unlock-research.md) |

## Kernel / init / RAM và điều kiện cứu hộ — 23/11/2026

| Nhánh | Phân loại | Tài liệu |
| --- | --- | --- |
| uknet.ko | BINARY STATIC; SYSFS OBSERVED, daemon peer chưa xác nhận | [Kernel module](../hardware/uknet-kernel-module.md) |
| Init Qualcomm/UCloudlink | RC STATIC VERIFIED + PROCESS SNAPSHOTS | [Init map](../system/init-service-map.md) |
| /firmware | MOUNT VERIFIED, ADB DAC BLOCKED | [Permissions](../system/firmware-mount-permissions.md) |
| RAM | SNAPSHOT OBSERVED, không chứng minh thiếu RAM | [RAM audit](../system/ram-and-package-audit.md) |
| LK/ABOOT | STATIC CALL GRAPH, QSEE runtime chưa kiểm chứng | [Boot verifier](../boot/boot-verification-chain.md) |
| Magisk 30.7 | REPORTED PASS boot RAM & root cố định | [Timeline](../boot/magisk-root-timeline.md) |
| Phục hồi H01 | READINESS checklist, full restore CHƯA PASS | [Recovery readiness](../boot/recovery-readiness.md) |
