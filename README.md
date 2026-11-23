# ZEUS H01 Open Firmware Research

**Dự án nghiên cứu mở, độc lập** về ZEUS H01 / GlocalMe K1: phần cứng, Android 8.1, firmware, bootloader, EDL, OTA, modem/SIM, các chức năng ẩn và ứng dụng tùy biến.

> **Trạng thái: v0.2.0 — tài liệu GPT đã lược bỏ định danh và công cụ kiểm tra chỉ đọc.** Tài liệu được biên soạn lại từ ghi chép và báo cáo kiểm thử của dự án. Không phải firmware chính thức, không phải ROM phục hồi sẵn dùng, cũng không bảo đảm mọi kết quả áp dụng cho mọi biến thể H01.

English: [README.en.md](README.en.md)

## Bắt đầu

- [Tổng quan phần cứng](docs/hardware/overview.md)
- [Bảng GPT 42 phân vùng đã lược bỏ định danh](docs/firmware/gpt-layout.md)
- [Đối chiếu APK GlocalmeHome và cơ chế 2846 giữa các mẫu](docs/firmware/2846-apk-comparison.md)
- [Thu thập báo cáo ADB chỉ đọc (Windows 7 / antiX)](docs/tools/read-only-report.md)
- [Xác minh bản sao SHA-256 ngoại tuyến](docs/tools/backup-hashes.md)
- [Bản đồ nghiên cứu firmware / phân vùng](docs/firmware/overview.md)
- [OTA tăng dần, bản 81 → 87](docs/firmware/ota.md)
- [Bootloader, Fastboot, EDL và root](docs/boot/root-and-recovery.md)
- [Hai kênh SIM logic / DSDS](docs/network/dual-sim.md)
- [Đường âm thanh chưa hoạt động](docs/system/audio.md)
- [Mã 2846: menu kỹ thuật ẩn trong About của GlocalmeHome](docs/system/glocalmehome-about-secret-code-2846.md)
- [Assistant Function: định tuyến MMI / Log Tools / System Settings](docs/system/assistant-function-routing.md)
- [Phân tích VDEX010: MMI SecretCodeReceiver.onReceive và mã 2846](docs/system/mmi-secret-code-receiver.md)
- [Danh mục 30 bài kiểm tra MMI](docs/system/mmi-factory-tests.md)
- [Hướng dẫn ADB thủ công quan sát menu 2846 trên Windows 7](docs/tools/secret-2846-readonly.md)
- [Launcher3 AutoHotspot v0.4](docs/projects/autohotspot.md)
- [Các repository ứng dụng liên quan](docs/projects/index.md)
- [Bảng trạng thái và đầu việc](docs/research/status.md)
- [Nguồn gốc và độ tin cậy](docs/research/provenance.md)
- [Quy định an toàn khi công khai](docs/security/publication-policy.md)

## Mở rộng kho nghiên cứu H01 — 23/11/2026

- **Khởi động/firmware:** [Auto Power-On USB-C v0.6](docs/boot/auto-power-on-usb.md), [sao lưu và ghép firmware](docs/firmware/backup-and-reconstruction.md).
- **Mạng:** [khôi phục biểu tượng 4G v1.1](docs/system/4g-status-icon.md), [SMS](docs/network/sms.md), [Dual SIM](docs/network/dual-sim.md).
- **Giao diện/hệ thống:** [Keyguard và khóa OEM](docs/system/keyguard-and-lockscreen.md), [chức năng ẩn (473 component)](docs/system/hidden-feature-inventory.md), [xoay/IME/navigation](docs/system/display-rotation-navigation.md).
- **Ứng dụng:** [Share Server v0.1.4](docs/projects/share-server.md), [H01 Home installer](docs/projects/h01-home-installer.md), [App Control](docs/projects/app-control.md).
- **Tiến độ chuyển tài liệu:** [15 trang Notion đã đối chiếu](docs/research/notion-coverage.md), [mục lục đầy đủ 207 đề mục trong trang Notion tổng](docs/research/notion-master-index.md) và [backlog phần còn thiếu](docs/research/publication-backlog.md).

**Phạm vi:** chỉ công bố tài liệu và công cụ có quyền phân phối, không đăng bản dump firmware OEM hoặc dữ liệu riêng. Các mốc PASS chỉ áp dụng cho phép thử đã ghi chép.

## Phân tích firmware chuyên sâu — đợt bổ sung 23/11/2026

- [FOTA/ABUP APK và đường cập nhật Recovery](docs/firmware/fota-abup-internals.md)
- [UService: nạp DEX, thư viện native, BinaryUpdateHelper](docs/system/uservice-loader.md)
- [UCloudlink daemon, MQTT và socket runtime](docs/network/ucloud-daemons-and-sockets.md)
- [EDL 9008, Sahara, Firehose: bằng chứng READ và ranh giới an toàn](docs/firmware/edl-firehose-diagnostics.md)
- [Sao lưu 42 phân vùng GPT: phân biệt 42/42 và 46/46 IMG](docs/firmware/emmc-backup-verification.md)
- [eMMC Boot1/Boot2: hai bản đọc toàn 0x00, chưa xác nhận Boot Area trống](docs/firmware/emmc-boot-areas.md)
- [Diễn biến nghiên cứu OEM Unlock và bằng chứng sau reboot](docs/boot/oem-unlock-research.md)

**Không** đăng trình nạp Firehose, APK/VDEX, ảnh DEVINFO hoặc dữ liệu SIM trong đợt công bố.

## Kernel, init, RAM và cứu hộ — 23/11/2026

