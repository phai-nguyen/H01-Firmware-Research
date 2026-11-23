# H01 Assistant Function — định tuyến 3 nút và trạng thái Log Tools

**Mốc 23/11/2026; đổi hướng nghiên cứu do không có H01 thứ hai để đối chiếu.** Đây là **phân tích ngoại tuyến APK GlocalmeHome gốc**, không kích hoạt công cụ log/modem hay thay đổi H01.

## Kết quả đã đối chiếu trong `classes.dex`

| Giao diện | Phương thức `AssistantActivity` | Gói cần kiểm tra | Activity mở qua Intent tường minh |
| --- | --- | --- | --- |
| MMI | `startMMI(View)` | `com.ukelink.dusk.mmi` | `com.ukelink.dusk.mmi.MainActivity` |
| Log Tools | `startLogTools(View)` | `com.ucloudlink.feedback` | `com.ucloudlink.feedback.LogSettingActivity` |
| System Settings | `startSystemSettings(View)` | `com.android.settings` | `com.android.settings.Settings` |

Ở cả ba phương thức, bytecode có cùng khung: gọi `PackageUtil.isAppInstall(package)` trước; khi đi nhánh mở Activity, tạo `Intent`, `setClassName(package, activity)`, rồi `startActivity`. Khi kiểm tra package không đạt, phương thức có chuỗi log tương ứng: `MMI is not installed`, `Log Tools is not installed`, hoặc `System Settings not installed`. Bộ đối chiếu mới kiểm tra **thứ tự tham chiếu/opcode**, không phải trình phân tích đầy đủ biểu đồ điều khiển (CFG); không suy diễn chắc chắn mọi lỗi runtime đều được bắt.

`PackageUtil.isAppInstall()` gọi `PackageUtil.getPackageInfo()`; hàm này truy vấn `PackageManager.getPackageInfo()`. **Việc gói tồn tại trong danh sách không chứng minh Activity được bật, exported, có quyền mở hoặc hoạt động.** Gói bị disable có thể vẫn xuất hiện trong `pm path` hoặc metadata.

## Điểm riêng của Log Tools

- Đây **không** phải một Activity nằm trong package GlocalmeHome: launcher định tuyến sang package `com.ucloudlink.feedback`.
- Snapshot thu thập tính năng ẩn ngày 19/11/2026 ghi nhận `com.ucloudlink.feedback` ở danh sách package bị vô hiệu hóa. **Đó là trạng thái tại thời điểm snapshot**, không chứng minh hiện nay nó vẫn tắt.
- Video thiết bị ngày 23/11/2026 cho thấy màn hình Log Tools với `Open Android log`, `Open Modem log`, `Modem cfg`. Không có bằng chứng từ video rằng chế độ thu log đã được bật; không suy luận mức độ an toàn của các công tắc.
- Bộ APK 8 gói đã lưu trong RAR nghiên cứu **không chứa APK của Feedback**. Vì chưa có bytecode gói này, chưa thể kết luận tác dụng cụ thể của `Modem cfg` hoặc các nút bật log. Không tự kích hoạt hay thay đổi cấu hình.

## Công cụ và hướng khảo sát an toàn

- `tools/inspect_assistant_routes.py`: đọc *bản APK riêng của chủ sở hữu*, trích đúng tên gói, Activity và chuỗi gọi trong `classes.dex`, không viết DEX ra đĩa và không truy cập mạng.
- `tools/h01-assistant-readonly-win7.cmd`: tương thích CMD Windows 7, thu `pm path`, danh sách gói bị vô hiệu hóa **đã lọc**, một số dòng `dumpsys package` và Activity foreground; **không** gọi `su`, `pm enable`, `am start`, `logcat`, `settings put` hay các lệnh flash.
- Xem [hướng dẫn Windows 7](../tools/assistant-readonly-win7.md).

## Tình trạng và ưu tiên

**Đã hoàn tất:** định danh ba Activity đích từ DEX và đường giao diện `MiniAboutActivity → AssistantActivity → MMI.MainActivity` từ video/ADB. **Còn thiếu:** mã gốc `com.ucloudlink.feedback.LogSettingActivity`, kiểm thử trạng thái gói hiện tại, quyền/exported của Activity và tác dụng `Modem cfg`. Không cần thêm H01 khác cho các bước này.

**Không thực hiện khi chưa có phương án phục hồi:** bật log modem liên tục, bật ADB ROOT / USB Test Mode, sửa cấu hình modem, AgingTest, AutoReboot hoặc Factory Reset. Không công bố APK/DEX OEM, IMEI, SIM và log chưa ẩn danh.
