# H01 — nguyên nhân scanner tính năng ẩn lỗi và kết quả phân tích độc lập

**Nguồn:** [Notion — 8 APK/ODEx/VDEx, ngày 19/11/2026](https://app.notion.com/p/41dc5d5277a981db8ad1fff1aca10bc5). **STATIC VERIFIED trên bộ tệp đã lưu, chưa thử hàng loạt 393 Activity/Alias.**

## Phân biệt lỗi công cụ với kết quả firmware

| Giai đoạn | Kết quả |
| --- | --- |
| Scanner **v1.0** trên Windows 7 | CLR initialization failed, mã lỗi `800736b1`, mã thoát `-65536`; **chương trình chưa quét H01** |
| Scanner **v1.1** | Thu được **8 APK + 7 ODEX + 7 VDEX**, nhưng có **22 cảnh báo**, gồm lỗi trích APK và `VBArray expected` khi xử lý VDEX/ODEX |
| Bộ parser độc lập trên RAR đã thu | Đọc binary `AndroidManifest.xml`, metadata ZIP/APK và bảng class/string DEX/ART VDEX 010; không phụ thuộc VBScript lỗi |
| Kết quả parser độc lập | **473 component** gồm **369 Activity + 24 alias**; **29.735 DEX class** trên tám gói |

**DEX list trống ở scanner v1.1 là hậu quả parser lỗi**, không phải dấu hiệu firmware không có bytecode. Parser độc lập đã phát hiện mã, nhưng **chưa dequickening toàn bộ ART method body** và chưa thử chạy mọi component.

## Phân bố Activity/Alias

| Gói | Activity | Alias | Class DEX |
| --- | ---: | ---: | ---: |
| Android Settings | 220 | 20 | 3.826 |
| SystemUI | 19 | 1 | 3.830 |
| GlocalmeHome | 55 | 0 | 17.932 |
| MMI | 44 | 0 | 2.790 |
| Phone | 29 | 3 | 1.322 |
| Settings Provider | 0 | 0 | 31 |
| Provision | 1 | 0 | 1 |
| UklFactory | 1 | 0 | 3 |
| **Tổng** | **369** | **24** | **29.735** |

Các bộ manifest/class lớn có thể dùng chung giữa nhiều sản phẩm OEM. Không suy từ `pm list features` hoặc DEX strings rằng H01 có NFC, vân tay, GPS hoạt động hoặc SIM thứ hai đã sẵn sàng.

## Các cấp độ thông tin

- **STATIC VERIFIED:** một component được khai báo, class/string có mặt, ví dụ `UcApnEditorActivity`, `TunerActivity` (`enabled=false`), `LockSetActivity`.
- **OBSERVED ON DEVICE:** chỉ các màn đã có video/dumpsys riêng, chẳng hạn LockSet hoặc Assistant Function.
- **NOT TESTED:** những Activity còn lại và mọi thay đổi APN/band/Factory/AutoReboot.

Chưa đăng APK/ODEX/VDEX bản quyền, danh sách raw class có chuỗi riêng hoặc công cụ có quyền root tự kích hoạt các tính năng nguy hiểm. Xem [inventory](hidden-feature-inventory.md), [OEM flags](hidden-activity-and-oem-flags.md).