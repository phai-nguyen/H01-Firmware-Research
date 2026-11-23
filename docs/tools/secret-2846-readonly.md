# Thu thập bằng chứng menu 2846 — Windows 7, chỉ đọc

## Mục đích

So sánh màn hình Activity đang xuất hiện **trước và sau** khi chủ thiết bị **tự** nhập mã `2846` trong `GlocalmeHome > About`. Không tự gửi mã bí mật, không mở menu kỹ thuật bằng lệnh, không đổi cấu hình trên H01.

## Chuẩn bị

- Windows 7 SP1, USB ADB đã ủy quyền và **chỉ một H01** đang kết nối.
- Chép [`tools/h01-2846-readonly-win7.cmd`](../../tools/h01-2846-readonly-win7.cmd) vào `C:3\platform-tools` (cùng `adb.exe`).
- GlocalmeHome có thể truy cập được theo thao tác thường ngày trên H01. **Không** dùng `pm unhide` hoặc `pm enable` nếu ứng dụng hiện bị ẩn; đó là thao tác thay đổi trạng thái ngoài phạm vi kiểm tra này.

## Thực hiện

```bat
cd /d C:3\platform-tools
h01-2846-readonly-win7.cmd
```

Công cụ ghi thông tin package và Activity trước khi nhập mã, sau đó tạm dừng. Trên **màn hình H01**, vào GlocalmeHome → About → nhập `2846` theo cách anh đã sử dụng và dừng tại màn hình xuất hiện. Trên máy tính nhấn phím bất kỳ để ghi lại trạng thái.

Kết quả lưu trong thư mục `H01-2846-RESULTS`:

| Tệp | Nội dung |
| --- | --- |
| `01-build-packages.txt` | Phiên bản firmware và vị trí của ba APK |
| `02-component-lines.txt` | Những dòng PackageManager liên quan mã, receiver, MainActivity và About |
| `03-before.txt` | Activity liên quan đến ba package trước khi nhập mã |
| `04-after.txt` | Activity liên quan sau khi nhập mã |

Dữ liệu lọc có thể vẫn chứa đường dẫn, tên Activity hoặc thành phần không mong muốn. **Rà soát thủ công trước khi gửi hoặc đăng GitHub.** Không gửi logcat đầy đủ, ảnh có IMEI/ICCID/IMSI, số điện thoại hay mật khẩu.

## Kết luận có thể rút ra

- Nếu `04-after.txt` có `com.ukelink.dusk.mmi/.MainActivity` là Activity đang foreground, đó là bằng chứng MMI được đưa lên khi nhập mã.
- Nếu xuất hiện Activity GlocalmeHome, có thể menu vẫn là màn hình trong launcher; cần ảnh/ghi chép để xác định.
- Nếu không thấy dòng nào, đó **không chứng minh** receiver hoặc menu không tồn tại: bản Android có thể có định dạng `dumpsys` khác hoặc Activity không nằm ở foreground thời điểm đọc.
- **Không** thể kết luận trực tiếp rằng `MySecretCodeReceiver.onReceive()` gọi MainActivity từ các dòng Activity. Muốn kết luận cần mã phương thức hoặc log intent được kiểm tra.

## Giới hạn an toàn

Script chỉ sử dụng `getprop`, `pm path`, `dumpsys package`, `dumpsys activity activities` và `findstr` phía Windows. Không yêu cầu root, không thực thi chức năng MMI. Người dùng chủ động truy cập giao diện trên H01, không chọn nút USB Test Mode, ADB ROOT, AutoReboot, Factory Reset hoặc AgingTest.
