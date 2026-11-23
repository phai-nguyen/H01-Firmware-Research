# H01 — lỗi BackKeyManager làm GlocalmeHome phục hồi Activity

**Nguồn:** [Notion BackKeyManager (19/11/2026)](https://app.notion.com/p/41dc5d5277a98151bda6fc8ec359addd), log GlocalmeHome đã đối chiếu cùng DEX `classes.dex/classes2.dex/classes3.dex`. **Trạng thái: crash stack VERIFIED, giả thuyết khởi tạo chưa xác minh hoàn toàn.**

## Lỗi và chuỗi ứng dụng

Một `NullPointerException` xảy ra tại:

```text
BackKeyManager.monitor(BackKeyManager.java:83)
BaseActivity.onStop(BaseActivity.java:230)
```

Lỗi là cuộc gọi `android.os.Handler.sendMessage(Message)` trên đối tượng Handler **null**. Có **5 lần cùng dấu vết** trong log ngày 19/11/2026: một lần ở `LockSetActivity`, bốn lần ở `LockScreenActivity` theo bảng đối chiếu.

Phân tích DEX tìm:

| Phương thức | Quan sát |
| --- | --- |
| `BackKeyManager.setup()` | Tạo Handler và gán vào trường |
| `InitManager.init()` | Có đường gọi `BackKeyManager.setup()` |
| `BaseActivity.onResume()/onStop()` | Có đường gọi `BackKeyManager.monitor()` |
| `BackKeyManager.monitor()` | Ở nhánh cập nhật Back, gọi `handler.sendMessage()` không check null |
| `GlocalmeExceptionHandler.uncaughtException()` | Có đường phục hồi mở `InitActivity` |

**Giả thuyết có căn cứ:** gọi thẳng LockScreenActivity khi GlocalmeHome khởi tạo chưa đủ đã bỏ qua `InitManager.init()`, khiến Handler null khi Activity Stop. Phần Handler null là **bằng chứng lỗi trực tiếp**, còn lý do chưa setup **chưa được chứng minh bằng trace đầy đủ**.

## Hệ quả điều hướng

Exception handler có thể đưa GlocalmeHome qua `InitActivity` lên foreground, lấn lên Launcher3. Không được diễn giải sự xuất hiện GlocalmeHome sau crash là người dùng cố ý chuyển Home.

Trong một mốc hoạt động được báo cáo PASS, log có chuỗi `LockScreenActivity.onCreate` → `BackKeyManager.hide` → `UnlockLayout.unlock` → Activity destroy → `BackKeyManager.show`, **không có crash ở lần đó**. Điều này chỉ cho biết một phiên có thể qua luồng khóa, không chứng minh ổn định qua reboot hoặc tự khóa mặc định.

## Điều chưa làm

Không vá APK để thêm check null hoặc ép gọi setup; không tắt exception handler toàn cục; không sửa gói GlocalmeHome bằng cách chép đè APK khác chữ ký. Không trích log gốc vì chứa ID thiết bị/nhật ký nhạy cảm.

Xem [khóa OEM và Android](keyguard-framework-vdex-ucloud-sleep.md), [UI LockSet](glocalme-lockscreen-ui-history.md).