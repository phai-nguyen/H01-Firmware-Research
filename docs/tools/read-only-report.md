# Thu thập báo cáo H01 chỉ đọc (Windows 7 / Linux)

Bộ công cụ này chạy từ **máy tính của người nghiên cứu** có ADB và chỉ dùng lệnh `adb shell getprop <tên cụ thể>`, `id`, `wm size`, `wm density`, `cat /proc/...`, `ls -l /dev/snd`. Nó **không flash, không đổi cấu hình, không cài APK, không root** và không ghi file lên H01. Báo cáo được lưu trên máy tính chủ.

## Windows 7 SP1

Yêu cầu: ADB hoạt động và `adb.exe` có trong `PATH` hoặc chạy từ thư mục `C:\v3\platform-tools`; H01 đã cho phép USB debugging. Giữ kết nối **một thiết bị ADB duy nhất**.

1. Chép [`h01-readonly-win7.cmd`](../../tools/h01-readonly-win7.cmd) vào thư mục có `adb.exe`.
2. Mở CMD tại thư mục đó, chạy `h01-readonly-win7.cmd`.
3. Kết quả nằm trong thư mục `H01-READONLY-RESULTS\report.txt` bên cạnh script. Có thể truyền đường dẫn thư mục đầu ra làm tham số thứ nhất, ví dụ `h01-readonly-win7.cmd C:\H01_Results`.

Script dùng CMD của Windows 7; không yêu cầu PowerShell, Python hay quyền Administrator.

## Linux / antiX

Yêu cầu: ADB trong `PATH`, USB debugging, một thiết bị được chọn.

```sh
sh tools/h01-readonly-linux.sh
# hoặc chọn thư mục đầu ra
sh tools/h01-readonly-linux.sh ~/H01_READONLY_RESULTS
```

## Báo cáo gồm những gì?

- Bản Android, mã build, chipset/ABI và trạng thái boot (thuộc tính không định danh).
- Danh sách kích thước block từ `/proc/partitions`, **không** đọc dữ liệu block.
- Cấu hình DSDS và trạng thái `READY/ABSENT` không kèm IMEI, IMSI hay ICCID.
- Tình trạng âm thanh ALSA/PCM và thông số màn hình dạng chỉ đọc.

**Không thu thập** `getprop` toàn bộ, `dumpsys telephony`, logcat, danh sách Wi-Fi, SSID, MAC, IP, mã khóa OTA, danh bạ hoặc firmware binary. Dù vậy, phải **đọc và ẩn danh từng dòng** trước khi nộp báo cáo công khai: môi trường Android có thể chứa tùy biến ngoài dự kiến.

## Phân tích lỗi

- `adb: not found` / `'adb' is not recognized`: bổ sung ADB vào `PATH` hoặc đặt script cạnh `adb.exe`.
- `unauthorized`: cấp quyền USB debugging trên H01.
- `more than one device`: ngắt thiết bị ADB khác trước khi chạy.
- `Permission denied`: chấp nhận mục đó không đọc được, không tự thử root hoặc `chmod`.

**Không xem việc thu thập báo cáo là chứng minh mọi tính năng hoạt động.** Trạng thái `running` của RIL/audio service không chứng minh phần cứng SIM thứ hai hoặc audio phát tiếng.
