# H01 Auto Power-On v0.6 — bằng chứng boot eMMC và tích hợp ba chức năng

**Nguồn:** [Notion Auto Power-On](https://app.notion.com/p/41ec5d5277a9815799c4d61fba41a3ea), mục 9–10, các phép thử 20–21/11/2026. Biên soạn 24/11/2026. **REPORTED PASS** trên một H01, không phải hướng dẫn flash.

## Mốc thực nghiệm v0.6

| Bước | Kết quả |
| --- | --- |
| Sao lưu boot Magisk đang chạy trước thử | 33.554.432 byte; công cụ FC báo không có khác biệt với ảnh cứu hộ |
| Từ máy tắt vào Fastboot | DN + Power **PASS** |
| Nạp tạm ảnh boot Magisk cứu hộ qua `fastboot boot` | Android, root, hotspot **PASS** |
| Kiểm tra trước lần ghi v0.6 | So hash bản sao/ảnh thử/ảnh cứu hộ, có xác nhận rủi ro |
| Thử ghi v0.6 vào phân vùng boot eMMC | Fastboot `Sending OKAY`, `Writing OKAY` |
| Reboot sau khi ghi | `sys.boot_completed=1`, `uid=0(root)` |
| Tắt hẳn → cắm USB-C, không nhấn Power | **Người dùng xác nhận Android tự boot PASS** |
| Sau boot, AutoHotspot v0.4 | Wi-Fi AP bật, **REPORTED PASS** |

Nạp tạm bằng `fastboot boot` **khác** boot đã ghi eMMC. Ở lượt chẩn đoán, màn logo H01 khi còn trong Fastboot không phải bằng chứng treo Android.

## Chuỗi tích hợp 21/11/2026

```text
H01 tắt hoàn toàn
 → cấp USB-C, không nhấn Power
 → Auto Power-On v0.6 đưa máy vào Android
 → Magisk AutoHotspot v0.4 phát Wi-Fi
 → 4G AutoShow v1.1 hiển thị 4G và cột sóng
```

Chủ thiết bị xác nhận **cả ba cùng PASS trong một lần kiểm tra cấp nguồn lạnh**, không cần ADB. Log AutoShow v1.1 ghi cờ `uservice.control.slot0` chuyển false → true rồi kết thúc one-shot. Điều này khác giai đoạn trước khi tính năng Auto Power-On chỉ mới được thử bằng cách nạp tạm.

## Giới hạn

- **Chưa thử:** không lắp pin, nhiều lần mất điện chập chờn, nguồn 5V yếu, 24/7, revision khác hoặc một H01 thứ hai.
- **Chưa có báo cáo riêng:** đọc lại boot từ eMMC sau lần ghi v0.6 và so byte; khôi phục bằng cách ghi boot cứu hộ sau flash. Chỉ có thử nạp tạm ảnh cứu hộ PASS.
- Giữ riêng boot OEM/Magisk, module có binary, SHA-256 của các bản ảnh, dữ liệu radio/định danh. **Không tạo bản flash hoặc yêu cầu kiểm thử mới trong đợt công bố.**

Xem [LK/PMIC](lk-pmic-charger-analysis.md), [AutoHotspot](../projects/autohotspot-api-history.md), [4G SystemUI](../system/4g-slot0-systemui-evidence.md).