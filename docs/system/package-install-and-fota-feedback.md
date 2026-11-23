# Cơ chế hạn chế cài APK và trạng thái FOTA/Feedback

**Nguồn:** Notion H01, mục cài J2ME Loader, mục “Nghiên cứu gỡ FOTA và GlocalMe Feedback”, “H01 Home 0.4” và “Đổi phạm vi: giữ disable”. **Phân loại: static VERIFIED + các phiên thử package state trên H01, không thực hiện thay đổi mới trong lần biên soạn.**

## Cơ chế từ PackageManagerService

Phân tích `services_classes.dex` của firmware ghi nhận nhánh OEM `allowInstallPackageAsUser(installerPackageName, slavePkgName)`. Nhánh này phụ thuộc dạng build, whitelist cài đặt và trường hợp ứng dụng đích đã tồn tại. Nếu không được cho phép, trong `installPackageLI` có thể trả mã `-115` với thông báo **Not allow install app by user!**.

Trong snapshot ADB, danh sách tên nguồn được cho phép gồm `com.glocalme.appstore`, `com.ucloudlink.base.installservice` và một số UID hệ thống/điện thoại. Thử cài J2ME Loader qua nguồn InstallService và thử cài APK từ H01 Home có kết quả riêng: xem [lịch sử ứng dụng](../projects/launcher-and-j2me-history.md). **Không** suy ra việc tắt kiểm tra chữ ký, không sửa whitelist hoặc thay framework chỉ dựa vào log này.

## FOTA và Feedback

Hồ sơ phân biệt **disable-user** với **uninstall for user 0**:

- Ở snapshot sau thao tác cũ, FOTA (`com.abupdate.fota_demo_iot`) và Feedback (`com.ucloudlink.feedback`) còn installed, nhưng trạng thái cho user 0 là `enabled=3` (*disabled-user*).
- Một đề xuất gỡ riêng user 0 xuất hiện sau khi H01 Home v0.4 cài được APK, nhưng **người dùng sau đó quyết định giữ hai app ở trạng thái disabled**, không tiếp tục gỡ. Không ghi các lệnh uninstall trong tài liệu cũ thành hành động đã thực thi.
- Trong snapshot RAM sau đó, FOTA không thấy tiến trình chạy; một process thuộc UID system vẫn xuất hiện liên quan Feedback ở mức PSS nhỏ. Điều này **không tự chứng minh** Package Manager disable thất bại vì APK hệ thống và process persistent có thể tách biệt.

## Khuyến nghị nghiên cứu lưu trữ

Không giả định các package OEM có thể xóa an toàn. Giữ các thành phần mạng/SIM, `UService`, `InstallService`, GlocalmeHome, Android Phone/SystemUI và module đang PASS; không tắt hàng loạt chỉ từ tên APK. Các mốc tắt/gỡ phải có before/after từ chính thiết bị, theo [báo cáo RAM](ram-and-package-audit.md).

**Không có thay đổi package hoặc root nào được thực thi trong đợt đăng GitHub này.**