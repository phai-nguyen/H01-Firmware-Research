# H01 — phân biệt lỗi probe v0.2, xoay tay v0.2.1 và lỗi startup v0.3.1

**Nguồn:** [Notion tổng H01, H198–H206](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Lịch sử lỗi/PASS theo mốc**; không phải gói sửa framework mới.

## Phân tích ban đầu: cờ ép ngang K1

Bytecode `DisplayContent$NonAppWindowContainers.getOrientation()` có nhánh cho model `K1` trả orientation **8** (hướng ngang). `StatusBarWindowManager` còn có hai nhánh OEM dùng `Build.PRODUCT=K1`. Vì vậy đổi mỗi `user_rotation=0` không vượt được yêu cầu từ policy/framework. Trên snapshot H01, `dumpsys sensorservice` ghi **No Sensors on the device**, mặc dù PackageManager khai báo accelerometer/compass/gyro/light/proximity. Có `sensors-hal` running **không chứng minh cảm biến hoạt động**.

## Từ ép dọc sang quyền chọn USER

- **v0.1:** thử tạm hướng dọc **240×320** với app orientation 1; candidate JAR được nạp sau preflight, người dùng xác nhận **PASS dọc**. Đây không phải lựa chọn dọc/ngang hoặc persistence.
- **v0.2:** đưa orientation về policy **USER=2**, app `vn.h01.rotation` chọn dọc `user_rotation=0` hoặc ngang `user_rotation=3`, khóa auto-rotate khi chọn. Nhưng bước kiểm **chưa hoàn thành**.
- **v0.2.1:** giữ APK/candidate framework của v0.2, sửa **môi trường probe** để dùng `app_process` (AndroidRuntime có đăng ký JNI) thay vì bare `dalvikvm`.

## Lỗi v0.2 không phải lỗi xoay live

Báo cáo v0.2 dừng trước ART verify/mount/timer vì `UnsatisfiedLinkError` trên `android.os.SystemProperties.native_get_boolean`. Static initializer của `WindowOrientationListener` trong probe cần JNI AndroidRuntime, nhưng tiến trình bare dalvikvm chưa nạp. **Không có bằng chứng candidate USER=2 đã nạp mà không xoay**.

Bản v0.2.1 sau sửa đã ghi **2.587 assertions PASS** cho mỗi probe baseline/candidate, DEX2OAT exit 0, candidate được nạp tạm và zygote restart. Ảnh H01 cho thấy có thể chọn dọc/ngang, mở launcher/cài đặt/bảng thông báo, nhìn thấy menu Diamond Rush trong J2ME. **Không suy ra toàn bộ game/playback đã được kiểm**.

## v0.3 cố định: hai lỗi khác nhau

1. Các lượt cài v0.3 đầu dừng với `Use old trial file3 to restore settings first`, vì trạng thái thử cũ cần được xử lý. Đây là **điều kiện bảo vệ**; candidate chưa nạp ở các lượt dừng.
2. Sau khi đã vào một **boot khác**, trạng thái `MODE=awaiting_boot_confirmation`, JAR candidate đã live, orientation USER=2, nhưng service không ghi ready vì `settings` qua Binder trả **Failed transaction (2147483646)**. Đây là **lỗi áp dụng setting ở đường service lúc boot**, không phải lỗi ROOT/JAR/mất quyền. Chưa đủ bằng chứng chỉ đích danh SELinux hay fd leak là nguyên nhân cấp thấp.

## v0.3.1 sửa đường áp dụng và xác nhận sau reboot

Bản sửa giữ nguyên APK và JAR so với v0.3, thay cách service gọi controller và thu stdout/stderr qua pipe thay vì truyền trực tiếp file descriptor log riêng; thêm kiểm `settings` trả về đúng giá trị và retry có giới hạn. Đây là giải pháp được **ghi là đã thử**, không suy ra mọi lỗi Binder đều do FD.

| Mốc | Kết quả trong hồ sơ |
| --- | --- |
| Cài sửa | Đã sửa module hiện có; báo cần reboot |
| Sau boot thử | `H01_ROTATION_SERVICE_READY`, `LOCKED_ROTATION=0`, áp thành công ngay lần đầu |
| Xác nhận | `H01_ROTATION_FIXED_CONFIRMED` |
| Boot kế tiếp | `MODE=persistent`, `NEXT_BOOT_ENABLED=true`, `BOOT_COMPLETED=1` |
| Trạng thái hướng sau reboot | `ACCELEROMETER_ROTATION=0`, `USER_ROTATION=0`, **240×320**, orientation USER=2 |

**Giới hạn:** xác nhận khóa dọc đã giữ qua reboot và chuyển hướng tay trên mẫu H01 thử; chưa có phép thử khi pin cạn, mất nguồn kéo dài, cảm biến tự xoay thật, mọi game/ứng dụng hoặc nhánh bảng thông báo.

Không phát hành framework JAR/DEX, APK OEM đã sửa, khóa ký, module riêng, byte patch/offset hay thao tác flash. Xem [timeline xoay](rotation-and-sensors-timeline.md), [máy B](device-b-rotation-evidence.md).