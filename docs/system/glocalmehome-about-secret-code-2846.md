# Mã 2846 — menu kỹ thuật ẩn trong About của GlocalmeHome

> **Kết quả phân tích tĩnh và video thực tế, cập nhật 23/11/2026:** đã tìm được **nơi đăng ký nhận mã 2846 trong MMI.apk**, đồng thời video H01 xác nhận mã mở giao diện **Assistant Function** trong GlocalmeHome. Chưa chứng minh bằng log runtime hoặc decompile method body đường gọi sang MMI. Không nhầm với ứng dụng [H01 Hidden Settings](https://github.com/phai-nguyen/H01-Hidden-Settings).

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

Dùng [hướng dẫn quan sát ADB thủ công trước/sau khi nhập mã](../tools/secret-2846-readonly.md). Các lệnh kiểm tra chỉ đọc trạng thái qua ADB; **không** gọi `su`, `am start`, gửi secret-code broadcast, kích hoạt factory test hoặc thay đổi cài đặt. Chủ thiết bị tự thao tác About trên màn hình khi thấy an toàn.

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
- **Đã kiểm chứng trực quan từ video ngày 23/11/2026:** màn hình Assistant Function hiện sau khi nhập `2846`, có ba nút MMI / Log Tools / System Settings; các nhánh mở được giao diện tương ứng trên máy thử.
- **Chưa kiểm chứng:** tên Activity foreground chính xác ở mỗi bước, đường Intent/IPC từ GlocalmeHome sang MMI, body `onReceive` và khả năng tương thích giữa các firmware H01.

## 8. Bằng chứng bổ sung: video thao tác thực tế 23/11/2026

**Nguồn:** video người dùng cung cấp trong phiên nghiên cứu (`IMG_5366.mp4`, dài khoảng 48 giây). Không đăng video nguyên bản lên GitHub vì màn hình About có thể chứa thông tin riêng về thiết bị.

| Mốc tương đối | Quan sát trực tiếp trên màn hình H01 | Mức độ |
| --- | --- | --- |
| 00:05–00:10 | Vào trang **About** của launcher GlocalmeHome | VIDEO OBSERVED |
| 00:13–00:21 | Hộp thoại **Please enter password**, bàn phím số nhập **2846** | VIDEO OBSERVED |
| 00:24–00:26 | Mở trang **Assistant Function** với **MMI**, **Log Tools**, **System Settings** | VIDEO OBSERVED |
| 00:29–00:34 | Chọn **MMI**, hiện menu thử phần cứng có nhãn tiếng Trung (gồm mục tự động/kiểm thử thủ công và thông tin) | VIDEO OBSERVED |
| 00:39–00:42 | Màn hình **Log Tools** hiển thị **Open Android log**, **Open Modem log**, **Modem cfg** | VIDEO OBSERVED |
| 00:44–00:47 | Màn hình **System Settings** của Android xuất hiện (Apps & notifications, Battery, Display) | VIDEO OBSERVED |

**Kết luận mới:** Trên một H01 thực tế, luồng người dùng `GlocalmeHome > About > nhập 2846 > Assistant Function` đã hoạt động. **Assistant Function không đồng nhất với MMI MainActivity**: người dùng còn phải chọn nút **MMI**. Điều này điều chỉnh giả thuyết trước rằng nhập mã có thể mở thẳng MMI.

**Chưa kết luận từ video:** component Android phụ trách Assistant Function, có/không sử dụng `MySecretCodeReceiver`, cách `2846` được đối chiếu trong code, khả năng phát log có thực sự được kích hoạt khi xem trang Log Tools. Video không có kết quả `dumpsys activity` nên không đủ để gán chính xác Activity/package cho từng màn hình.

**Kiểm chứng kế tiếp:** lấy `dumpsys activity activities` theo ba mốc **trước nhập mã**, **Assistant Function**, **sau khi chọn MMI**; chỉ trích các dòng chứa tên package/activity, không gửi nguyên log chứa định danh. Không thử những công tắc có thể thay đổi modem/ADB/root hoặc khởi động lại.

## 9. Kiểm chứng foreground Activity từ ảnh CMD Windows 7 (23/11/2026)

Trong ảnh người dùng cung cấp sau khi mở menu **MMI**, đầu ra `adb shell dumpsys activity activities` hiển thị:

```text
mResumedActivity: ... com.ukelink.dusk.mmi/.MainActivity ...
mLastPausedActivity: ... com.glocalme.g4home/com.glocalme.minilauncher.assistant.AssistantActivity ...
```

**Kết luận quan sát runtime:** màn hình Assistant Function sử dụng `com.glocalme.minilauncher.assistant.AssistantActivity` của package `com.glocalme.g4home`; sau khi chọn **MMI**, Activity `com.ukelink.dusk.mmi/.MainActivity` của package MMI ở foreground. Như vậy đoạn **Assistant Function → MMI** đã được đối chiếu từ trạng thái Activity thật, không còn là suy đoán chỉ dựa trên Manifest.

**Giới hạn bằng chứng:** ảnh được chụp khi MMI đang mở; `mLastPausedActivity` cho biết Activity trước đó, nhưng không khẳng định cách gửi Intent, không chứng minh `MySecretCodeReceiver` được gọi, cũng không chỉ ra method kiểm tra mật mã trong trang About.

### Thu thập TXT đúng thứ tự trên Windows 7

Mở **Assistant Function** (trước khi chọn MMI), rồi thực thi:

```bat
cd /d C:\\v3\\platform-tools
adb shell dumpsys activity activities > H01-2846-Assistant.txt 2>&1
```

Chọn **MMI** trên H01, sau đó chạy:

```bat
adb shell dumpsys activity activities > H01-2846-MMI.txt 2>&1
copy /b H01-2846-Assistant.txt+H01-2846-MMI.txt H01-2846-RESULT.txt
```

Mỗi lệnh tạo tệp trước khi gộp. Tệp `dumpsys` đầy đủ có thể chứa dữ liệu riêng của thiết bị; rà soát và ẩn danh trước khi phát hành công khai.

## 10. Bằng chứng ảnh CMD mới — xác định chính xác Activity About (23/11/2026)

Người dùng cung cấp **ba ảnh màn hình Windows 7 CMD** sau khi khảo sát `dumpsys activity activities` với bộ lọc `findstr`. Ảnh hiển thị cùng task **#150**, gồm những Activity sau theo thứ tự chuyển màn hình:

| Bước | Package | Activity thực tế | Bằng chứng |
| --- | --- | --- | --- |
| About / Giới thiệu | `com.glocalme.g4home` | `com.glocalme.minilauncher.about.MiniAboutActivity` | `mLastPausedActivity` khi Assistant Function ở foreground |
| Assistant Function | `com.glocalme.g4home` | `com.glocalme.minilauncher.assistant.AssistantActivity` | `mResumedActivity` ở ảnh đầu và `mLastPausedActivity` khi MMI ở foreground |
| MMI | `com.ukelink.dusk.mmi` | `com.ukelink.dusk.mmi.MainActivity` | `mResumedActivity` trong ảnh thứ hai |

**Kết luận:** Đã xác minh đường chuyển màn hình **MiniAboutActivity → AssistantActivity → MMI MainActivity** trên H01 thật. Đây là quan sát trạng thái Activity, **không đồng nghĩa** đã đọc được lệnh gọi Intent, broadcast hay biểu thức xác thực `2846` trong Java.

**Điều chỉnh trọng tâm RE:** Ưu tiên phân tích method/callback nhập mật mã của `com.glocalme.minilauncher.about.MiniAboutActivity` và logic mở `AssistantActivity` trong ba DEX của `GlocalmeHome.apk`. Receiver MMI có host `2846` là **một nhánh chức năng có thể liên quan**, nhưng không được coi là đường gọi chắc chắn từ màn About nếu chưa có bằng chứng.

### Lưu riêng báo cáo rút gọn vào TXT (Windows 7)

Đang ở About, gõ:

```bat
cd /d C:\v3\platform-tools
adb shell dumpsys activity activities ^| findstr /I /C:"mResumedActivity" /C:"mLastPausedActivity" > H01-2846-About.txt
```

Sau khi nhập `2846` và ở Assistant Function, chạy:

```bat
adb shell dumpsys activity activities ^| findstr /I /C:"mResumedActivity" /C:"mLastPausedActivity" > H01-2846-Assistant.txt
```

Sau khi chọn MMI, chạy:

```bat
adb shell dumpsys activity activities ^| findstr /I /C:"mResumedActivity" /C:"mLastPausedActivity" > H01-2846-MMI.txt
copy /b H01-2846-About.txt+H01-2846-Assistant.txt+H01-2846-MMI.txt H01-2846-RESULT.txt
```

**Lưu ý:** Trong CMD chạy trực tiếp, dùng toán tử ống `|` (không có dấu `^`); ký hiệu `^|` chỉ dùng khi cần escape pipe trong một lớp lệnh bao quanh. Sau khi tạo tệp có thể chạy `dir H01-2846-*.txt` để xác nhận chúng có thật. Không đưa log đầy đủ lên GitHub trước khi ẩn danh.
