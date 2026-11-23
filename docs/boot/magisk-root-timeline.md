# Magisk 30.7 trên H01: từ fastboot boot RAM tới root cố định

**Nguồn:** Notion trang tổng H01, các mục “H01 thật: thử boot RAM ảnh gốc và marker”, “Mốc mới: root Magisk 30.7 qua boot RAM”, “Root cố định đã PASS” (18/11/2026). **Trạng thái: REPORTED PASS trên thiết bị thử, không phải quy trình cài phổ quát.**

## Các mốc đã xác nhận theo thứ tự

| Mốc | Kết quả |
| --- | --- |
| Boot RAM ảnh boot gốc | Fastboot `Booting OKAY`, ADB `sys.boot_completed=1` |
| Boot RAM ảnh marker (chỉnh cmdline) | `ro.boot.h01_ramtest=ram-20261118`, chứng minh kernel nhận marker |
| Magisk 31.1 thử unpack | Báo `Unable to unpack boot image`; phân tích ghi nhận nhận nhầm gzip marker |
| Magisk 30.7 patch và thử boot RAM | Fastboot `Booting OKAY`, Android lên; sau khi cấp quyền `su -c id` trả `uid=0(root)` |
| Ghi boot đã kiểm chứng và reboot bình thường | Fastboot báo Writing/Booting OKAY, boot đọc lại khớp hash ảnh root, `sys.boot_completed=1`, `uid=0` — **PASS** |

Bản gốc/ảnh Magisk được phân tích ngoại tuyến: kernel/DTB giữ nguyên theo báo cáo, ramdisk thay init và bổ sung thành phần Magisk; không coi ảnh đã vá là được OEM ký lại. Dải dữ liệu cuối boot gốc không được giữ nguyên hoàn toàn trong bản vá, cần phân biệt khi đối chiếu binary.

### Lưu ý về mốc lịch sử

Những mục cũ trước lần flash ghi “root chưa cố định”, nhưng **mục sau đã ghi nhận root cố định sau một lần reboot**. Không kết luận root còn sau factory reset, OTA, tắt hẳn nguồn hoặc mọi firmware revision nếu chưa thử riêng.

## An toàn/khả năng khôi phục

- Boot RAM bằng `fastboot boot` không ghi phân vùng `boot`, nhưng Magisk và Android **có thể ghi vào userdata** sau khi chạy.
- Sau khi flash, chỉ có bằng chứng trên thiết bị/boot đã thử; giữ cả ảnh gốc, ảnh root, file hash, bản sao recovery và cách dùng Fastboot/cứu hộ.
- Không đưa `magisk_patched.img`, file boot OEM hoặc module kết hợp binary hãng vào GitHub.
- Không flash lại boot gốc khi ba tính năng Auto Power-On/AutoHotspot/4G đang PASS, trừ khi có kế hoạch rollback rõ và chủ máy chấp thuận.

**Liên quan:** [mở khóa](oem-unlock-research.md), [Auto Power-On v0.6](auto-power-on-usb.md), [kiểm kê bản sao](../firmware/emmc-backup-verification.md), [quy trình cứu hộ thận trọng](recovery-readiness.md).