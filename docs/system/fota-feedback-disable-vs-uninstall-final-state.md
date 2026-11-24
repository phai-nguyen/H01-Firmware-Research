# H01 — FOTA và Feedback: từng đề xuất gỡ, nhưng trạng thái cuối là disabled-user

**Nguồn:** [Notion tổng H01 H187–H191, tháng 11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Có bằng chứng package-state runtime**, không thực hiện lệnh mới trong đợt đăng tài liệu.

| Mốc | Diễn biến chính |
| --- | --- |
| H187 | Nhận diện `com.abupdate.fota_demo_iot` (FOTA) và `com.ucloudlink.feedback` (Feedback). Bàn phương án disable trước, gỡ user 0 chỉ khi cần |
| H188 | Ảnh CMD xác nhận hai package **disabled-user** và chưa uninstall |
| H189 | H01 Home v0.4 đã cài APK thử thành công; có đề xuất gỡ ứng dụng riêng user 0, **chưa có bằng chứng thực thi** |
| H190 | Người dùng **chọn chỉ giữ disable, không tiếp tục gỡ hai package** |
| H191 | `installed=true`, `enabled=3` ở cả hai gói; FOTA không thấy tiến trình, Feedback có tiến trình khoảng **3.070 kB PSS** |

APK FOTA ở `/system/app/FOTA/FOTA.apk`, Feedback ở `/system/app/GlocalMeFeedback/GlocalMeFeedback.apk`. Log cũ ghi Feedback có UID **1000** và **LocalLogService**, nhưng **không đủ để kết luận nó gửi dữ liệu ra bên ngoài**.

## Phân biệt ba thao tác

- **disable-user:** ứng dụng vẫn installed nhưng user state disabled.
- **uninstall riêng user 0:** khác với disable; APK trong system vẫn tồn tại, chưa có bằng chứng đã làm tại mốc này.
- **xóa APK trong /system:** không được người dùng chọn, không thể giả định là cách tối ưu RAM an toàn.

Feedback vẫn có process theo snapshot dù `enabled=3`; điều đó **không tự chứng minh disable thất bại**, vì package user-state khác vòng đời dịch vụ persistent/UID system. Không coi 3 MiB PSS là bộ nhớ chắc chắn giải phóng bằng cách gỡ APK.

**Vấn đề còn mở:** không có before/after RAM khi gỡ vì **không gỡ**, không có thử nghiệm đầy đủ ảnh hưởng của hai package lên 4G/SIM/hotspot. Vô hiệu hóa FOTA **không có nghĩa các đường UService APK/binary update cũng đã dừng**.

Không đăng lệnh gỡ, log cá nhân, định danh SIM, APK OEM hoặc yêu cầu thay đổi thiết bị. Xem [lịch sử PackageManager](package-install-and-fota-feedback.md), [đo RAM](ram-and-package-audit.md), [ba cơ chế update](uservice-update-control-plane-v16.md).