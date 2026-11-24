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

## Bằng chứng từ tài liệu chuyên đề Notion (đã đưa lên GitHub 23/11)

| Nhánh | Trạng thái | Chi tiết |
| --- | --- | --- |
| OTA delta 81→87 | CMS/Recovery KEY MATCH; system/vendor TARGET BLOCK PASS, server SHA-256 UNRESOLVED | [V10](../firmware/ota-delta-validation-v10.md) |
| OTA ext4 mapping | STATIC; các tệp có vùng bsdiff/new giao nhau | [V11](../firmware/ota-patch-file-map-v11.md) |
| UService update channels | STATIC; runtime mode UNKNOWN | [UService](../system/uservice-update-channels-v12-v16.md) |
| Network PID | RUNTIME, 3 snapshot v14; WAN reachability UNKNOWN | [Network](../network/ucloud-live-sockets-v13-v14.md) |
| Audio K1 | RUNTIME DTB disabled; AUDIO FIX NOT PASS | [Audio](../hardware/k1-audio-device-tree-confirmation.md) |
| Dual SIM | DSDS/RIL2 RUNTIME; second physical SIM NOT PASS | [DSDS](../network/dual-sim-ril-pcb-evidence.md) |

## Mốc SystemUI/GlocalmeHome (23/11/2026)

