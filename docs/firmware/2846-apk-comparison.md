# Đối chiếu cơ chế menu 2846 trong các APK GlocalmeHome lưu trữ

**Ngày phân tích:** 23/11/2026. **Phạm vi:** phân tích ngoại tuyến các bản APK đã có trong kho tệp người dùng, **không** chạy các bản trên thiết bị hay truy cập dữ liệu SIM. Các APK OEM không được đưa vào GitHub.

## Những mẫu đã kiểm tra

| Tệp trong kho lưu trữ | Dung lượng (byte) | Quan hệ với bản gốc |
| --- | ---: | --- |
| `GlocalmeHome.apk` | 19.430.048 | Mẫu gốc đối chiếu |
| `H01-GlocalmeHome-original.apk` | 19.430.048 | Trùng **SHA-256 toàn APK** với mẫu gốc |
| `H01-GlocalmeHome.apk` | 19.430.048 | Trùng **SHA-256 toàn APK** với mẫu gốc |
| `H01-GlocalmeHome(1).apk` | 19.430.048 | Trùng **SHA-256 toàn APK** với mẫu gốc |
| `GlocalmeHome-VietHoa-Test.apk` | 19.614.541 | APK đã sửa đổi: hash toàn tệp **khác** mẫu gốc |

**Bốn tệp cùng hash là một mẫu nhị phân duy nhất**, không phải bốn bản firmware độc lập. Chưa có APK được xác minh là lấy từ **chiếc H01 thứ hai**.

## Kết quả so sánh

| Kiểm tra | Bản sao OEM so với mẫu gốc | Bản thử Việt hóa so với mẫu gốc |
| --- | --- | --- |
| APK toàn tệp | IDENTICAL | DIFFERENT |
| `classes.dex` | IDENTICAL | DIFFERENT |
| `classes2.dex` | IDENTICAL | DIFFERENT |
| `classes3.dex` | IDENTICAL | DIFFERENT |
| `res/layout/about_settings_activity.xml` | IDENTICAL | DIFFERENT |
| `res/layout/assistant_activity.xml` | IDENTICAL | DIFFERENT |
| `MiniAboutActivity.startAssistantFunction()` | MATCH | MATCH |
| `MiniAboutActivity$5.onClick()` | MATCH | MATCH |
| `AssistantActivity.startMMI()` | MATCH | MATCH |
| `AssistantActivity.startLogTools()` | MATCH | MATCH |
| `AssistantActivity.startSystemSettings()` | MATCH | MATCH |

Mỗi **MATCH** là chuỗi opcode và tham chiếu string/method mà trình phân tích đọc được **giống nhau ở phương thức mục tiêu**. Phép so sánh này **không** xác thực toàn bộ code item, thanh ghi, bảng ngoại lệ, nhánh điều khiển, lớp khác hay chữ ký cài đặt Android. Không được đồng nhất với kiểm thử chức năng trên máy.

Phân tích theo mẫu gốc tiếp tục hỗ trợ quan sát trước đó:

1. Nhấn 5 lần vào dòng **Version No.** trong About.
2. Hộp thoại nhập mã **2846**, callback `MiniAboutActivity$5.onClick()`.
3. Mã đúng đi tới đường ARouter **`/minilauncher/assistant`**.
4. `AssistantActivity` có các nút **MMI**, **Log Tools**, **System Settings**.

**Không suy ra:** Tất cả firmware H01 đều có cơ chế trên; một APK Việt hóa khác hash là phiên bản firmware mới; hay dòng About trực tiếp gửi secret-code broadcast của MMI.

## Công cụ kiểm tra độc lập

- [`tools/compare_glocalmehome_2846.py`](../../tools/compare_glocalmehome_2846.py): so sánh hash APK, 3 DEX, 2 layout và chữ ký tham chiếu/opcode của 5 method.
- Phụ thuộc `tools/inspect_2846.py` có sẵn trong repository. Python 3, không cần ADB, root, APKTool/JADX, không gọi mạng.
- Chạy:

```sh
python3 tools/compare_glocalmehome_2846.py "path/to/first.apk" "path/to/second.apk"
python3 -m unittest discover -s tests -v
```

Cả hai APK chỉ được đọc trên máy phân tích. **Không đưa tệp APK hoặc log chứa IMEI, IMSI, SN, thông tin tài khoản lên GitHub.** Chương trình có `--json` để xuất metadata cho kiểm thử cục bộ; kiểm tra nội dung trước khi công khai.

## Bước xác minh phiên bản trên chiếc H01 thứ hai (chưa thực hiện)

Nếu được chủ thiết bị đồng ý thử máy thứ hai, chỉ thu APK GlocalmeHome và các thuộc tính hệ thống không nhạy cảm rồi đối chiếu hash/chữ ký, không flash:

```bat
cd /d C:\v3\platform-tools
adb devices
adb shell getprop ro.build.display.id
adb shell pm path com.glocalme.g4home
```

Đường APK sẽ do `pm path` báo về. Chỉ dùng `adb pull <đường-dẫn-APK> <thư-mục-riêng>` sau khi xác định đúng một thiết bị và đúng đường dẫn. Không cần sửa launcher hay bật factory mode. Hai H01 có thể dùng cùng build nên cần kiểm tra **bytecode thực**, không chỉ tên phiên bản.

## Điều chỉnh kế hoạch ngày 23/11/2026

Người dùng hiện **không có chiếc H01 thứ hai** để kiểm thử. Bước đối chiếu thiết bị thứ hai chỉ còn là giả thuyết lịch sử, **không đặt làm yêu cầu tiếp theo**. Nhánh chủ động hiện tại là [Assistant Function: kiểm tra ba nút và package Feedback](../system/assistant-function-routing.md), dùng dữ liệu trên một máy và APK gốc đã lưu.

## Trạng thái

**Đã hoàn thành:** 4 bản OEM lưu trữ có hash y hệt; mẫu Việt hóa khác hash nhưng cả 5 phương thức mục tiêu cho chữ ký đối chiếu khớp; công cụ so sánh đã chạy trên 2 cặp mẫu; 6/6 unit test synthetic PASS. **Chưa hoàn thành:** đối chiếu máy H01 thứ hai và kiểm thử chạy APK Việt hóa trên thiết bị thật.
