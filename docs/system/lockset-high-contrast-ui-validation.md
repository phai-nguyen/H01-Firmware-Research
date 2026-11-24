# H01 — LockSetActivity, trạng thái hidden và thử High Contrast Text

**Nguồn:** [Notion — mốc PIN 19/11/2026](https://app.notion.com/p/41dc5d5277a98195a387cbc89b6c1a81), mục 1–2 và cập nhật lỗi khi thoát màn hình. **Kết quả: UI PASS, khóa PIN chưa kiểm thử, nhánh từng được chủ thiết bị yêu cầu tạm dừng.**

## Lần thử trên Android 8.1

Ban đầu gọi `com.glocalme.g4home/com.glocalme.basic.lock.set.LockSetActivity` báo **Error type 3 — Activity class does not exist**. Đây không đủ kết luận APK thiếu class: `dumpsys package` cùng phiên ghi `installed=true`, `hidden=true`, `enabled=0` ở User 0.

Lần thử dùng ADB shell thông thường để bỏ ẩn thất bại vì thiếu `MANAGE_USERS`. Khi người dùng dùng Magisk root trong phiên khảo sát, Package Manager trả **hidden=false**. Activity lúc đó khởi động `Status: ok`; H01 hiển thị tiêu đề **Lock screen**.

**Không được hiểu:** việc hiển thị menu nghĩa đã có màn khóa PIN hoạt động khi tắt/bật màn.

## Chứng cứ về thành phần UI

Đầu ra `uiautomator dump` và các ảnh chụp trong hồ sơ ghi:

| Thành phần | Trạng thái khi chưa bật PIN |
| --- | --- |
| `tv_modify` / **Change** | Có trong UI, `enabled=false` |
| `tv_enable` / **Enable** | Có trong UI, `enabled=true`, `clickable=true` |
| Tiêu đề | **Lock screen**, hiển thị đúng |
| Nhãn hai nút | Chữ tối trên nền tối, rất khó quan sát |

Bật tạm **High contrast text** bằng bộ kiểm thử Windows v1.1 giúp nhãn **Change/Enable hiện trắng, viền đen**, không làm hỏng bố cục. Công cụ v1.0 từng lỗi không tìm thấy `adb.exe` là lỗi host, không phải firmware. Video bản v1.1 ghi **5/5 Completed**, hoàn nguyên tùy chọn về `null` (giá trị trước thử).

## Điều không được suy diễn

- Chưa bấm hoàn tất Enable, chưa tạo/đổi/xác thực mã PIN và chưa đo khóa qua reboot/sleep.
- Chưa xác định cơ chế khôi phục khi quên PIN. Không đăng bất cứ script xóa khóa hoặc sửa system package.
- Việc bỏ ẩn package launcher có thể ảnh hưởng ưu tiên HOME; và nghiên cứu khác ghi crash **`BackKeyManager.monitor()` gọi `Handler.sendMessage()` khi Handler null** trong nhánh LockScreen.
- Ghi chú “tạm dừng” là trạng thái nghiên cứu PIN tại thời điểm lưu; lịch sử dự án sau đó có nhánh phân tích khóa vuốt, **không đồng nghĩa PIN tự động đã PASS**.

**Liên quan:** [UI LockSet tổng quan](glocalme-lockscreen-ui-history.md), [BackKeyManager](backkeymanager-lock-crash.md), [Keyguard](keyguard-framework-vdex-ucloud-sleep.md).

Tài liệu này chỉ lưu bằng chứng; không thay trạng thái launcher, PIN hoặc High contrast trên máy hiện tại.