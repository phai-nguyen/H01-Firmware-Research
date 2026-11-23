# LK/ABOOT trên H01: boot-image verifier khác Fastboot flash authorization

**Nguồn:** Notion H01 mục 100, 104–109, đặc biệt **mục 107 — hiệu chỉnh call graph (11/11/2026)**. **Trạng thái: phân tích tĩnh ABOOT với đối chiếu Qualcomm LK cùng họ; các trạng thái QSEE/SCM lúc boot chưa được ghi trực tiếp.**

## Các khái niệm không nên nhập làm một

| Thành phần | Vai trò |
| --- | --- |
| PBL/SoC Secure Boot | Hardware chain-of-trust; **chưa xác minh fuses trực tiếp** |
| LK/ABOOT | Xử lý boot image, gọi logic verifier và triển khai Fastboot |
| Boot verifier init | Khởi tạo trạng thái boot verification dựa vào lock state và keystore |
| Image verifier | Kiểm tra chữ ký/metadata theo image được boot |
| Fastboot `flash:` callback | **Cổng cho phép ghi** theo trạng thái lock, partition, header, kích thước, secure-image |
| QSEE/Keymaster | Nhận Root-of-Trust / trạng thái boot theo những nhánh trong ABOOT |

Việc Fastboot báo `secure:no` trong một snapshot **không chứng minh** PBL hardware fuses đã tắt, không khẳng định mọi ảnh unsigned đều flash được.

## Call graph đã hiệu chỉnh trong báo cáo gốc

Phân tích disassembly ghi hai loader-path gọi boot-verifier init và image verifier riêng biệt. **Điều chỉnh quan trọng từ mục 107:** nhận định cũ trong mục 104.5/105.6 rằng callback Fastboot `flash:` gọi trực tiếp boot-verifier init **đã được rút lại**; call-site trước đó thuộc đường nạp boot image, không phải callback flash.

Callback flash có handler riêng với các kiểm tra `Device is locked`, `Partition flashing is not allowed`, `image header corrupt`, `image size mismatch`, `Invalid secure image`. Không suy diễn allowlist tên phân vùng hoặc đưa lệnh thử flash từ chuỗi log này.

State raw `2` trong kết quả khởi tạo keystore được đối chiếu với nhánh **YELLOW** trong source LK cùng họ; không có bằng chứng runtime H01 đã đi qua nhánh đó. `0x8f627f58` là helper kiểm tra có phân vùng Keymaster, không phải getter màu Verified Boot.

## OEM keystore được phân tích

Notion ghi một object DER ký RSA có trong ABOOT, dài 1.619 byte; kiểm tra nhất quán inner keystore/certificate bằng OpenSSL đã đạt. Certificate mang tên Android generic. **Không suy ra** đó là khóa GlocalMe production, hardware root key hoặc private key. Bằng chứng object ký khớp public key đi kèm khác hoàn toàn bằng chứng PBL đã xác thực toàn bộ image.

ABOOT có nhánh tạo digest Root of Trust và gửi tới QSEE/Keymaster; chưa đọc được phản hồi runtime của các secure-app request. Không đăng public-key blob OEM, hash thiết bị, các file keystore/keymaster partition hoặc raw dump QSEE.

## Kết quả sau này và ngữ cảnh

Trước khi unlock, snapshot ghi Verified Boot `green`; nghiên cứu unlock sau đó trên H01 thử nghiệm ghi `ro.boot.flash.locked=0` và `verifiedbootstate=orange`. Đây là **các thời điểm khác nhau**. Phân tích tĩnh trạng thái khóa cũ không được chép thành trạng thái thiết bị mới nhất.

**Liên quan:** [OEM Unlock](oem-unlock-research.md), [root](root-and-recovery.md), [Auto Power-On](auto-power-on-usb.md). Không chạy `fastboot flash`, sửa DEVINFO, patch keystore hoặc bỏ qua verification từ tài liệu này.