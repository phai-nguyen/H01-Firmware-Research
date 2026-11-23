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
- [Phân tích VDEX010: MMI SecretCodeReceiver.onReceive và mã 2846](docs/system/mmi-secret-code-receiver.md)
- [Danh mục 30 bài kiểm tra MMI](docs/system/mmi-factory-tests.md)
- [Hướng dẫn ADB thủ công quan sát menu 2846 trên Windows 7](docs/tools/secret-2846-readonly.md)
- [Launcher3 AutoHotspot v0.4](docs/projects/autohotspot.md)
- [Các repository ứng dụng liên quan](docs/projects/index.md)
- [Bảng trạng thái và đầu việc](docs/research/status.md)
- [Nguồn gốc và độ tin cậy](docs/research/provenance.md)
- [Quy định an toàn khi công khai](docs/security/publication-policy.md)

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