| Nhánh | Trạng thái | Chi tiết |
| --- | --- | --- |
| Android Keyguard | Framework flag + VDEX stub STATIC VERIFIED; runtime lock OPEN | [Keyguard](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| UCloud sleep | Model K1 branch STATIC, quick vtable 51 UNKNOWN | [Sleep](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| BackKeyManager | NPE trace VERIFIED; missing setup cause HYPOTHESIS | [Crash](../system/backkeymanager-lock-crash.md) |
| LockSet | Activity/UI/high contrast PASS; PIN NEVER TESTED | [UI](../system/glocalme-lockscreen-ui-history.md) |
| Activity/flags | 473 components STATIC; most runtime UNKNOWN | [Inventory](../system/hidden-activity-and-oem-flags.md) |

## Chi tiết bổ sung từ nguồn 19–21/11 (đăng 24/11/2026)

| Nhánh | Trạng thái | Báo cáo |
| --- | --- | --- |
| LK/PMIC Charger Mode | STATIC VERIFIED, thanh ghi thời điểm cấp nguồn NOT OBSERVED | [LK](../boot/lk-pmic-charger-analysis.md) |
| Auto Power-On v0.6 | REPORTED PASS trên eMMC/cấp USB-C lạnh một H01; không pin NOT TESTED | [v0.6](../boot/auto-power-on-cold-boot-evidence.md) |
| SystemUI 4G AutoShow | One-shot v1.1 REPORTED PASS; nguyên nhân cờ reset OPEN | [SIM1](../system/4g-slot0-systemui-evidence.md) |
| AutoHotspot | v0.3.4 manual PASS; v0.4 after boot REPORTED PASS | [API](../projects/autohotspot-api-history.md) |
| SMS | ISms/Provider OBSERVED, receive/send UNVERIFIED | [SMS](../network/sms-telephony-permission-evidence.md) |
| Clone H01 | Historical proposal only; no second device | [Limitations](../firmware/boot-image-reuse-limitations.md) |

## Mốc nguồn 23–24/11/2026 mới biên soạn

| Nhánh | Trạng thái nguồn | Báo cáo |
| --- | --- | --- |
| H01 máy B EDL/GPT | OBSERVED 42 partition + backup riêng | [A/B](h01-device-b-comparison-20261124.md) |
| H01 máy B unlock + Magisk | REPORTED PASS trước/sau reboot, root cố định | [Boot/root](../boot/device-b-unlock-root-evidence.md) |
| Launcher3 / IME trên B | REPORTED PASS; IME input và persistence là hai snapshot khác nhau | [IME](../system/device-b-launcher-ime-evidence.md) |
| Xoay trên B | REPORTED PASS; dọc 0 sau một boot, chưa xác nhận giữ qua boot tiếp theo | [Xoay](../system/device-b-rotation-evidence.md) |
| Share Server v0.1.4 | REPORTED PASS tải/gửi trên H01 thử trước; chưa chứng minh truyền trên B | [Protocol](../projects/share-server-protocol-v014.md) |

## Rà nguồn lại ngày 24/11/2026

| Nhánh | Kết luận lưu trữ | Chi tiết |
| --- | --- | --- |
| LockSet PIN | Menu/UI và tương phản PASS; tạo PIN/sleep/reboot chưa thử | [High Contrast](../system/lockset-high-contrast-ui-validation.md) |
| OTA Recovery | Recovery còn version cũ; có incremental 81→87, không cài, không có new update được xác nhận cho build hiện tại | [Recovery trace](../firmware/ota-recovery-version-trace-and-trust-levels.md) |
| Cache server v15 | Host fixture PASS, không có kết quả thực trên H01 | [v15](../firmware/ota-server-cache-v15-evidence.md) |

## Các kết quả kỹ thuật vừa đối chiếu sâu — 24/11/2026

| Nhánh | Mức bằng chứng | Báo cáo |
| --- | --- | --- |
| eMMC User Area reconstruction | 42 ảnh ứng viên size match, **158.953.472 byte gap còn thiếu** ở mốc 18/11; NO FULL IMAGE | [Coverage](../firmware/user-area-reconstruction-overlap-and-gaps.md) |
| J2ME/KISS | INSTALL/LAUNCHER UI REPORTED PASS; JAR/game not tested | [Tests](../projects/j2me-kiss-launcher-source-tests.md) |
| Treble GSI | Recovery prop `ro.treble.enabled=true` OBSERVED; no compatible GSI PASS | [Analysis](../firmware/h01-treble-recovery-flags-and-rom-decision.md) |
| H01 Home v0.4 | Root denied first; app install trial REPORTED PASS after grant | [Home](../projects/h01-home-versions-and-root-installer-evidence.md) |
| IME navigation | IME open/HIDDEN v0.2 real; module persistent v0.3 after reboot; notification OPEN | [IME](../system/ime-nav-policy-window-evidence-v01-v03.md) |
| Orientation | v0.2 preflight JNI FAIL; v0.2.1 rotation PASS; v0.3.1 reboot/persistent PASS | [Rotation](../system/rotation-v02-v031-regression-evidence.md) |

## Bằng chứng công bố bổ sung — 24/11/2026

| Phần | Phạm vi đã xác nhận từ nguồn | Giới hạn |
| --- | --- | --- |
| FOTA files | APK/ODEX/VDEX sizes MATCH giữa Dropbox TXT và Notion | Tên file/mtime không xác minh build, không tính lại binary hash |
| Hidden Activity | Manifest/DEX và cờ OEM có mặt trong các mẫu phân tích | Chưa chạy tất cả Activity, không xác nhận tính năng phần cứng |
| UService updates | Ba đường FOTA/APK/binary trong code v16 | Mode hiệu lực, lịch và hot-update runtime chưa được đo |

Xem [FOTA metadata](../firmware/fota-filesystem-metadata-source-audit.md), [Hidden Matrix](../system/hidden-features-manifest-risk-matrix.md), [UService v16](../system/uservice-update-control-plane-v16.md).

## Mốc bổ sung — Magisk/Root Control/Navbar/FOTA (24/11/2026)

| Nhánh | Bằng chứng | Tài liệu |
| --- | --- | --- |
| Magisk 31.1 vs 30.7 | 31.1 unpack FAIL; 30.7 root RAM REPORTED PASS, bản sau đã root cố định | [Compatibility](../boot/magisk-311-vs-307-boot-compatibility.md) |
| Rootctl v1.1 | `hash` alias lỗi ở mksh; host 12/12 PASS; device readback v1.1 PASS | [Rootctl](../boot/rootctl-mksh-hash-alias-regression.md) |
| Navbar | Phím Back/Home/Recents dùng thử PASS, sau boot mới module=enabled/NavigationBar VISIBLE | [Navbar](../system/native-navbar-debug-flags-and-persistence.md) |
| FOTA/Feedback | Installed=true, enabled=3 user0; chủ thiết bị quyết định **không uninstall** | [Package scope](../system/fota-feedback-disable-vs-uninstall-final-state.md) |
