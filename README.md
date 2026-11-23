# ZEUS H01 Open Firmware Research

**Dự án nghiên cứu mở, độc lập** về ZEUS H01 / GlocalMe K1: phần cứng, Android 8.1, firmware, bootloader, EDL, OTA, modem/SIM, các chức năng ẩn và ứng dụng tùy biến.

> **Trạng thái: v0.1.0 — bộ khung tài liệu công khai.** Tài liệu được biên soạn lại từ ghi chép và báo cáo kiểm thử của dự án. Không phải firmware chính thức, không phải ROM phục hồi sẵn dùng, cũng không bảo đảm mọi kết quả áp dụng cho mọi biến thể H01.

English: [README.en.md](README.en.md)

## Bắt đầu

- [Tổng quan phần cứng](docs/hardware/overview.md)
- [Bản đồ nghiên cứu firmware / phân vùng](docs/firmware/overview.md)
- [OTA tăng dần, bản 81 → 87](docs/firmware/ota.md)
- [Bootloader, Fastboot, EDL và root](docs/boot/root-and-recovery.md)
- [Hai kênh SIM logic / DSDS](docs/network/dual-sim.md)
- [Đường âm thanh chưa hoạt động](docs/system/audio.md)
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

## Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [SECURITY.md](SECURITY.md). Báo cáo cần ghi rõ **mã thiết bị, phiên bản, cách kiểm tra, nguồn bằng chứng và mức độ chắc chắn**, loại bỏ dữ liệu riêng tư trước khi gửi.

## Giấy phép

- Mã nguồn tự viết trong `tools/` và các script: **MIT**, xem [LICENSE](LICENSE).
- Nội dung tài liệu/sơ đồ gốc do cộng đồng sáng tạo: **CC BY 4.0**, xem [LICENSE-DOCS.md](LICENSE-DOCS.md).
- Firmware, trình điều khiển, APK hệ thống, logo nhãn hiệu và phần mềm OEM/Qualcomm/GlocalMe **không** được cấp phép lại bởi repository này. Không đưa các bản dump đó vào Git.

Đây là dự án cộng đồng **không liên kết và không được bảo trợ** bởi ZEUS, GlocalMe, UCloudlink hoặc Qualcomm.
