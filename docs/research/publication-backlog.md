# Kế hoạch công bố toàn bộ nghiên cứu H01

**23/11/2026:** Các mảng đã ghi tài liệu ≠ đã phát hành toàn bộ file/source/binary. Tiêu chí: tài liệu có nguồn và mức độ chứng cứ, không tiết lộ dữ liệu riêng.

| Nhánh | Mức hiện tại | Còn thiếu |
| --- | --- | --- |
| Hardware/GPT/eMMC | DOCUMENTED | Sơ đồ điện/UART chính xác |
| Bootloader/EDL/Magisk | DOCUMENTED | Quy trình recovery end-to-end |
| Auto Power-On v0.6 | DOCUMENTED, REPORTED PASS | Không pin, nhiều lần mất điện |
| Wi-Fi/AutoHotspot/4G AutoShow | DOCUMENTED, REPORTED PASS | Soak test và các biến thể |
| SIM/SMS | DOCUMENTED, PARTIAL | Nhận/gửi SMS, hai SIM vật lý |
| Firmware/OTA | DOCUMENTED | Full factory rescue |
| MMI/2846/Hidden Settings | DOCUMENTED | Feedback APK nội bộ, thử chức năng an toàn |
| SystemUI/Keyguard | DOCUMENTED, PARTIAL | Nhánh Swipe/PIN tạm dừng |
| Audio/Media | FAIL/PAUSED | Codec/output âm thanh |
| Rotation/IME/navigation | DOCUMENTED, PARTIAL | App compatibility, nguồn chập chờn |
| H01 Home / Share Server | REPORTED PASS | Phát hành source sau review license |
| H01 App Control | PROPOSED | Cấu trúc service dependency, rollback |
| Nokia logo boot | RESEARCH | Review video/bản vá trước khi chốt |
| Camera/NewPipe/YouTube | RESEARCH | Chưa có kết quả fix PASS để phát hành |
| Log, ảnh, TXT, ZIP, OEM APK/IMG | PRIVATE/NEEDS REVIEW | Ẩn danh, xét quyền phân phối |

**Quy tắc chuyển:** đọc đúng nguồn; phân biệt `OBSERVED`, `STATIC VERIFIED`, `REPORTED PASS`, `FAIL`, `PROPOSED`; lưu mốc ngày; tránh phát hành binary OEM và thông tin bảo mật. Sau mỗi lô, rà link nội bộ, thay đổi README/CHANGELOG và chạy `tools/check_public_content.py`.

**Bản đồ các trang đã đối chiếu:** [Notion coverage](notion-coverage.md).
## Đã biên soạn bổ sung — 23/11/2026

- [x] [FOTA ABUP chuyên sâu](../firmware/fota-abup-internals.md) — phân biệt Recovery OTA và EDL.
- [x] [UService loader](../system/uservice-loader.md) — sửa mốc raw/dequickened.
- [x] [UCloud daemon/network](../network/ucloud-daemons-and-sockets.md) — chưa quy port-to-PID chắc chắn.
- [x] [EDL/Firehose](../firmware/edl-firehose-diagnostics.md) — không công khai programmer OEM.
- [x] [Sao lưu eMMC](../firmware/emmc-backup-verification.md) — 42 phân vùng, 46 đối tượng.
- [x] [PPN1/2](../firmware/emmc-boot-areas.md) — zero-filled nhưng chưa xác minh physical Boot Area.
- [x] [OEM Unlock](../boot/oem-unlock-research.md) — kết quả trên máy thử, không phát hành patch.
- [ ] Kiểm kê mảng kernel/init/driver khác, đối chiếu tệp raw đã lọc.
- [ ] Trích công bố công cụ tự viết sau review license, bảo mật và tests.

## Kernel/init/RAM/boot chain — đợt đã biên soạn 23/11/2026

- [x] [uknet.ko](../hardware/uknet-kernel-module.md) — symbols/Netfilter/Generic Netlink, chưa thử load module.
- [x] [init system](../system/init-service-map.md) — daemon sockets, trigger và vùng còn thiếu.
- [x] [/firmware](../system/firmware-mount-permissions.md) — mount VFAT ro và DAC 0550.
- [x] [RAM/PSS](../system/ram-and-package-audit.md) — snapshot gốc, không khuyến nghị tắt hàng loạt.
- [x] [Boot verifier vs Fastboot](../boot/boot-verification-chain.md) — gọi đúng call graph đã được hiệu chỉnh.
- [x] [Magisk 30.7 timeline](../boot/magisk-root-timeline.md) — root RAM rồi root cố định.
- [x] [Recovery readiness](../boot/recovery-readiness.md) — checklist, không phải bộ restore hoàn chỉnh.
- [ ] Rà source tự viết của công cụ backup/recovery để phát hành riêng có unit tests và dry-run; không tải OEM binary.
- [ ] Bổ sung toàn bộ mapping init import và kiểm chứng Netlink peer nếu có log đọc thụ động được phép.

