# H01 FOTA — kết quả khôi phục DEX từ VDEX 010 của ứng dụng ABUP

**Nguồn gốc:** [Nhật ký Notion H01, mục 4 và 14](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), phân tích 10/11/2026. **STATIC VERIFIED**, không kiểm thử lệnh OTA trên thiết bị.

## Các ảnh gốc trong hồ sơ

| Thành phần | Dữ liệu nguồn |
| --- | --- |
| Android package | `com.abupdate.fota_demo_iot` |
| APK | **577.817 byte** |
| ODEX | **74.208 byte** |
| VDEX | **2.865.228 byte**, định dạng **`vdex010`** |
| DEX được khôi phục | **2.540.284 byte**, version **038** |
| Định nghĩa lớp | **2.795** |
| String ID | **16.587** |
| Type ID | **3.605** |
| Method ID | **23.619** |

## Phạm vi phép khôi phục

Bộ phân tích VDEX010 đã phục hồi **13.143 bản ghi quickening**; tiêu thụ **74.706 giá trị 16-bit**, không còn entry dư. Báo cáo kiểm:
- **11.954** opcode `return-void-no-barrier` được phục hồi;
- **200** trường hợp quickened NOP được khôi phục thành `check-cast`;
- **412** NOP thường được giữ nguyên;
- trường checksum **Adler-32 `0x3e0a40bc`** khớp header DEX.

**Ý nghĩa:** DEX sau khôi phục có cấu trúc/checksum nhất quán và có thể đưa vào trình đọc bytecode. Điều đó **không tạo ra source Java chính hãng** hoặc chứng minh các API có thể được gọi trên thiết bị ngoài thí nghiệm.

## Dấu vết cơ chế FOTA

Các namespace phân tích có `com.abupdate.iot_libs`, `iot_download_libs`, `mqtt_libs` cùng các class `CustomConfig`, `SystemReceiver`, `AlarmCheckReceiver`, `OtaService`, `UpgradeReceiver`, `MqttService`.

Từ method, SDK có đường **checkVersion → metadata/policy → download/kiểm đoạn MD5 → RecoverySystem.installPackage**. Đây là đường **OTA Android qua Recovery**, không tương đương EDL/Firehose. Một số chuỗi/URL/template nằm trong DEX SDK là cấu hình mẫu; không phải bằng chứng máy chủ đang cấp gói cho H01.

**Giới hạn:** APK signature không tự đồng nghĩa khóa ký OTA Recovery; không lấy DEX strings để kết luận có bản cập nhật mới; không xuất bản APK/ODEX/VDEX, bytecode được giải, credential/backend, token hoặc raw log.

Xem [FOTA internals](fota-abup-internals.md), [OTA 81→87](ota-delta-validation-v10.md).