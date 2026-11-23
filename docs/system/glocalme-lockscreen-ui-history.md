# H01 — màn LockSet của GlocalmeHome: PASS giao diện, PIN chưa thử

**Nguồn:** [Notion mốc khóa PIN và tương phản cao (19/11/2026)](https://app.notion.com/p/41dc5d5277a98195a387cbc89b6c1a81). **Trạng thái: UI PASS, PIN/Pattern/Swipe tự động CHƯA PASS, nhánh đã tạm dừng.**

## Mốc thử ghi trong hồ sơ

| Mốc | Kết quả |
| --- | --- |
| Gọi Activity ban đầu | `Error type 3`; package GlocalmeHome tồn tại nhưng `hidden=true` cho User 0 |
| Kiểm tra quyền | Shell thường không đủ `MANAGE_USERS` để bỏ ẩn |
| Bỏ ẩn trong phiên thử bằng root | Package chuyển sang `hidden=false`; **PASS** |
| Mở `com.glocalme.basic.lock.set.LockSetActivity` | `am start` báo Status ok, tiêu đề **Lock screen** xuất hiện |
| UI hierarchy | Nút **Change** tồn tại nhưng disabled; nút **Enable** enabled/clickable |
| High contrast text | Nhãn Change/Enable xuất hiện rõ; công cụ v1.1 hoàn nguyên setting ban đầu sau thử |

Màn Lock screen ban đầu có chữ đen trên nền tối, vì vậy tưởng như giao diện trống. Sau bật **High contrast text** tạm thời, hai nhãn trở nên đọc được. Đây là một vấn đề **tương phản văn bản**, không chứng minh trình đặt PIN hoạt động.

## Phân biệt các mức chứng cứ

- **VERIFIED trên H01:** Package không còn ẩn trong lượt thử, Activity mở, cây UI thấy hai nút, High contrast text cải thiện chữ.
- **CHƯA THỬ:** bấm Enable hoàn chỉnh, tạo/đổi/xác thực PIN, khóa sau bật/tắt màn, khôi phục khi quên PIN hoặc vận hành sau reboot.
- **RỦI RO:** GlocalmeHome cũng khai báo Activity HOME, thay trạng thái hidden có thể ảnh hưởng launcher; nhóm có bản ghi crash [BackKeyManager](backkeymanager-lock-crash.md) khi mở trực tiếp đường khóa.

Người dùng đã yêu cầu **tạm dừng nhánh thực nghiệm khóa màn hình**, không được tự tiếp tục tác động thiết bị. Không đưa lệnh xóa locksettings, đặt PIN hoặc flash APK lên GitHub chỉ vì lưu hồ sơ. Xem [phân tích Keyguard](keyguard-framework-vdex-ucloud-sleep.md).