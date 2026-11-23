# Quan sát menu 2846 bằng ADB — Windows 7, chỉ đọc

## Mục đích

So sánh Activity của H01 trước và sau khi chủ thiết bị **tự** nhập `2846` trong `GlocalmeHome > About`. Các lệnh bên dưới **chỉ đọc** trạng thái. Không có script tự chạy mã bí mật hoặc thao tác vào factory menu.

## Chuẩn bị

- Windows 7 SP1, ADB đã ủy quyền; kết nối **một thiết bị H01** qua USB.
- Mở CMD trong `C:\v3\platform-tools`.
- GlocalmeHome có thể truy cập bình thường. Không dùng `pm unhide` hoặc `pm enable` nếu ứng dụng hiện đang ẩn vì đó là thay đổi trạng thái ngoài phạm vi kiểm tra.

## Bước A — Chụp trạng thái ban đầu

```bat
cd /d C:\v3\platform-tools
adb get-state
adb shell getprop ro.fota.version
adb shell pm path com.glocalme.g4home
adb shell pm path com.ukelink.dusk.mmi
adb shell pm path com.ukl.factory
adb shell dumpsys activity activities | findstr /I /C:"com.glocalme.g4home" /C:"com.ukelink.dusk.mmi" /C:"com.ukl.factory" > H01-2846-before.txt
```

Chạy thêm truy vấn receiver; chỉ xem một số dòng phù hợp, không xuất toàn bộ package metadata:

```bat
adb shell dumpsys package com.ukelink.dusk.mmi | findstr /I /C:"MySecretCodeReceiver" /C:"2846" /C:"android_secret_code"
```

## Bước B — Thao tác thủ công trên H01

Tại màn hình H01, vào **GlocalmeHome → About** rồi nhập mã `2846` đúng cách anh đã sử dụng. Khi menu xuất hiện, **chỉ xem giao diện**, không bấm các mục cấu hình kỹ thuật hoặc hiệu chuẩn. Giữ màn hình này đang mở.

## Bước C — Chụp trạng thái sau

```bat
adb shell dumpsys activity activities | findstr /I /C:"com.glocalme.g4home" /C:"com.ukelink.dusk.mmi" /C:"com.ukl.factory" > H01-2846-after.txt
```

So sánh hai tệp TXT. Nếu `H01-2846-after.txt` cho thấy `com.ukelink.dusk.mmi/.MainActivity` đang foreground, điều đó ủng hộ việc chuyển sang MMI; tuy vậy **không đủ kết luận** rằng GlocalmeHome gửi secret-code broadcast hay gọi trực tiếp một Activity.

Nếu không có kết quả `findstr`, điều đó có thể do định dạng `dumpsys` khác nhau hoặc menu đang hiển thị trong cùng một Activity. Không tự kích hoạt receiver để thử.

**Trước khi chia sẻ:** kiểm tra và xóa mọi định danh/đường dẫn không mong muốn trong tệp TXT. Không gửi toàn bộ `logcat`, ảnh chứa IMEI/ICCID/IMSI, số điện thoại, mật khẩu hay khóa.

## Trạng thái

Đây là **quy trình đề xuất, chưa được chạy trên thiết bị H01 trong lần nghiên cứu này**. Chưa có bằng chứng runtime xác nhận chuỗi `About → receiver → MainActivity`. Không root, không flash, không ghi modem, không bật USB Test Mode / ADB ROOT / AutoReboot / Aging Test / Factory Reset.
