# Sao lưu eMMC và ghép bộ firmware H01

**Trạng thái:** đã có nhiều bản sao phân vùng trong kho lưu trữ riêng, **chưa có gói factory ROM đầy đủ được kiểm chứng phục hồi đầu-cuối**.

| Nguồn | Kết quả đã ghi nhận |
| --- | --- |
| eMMC GPT | 42 phân vùng; có [bảng công khai đã bỏ GUID](gpt-layout.md) |
| Boot chain | Có sao lưu `sbl1`, `aboot`, `rpm`, `tz`, `cmnlib`, `keymaster`, các bản `*bak` và một số phân vùng khác |
| Boot/cơ sở | Có ảnh `boot`, `recovery`, `splash`, `misc` trong kho riêng |
| Hệ thống | Đã báo cáo có `system.img`, `vendor.img`, `userdata.img` trên Dropbox — **không công bố** |
| eMMC boot area | Có nghiên cứu `boot1`, `boot2`; cần đối chiếu metadata/độ đầy đủ |
| OTA | Incremental source build 81 → target 87; **không phải factory firmware** |

**Không ghép tùy tiện** dữ liệu đặc thù từng máy: `modemst*`, `fsg*`, `persist`, `userdata`, `keystore`, `productinfo`, NV, SoftSIM. Cần kiểm tra checksum, GPT/partition mapping, bootloader/firmware revision, các vùng còn thiếu và phương án rollback trước khi gọi một gói “firmware khôi phục”.

Các file OEM/IMG/Firehose không được đưa lên repo công khai. Chỉ công bố cấu trúc, hướng dẫn tự kiểm tra ngoại tuyến và kết quả đã khử định danh. Xem [GPT](gpt-layout.md), [OTA](ota.md), [boot/root](../boot/root-and-recovery.md), [xác minh hash](../tools/backup-hashes.md).

**Nguồn:** trang Notion tổng H01, các mục GPT/eMMC/sao lưu 11–18/11/2026 và “phương án ghép firmware”.