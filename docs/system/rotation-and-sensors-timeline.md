# Nghiên cứu xoay màn hình và cảm biến H01 — chuỗi v0.1 đến v0.3.1

**Nguồn:** nhật ký Notion H01, các mục “Hướng xoay dọc: xác định khóa trong firmware”, “Xoay dọc v0.1 PASS”, “Chuyển dọc/ngang thủ công v0.2”, “v0.2.1 đã PASS”, “Sửa gói v0.3.1” và “Hoàn tất kiểm chứng khóa xoay”. **Phân loại: bytecode STATIC VERIFIED + kết quả thử H01 theo từng mốc.**

## Vì sao ứng dụng không tự xoay đúng mong muốn?

H01 có các nhánh OEM nhận diện `Build.MODEL=K1` trong `DisplayContent` và `Build.PRODUCT=K1` trong `StatusBarWindowManager`, ép orientation `8` (ngang theo chính sách thiết bị). Do đó chỉ sửa `user_rotation` hoặc yêu cầu một app dọc có thể bị bỏ qua. Đây là hai lớp can thiệp khác nhau trong services và SystemUI.

## Khảo sát cảm biến

`dumpsys sensorservice` của H01 ghi **No Sensors on the device** dù `PackageManager` khai báo một số sensor feature, và service HAL cảm biến có trạng thái running. Trong logic `WindowOrientationListener`, `mSensor=null` khi không lấy được sensor mặc định. **Điều được xác minh là Android không công bố cảm biến tự xoay trong snapshot này**, không được khẳng định PCB chắc chắn không gắn phần cứng cảm biến.

Vì vậy các mốc sau ưu tiên **chọn khóa dọc/ngang thủ công**, không phụ thuộc tự xoay theo gia tốc.

## Dòng thời gian thử nghiệm

| Giai đoạn | Thử nghiệm | Kết quả |
| --- | --- | --- |
| v0.1 | Đổi nhánh trả hướng K1 trong services ở chế độ thử tạm; UI 240×320 và chính sách dọc được quan sát | **Người dùng xác nhận PASS trên H01**, chưa phải bản giữ qua reboot |
| v0.2 | Controller chuyển dọc/ngang, thêm probe | **Chưa PASS**: preflight gặp lỗi môi trường JNI `SystemProperties.native_get_boolean` |
| v0.2.1 | Chuyển probe sang môi trường AndroidRuntime phù hợp, controller chuyển theo USER rotation | **PASS trên H01**: dọc ↔ ngang, mở launcher/cài đặt, hiển thị menu trò chơi trong video |
| v0.3 | Đóng gói cơ chế cố định lựa chọn qua boot | Có lỗi trạng thái và áp dụng settings; **chưa PASS** |
| v0.3.1 | Sửa luồng kiểm tra và áp dụng settings sau boot; module được báo sửa, xác minh boot mới | **PASS sau reboot**: `MODE=persistent`, `NEXT_BOOT_ENABLED=true`, `ACCELEROMETER_ROTATION=0`, `USER_ROTATION=0`, khung dọc 240×320 |

Các video một phần chỉ chứng minh có thể chuyển hướng và mở giao diện được quay; không xác nhận toàn bộ game, SIM/hotspot hoặc ứng dụng khác đều tương thích.

## Kết luận và giới hạn

Đã có bằng chứng **khóa hướng dọc thủ công và áp dụng lại sau một lần reboot** trên H01 được thử. Chưa có bằng chứng hoạt động qua pin cạn, mất điện nhiều lần, mọi Activity bên thứ ba hoặc cảm biến tự xoay vật lý. Phần bảng thông báo trong nhánh tự ẩn navigation còn hoãn.

Không phát hành JAR framework OEM đã chỉnh sửa, nội dung APK hệ thống hoặc script thay thế mù lên repo công khai. Xem [tổng quan xoay/IME](display-rotation-navigation.md) và [nhật ký thanh điều hướng](ime-navigation-research-timeline.md).