# ZEUS H01 (GlocalMe K1) — quy trình nghiên cứu mở khóa bootloader đã thực hiện

**Phạm vi nguồn: chỉ Notion.** [H101–H116, H142–H171 trong nhật ký tổng H01](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd) và [trang H01 máy B](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2), các lần thử 11–18 và 23–24/11/2026.

**Trạng thái:** **REPORTED PASS** trên hai hồ sơ thiết bị được thử; **không phải quy trình OEM chính thức hoặc lệnh unlock an toàn cho mọi revision**. Hướng dẫn này tách **bước kiểm tra có thể thực hiện chỉ đọc** khỏi **thao tác DEVINFO từng được chấp thuận và đã thực hiện trên máy nghiên cứu**. Tuyệt đối không flash ảnh DEVINFO, ABOOT hoặc boot image lấy từ máy H01 khác.

## 1. Chuẩn bị và điều kiện dừng

- Xác nhận máy là dòng **ZEUS H01 / GlocalMe K1**, Android 8.1, và ghi chính xác build/board. Hai H01 cùng tên sản phẩm **không** tự có cùng boot image hay trạng thái DEVINFO.
- Có kết nối ADB/Fastboot ổn định, đã sao lưu dữ liệu người dùng cùng các phân vùng gốc cần cho rollback, đặc biệt **DEVINFO, ABOOT, BOOT, RECOVERY** của chính máy. Lưu SHA-256 và giữ bản sao bất biến ngoài máy.
- Có cơ chế đọc lại phân vùng, kiểm hash và cứu hộ/EDL đã được chứng minh với **đúng máy**. Nếu không có, **dừng ở bước chỉ đọc**.
- Mở khóa chuẩn có thể **xóa userdata**; thao tác sửa DEVINFO sai có thể khiến máy không boot hoặc mất cấu hình bảo mật. Không dùng tài liệu này để “thử cho biết” trên máy đang chạy ổn định.

## 2. Ghi trạng thái ban đầu (chỉ đọc)

Trên máy tính có ADB/Fastboot và khi H01 đang chạy Android:

```sh
adb devices
adb shell getprop ro.build.display.id
adb shell getprop ro.oem_unlock_supported
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.verifiedbootstate
adb reboot bootloader
fastboot devices
fastboot flashing get_unlock_ability
fastboot oem device-info
fastboot getvar unlocked
```

**Dữ liệu thực tế từ Notion (11/11):** `get_unlock_ability: 1`, `Device unlocked: false`, `Device critical unlocked: true`; trước thao tác unlock Android ghi `flash.locked=1`, `verifiedbootstate=green`. Cờ **cho phép yêu cầu unlock** không phải cờ **đã unlock**. `critical unlocked` là trạng thái khác với main unlock.

## 3. Vì sao các lệnh tiêu chuẩn ngày 14/11 chưa thành công?

Notion H142–H150 ghi nhận thử `fastboot flashing unlock`, `fastboot oem unlock` và nhánh `oem unlock-go`: host có lần báo **OKAY**, thiết bị reset/xóa dữ liệu, **nhưng** trạng thái main sau reboot vẫn `unlocked: no` hoặc `Device unlocked: false`. H01 có đường xác nhận UI/nhánh OEM riêng; một số lần không thấy prompt trên màn hình. Không lặp lệnh ghi/xóa để suy đoán hiệu quả.

**Nguyên tắc xác minh:** phản hồi `OKAY` chỉ xác nhận lệnh được bootloader trả kết quả. **Không đánh dấu PASS** nếu chưa đọc lại trạng thái khóa sau reboot.

## 4. Phương án đã thực sự cho kết quả PASS ngày 17–18/11

Theo mục **H171** của Notion, phân tích tĩnh dump **ABOOT của chính máy** xác định `read_device_info` có **hai nhánh theo nhãn record DEVINFO**:

