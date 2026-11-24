# H01 — 37 mục Notion H171–H207: launcher, root, IME, xoay và Share Server

**Nguồn duy nhất:** [Notion tổng H01, H171–H207](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), diễn biến đã lưu tháng 11/2026. Đây là báo cáo **theo thời gian và mức bằng chứng**, không công bố ý tưởng/phiên thử phát sinh sau khi ghi Notion. Tách từng bản `BUILD`, `HOST TEST`, `DEVICE PASS`, `REBOOT PASS`; không biến bản vừa đóng gói thành bản đã chạy trên H01.

## H171–H178 — unlock, kế hoạch boot RAM, launcher và giới hạn ghép firmware

| Mục | Phát hiện trong nhật ký | Phân loại |
| --- | --- | --- |
| H171 | Unlock báo PASS trên H01 thử sau reboot; chỉ áp dụng máy/mốc đã ghi, không mặc định máy khác | REPORTED PASS |
| H172 | Sau unlock, kế hoạch kiểm boot RAM ảnh gốc rồi marker trước khi thử Magisk; tại mục này chưa root | PLAN |
| H173 | J2ME Loader 1.8.2 cài và mở giao diện, **chưa xác nhận chạy game JAR** | INSTALL/UI PASS ONLY |
| H174 | KISS Launcher mở giao diện/danh sách app; Home mặc định và mọi launcher action chưa thử đủ | UI PASS / PARTIAL |
| H175 | Đề xuất ưu tiên bổ sung tính năng trên firmware Android 8.1 gốc; thay ROM/GSI vẫn là nghiên cứu | DECISION / NOT TEST PASS |
| H176 | Tạo H01 Home v0.1 có launcher/cử chỉ/quản lý tệp; phát hành bản thử không chứng minh mọi chức năng PASS | BUILD / PROPOSED |
| H177 | H01 Home v0.2 bổ sung LAUNCHER/HOME query, loại mục trùng; kết quả cần ghi theo từng phép thử | BUILD / PARTIAL |
| H178 | Danh mục IMG 42/42 tên phân vùng nhưng thiếu dữ liệu các khoảng ngoài phân vùng; chưa có full restore image | INVENTORY / RESTORE OPEN |

## H179–H191 — root Magisk, thanh điều hướng và FOTA/Feedback

| Mục | Phát hiện trong nhật ký | Phân loại |
| --- | --- | --- |
| H179 | Ảnh cho thấy H01 Home chạy; hướng thử root qua RAM được lên kế hoạch, chưa có `su` PASS tại mục này | UI OBSERVED / ROOT PLAN |
| H180 | Fastboot boot ảnh gốc và ảnh marker qua RAM báo PASS; chưa phải root Magisk hay thay boot cố định | RAM BOOT PASS |
| H181 | Khóa xoay: `user_rotation` không thắng policy ngang của giao diện; thử lớp phủ chỉ là phương án | ORIENTATION DIAGNOSIS |
| H182 | Magisk 31.1 có lỗi unpack, Magisk 30.7 boot RAM/ `su -c id` `uid=0` PASS | ROOT RAM REPORTED PASS |
| H183 | Bật Back/Home/Recents Android gốc trong phiên hiện tại được người thử báo PASS; chưa tự nạp sau boot | NAV TEMP PASS |
| H184 | Chuẩn bị gói root cố định và module thanh phím; host test không phải ghi boot thành công | PREPARATION |
| H185 | Sau thao tác được ghi trong Notion, boot root cố định và Android reboot PASS; module nav chưa được xác nhận ở mốc này | PERSISTENT ROOT REPORTED PASS |
| H186 | Log module sau reboot báo enabled và NavigationBar visible; chưa xác minh mọi thao tác bấm phím lần nữa | MODULE PERSISTENCE PASS |
| H187 | Nghiên cứu vô hiệu hóa/gỡ FOTA và GlocalMe Feedback; đề xuất không đồng nghĩa uninstall | RESEARCH |
| H188 | H01 Home v0.4 thử cài APK qua root; lần đầu bị chặn ở quyền su của ứng dụng, chưa tới PackageManager install | TRIAL FAIL / ROOT DENIED |
| H189 | Sau khi cấp quyền Magisk riêng, H01 Home v0.4 cài APK thử và hiện màn hình thành công | INSTALL REPORTED PASS |
| H190 | Người dùng chốt **chỉ giữ FOTA và Feedback disabled-user; không uninstall**; đổi phạm vi sang đo RAM | USER DECISION |
| H191 | Snapshot RAM: MemTotal 929.480 kB, MemAvailable 549.540 kB; PSS là một lần đo, không có bằng chứng tắt app giúp tăng RAM | RAM OBSERVED / OPTIMIZATION OPEN |

## H192–H197 — tự ẩn thanh phím, IME và khởi động cố định

| Mục | Phát hiện trong nhật ký | Phân loại |
| --- | --- | --- |
| H192 | Đề xuất ẩn thanh điều hướng sau 5 giây, gọi bằng vuốt; không coi điều này đã PASS | RESEARCH / PROPOSED |
| H193 | Hai báo cáo cửa sổ và services.jar/ODEX/VDEX cho thấy giới hạn: không chỉ thay JAR là có patch hoạt động | STATIC/LOG DIAGNOSIS |
| H194 | Dựng thử IME v0.1 và gói kiểm tra; host/synthetic PASS, **chưa có thiết bị PASS tại mốc này** | BUILD / HOST TEST |
| H195 | Đợt kiểm trên H01 cho v0.1 PASS phần kiểm thử, v0.2 được chuẩn bị với phương án hoàn tác | DEVICE PARTIAL PASS |
| H196 | Người thử xác nhận v0.2 PASS trên H01, v0.3 mới đóng gói nhưng chưa PASS ở mốc này | DEVICE v0.2 PASS / v0.3 BUILD |
| H197 | v0.3 được báo PASS sau reboot, giữ policy IME tự ẩn/nạp lại qua module; thông báo chưa xác minh | PERSISTENCE REPORTED PASS |

