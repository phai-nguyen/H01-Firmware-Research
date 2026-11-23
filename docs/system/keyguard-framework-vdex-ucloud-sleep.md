# H01 — Android Keyguard và nhánh khóa UCloud khi tắt màn hình

**Nguồn:** [Notion framework Keyguard](https://app.notion.com/p/41ec5d5277a981879644efda02037161), [phân tích SystemUI VDEX](https://app.notion.com/p/41ec5d5277a9815e9ab9ee60633cfa9b) và [nhánh sleep/K1](https://app.notion.com/p/41ec5d5277a981feaf8ede50c6148510), 20/11/2026. **Trạng thái: static VERIFIED; Swipe/PIN chưa thử hoạt động đầu-cuối.**

## Framework và runtime

Từ `framework-res.apk`:

| Resource | Giá trị được xác minh |
| --- | --- |
| `config_disableLockscreenByDefault` | **true** |
| `config_keyguardComponent` | `com.android.systemui.keyguard.KeyguardService` |
| `config_ucloud_lockscreen_cls` | `com.glocalme.basic.lock.LockScreenActivity` |

Snapshot `dumpsys window policy` khi H01 đang sáng có `deviceHasKeyguard=true`, `enabled=true`, `showing=false`. `locksettings set-disabled false` báo chấp nhận nhưng `get-disabled` vẫn trả **true**. Có giao diện Security với None/Swipe/Pattern/PIN/Password **không chứng minh khóa tự xuất hiện**.

## SystemUI VDEX

Bản VDEX 010 gốc có một DEX 037; `KeyguardViewMediator.doKeyguardLocked(Bundle)` chỉ có một code unit `0x0073` (return-void-no-barrier), tương đương **trả về ngay**. Nhánh `doKeyguardLockedWhenSimIsPinPukState(Bundle)` vẫn có logic, nên không được kết luận toàn bộ SIM PIN/PUK đã bị xóa.

VDEX còn lệnh ART quickening, không phải source Java nguyên bản có thể build/flash trực tiếp. Không đồng nhất `config_disableLockscreenByDefault` với việc doKeyguardLocked bị thay, vì đây là **hai lớp giới hạn độc lập**.

## UCloud/GlocalMe khi bắt đầu sleep

Trong `KeyguardViewMediator` có `enableUcloudLockScreen()`, `startUcloudLockscreen()` và các trường theo dõi UCloud Home/LockScreen.

`enableUcloudLockScreen()` đọc `ro.product.model`, so sánh với `K1` và đảo boolean. Mã tương đương nhiều khả năng là `!K1.equals(model)`, nhưng tham chiếu gọi virtual đã quicken, **chưa khôi phục tuyệt đối**.

`KeyguardViewMediator$4.handleMessage` nhánh 17 tương ứng **NOTIFY_STARTED_GOING_TO_SLEEP**, không phải `SCREEN_ON`. Nếu điều kiện cho phép, logic đặt lịch `postDelayed()` với **50 ms hoặc 200 ms**, có kiểm tra uptime mốc **180.000 ms**. Task `KeyguardViewMediator$4$1.run()` gọi slot vtable 51; **chưa chứng minh** slot đó chính xác là `startUcloudLockscreen()`.

Tham số boolean đi từ `KeyguardService$1.onStartedGoingToSleep(int,boolean)` tới `KeyguardViewMediator.onStartedGoingToSleep(int,boolean)`, được ghi vào quick field offset `0xB4`; tên field vẫn cần xác minh.

## Trạng thái thực tế và giới hạn

- **VERIFIED:** default lockscreen disabled trong resources; stub `doKeyguardLocked`; nhánh riêng UCloud; logic sleep với điều kiện K1.
- **NOT VERIFIED:** tác vụ tự mở khóa vuốt OEM đã chạy được trên K1, call-target slot 51, Swipe tự xuất hiện khi sáng màn hình.
- **NOT DONE:** flash/patch SystemUI, services.jar, framework-res; đặt PIN/Pattern/Password; thay model.

Không nhầm một UI khóa vuốt với bảo mật khóa màn hình. Xem [tổng quan](keyguard-and-lockscreen.md) và [crash BackKeyManager](backkeymanager-lock-crash.md).