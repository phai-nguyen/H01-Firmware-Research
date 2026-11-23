# FOTA / ABUP — phân tích APK, VDEX và đường cài Android Recovery

**Nguồn:** nhật ký Notion H01, mục 4 và 14, nghiên cứu 10/11/2026; đối chiếu thêm [OTA incremental 81→87](ota.md). **Trạng thái: phân tích tĩnh và kết quả kiểm tra lưu trữ; không phải bản cập nhật được cài trong đợt nghiên cứu này.**

## Thành phần đã khảo sát

| Thành phần | Ghi nhận từ bản sao |
| --- | --- |
| APK FOTA | `/system/app/FOTA/FOTA.apk` — 577.817 byte |
| Package | `com.abupdate.fota_demo_iot` |
| ODEX | 74.208 byte |
| VDEX | 2.865.228 byte, `vdex010` |
| DEX phục hồi | `dex 038`, 2.540.284 byte, 2.795 lớp, 23.619 method ID |

Nhật ký ghi dequickening với 13.143 bản ghi quickening, 74.706 giá trị 16-bit, checksum Adler-32 sau khôi phục khớp header. Đây là bằng chứng về tính nhất quán của **DEX đã phục hồi**, không đồng nghĩa có source Java nguyên thủy.

Các lớp được tìm thấy: `CustomConfig`, `SystemReceiver`, `AlarmCheckReceiver`, `OtaService`, `UpgradeReceiver`, `MqttService`. SDK có mẫu API kiểm tra phiên bản, báo cáo tải và nâng cấp, nhưng **endpoint/template nằm trong DEX không phải URL tải bản firmware H01 hợp lệ đã xác minh**. Không xuất bản product ID, secret, token hoặc endpoint có tính xác thực thiết bị.

## Đường hoạt động

Phân tích method `OtaService` ghi nhận các bước: lấy policy/metadata, kiểm tra dữ liệu tải theo đoạn và MD5, ghi đường dẫn gói đã tải, sau đó gọi `android.os.RecoverySystem.installPackage(context, file)`. Đây là đường chuyển **OTA tới Recovery**, không phải giao thức đọc/ghi eMMC Firehose.

- `ro.fota.oem`, `ro.fota.device`, `ro.fota.platform`, `ro.fota.type`, `ro.fota.version` là các thuộc tính runtime được dùng để xác định cấu hình.
- Chuỗi product `mi/HM-Note4X/MSM8625` trong asset mặc định chỉ là cấu hình mẫu của SDK, **không phải nhận dạng H01**.
- Đường `FOTAK1_057.apk` được thấy trong thông tin build-time của ODEX không chứng minh tệp đó còn ở filesystem đang chạy.

## Phân biệt các nhánh cập nhật

1. **ABUP FOTA:** OTA Android → Recovery.
2. **UService BinaryUpdateHelper:** metadata cho binary/payload phụ trợ; chưa chứng minh ghi firmware partition.
3. **UService loader:** nạp mã DEX/JAR/ELF từ assets/dữ liệu, không tự tương đương OTA.
4. **EDL/Firehose:** giao thức dịch vụ bộ nhớ eMMC, tách biệt với các app Android.

### Giới hạn an toàn

Gói OTA incremental 81→87 trong [nghiên cứu OTA](ota.md) **không phải factory ROM hay ảnh eMMC hoàn chỉnh**. Không công khai APK/VDEX, khóa ký, mật khẩu API, định danh, file OTA OEM hoặc script bỏ qua kiểm tra TLS. Không tự gọi API cập nhật đang hoạt động.

**Tài liệu liên quan:** [UService](../system/uservice-loader.md), [Firehose](edl-firehose-diagnostics.md), [phân vùng](overview.md).