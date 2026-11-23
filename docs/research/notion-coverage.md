# Bản đồ nguồn Notion → tài liệu GitHub

**Kiểm kê 23/11/2026.** Đã xác định 15 trang trong nhánh Notion H01 và trang tổng rất dài. Các đường dẫn GitHub dưới đây là **bản biên soạn đã lọc**, không phải bản sao toàn văn Notion.

| Trang Notion theo chủ đề | Tài liệu GitHub |
| --- | --- |
| Nghiên cứu firmware K1 / MSM8909 (trang tổng) | [Hardware](../hardware/overview.md), [Firmware](../firmware/overview.md), [Backup](../firmware/backup-and-reconstruction.md), [Rotation](../system/display-rotation-navigation.md), [Share Server](../projects/share-server.md) |
| Auto Power-On / LK / kernel | [Auto Power-On](../boot/auto-power-on-usb.md) |
| SystemUI 4G SIM1 | [4G AutoShow](../system/4g-status-icon.md) |
| Launcher3 AutoHotspot | [AutoHotspot](../projects/autohotspot.md) |
| Sao lưu boot / tái tạo cấu hình | [Backup](../firmware/backup-and-reconstruction.md) |
| APK/ODEX/VDEX và chức năng ẩn | [Hidden Inventory](../system/hidden-feature-inventory.md) |
| Mã 2846/Assistant Function | [2846](../system/glocalmehome-about-secret-code-2846.md), [MMI](../system/mmi-secret-code-receiver.md) |
| SMS | [SMS](../network/sms.md) |
| Dual SIM / PCB | [DSDS](../network/dual-sim.md) |
| AudioTrack / ALSA | [Audio](../system/audio.md) |
| PIN / tương phản cao | [Keyguard](../system/keyguard-and-lockscreen.md) |
| SystemUI Keyguard | [Keyguard](../system/keyguard-and-lockscreen.md) |
| Framework config_disableLockscreenByDefault | [Keyguard](../system/keyguard-and-lockscreen.md) |
| BackKeyManager NPE | [Keyguard](../system/keyguard-and-lockscreen.md) |
| UCloud Keyguard / sleep | [Keyguard](../system/keyguard-and-lockscreen.md) |

**Các nguồn chưa phát hành:** IMG OEM, APK/ODEX/VDEX/ELF, SoftSIM và NV, log có số thuê bao/định danh, ảnh/video có thông tin người dùng, bản vá flash, full dump. Không đưa URL Dropbox riêng hoặc token. Xem [Backlog](publication-backlog.md) và [Publication Policy](../security/publication-policy.md).

**Giới hạn:** vẫn có các kết quả trong trang Notion tổng và kho tệp chưa trích biên soạn; không tuyên bố đã chuyển hết.
## Mục lục đầy đủ của trang tổng

Đã ghi riêng [207 tiêu đề cấp 2 của nhật ký Notion tổng](notion-master-index.md) theo thứ tự nguồn. Đây chỉ là kiểm kê để tránh bỏ sót, **không có nghĩa toàn bộ 207 mục đã được biên soạn thành báo cáo độc lập**.

## Bổ sung nghiên cứu từ nhật ký Notion tổng (23/11/2026)

| Các mốc nội bộ nguồn | Tài liệu mới |
| --- | --- |
| 4, 14: FOTA/ABUP, VDEX | [FOTA](../firmware/fota-abup-internals.md) |
| 5, 6, 14: UService/native/DEX loader | [UService](../system/uservice-loader.md) |
| 7, 15, 19, 22: Daemon/socket/init | [Network](../network/ucloud-daemons-and-sockets.md) |
| 32, 115–123, 132: EDL, Firehose | [EDL](../firmware/edl-firehose-diagnostics.md) |
| 95, 98: 42/42 và 46/46 IMG | [Backup](../firmware/emmc-backup-verification.md) |
| 132, 137, 138: PPN1/PPN2 | [Boot areas](../firmware/emmc-boot-areas.md) |
| 99–113 và mốc 60 ngày 18/11: unlock | [OEM Unlock](../boot/oem-unlock-research.md) |