- [Module uknet.ko: Netfilter và Generic Netlink](docs/hardware/uknet-kernel-module.md)
- [Bản đồ init service Qualcomm/UCloudlink](docs/system/init-service-map.md)
- [Lý do ADB không liệt kê được /firmware](docs/system/firmware-mount-permissions.md)
- [Đánh giá RAM/PSS thực tế, không tắt dịch vụ hàng loạt](docs/system/ram-and-package-audit.md)
- [ABOOT: Verified Boot khác cổng Fastboot flash](docs/boot/boot-verification-chain.md)
- [Magisk 30.7: boot RAM và root cố định](docs/boot/magisk-root-timeline.md)
- [Danh sách điều kiện cần có trước khi cứu hộ firmware](docs/boot/recovery-readiness.md)

## Công cụ kiểm chứng ZIP sao lưu — 23/11/2026

- [Chương trình kiểm tra ZIP/IMG ngoại tuyến](tools/audit_backup_archives.py): đọc hết ZIP member để xác minh CRC, kiểm tra sidecar SHA-256, không giải nén/ghi thiết bị.
- [Hướng dẫn và giới hạn bằng chứng](docs/tools/backup-archive-audit.md): phân biệt MATCH, REVIEW, MISMATCH và ERROR.
- [12 unit tests tổng hợp](tests/test_backup_archive_audit.py): không cần APK, IMG hay ZIP OEM.

## Phần cứng / firmware khảo sát

| Mục | Ghi nhận |
| --- | --- |
| Thiết bị | ZEUS H01, nền tảng được báo cáo là GlocalMe K1 |
| SoC | Qualcomm MSM8909, ARMv7 |
| Android | 8.1.0 / API 27 |
| eMMC | Hạng dung lượng 8 GB (đối chiếu GPT khi cần) |
| RAM | xấp xỉ 929 MB khả dụng theo `/proc/meminfo` ở snapshot nghiên cứu |
| Build OTA đích đã phân tích | `K1_TSV3.1.005.001.240116_20240116-1930` |

Những giá trị trên là **snapshot từ một thiết bị/nhóm bản sao nghiên cứu**, không khẳng định mọi máy H01 đều dùng cùng phân vùng và firmware.

## Các phát hiện tiêu biểu

- **Bootloader / root:** nhật ký nghiên cứu 18/11/2026 ghi nhận bootloader ở trạng thái unlocked và `uid=0` qua Magisk trên máy thử; **không** khẳng định phương pháp tương thích với mọi thiết bị.
- **OTA:** ghi chép 22/11/2026 báo cáo đã lấy và kiểm tra gói cập nhật **block-based incremental 81 → 87**, dung lượng **44.118.207 byte**; **không phải** ROM đầy đủ để khôi phục toàn bộ eMMC.
- **SIM:** quan sát `persist.radio.multisim.config=dsds` và hai kênh RIL logic; khả năng dùng hai SIM vật lý cùng lúc **chưa được xác minh**.
- **Hotspot:** mô-đun Launcher3 AutoHotspot v0.4 được báo cáo PASS sau reboot; kiểm thử 24/7 và trên biến thể khác còn mở.
- **Âm thanh:** thời điểm thử `/proc/asound/cards` không có sound card, Device Tree ghi `sound/status=disabled`; việc sửa âm thanh **chưa hoàn tất** và nhánh này đang **tạm dừng**.

## Bộ công cụ v0.2.0

- `tools/h01-readonly-win7.cmd`: dùng trực tiếp với ADB trên Windows 7, chỉ truy vấn thuộc tính và thống kê đã chọn.
- `tools/h01-readonly-linux.sh`: phiên bản POSIX shell cho Linux/antiX.
- `tools/verify_sha256.py`: kiểm tra SHA-256 ngoại tuyến từ các tệp sidecar, không đăng firmware hay checksum riêng lên mạng.
- `tools/inspect_2846.py`: kiểm tra 6 điều kiện logic About → Assistant Function từ APK gốc, không cần ADB.
- `tools/inspect_mmi_vdex.py`: đọc VDEX 010 và khôi phục riêng 9/9 tham chiếu quickening của `MySecretCodeReceiver.onReceive()`; chỉ xuất kết luận, không ghi bytecode OEM.
- `tests/test_repository.py`: kiểm tra CSV GPT và logic xác minh hash bằng dữ liệu giả.

Chạy thử trên PC bằng `python3 -m unittest discover -s tests -v`; không cần kết nối H01. Đây là **công cụ dành cho nghiên cứu**, chưa được kiểm thử trực tiếp trên mọi cấu hình H01.

- `tools/compare_glocalmehome_2846.py`: đối chiếu ngoại tuyến các APK GlocalmeHome, không đăng lại APK OEM; xem [báo cáo mẫu lưu trữ](docs/firmware/2846-apk-comparison.md).

## Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [SECURITY.md](SECURITY.md). Báo cáo cần ghi rõ **mã thiết bị, phiên bản, cách kiểm tra, nguồn bằng chứng và mức độ chắc chắn**, loại bỏ dữ liệu riêng tư trước khi gửi.

## Giấy phép

- Mã nguồn tự viết trong `tools/` và các script: **MIT**, xem [LICENSE](LICENSE).
- Nội dung tài liệu/sơ đồ gốc do cộng đồng sáng tạo: **CC BY 4.0**, xem [LICENSE-DOCS.md](LICENSE-DOCS.md).
- Firmware, trình điều khiển, APK hệ thống, logo nhãn hiệu và phần mềm OEM/Qualcomm/GlocalMe **không** được cấp phép lại bởi repository này. Không đưa các bản dump đó vào Git.

Đây là dự án cộng đồng **không liên kết và không được bảo trợ** bởi ZEUS, GlocalMe, UCloudlink hoặc Qualcomm.
