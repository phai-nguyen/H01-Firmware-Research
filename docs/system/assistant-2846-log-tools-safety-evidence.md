# H01 2846 — ba nhánh Assistant Function và trạng thái Log Tools

**Nguồn:** [Notion — Mã 2846 và Log Tools, cập nhật 23/11/2026](https://app.notion.com/p/421c5d5277a98192b864cbdb37b94203). **APK STATIC VERIFIED; Log Tools được nhìn thấy trên màn hình, chưa kích hoạt chế độ ghi.**

## Đường đi từ About đã giải mã và quan sát

Trong `GlocalmeHome.apk` gốc, nhấn **Version No. 5 lần** ở `MiniAboutActivity` làm xuất hiện dialog; `MiniAboutActivity$5.onClick()` so mã `2846` trong EditText, rồi đi theo ARouter `/minilauncher/assistant`. Đây là đường trực tiếp qua **launcher OEM**, độc lập với `MMI.MySecretCodeReceiver` có host 2846 trong VDEX.

Tại `AssistantActivity`, ba callback kiểm tra package trước khi gọi Activity đích:

| Nút | Callback | Activity đích |
| --- | --- | --- |
| MMI | `startMMI(View)` | `com.ukelink.dusk.mmi.MainActivity` |
| Log Tools | `startLogTools(View)` | `com.ucloudlink.feedback.LogSettingActivity` |
| System Settings | `startSystemSettings(View)` | `com.android.settings.Settings` |

Bộ phân tích APK gốc đã xác nhận **3/3 route** ở mức static, còn **6/6 unit test Python synthetic** đạt. Những kết quả này **không chứng minh** tất cả package đang enabled hoặc Activity mở được trong runtime.

## Kết quả Log Tools

Trong video H01, màn Log Tools hiển thị **Open Android log**, **Open Modem log** và **Modem cfg**. Người dùng chưa bật các công tắc đó trong nhánh này, vì vậy **không có bằng chứng logger/diag modem đã bật hoặc đã lưu dữ liệu thành công**.

Danh sách package ngày 19/11 từng cho thấy `com.ucloudlink.feedback` bị disable; đây là **snapshot cũ**. Nghiên cứu tĩnh gói GlocalmeHome đã tìm ra component đích, nhưng bộ **8 APK cũ chưa có bytecode Feedback `LogSettingActivity`**, nên chưa thể đánh giá side effect của từng công tắc.

## Ranh giới

Chỉ công bố giao diện/route và giới hạn; không đưa lệnh gửi secret-code broadcast, bật modem diag/log, `ADB ROOT`, USB Test Mode hoặc Factory Reset. Không coi một app nguồn gốc OEM được cài là quyền được tự động thử mọi tính năng có tác dụng thay đổi trạng thái.

Tham khảo [trang 2846](glocalmehome-about-secret-code-2846.md), [MMI Receiver](mmi-secret-code-receiver.md), [UCloud Feedback](package-install-and-fota-feedback.md).