Các số mục là **số trong trang nguồn**, có thể trùng nhau do nhiều giai đoạn cập nhật; không dùng chúng làm ID tệp.

## Chủ đề mới từ trang Notion tổng

| Mục/hồ sơ trong Notion | Báo cáo đã biên soạn |
| --- | --- |
| 19–24: init RC, qcom init, uknet.ko | [Module](../hardware/uknet-kernel-module.md), [Init](../system/init-service-map.md), [Mount](../system/firmware-mount-permissions.md) |
| Đổi phạm vi và kết quả đo RAM thật | [RAM/PSS](../system/ram-and-package-audit.md) |
| Mục 100, 104–109: ABOOT, Verified Boot, QSEE | [Boot chain](../boot/boot-verification-chain.md) |
| Boot RAM marker, Magisk 30.7, root cố định | [Magisk](../boot/magisk-root-timeline.md) |
| 42 GPT, eMMC, EDL, boot và sao lưu | [Recovery readiness](../boot/recovery-readiness.md) |

Đây là các bản **tổng hợp kỹ thuật**, không phải dump nguyên văn Notion hoặc binary gốc.

## Lịch sử chi tiết đã chuyển vào GitHub — 23/11/2026

| Chủ đề Notion | Bản công bố |
| --- | --- |
| 25–27: hai lần kiểm tra OTA 20–21/10 và hai lần 10/11 | [FOTA timeline](../firmware/fota-update-history.md) |
| 26–31: H01/ZEUS, tìm firmware và phản hồi OEM | [Firmware sources](../firmware/oem-firmware-sources-and-support.md) |
| 32–98, 114–138: các bước sao lưu eMMC, GPT và Boot Areas | [eMMC history](../firmware/emmc-acquisition-chronology.md) |
| J2ME Loader, KISS Launcher, H01 Home v0.1–v0.4 | [Apps](../projects/launcher-and-j2me-history.md) |
| Cài APK qua InstallService, FOTA/Feedback disabled-user | [Package policy](../system/package-install-and-fota-feedback.md) |
| Thanh phím/IME: thử v0.1/v0.2/v0.3 | [IME/navigation](../system/ime-navigation-research-timeline.md) |
| Khóa xoay và cảm biến: v0.1–v0.3.1 | [Rotation](../system/rotation-and-sensors-timeline.md) |

Bảng ghi **bản tóm tắt kỹ thuật đã lọc**, không phải chuyển toàn văn log/ảnh/nhật ký riêng. Các mục Notion khác còn cần đọc và chuyển tiếp.

## Chuyên đề chi tiết đọc từ Notion 20–22/11

| Nguồn Notion | Tài liệu đã đưa GitHub |
| --- | --- |
| OTA v1–v9 | [Lịch sử nhận gói](../firmware/ota-discovery-history-v1-v9.md) |
| OTA v8–v10 | [Chữ ký và khối đích](../firmware/ota-delta-validation-v10.md) |
| OTA v11 | [Ánh xạ vùng vá → tệp](../firmware/ota-patch-file-map-v11.md) |
| OTA/UService v12, v16 | [Ba cơ chế cập nhật](../system/uservice-update-channels-v12-v16.md) |
| OTA/Network v13–v14 | [Socket runtime](../network/ucloud-live-sockets-v13-v14.md) |
| Audio 21/11: DTB/runtime | [Device Tree K1](../hardware/k1-audio-device-tree-confirmation.md) |
| Dual SIM 20/11: init/getprop/PCB | [DSDS chi tiết](../network/dual-sim-ril-pcb-evidence.md) |

Mỗi tài liệu ghi rõ phạm vi kiểm chứng; không đồng nghĩa nội dung nhị phân hoặc tất cả 207 đề mục đã được chuyển.