- `ANDROID-BOOT!`: trong trường hợp metadata cụ thể của H01 thử, nhánh khởi tạo có thể trả main unlock về `0`.
- `GLOCALME-BOOT`: trong bản ABOOT đã kiểm, nhánh riêng thiết lập trạng thái main unlock và critical unlock tương ứng `1`.

**Lịch sử đã thực hiện — không phải thao tác mặc định dành cho độc giả:**

1. Thu **DEVINFO mới từ đúng máy** qua EDL, không dùng bản sao từ máy khác hoặc bản cũ sau khi trạng thái đã thay đổi.
2. So sánh bản mới với ABOOT và GPT đúng máy, kiểm toàn vẹn; phân tích ngoại tuyến quy tắc xử lý record và lập **ảnh ứng viên riêng** chỉ thay nhãn metadata tương ứng. Bản gốc giữ nguyên.
3. Xác nhận phạm vi byte khác nhau bằng công cụ kiểm ngoại tuyến; người thử **đã cho phép riêng** ghi bản ứng viên trên đúng H01.
4. Sau khi ghi DEVINFO, **đọc lại cùng phân vùng qua EDL và đối chiếu SHA-256** bản thử trước khi khởi động. Không coi tiến độ write 100% là đủ bằng chứng.
5. Reset và khởi động Android; đọc `ro.boot.flash.locked` và `ro.boot.verifiedbootstate` trước/sau một lần reboot.

**Kết quả ở H171:** `ro.boot.flash.locked=0` và `verifiedbootstate=orange` cả **trước và sau một lần ADB reboot**. Nhật ký thiết bị B ngày 23–24/11 có đợt readback/unlock riêng được báo PASS; không dùng số LBA, hash, IMG hoặc kết quả của A làm dữ liệu áp dụng cho B.

**Không đưa lệnh `edl.py w` theo một giá trị offset cố định, byte-patch tự động hay ảnh DEVINFO đã sửa vào tài liệu công khai:** đây là thao tác trên metadata khóa boot có rủi ro brick và phụ thuộc biến thể. Notion giữ nhật ký thí nghiệm theo máy; nguồn này **không** xác nhận cách sửa tương tự trên mọi H01. Phần này là **giải thích quy trình thực nghiệm**, không phải hướng dẫn tự động unlock trên máy chưa xác minh.

## 5. Kiểm tra sau thao tác — chỉ đọc

Sau khi máy đã boot trở lại Android, kiểm đúng hai thuộc tính sau, sau đó kiểm lại qua reboot nếu cần lưu chứng cứ:

```sh
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.verifiedbootstate
```

| Kết quả | Diễn giải trong nhật ký H01 |
| --- | --- |
| `1` + `green` | Trạng thái locked ở các phiên trước unlock |
| `0` + `orange` | Trạng thái unlocked được Android báo sau thí nghiệm H171 |
| Cùng cặp `0/orange` sau `adb reboot` | PASS độ bền **qua một lần khởi động lại**, chưa có kết luận factory reset/OTA/cold boot |

Không suy từ `orange` rằng mọi cổng Fastboot flash đều mở hoặc Secure Boot fuse đã tắt. Việc chưa có thử nghiệm restore đầu-cuối vẫn là giới hạn quan trọng.

## 6. Những điều chưa được chứng minh

- Khả năng áp dụng một bản sửa DEVINFO cho **mọi** H01, revision bo mạch hoặc firmware khác.
- Trạng thái unlock qua OTA, factory reset, thay bootloader hoặc nhiều chu kỳ mất điện.
- Quy trình khôi phục máy mất boot hoàn chỉnh.
- Có thể flash tùy ý mọi phân vùng chỉ vì `critical unlocked=true`.

**Liên quan:** [lịch sử thử unlock thất bại](oem-unlock-failed-attempts.md), [mục H142–H170](oem-unlock-h142-h170-evidence-chronology-20261124.md), [mốc unlock PASS](oem-unlock-research.md), [thiết bị B](device-b-unlock-root-evidence.md), [Magisk 30.7](h01-magisk-root-notion-procedure-20261124.md), [chính sách công bố](../research/notion-only-publication-policy-20261124.md).
