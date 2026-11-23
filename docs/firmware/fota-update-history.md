# Nhật ký kiểm tra cập nhật OTA H01 — ABUP/FOTA

**Nguồn:** Notion nghiên cứu H01, mục 25–27 (log ngày 20–21/10 và 10/11/2026), đối chiếu mục FOTA/ABUP đã công bố. **Phân loại: quan sát lịch sử từ log; không phải kiểm tra API tại thời điểm xuất bản.**

## Các mốc đã có bằng chứng

| Thời điểm trong log | Hoạt động | Kết quả backend |
| --- | --- | --- |
| 20/10/2026 | FOTA đăng ký thiết bị và gọi kiểm tra phiên bản | `No new updates were found`, status `2101`, `data=null` |
| 21/10/2026 | Kiểm tra lại cùng phiên bản đang chạy | `No new updates were found`, status `2101`, `data=null` |
| 10/11/2026 09:47 | `checkVersion` từ H01 | `No new updates were found`, status `2101`, `data=null` |
| 10/11/2026 17:05 | `checkVersion` từ H01 | `No new updates were found`, status `2101`, `data=null` |

Bộ dữ liệu phân tích cho thấy firmware có khả năng **kết nối tới hệ thống ABUP và nhận phản hồi JSON hợp lệ**. Đây không phải lỗi HTTP và không chứng minh backend đã dừng cung cấp cập nhật vĩnh viễn. Những log trên **không chứa URL tải payload hợp lệ** cho các phiên truy vấn đó.

Version được ghi trong snapshot: `K1_TSV3.1.005.001.240116_20240116-1930`. Trong tài liệu Notion có cả các chuỗi `TSU` ở phần tìm kiếm cũ; phải phân biệt chúng với build `TSV` đã được xác nhận trong bản ghi `checkVersion`.

## Diễn giải theo tiến trình nghiên cứu

- **Nhánh log lịch sử:** không có update ở các lần truy vấn 20–21/10 và 10/11. Không được suy từ mốc này rằng trong tháng 11 không thể có gói OTA nào.
- **Nhánh phân tích sau đó:** báo cáo [OTA incremental 81 → 87](ota.md) ghi nhận một gói block-based incremental ở mốc khảo sát khác. **Không tự đồng nhất** với payload do bốn lần `checkVersion` trên trả về.
- **Nhánh phân tích APK:** [FOTA ABUP internals](fota-abup-internals.md) xác nhận cơ chế gọi `RecoverySystem.installPackage()` trong DEX; không đồng nghĩa người dùng đã nhận và cài bản update từ API đó.

## Bảo mật và giới hạn công bố

Log FOTA gốc có `deviceSecret`, `deviceId`, request signature, địa chỉ mạng và định danh modem/thuê bao. Không xuất bản hoặc phát lại request, kể cả khi endpoint dạng REST có thể thấy trong log; những thông tin ấy không cần thiết để ghi nhận **kết quả kiểm tra phiên bản**.

Đây là tóm tắt lịch sử từ bản ghi của H01, **không phải lời khẳng định khả dụng của dịch vụ ABUP hôm nay**. Không có thao tác gọi server hay thay đổi firmware trong lượt biên soạn tài liệu này.