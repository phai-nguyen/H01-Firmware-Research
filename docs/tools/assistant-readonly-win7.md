# Kiểm tra 3 nút Assistant Function trên Windows 7 — chỉ đọc

**Điều kiện:** H01 đã cấp quyền ADB; trên PC có `adb.exe` ở `C:\v3\platform-tools`. Chỉ kết nối **một** thiết bị Android khi chạy. Không yêu cầu root hoặc thao tác trong menu kỹ thuật.

1. Đặt `tools/h01-assistant-readonly-win7.cmd` trong `C:\v3\platform-tools` (cùng nơi có `adb.exe`).
2. Nhấp đôi file CMD hoặc gõ:

```bat
cd /d C:\v3\platform-tools
h01-assistant-readonly-win7.cmd
```

3. Kết quả xuất ra `C:\v3\platform-tools\H01-ASSISTANT-RESULTS`:
   - `01-package-status.txt` — đường APK và trạng thái tên package `com.ucloudlink.feedback`.
   - `02-feedback-state.txt` — các dòng `LogSettingActivity`, `enabled=`, `hidden=` hoặc `User 0:` trong `dumpsys package`.
   - `03-foreground.txt` — Activity đang mở ở thời điểm thu thập.
4. Đọc hai tệp đầu và **ẩn thông tin thiết bị** nếu xuất hiện trước khi chia sẻ. Không đưa nguyên `dumpsys` hay nội dung nhật ký hệ thống lên GitHub.

**Kết luận khả dĩ:**

- Nếu `pm path` không trả đường APK: có thể gói vắng mặt, bị ẩn đối với Package Manager, hoặc thông tin không hiển thị với phiên ADB hiện tại. Không tự sửa trạng thái để thử.
- Nếu gói nằm trong `pm list packages -d`: đang được đánh dấu disabled trong ngữ cảnh truy vấn đó, cần xác minh thêm theo user.
- Nếu tìm thấy `LogSettingActivity`, mới chỉ xác nhận có khai báo; **không có nghĩa Activity khởi chạy được**.

Không bấm `Open Android log`, `Open Modem log` hay `Modem cfg` trong giai đoạn chỉ đọc. Bộ công cụ này không thực hiện ba thao tác đó.
