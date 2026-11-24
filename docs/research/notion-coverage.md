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

## Bổ sung nghiên cứu Keyguard và Activity ẩn

| Nguồn Notion | Tài liệu |
| --- | --- |
| Android Keyguard + SystemUI VDEX + UCloud sleep (20/11) | [Keyguard bytecode](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| BackKeyManager NullPointerException (19/11) | [BackKeyManager case study](../system/backkeymanager-lock-crash.md) |
| LockSet UI/High contrast (19/11) | [LockSet UI history](../system/glocalme-lockscreen-ui-history.md) |
| Scanner 8 APK/7 ODEX/7 VDEX (19/11) | [Hidden Activity & flags](../system/hidden-activity-and-oem-flags.md) |

Các tệp chỉ biên soạn phát hiện đã lưu và giới hạn kiểm chứng; không kích hoạt thiết bị.

## Chuyển chi tiết các trang Notion 19–21/11 (đăng 24/11/2026)

| Trang nguồn đã đọc lại | Báo cáo chi tiết mới |
| --- | --- |
| Tự khởi động USB-C, phân tích ABOOT/LK/PMIC | [LK charger mode](../boot/lk-pmic-charger-analysis.md) |
| Cùng trang: thử eMMC v0.6 và 3 chức năng ngày 21/11 | [Cold boot PASS](../boot/auto-power-on-cold-boot-evidence.md) |
| SystemUI 4G slot 0, AutoShow v1.1 | [SystemUI slot0](../system/4g-slot0-systemui-evidence.md) |
| Launcher3 AutoHotspot v0.3.1–v0.4 | [API & logs](../projects/autohotspot-api-history.md) |
| SMS/TelephonyProvider và phân quyền ADB | [SMS evidence](../network/sms-telephony-permission-evidence.md) |
| Sao lưu boot/đề xuất máy thứ hai (chỉ lịch sử) | [Boot reuse limitations](../firmware/boot-image-reuse-limitations.md) |

Đây là bản tóm tắt bằng chứng đã thu, không phải ảnh thử mới hoặc yêu cầu có máy thứ hai.

## Trang Notion cập nhật 23–24/11: H01 máy B và Share Server

| Nguồn đã đọc trực tiếp | Báo cáo GitHub |
| --- | --- |
| “H01 MÁY MỚI #2”, mục 1–4,13–14 | [Đối chiếu A/B](h01-device-b-comparison-20261124.md) |
| Cùng trang, mục 5–7 | [Bootloader, EDL, Magisk B](../boot/device-b-unlock-root-evidence.md) |
| Cùng trang, mục 8–9 | [DPI, Launcher3, navigation, IME](../system/device-b-launcher-ime-evidence.md) |
| Cùng trang, mục 10 | [Xoay và module tích hợp](../system/device-b-rotation-evidence.md) |
| Nhật ký tổng, mục Share Server v0.1.4 | [Giao thức và kết quả thử](../projects/share-server-protocol-v014.md) |

Bằng chứng B tách khỏi A; phần danh sách tệp riêng ở Notion không được sao chép sang repo. Các tệp công khai là **bản biên soạn đã lọc**, không phải toàn văn hồ sơ.

## Bảng truy vết mới (24/11/2026)

Toàn bộ 207 đề mục đã được **gắn tuyến đến báo cáo liên quan** trong [bảng mapping 207 mục](notion-207-routing-map.md). Chưa đối chiếu đủ từng đoạn nội dung; không coi 207 link là 207 báo cáo hoàn chỉnh. Bổ sung [batch EDL](../firmware/edl-partition-backup-batches-20261110-11.md) và [kiểm chứng ZIP/GPT](../firmware/emmc-iphone-gpt-integrity-timeline.md).

## Nguồn ngoài nhật ký tổng (24/11/2026)

Đã tóm tắt báo cáo TXT trực tiếp trên Dropbox về [USB host/EDL](../firmware/edl-usb-host-endpoint-diagnostics-20261114.md) và [MMC/sysfs](../hardware/mmc-hosts-sysfs-dac-evidence-20261114.md); đồng thời chuyển các mục phần cứng/ADB/Fastboot lịch sử thành [PCB](../hardware/h01-board-pads-and-identification.md), [ADB](../system/adb-pre-root-baseline-and-limitations.md), [Fastboot](../boot/fastboot-device-info-gpt-audit.md). Xem [ranh giới nguồn](source-boundaries-and-coverage.md). Không công bố nguyên bản log và số định danh.

## Trang Notion H01 chuyên đề — lập bảng ngày 24/11

Đã lập [bảng 17 trang](notion-specialist-source-matrix.md), mỗi trang có đường tới ít nhất một báo cáo công khai liên quan. Bảng này **không** phải công bố toàn văn 16 trang hay tất cả đính kèm. Kết quả nguồn cần kiểm thêm theo tiêu chí ở trang bảng đối chiếu.

## Bổ sung chi tiết PIN và Recovery OTA — 24/11/2026

Đã chuyển [kết quả LockSet/High Contrast](../system/lockset-high-contrast-ui-validation.md), chỉ PASS hiển thị menu, **chưa PASS PIN**; và [dấu vết Recovery phiên bản cũ cùng các lớp tin cậy OTA](../firmware/ota-recovery-version-trace-and-trust-levels.md), không suy có bản cập nhật mới cho firmware hiện tại.

## Báo cáo Dropbox đã đối chiếu chi tiết — 24/11/2026

- [GPT 42/42 khớp với CSV trên GitHub](../firmware/gpt-dropbox-csv-direct-audit-20261124.md).
- [HAL/hostapd từ vendor init RC](../system/vendor-init-hals-hostapd-20261114.md).
- [FOTA 10/11 đã trả 2101 ở hai lần hỏi](../firmware/fota-nov10-runtime-no-update-evidence.md).

Đây là nội dung biên soạn từ các TXT đã kiểm, không tự tính là bằng chứng cập nhật mới hoặc tăng tỷ lệ 207 đề mục gốc đã hoàn tất.

## Đối chiếu cụ thể thêm các mục H173–H206 (24/11)

- [J2ME/KISS](../projects/j2me-kiss-launcher-source-tests.md) (H173–174), [Treble/ROM](../firmware/h01-treble-recovery-flags-and-rom-decision.md) (H175).
- [H01 Home](../projects/h01-home-versions-and-root-installer-evidence.md) (H176–177, H188–189), [bộ ảnh User Area](../firmware/user-area-reconstruction-overlap-and-gaps.md) (H178).
- [IME](../system/ime-nav-policy-window-evidence-v01-v03.md) (H192–197), [xoay thủ công/persistent](../system/rotation-v02-v031-regression-evidence.md) (H198–206).

Các tài liệu lưu lại diễn biến và phân loại bằng chứng, không đưa APK/IMG/JAR OEM hoặc nhật ký riêng lên repository.

## Đối chiếu FOTA metadata và các chuyên đề (24/11/2026)

- [FOTA file list từ Dropbox](../firmware/fota-filesystem-metadata-source-audit.md) — nguồn là TXT liệt kê, không phải bytecode dump mới.
- [Risk matrix của Activity/flags ẩn](../system/hidden-features-manifest-risk-matrix.md) — dựa trực tiếp Notion ngày 19/11, chưa chứng minh tất cả Activity mở được.
- [Control plane cập nhật UService v16](../system/uservice-update-control-plane-v16.md) — mode runtime chưa đo.

Chỉ là bổ sung phân tích và nguồn chứng cứ; bảng [207 đề mục](notion-207-routing-map.md) vẫn không được phép diễn giải thành 100% nội dung đã chuyển.

## Đối chiếu thêm nhật ký H179–H191 (24/11/2026)

- [Magisk compatibility 31.1/30.7](../boot/magisk-311-vs-307-boot-compatibility.md) tách root RAM và root sau ghi boot.
- [Root Control mksh hash alias v1.1](../boot/rootctl-mksh-hash-alias-regression.md) có mốc host reproduction và readback sau này.
- [Thanh điều hướng Android gốc](../system/native-navbar-debug-flags-and-persistence.md) có USER UI PASS và module persistence PASS nhưng không đồng nhất phép thử thao tác phím sau module.
- [FOTA/Feedback](../system/fota-feedback-disable-vs-uninstall-final-state.md) xác nhận **disable, chưa uninstall** theo quyết định cuối.

Tất cả được biên soạn từ các mục đã đọc trực tiếp trong trang tổng, không phát hành ảnh boot, Magisk module hoặc log nguyên bản.