## Công cụ kiểm tra ZIP/IMG — 23/11/2026

- [x] Đã đăng [ZIP auditor](../../tools/audit_backup_archives.py), [tài liệu](../tools/backup-archive-audit.md) và 12 bài kiểm thử tổng hợp.
- [ ] Chưa chạy công cụ trên các ZIP nhiều GB trong kho riêng của H01; không ghi PASS thực địa khi chưa có kết quả.
- [ ] Chưa tạo đối chiếu tự động **42 partition name/LBA/size** với mỗi IMG; checksum khớp không tự chứng minh đúng phân vùng.

## Đối chiếu 42 phân vùng bằng metadata — 23/11/2026

- [x] [Công cụ kiểm kê partition](../../tools/audit_partition_inventory.py), [hướng dẫn](../tools/partition-inventory-audit.md) và unit tests tổng hợp.
- [ ] Chưa chạy trên bản sao H01 thực tế. Metadata/kích thước khớp **không** thay thế kiểm tra SHA-256/CRC, LBA hay phục hồi.

## Tiếp tục chuyển nội dung nghiên cứu — 23/11/2026

- [x] [Lịch sử truy vấn FOTA/ABUP](../firmware/fota-update-history.md), không đăng request credential.
- [x] [Truy vết firmware OEM và phản hồi hãng](../firmware/oem-firmware-sources-and-support.md), không đăng thread/IMEI.
- [x] [Dòng thời gian sao lưu eMMC](../firmware/emmc-acquisition-chronology.md) và phân biệt các mốc 42/46.
- [x] [Lịch sử J2ME/KISS/H01 Home](../projects/launcher-and-j2me-history.md) và [chính sách cài APK](../system/package-install-and-fota-feedback.md).
- [x] [Thử nghiệm IME](../system/ime-navigation-research-timeline.md) và [xoay/cảm biến](../system/rotation-and-sensors-timeline.md).
- [ ] Tiếp tục biên soạn các mục nguồn chưa có báo cáo chi tiết, không xuất nguyên văn log, bí mật backend hoặc firmware OEM.
- [ ] Không mở thêm nhánh phát triển công cụ trong lộ trình **chỉ công bố nghiên cứu**.

## Thêm kết quả nghiên cứu (23/11/2026)

- [x] [OTA v1–v9](../firmware/ota-discovery-history-v1-v9.md), [v10](../firmware/ota-delta-validation-v10.md), [v11](../firmware/ota-patch-file-map-v11.md).
- [x] [UService v12/v16](../system/uservice-update-channels-v12-v16.md), [network v13/v14](../network/ucloud-live-sockets-v13-v14.md).
- [x] [DTB âm thanh K1](../hardware/k1-audio-device-tree-confirmation.md), [Dual SIM/RIL/PCB](../network/dual-sim-ril-pcb-evidence.md).
- [ ] Tiếp tục rà các trang Notion và báo cáo H01 chưa có tài liệu độc lập; không công bố log/firmware OEM hoặc thông tin riêng.

## Nhánh Keyguard/Activity đã biên soạn (23/11/2026)

- [x] [Android Keyguard và UCloud sleep](../system/keyguard-framework-vdex-ucloud-sleep.md).
- [x] [BackKeyManager crash](../system/backkeymanager-lock-crash.md), [UI LockSet](../system/glocalme-lockscreen-ui-history.md).
- [x] [Danh mục Activity/flags OEM](../system/hidden-activity-and-oem-flags.md).
- [ ] Không có bằng chứng PIN/Swipe tự khóa PASS; giữ trạng thái PAUSED.
- [ ] Chưa thử thực tế mọi Activity/feature; manifest không đồng nghĩa có phần cứng.

## Đã công bố thêm ngày 24/11/2026 — chỉ nghiên cứu