## H198–H206 — khóa xoay dọc/ngang và các lần sửa lỗi

| Mục | Phát hiện trong nhật ký | Phân loại |
| --- | --- | --- |
| H198 | Rà policy ép ngang ở firmware, giữ IME v0.3; chưa ép dọc PASS chỉ từ phân tích | RESEARCH |
| H199 | Tạo gói xoay dọc tạm v0.1 và rollback, chưa chạy H01 lúc biên soạn mục này | BUILD / NOT TESTED |
| H200 | v0.1 được người dùng xác nhận xoay dọc PASS; tự xoay cảm biến vẫn chưa được chứng minh | PORTRAIT REPORTED PASS |
| H201 | Dựng gói chuyển dọc/ngang thủ công v0.2, host kiểm tra PASS; chưa có kết quả runtime bản v0.2 | BUILD / HOST TEST |
| H202 | v0.2 không xoay theo log, sửa công cụ/đường kiểm thành v0.2.1 | FAIL → FIX |
| H203 | v0.2.1 thử trên H01 được người dùng xác nhận PASS nhưng chỉ là thử tạm, chưa xác nhận giữ sau reboot | TEMPORARY PASS |
| H204 | Dựng gói giữ lựa chọn sau reboot v0.3, chưa đồng nghĩa thiết bị đã PASS | BUILD |
| H205 | Sửa lỗi gói giữ xoay v0.3.1, phân biệt các trạng thái lỗi cũ và lượt cài mới | REGRESSION ANALYSIS |
| H206 | v0.3.1 được người dùng xác nhận hướng dọc 0 và khóa xoay tự nạp sau khởi động lại; các chế độ khác cần kiểm riêng | REBOOT PERSISTENCE REPORTED PASS |

## H207 — Share Server bản ổn định

| Mục | Phát hiện trong nhật ký | Phân loại |
| --- | --- | --- |
| H207 | Share Server H01 v0.1.4 được người dùng xác nhận biểu tượng launcher, gửi/tải tệp hai chiều với iPhone; không suy thử tải bền bỉ 24/7 | REPORTED PASS |

## Ranh giới kỹ thuật đã được Notion làm rõ

**Root không đồng nghĩa tất cả ứng dụng có quyền root.** H188 là lỗi quyền Magisk của H01 Home; sau khi cấp quyền riêng mới có H189 PASS cài APK thử. Mốc Magisk boot RAM H182 cần tách khỏi mốc root cố định H185; phím Android bật tạm H183 cũng phải tách khỏi module nạp sau boot H186.

**Cơ chế giao diện gồm nhiều lớp độc lập.** IME v0.3 (H197) đã được báo PASS nhưng yêu cầu ẩn sau **5 giây bất động** ở H192 không được đồng nhất với tự ẩn khi bàn phím xuất hiện. V0.1 xoay dọc H200 không có nghĩa cảm biến gia tốc đã được phát hiện. Xoay tạm H203 không chứng minh trạng thái giữ qua reboot; chỉ H206 ghi nhận kết quả persistence của v0.3.1 trên thiết bị thử.

**Giới hạn tối ưu RAM.** H190 là quyết định **giữ hai ứng dụng FOTA/Feedback ở trạng thái disabled-user**, không gỡ. Chỉ số `MemAvailable` của H191 đã bao gồm các vùng RAM có thể thu hồi và PSS một tiến trình không phải lượng RAM bảo đảm giải phóng nếu xóa ứng dụng.

**Độ tin cậy của bộ firmware.** H178 ghi nhận thiếu dữ liệu giữa các vùng GPT và thiếu xác minh restore, dù có ứng viên ảnh cho 42/42 phân vùng. Không đánh dấu H01 có factory recovery kit chỉ từ kiểm ZIP/hashes.

## Các báo cáo chuyên sâu đã có

- [Mốc Unlock](../boot/oem-unlock-research.md), [root timeline](../boot/magisk-root-timeline.md), [Magisk versions](../boot/magisk-311-vs-307-boot-compatibility.md), [thanh phím Android](../system/native-navbar-debug-flags-and-persistence.md).
- [H01 Home/J2ME/KISS](../projects/h01-home-versions-and-root-installer-evidence.md), [IME v0.1–v0.3](../system/ime-nav-policy-window-evidence-v01-v03.md), [xoay v0.2–v0.3.1](../system/rotation-v02-v031-regression-evidence.md).
- [Share Server v0.1.4](../projects/share-server-protocol-v014.md), [RAM snapshot](../system/ram-and-package-audit.md), [FOTA & Feedback](../system/fota-feedback-disable-vs-uninstall-final-state.md).

**Chính sách công bố:** không đăng APK/ZIP cài thử chứa nội dung hãng, module Magisk/boot đã patch, private link tệp, mã ký hoặc log serial/IMEI. Danh sách 37 mục được đối chiếu ở **mức kết quả nghiên cứu**, không phải toàn bộ tệp đính kèm và mã gốc đã được phát hành.
