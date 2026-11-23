# Khảo sát J2ME Loader, KISS Launcher và H01 Home

**Nguồn:** Notion H01 các mục 62–66 (vòng nghiên cứu ứng dụng tháng 11/2026) và các mốc H01 Home 0.4 sau đó. **Phân loại:** phân tích chính sách cài package, kiểm chứng giao diện bằng ảnh/video và lịch sử phát triển.

## Tại sao APK không cài theo cách thông thường?

Trong báo cáo ban đầu, `install_non_market_apps=1` nhưng `PackageManager` vẫn chặn một phiên ADB với thông báo `Not allow install app by user!`. Log cho thấy tên nguồn cài `installerPackageName=null` và một whitelist OEM có các package cài đặt được phép.

Thử `adb install -i com.ucloudlink.base.installservice` trong nhật ký trả **Success**. Đây là đường cài thông qua tên nguồn đã được firmware cho phép, **không phải bằng chứng mở toàn bộ khóa cài đặt cho mọi app**.

## J2ME Loader

- Đã cài thành công ứng dụng J2ME Loader lên H01.
- Lệnh mở qua Intent MAIN/LAUNCHER có trường hợp `unable to resolve Intent`; mở trực tiếp `MainActivity` thành công.
- Ảnh H01 cho thấy giao diện ứng dụng với “No data”. **Chưa kết luận trò chơi JAR đã chạy hoặc game có âm thanh** chỉ từ bước mở giao diện.

## KISS Launcher

Video H01 xác nhận KISS Launcher mở được danh sách có Settings, Phone, J2ME Loader và ứng dụng khác, cuộn/cảm ứng hoạt động. Không coi ảnh ban đầu chỉ hiện một icon là bằng chứng Android chỉ có một ứng dụng. Chưa chứng minh KISS đã được đặt HOME mặc định hay mọi ứng dụng đều có thể mở.

## H01 Home: các mốc v0.1 → v0.4

| Phiên bản | Trọng tâm | Kết quả trong hồ sơ |
| --- | --- | --- |
| v0.1 | Launcher, cử chỉ, quản lý tệp | Biên dịch và kiểm tra trên Android 8.1 mô phỏng; **chưa có PASS trên H01 thật ở mốc này** |
| v0.2 | Liệt kê cả Activity LAUNCHER và HOME, mở giao diện GlocalMe | APK xây dựng/kiểm tra cấu trúc đạt; không tự kết luận đã đổi HOME mặc định |
| v0.3 | Luồng chọn tệp hỗ trợ ứng dụng khác như Magisk | Được dùng trong nhánh chuẩn bị root; cần đối chiếu riêng từng phép thử |
| v0.4 | Xem/chọn APK và cài qua Magisk root, giữ luồng cài đặt có xác nhận | **Người dùng xác nhận cài mới và mở ứng dụng thử thành công** sau khi cấp quyền root cho H01 Home |

## Giới hạn cần ghi lại

H01 Home không phải ROM tùy biến, không có nghĩa thay GlocalmeHome an toàn hoặc cho phép cài APK khác chữ ký/split APK. Gỡ các dịch vụ mạng của hãng có thể ảnh hưởng SIM/hotspot. Đã từng cân nhắc thay system bằng ROM/GSI; hồ sơ thời điểm đó **không xác định được bản ROM đã kiểm chứng dành riêng H01/K1**, nên tiếp tục nghiên cứu mod từng chức năng trên firmware gốc.

APK gốc, binary bên thứ ba và khóa ký không được đăng trong báo cáo này; đây chỉ là lịch sử nghiên cứu.