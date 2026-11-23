# Mã 2846 — menu kỹ thuật ẩn trong About của GlocalmeHome

> **Kết quả phân tích tĩnh, cập nhật 23/11/2026:** đã tìm được **nơi đăng ký nhận mã 2846 trong MMI.apk**. Chưa chứng minh bằng log runtime bước trung gian giữa About của GlocalmeHome và MMI. Không nhầm với ứng dụng [H01 Hidden Settings](https://github.com/phai-nguyen/H01-Hidden-Settings).

## 1. Phát hiện xác minh từ ba APK nghiên cứu

Báo cáo phân tích ngoại tuyến ngày 19/11/2026 (từ ba APK H01 do chủ thiết bị cung cấp) ghi nhận:

| APK | Package | Quan sát đáng chú ý |
| --- | --- | --- |
| `GlocalmeHome.apk` | `com.glocalme.g4home` | Launcher gốc, 55 Activity; theo người dùng, mục **About / Giới thiệu** là nơi nhập mã `2846`. APK có 3 DEX. |
| `MMI.apk` | `com.ukelink.dusk.mmi` | 44 Activity; **`MySecretCodeReceiver`** đăng ký nhận `android_secret_code` với **host `2846`**. Có `MainActivity` và các trang kiểm tra phần cứng. APK gốc không có `classes.dex` trong ZIP. |
| `UklFactory.apk` | `com.ukl.factory` | Một Activity `UklFacMainActivity`; bố cục có hai tùy chọn **USB Test Mode** và **ADB ROOT**. APK gốc không có `classes.dex` trong ZIP. |

Mã `2846` là **mã người dùng đã xác nhận** để vào menu kỹ thuật từ About; phần đăng ký secret-code trong MMI.apk được **đối chiếu từ AndroidManifest**. Một chương trình tự nhận secret-code không chứng minh launcher gọi nó theo cách nào.

## 2. Sơ đồ luồng — mức độ chắc chắn

```text
[GlocalmeHome / About]
          |
          | Nhập 2846 (đã được chủ H01 xác nhận)
          v
[Điểm kiểm tra/chuyển tiếp trong launcher: CHƯA XÁC ĐỊNH]
          |
          | Giả thuyết: secret-code intent / explicit Activity / IPC
          v
[MMI: MySecretCodeReceiver đăng ký host=2846]
          |
          | Receiver mở MainActivity? CHƯA KIỂM CHỨNG METHOD BODY
          v
[MMI MainActivity / giao diện kiểm tra kỹ thuật]
```

**Không coi các mũi tên giả thuyết là luồng đã được xác minh thực tế.** Một luồng khác cũng có thể tồn tại, ví dụ About tự mở Activity của OEM thay vì sử dụng receiver; cần quan sát Activity được đưa lên foreground khi nhập mã.

## 3. Định danh component quan trọng

- **MMI secret-code receiver:** `com.ukelink.dusk.mmi/.MySecretCodeReceiver`.
- **MMI main activity:** `com.ukelink.dusk.mmi/.MainActivity`.
- **UklFactory main activity:** `com.ukl.factory/com.ukl.factory.UklFacMainActivity`.
- **GlocalmeHome launcher:** `com.glocalme.g4home/com.glocalme.common.boot.BootActivity`.

Sự có mặt của component trong manifest **không tự chứng minh** ứng dụng ngoài có quyền mở component đó, hoặc rằng component an toàn khi chạy. Không sử dụng lệnh tự kích hoạt receiver hay menu kỹ thuật trong phép khảo sát này.

## 4. Có bao nhiêu chức năng trong MMI?

Tài nguyên XML phân tích ngoại tuyến chứa **30 bài kiểm tra**. Có hai cấu hình hiển thị khác nhau: **thường bật 20/30**, **DG4 bật 10/30**. Danh sách và trạng thái từng mục xem [MMI factory test inventory](mmi-factory-tests.md). Chưa có bằng chứng xác định cấu hình nào đang được sử dụng trên H01 K1 thực tế hoặc các bài kiểm tra có phần cứng tương ứng.

## 5. Kiểm chứng runtime an toàn trên H01 (Windows 7)

Dùng [công cụ quan sát trước/sau khi nhập mã](../tools/secret-2846-readonly.md). Công cụ chỉ chạy `getprop`, `pm path`, `dumpsys package` và `dumpsys activity activities` qua ADB, lọc các component có liên quan; **không** gọi `su`, `am start`, gửi secret-code broadcast, kích hoạt factory test hoặc thay đổi bất cứ cài đặt nào. Chủ thiết bị tự thao tác About trên màn hình khi thấy an toàn.

Nếu Activity foreground sau khi nhập mã là `com.ukelink.dusk.mmi/.MainActivity`, đó sẽ là bằng chứng MMI được mở trong luồng menu; tuy nhiên vẫn **chưa chứng minh MMI được gọi bằng BroadcastReceiver hay explicit Intent**. Để xác định điểm gọi cần phân tích body DEX của About và MMI VDEX/ODEX gốc, hoặc có log intent đã được kiểm tra an toàn.

## 6. Hướng phân tích mã tiếp theo

1. **GlocalmeHome**: tìm lớp About, callback nhập mã và chuỗi/constant liên quan; nếu mã được chuyển qua IPC, ghi lại loại Intent và component đích (không công bố APK/DEX OEM).
2. **MMI**: phân tích method `MySecretCodeReceiver.onReceive()` từ `MMI.vdex`/`.odex` theo đúng bản firmware. MMI.apk không chứa DEX thông thường, do đó kết quả chỉ nhìn trong APK là chưa đủ.
3. **UklFactory**: chỉ ghi nhận Activity và hai key `CheckBoxPreferenceUsbTesNodeKey`, `CheckBoxPreferenceAdbDebug`; chưa có method body chứng minh hành vi của các công tắc.
4. **Runtime**: quan sát foreground Activity trước/sau trên máy, không bật các chức năng kỹ thuật.

## 7. An toàn và giấy phép

Không bấm **ADB ROOT, USB Test Mode, AutoReboot, Aging Test, Factory Reset, Charging/DisCharging** hoặc chỉnh modem, eMMC, khóa/bảo mật từ menu này trước khi xác minh hành vi. Bản quyền APK/ODEX/VDEX của nhà sản xuất vẫn thuộc chủ sở hữu tương ứng; repository chỉ phát hành tài liệu tự biên soạn và công cụ nghiên cứu độc lập.

### Nguồn và giới hạn

- Hồ sơ phân tích 19/11/2026: `H01_PhanTich_3APK_MenuAn_20261119.txt` (đọc trực tiếp từ kho tệp nghiên cứu, kiểm tra manifest/XML của ba APK; không phát hành tệp APK gốc).
- Nhật ký Notion 19/11/2026: nghiên cứu màn hình khóa và mã bí mật 2846; phần khảo sát MMI dựa trên phân tích tĩnh.
- Xác nhận về **mục About**: chủ thiết bị H01, 23/11/2026.
- **Chưa kiểm chứng:** đường gọi thực tế từ GlocalmeHome, body `onReceive`, màn hình sau khi nhập mã trong lượt thu thập hiện tại và khả năng tương thích giữa các firmware H01.
