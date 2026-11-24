# H01 Home v0.1 → v0.4 — kiến trúc, thử nghiệm và đường cài APK qua Magisk

**Nguồn:** [Nhật ký Notion tổng H01, H176–H177 và H188–H189](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), các mốc 17–18/11/2026. **Phân biệt BUILD/HOST TEST, DEVICE PASS và lỗi cấp root**.

## Tính năng theo từng bản

| Bản | Thay đổi đáng chú ý | Phạm vi kiểm chứng |
| --- | --- | --- |
| **0.1** | Launcher dạng lưới, tìm kiếm Activity, cử chỉ Back/Home/Recents bằng Accessibility Service, quản lý tệp dùng content URI | **Android 8.1 x86 emulator và kiểm tra logic PASS; H01 thật chưa thử ở mốc này** |
| **0.2** | Hợp nhất Activity `LAUNCHER` và `HOME`, giữ category HOME khi gọi giao diện OEM, thêm nút mở GlocalMe/Home khác; giữ cùng khóa ký | **Build/manifest/checks PASS**, chưa có phép thử H01 cụ thể của bản này |
| **0.3** | Thêm luồng để chuyển APK qua ứng dụng khác, chuẩn bị cài quyền root | Có sử dụng trong nhánh chuẩn bị; không có xác nhận mọi tình huống hoạt động |
| **0.4** | Trang chọn và xem thông tin APK; chỉ sau khi xác nhận mới yêu cầu Magisk root để cài | **REPORTED PASS cài và mở app thử** sau khi giải quyết quyền Superuser |

### Kiến trúc bản 0.1

Nguồn ghi **41.497 byte**; `vn.h01.home`, minSDK **23**, targetSDK **27**, Java thuần, không có native libs hay Internet permission. Các kiểm tra v1/v2 signature, zipalign, ZIP CRC và logic cử chỉ/file operations đạt. Thử trên emulator Android 8.1 x86 với APK đúng hash bản phát hành; Activity mở và service trợ năng bind.

Emulator từng xuất hiện **SystemUI ANR**, nên nhóm tạm disable SystemUI **chỉ ở emulator** trong một bước chẩn đoán. **Không có** mốc thực hiện thao tác này trên H01 thật. Các kết quả emulator không chứng minh thao tác Recents/touch trên H01 hay độ ổn định modem/hotspot.

### Bản 0.2 không “tự thay thế” GlocalMeHome

Mục `HOME` trong Manifest và câu lệnh mở Activity có thể đưa giao diện OEM lên foreground; **không** mặc nhiên thay HOME mặc định hoặc thay đổi logic 4G/Wi-Fi. Bản 0.2 có `versionCode=2` và cùng signing identity với 0.1, có khả năng cập nhật đè khi môi trường cài cho phép. Bộ kiểm tra H01 của nhánh này chỉ đọc HOME/LAUNCHER, màn hình/density/build/package và trạng thái trợ năng.

## Bản 0.4: lý do ban đầu thất bại

Bản 0.4 có kích thước **49.689 byte**, versionCode **4**, minSDK 23/targetSDK 27. Video kiểm thử đầu hiển thị APK thử `vn.h01.installtest`, tên, phiên bản và dung lượng **8,59 KB** — đường đọc tệp và trình phân tích package **PASS**. Nhưng sau bấm **Cài bằng root**, Magisk hiện Superuser request cho **`vn.h01.home`**, bị từ chối/timeout và báo **Permission denied**. Shell đã được cấp root trước đó **không đồng nghĩa** H01 Home có quyền root.

Sau khi chủ thiết bị cấp quyền riêng cho H01 Home, ảnh và phản hồi xác nhận đã cài mới và mở ứng dụng `vn.h01.installtest` với thông báo **“Cài APK đã thành công”**. Vì vậy timeline phải ghi rõ **lần đầu FAIL do quyền**, **lần sau PASS cài một APK mẫu**.

## Các ràng buộc được thiết kế

- Trình cài phân tích APK và tính hash trước khi yêu cầu người dùng xác nhận; chỉ thao tác cài thực tế mới gọi `su`.
- Dữ liệu được chép vào vùng tạm root có tên ngẫu nhiên; kiểm lại kích thước/hash, không chèn tên file người dùng thẳng vào lệnh shell.
- Sử dụng `pm install` với tên nguồn OEM `com.ucloudlink.base.installservice`, **không vô hiệu hóa kiểm tra chữ ký Android**.
- Báo lỗi riêng với thiếu root, app khác chữ ký, ABI/minSDK, package downgrade, dung lượng hoặc timeout.
- Chỉ APK **đơn** tối đa **256 MiB**; không hỗ trợ APKS/XAPK/split, không dùng `pm clear`, không tự uninstall.
- Host mock test không phải thực nghiệm SELinux/Magisk thật; sự xác nhận trên H01 chỉ là lượt cài app thử thành công.

**Chưa có bằng chứng:** cài update mọi APK OEM, khắc phục mismatch signature, cài APKS/XAPK, chạy hoàn chỉnh từ Amaze, nâng cấp H01 Home bằng chính nó hoặc chạy sau factory reset.

Không đăng APK/ZIP có signing identity riêng, khóa ký, script root với đường dẫn máy, tệp gốc OEM hoặc log chứa dữ liệu cá nhân. Xem [bản tổng quan H01 Home](h01-home-installer.md) và [cổng cài OEM](../system/package-install-and-fota-feedback.md).