- [x] [LK/PMIC](../boot/lk-pmic-charger-analysis.md) và [Auto Power-On v0.6 cold boot](../boot/auto-power-on-cold-boot-evidence.md).
- [x] [SystemUI 4G slot0](../system/4g-slot0-systemui-evidence.md), [AutoHotspot API history](../projects/autohotspot-api-history.md).
- [x] [SMS/Provider permission](../network/sms-telephony-permission-evidence.md), [giới hạn tái sử dụng boot](../firmware/boot-image-reuse-limitations.md).
- [ ] Vẫn còn các báo cáo TXT/ZIP/ảnh/video và các mục Notion chưa đối chiếu đủ; không tự tuyên bố hoàn thành 100%.
- [ ] Không thử H01 thứ hai, không tạo tool/app trong nhiệm vụ chỉ xuất bản nghiên cứu.

## Mục Notion bổ sung ngày 24/11 — đã đưa lên GitHub

- [x] [Đối chiếu A/B](h01-device-b-comparison-20261124.md), không công bố serial/HWID/PK_HASH.
- [x] [EDL/unlock/root B](../boot/device-b-unlock-root-evidence.md), ghi mốc PASS nhưng không xuất script ghi DEVINFO/boot.
- [x] [Launcher/IME B](../system/device-b-launcher-ime-evidence.md) và [xoay B](../system/device-b-rotation-evidence.md): giữ phân biệt snapshot cũ và boot persistent.
- [x] [Share Server v0.1.4 chi tiết](../projects/share-server-protocol-v014.md): PASS H01/iPhone ở máy đã thử, test hash 9 MiB chỉ ở fixture.
- [ ] Nội dung các hồ sơ khác, TXT/ZIP/ảnh/video còn phải kiểm kê và lọc dữ liệu. Không coi có mục lục 207 tiêu đề là đã xuất bản toàn bộ.

**Điều chỉnh mốc thời gian:** dòng “không thử H01 thứ hai” trong kế hoạch ngày 24/11 là giới hạn **không thực hiện thử mới trong nhiệm vụ công bố**. Nó không phủ định nhật ký Notion 23–24/11 ghi các phép thử đã xảy ra trên máy B; đã biên soạn và [ẩn định danh ở đây](h01-device-b-comparison-20261124.md).

## Tiến độ kiểm kê 207 mục (24/11/2026)

- [x] [Bảng liên kết 207 đề mục đến báo cáo theo chủ đề](notion-207-routing-map.md) — **không phải hoàn tất nội dung 207/207**.
- [x] [Kết quả đọc batch eMMC](../firmware/edl-partition-backup-batches-20261110-11.md), [đối chiếu ZIP/IMG/GPT trên iPhone](../firmware/emmc-iphone-gpt-integrity-timeline.md).
- [ ] Chưa kiểm soát nội dung chi tiết từng đoạn của toàn bộ 207 mục và mọi file log/ảnh/video; chỉ công bố bản biên soạn đã lược dữ liệu riêng.

## Mốc kiểm chứng bổ sung (24/11/2026)

- [x] [PCB/pad](../hardware/h01-board-pads-and-identification.md), [ADB trước root](../system/adb-pre-root-baseline-and-limitations.md), [Fastboot/GPT](../boot/fastboot-device-info-gpt-audit.md).
- [x] [USB 9008/PyUSB](../firmware/edl-usb-host-endpoint-diagnostics-20261114.md) và [MMC/sysfs](../hardware/mmc-hosts-sysfs-dac-evidence-20261114.md) được rút từ các báo cáo TXT có thật trên Dropbox.
- [x] [Ranh giới các nguồn đã kiểm kê](source-boundaries-and-coverage.md).
- [ ] Chưa duyệt từng nguồn log/ZIP/video còn lại để xác định phần nào có thể công bố thêm; không được đăng firmware OEM, dữ liệu SIM hay định danh.

## Rà các chuyên đề Notion (24/11/2026)

- [x] [Bảng tra 17 trang H01](notion-specialist-source-matrix.md) và [207 mục tổng](notion-207-routing-map.md).
- [x] [OTA server cache v15](../firmware/ota-server-cache-v15-evidence.md), [audio test matrix](../system/audio-playback-test-matrix-20261121.md), [ẩn tính năng scanner](../system/hidden-scanner-parser-failure-and-recovery.md), [Log Tools 2846](../system/assistant-2846-log-tools-safety-evidence.md).
- [x] [FOTA VDEX](../firmware/fota-vdex010-dequickening-evidence.md), [UService VDEX](../system/uservice-vdex010-recovery-progression.md), [UCloudlink ELF](../network/ucloudlink-elf-library-symbol-inventory.md).
- [ ] Phải kiểm đầy đủ chứng cứ từng mục/đính kèm, không báo 100% nội dung từ bảng liên kết.
