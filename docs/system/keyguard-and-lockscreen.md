# Android Keyguard và khóa OEM GlocalmeHome

**Trạng thái: STATIC VERIFIED / UI PARTIAL — PIN và Swipe đã tạm dừng, chưa PASS.**

### Hai cơ chế song song

1. Framework Android H01: trong `framework-res.apk`, `config_disableLockscreenByDefault=true`; `config_keyguardComponent` trỏ tới `SystemUI KeyguardService`.
2. Khóa riêng UCloud/GlocalMe: `config_ucloud_lockscreen_cls` tham chiếu `com.glocalme.basic.lock.LockScreenActivity`; VDEX SystemUI có `enableUcloudLockScreen()` và `startUcloudLockscreen()`.

Phân tích SystemUI VDEX cho thấy `KeyguardViewMediator.doKeyguardLocked(Bundle)` có một lệnh `return-void-no-barrier`, phù hợp việc bỏ qua khóa tiêu chuẩn. **Nhánh SIM PIN/PUK khác vẫn tồn tại**; không kết luận toàn bộ Keyguard bị xóa. Một số lời gọi bị ART quickening, nên nhánh điều kiện model K1 chưa được khôi phục hoàn toàn.

### Thực nghiệm và lỗi

- Màn hình khóa OEM đã mở được trên H01, chứa nút **Change** và **Enable**; **High contrast text** giúp đọc nhãn.
- `locksettings set-disabled false` từng báo nhận lệnh nhưng `get-disabled` vẫn `true`; không chứng minh đã bật khóa.
- Nhật ký ghi `NullPointerException` tại `BackKeyManager.monitor()` khi `BaseActivity.onStop()` gọi `Handler.sendMessage()` trên đối tượng chưa khởi tạo. Có giả thuyết luồng mở trực tiếp bỏ qua `InitManager.init()`; nguyên nhân này **chưa được chứng minh tuyệt đối**.
- **Chưa đặt hoặc thử PIN, Pattern, Password, khóa Swipe tự động**, chưa sửa SystemUI/framework.

Không xóa `locksettings.db`, không thay APK/JAR hệ thống, không bật PIN khi chưa có đường cứu hộ được kiểm chứng.

**Nguồn:** Notion các trang “Android Keyguard: config_disableLockscreenByDefault”, “Phân tích sâu SystemUI”, “UCloud Keyguard và sleep”, “Mốc khóa màn hình PIN” và “BackKeyManager NullPointerException” (19–20/11/2026).