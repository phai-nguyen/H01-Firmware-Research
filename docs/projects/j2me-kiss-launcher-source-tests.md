# H01 — thực nghiệm J2ME Loader 1.8.2 và KISS Launcher v3.27.1

**Nguồn:** [Notion tổng H01, H173–H174 — các mục “Cài J2ME Loader” và “Nghiên cứu launcher”](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Mức chứng cứ: APK INSTALL/UI PASS, chạy game Java JAR và HOME-default chưa kiểm.**

## J2ME Loader: hạn chế OEM không phải UserManager

Tại thời điểm đầu thử:

- User 0 `RUNNING_UNLOCKED`, restrictions/effective restrictions đều `none`; device managed `false`.
- `install_non_market_apps=1` nhưng vẫn có cổng PackageManager OEM.
- `mAllowInstallWhiteList` ghi `com.glocalme.appstore`, `com.ucloudlink.base.installservice`, `android.uid.system:1000` và `android.uid.phone:1001`.
- Lượt `adb install` ban đầu có `installerPackageName=null`, `slavePkgName=ru.playsoftware.j2meloader`, `allowInstall=false`, lỗi **Not allow install app by user!**.

Sau khi sử dụng **tên nguồn cài InstallService được OEM cho phép**, nhật ký ghi ADB install **Success**, không cần root hoặc sửa framework. Tên nguồn cài là **metadata của yêu cầu**, không chuyển UID shell thành UID của InstallService, không miễn trừ chữ ký APK và cũng không chứng minh mọi APK đều sẽ được chấp nhận.

Lệnh khởi chạy theo MAIN/LAUNCHER trong mốc đó trả **unable to resolve Intent**, trong khi mở **component `ru.playsoftware.j2meloader/.MainActivity`** thành công. Ảnh thực tế chỉ hiện J2ME Loader với **“No data”**: chưa có bằng chứng một JAR đã import/chạy hoặc phát âm thanh.

## KISS Launcher v3.27.1

| Dữ liệu tại nguồn phiên bản | Quan sát |
| --- | --- |
| Package / Activity | `fr.neamar.kiss`, `.MainActivity` |
| APK phát hành | **2.203.978 byte**, khoảng 2,10 MiB |
| Android tối thiểu | API 21 (Android 5.0) trong `app/build.gradle` tại tag |
| Manifest | Có HOME, DEFAULT, LAUNCHER; Activity exported |
| UI source | Có cơ chế mở danh sách ứng dụng và thanh cuộn theo chữ cái |
| Video H01 | **Giao diện KISS mở, cảm ứng và danh sách cuộn được** |

Video khoảng **43,87 giây**: từ khoảng giây 28–35 thấy **Settings, Phone, J2ME Loader** và ít nhất một mục GlocalMe bị che một phần. Do đó ảnh cũ chỉ hiện một icon **không phải bằng chứng Android chỉ có một ứng dụng**.

**Chưa chứng minh:** mọi ứng dụng trong danh sách mở thành công, launcher đã được đặt HOME mặc định, giữ trạng thái qua reboot hoặc tự truy cập được toàn bộ dịch vụ 4G/SIM gốc. Có thể khác biệt giữa package có MAIN/LAUNCHER và Activity mở trực tiếp.

## Ranh giới nghiên cứu

Hai phép thử ứng dụng đạt khi H01 còn giữ firmware Android 8.1 ban đầu, không phải bằng chứng cần thay ROM/GSI hoặc gỡ UService để cài APK. Không sao chép APK của bên thứ ba hay video có thông tin cá nhân lên repository. Nội dung chỉ lưu **lịch sử test đã có**, không tạo gói cài mới.

Xem [launcher/J2ME overview](launcher-and-j2me-history.md) và [cơ chế package install](../system/package-install-and-fota-feedback.md).