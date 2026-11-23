# H01 máy B — DPI, Launcher3, thanh điều hướng và IME AutoHide

**Nguồn:** Notion “H01 MÁY MỚI #2”, mục 8–9, 23–24/11/2026. **Bằng chứng runtime PASS có giới hạn**.

## DPI và Launcher

DPI mặc định H01 ở hồ sơ cũ là **160**, còn máy B đã sử dụng `wm density 120` để dễ thao tác Magisk trên màn hình nhỏ. Đây chỉ là **đổi tỷ lệ hiển thị**, không phải mở khóa hướng xoay hay bằng chứng ứng dụng chỉnh DPI đã được phát hành.

Báo cáo có `Launcher3.apk` trong `/system/priv-app` nhưng chưa hiện trong danh sách Launcher/Activity ban đầu. Việc thử cài lại APK system đã strip DEX gây lỗi `INVALID_APK`. Sau đặt **hai thuộc tính hệ thống qua một module Magisk** và reboot, Launcher3 đã xuất hiện trong bộ chọn HOME. Vì dùng hai thuộc tính đồng thời, **chưa biết riêng thuộc tính nào tạo khác biệt**. H01 Home thực tế đã cài/mở là bản **v0.4**, không phải v0.2 trong hướng dẫn cũ.

## Thanh phím và IME

Thanh Android **Back/Home/Recents** được xác nhận xuất hiện. Thiết lập `immersive.navigation=*` ẩn thanh trong launcher/app, nhưng thanh lại hiện khi IME mở; đó là lý do nghiên cứu nhánh IME riêng.

| Mốc IME | Kết quả |
| --- | --- |
| Host mock | 20 bài kiểm thử PASS, **không phải kiểm chứng trên Android thật** |
| `first_boot_trial` | Khi mở bàn phím, `mForcingShowNavBar=true` nhưng `NavigationBar=WINDOW_STATE_HIDDEN`; người dùng xác nhận ẩn/gọi lại thanh phím **PASS** |
| Báo cáo `trang-thai(1)/(2)` sau commit | Vẫn là **boot ID cũ**, không chứng minh đã reboot |
| Báo cáo mới sau reboot | **Boot ID khác**, `MODE=persistent`, `NEXT_BOOT_ENABLED=true`, service và JAR đúng bản — **PASS persistence** |

`NEXT_BOOT_ENABLED=false` ở first-boot trial là hành vi an toàn có chủ đích, không phải lỗi. Snapshot mới ở chế độ persistent đang focus Launcher3, **không chụp lúc bàn phím đang mở**. Bằng chứng IME PASS và module còn sau reboot thuộc **hai phép quan sát khác nhau**.

Nhánh bảng thông báo còn chưa xử lý; chưa xác minh “ẩn sau 5 giây” với mọi Activity. Không đăng JAR/ODEX/VDEX đã vá, Magisk module hoặc file có định danh. Xem [xoay B](device-b-rotation-evidence.md), [IME A](ime-navigation-research-timeline.md).