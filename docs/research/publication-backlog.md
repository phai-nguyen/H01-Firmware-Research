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
