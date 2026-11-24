# H01 — đối chiếu theo từng mục H142–H170: OEM Unlock, Fastboot và EDL (14/11/2026)

**Nguồn:** [Notion tổng H01 — H142–H170](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd) và [nghiên cứu unlock đã công bố](oem-unlock-failed-attempts.md). **Mục tiêu:** thay bảng liên kết 29 mục đến một tóm tắt ngắn bằng **truy vết từng kết quả**, giữ chính xác thứ tự thời gian. Đây là báo cáo lịch sử đã lọc; không sao chép bản dump ABOOT/DEVINFO, hash riêng thiết bị, offset vá hoặc thao tác ghi phân vùng.

## 1. Quy ước phân loại

- **HOST COMMAND OKAY**: công cụ Fastboot đã nhận phản hồi thành công; **không đồng nghĩa** trạng thái unlock được thay đổi.
- **DEVICE STATE OBSERVED**: có ảnh/output `getvar`, `device-info` hoặc thuộc tính `ro.boot.*` trong một lần khởi động cụ thể.
- **STATIC ANALYSIS**: đọc cấu trúc ABOOT/handler trong dump; không chứng minh nhánh đã chạy trên thiết bị.
- **PLAN / UNSUPPORTED**: phương án dự kiến hoặc kết luận chưa có readback phù hợp.

## 2. H142–H150 — phản hồi OKAY nhưng main unlock vẫn khóa

| ID | Mục nguồn và kết luận khi đó | Nhãn |
| --- | --- | --- |
| H142 | Lệnh OEM ở 14/11 trả OKAY nhưng máy khởi động lại và Fastboot vẫn báo khóa; có reset/setup sau thao tác | DEVICE STATE OBSERVED: **LOCKED** |
| H143 | Sau reset, `get_unlock_ability=1` và OEM toggle không tự biến thành `unlocked=true` | OBSERVED |
| H144 | Đánh giá các đường unlock khác nhau; lúc đó chỉ là phương án, chưa có PASS | PLAN |
| H145 | Đã phân tích dump bootloader trong kho riêng; bản phân tích tĩnh không tự xác nhận thao tác mở khóa | STATIC ANALYSIS |
| H146 | Nút âm lượng không hoạt động làm đường xác nhận UI trở thành vấn đề; không suy thao tác tự chấp thuận | UI REQUIREMENT / OPEN |
| H147 | Máy Windows 7 nhận phản hồi lệnh Fastboot, nhưng chưa có chứng cứ chuyển main unlock | HOST COMMAND OKAY |
| H148 | Sau lệnh chuẩn không thấy prompt; truy vấn tiếp theo vẫn `unlocked: no` | DEVICE STATE OBSERVED: **LOCKED** |
| H149 | So sánh hai alias lệnh: cùng nhận OKAY; đọc lại trạng thái main vẫn khóa | DEVICE STATE OBSERVED: **LOCKED** |
| H150 | Một lệnh OEM khác trả OKAY, thiết bị boot được; kiểm trạng thái Fastboot sau đó vẫn khóa | DEVICE STATE OBSERVED: **LOCKED** |

**Điểm dễ hiểu sai:** `Device critical unlocked`, `get_unlock_ability` và `Device unlocked` là các điều kiện/trạng thái khác nhau. Không dùng kết quả **OKAY** làm phép đo đầu ra thay cho đọc trạng thái.

## 3. H151–H155 — phân tích ABOOT, handler và cờ FRP

| ID | Kết quả được lưu | Mức bằng chứng |
| --- | --- | --- |
| H151 | Nhận dạng định dạng ELF ARM của bản ABOOT; nghiên cứu lý do handler trả OKAY | STATIC |
| H152 | Đối chiếu mã và chuỗi với một fork Qualcomm LK công khai; **chưa chứng minh** cùng nguồn build hoặc revision | STATIC / SIMILARITY ONLY |
| H153 | Dò bảng lệnh/handler bằng disassembler ngoại tuyến để phân biệt nhánh lệnh | STATIC |
| H154 | So sánh đường in `device-info` với nhánh OEM unlock; các trường báo trạng thái được tách khỏi cờ cho phép | STATIC |
| H155 | Truy nguồn `get_unlock_ability` tới logic đọc FRP/Persistent Data Block; không phải bằng chứng main-unlocked | STATIC + SNAPSHOT |

Nội dung gốc có địa chỉ handler, dải byte và ảnh nhị phân. Bản public này chỉ ghi **vai trò và giới hạn của từng bước**, không phát hành offset/patch có thể dùng nhầm trên H01 khác. Cũng không giả định trùng chuỗi Fastboot đồng nghĩa firmware H01 được build từ một fork LK cụ thể. Xem thêm [boot verifier](boot-verification-chain.md).

## 4. H156–H163 — đối chiếu Android runtime và Fastboot sau thao tác

| ID | Kết quả đúng với thời điểm ghi | Nhãn |
| --- | --- | --- |
| H156 | Sau một lệnh `unlock-go` trả OKAY, ADB nhìn thấy máy đã boot; điều này chỉ chứng minh máy lên Android | ADB OBSERVED |
| H157 | `ro.bootmode` báo `unknown`; build báo thuộc dòng K1 đã nghiên cứu | RUNTIME OBSERVED |
| H158 | Tập thuộc tính boot bổ sung cho thấy Android đang hoạt động; chưa có unlocked PASS | RUNTIME OBSERVED |
| H159 | `ro.boot.flash.locked=1` và `verifiedbootstate=green` ở ảnh 14/11 | **LOCKED AT SNAPSHOT** |
| H160 | Người thử xác nhận dump ABOOT được đọc qua EDL từ chính H01 đang điều tra, không phải mượn từ máy khác | SOURCE PROVENANCE REPORTED |
| H161 | Có lệnh ADB/fastboot nhập không đúng chế độ hoặc dính vào nhau; các dòng đó không được xem là output hợp lệ | COMMAND CONTEXT REVIEW |
| H162 | Lệnh Fastboot được chạy riêng, `product=MSM8909`; kết luận main unlocked vẫn `no` | **LOCKED AT SNAPSHOT** |
| H163 | Thiết bị đã khởi động bình thường; bản đọc Fastboot ở mục trước thuộc phiên cũ | TEMPORAL CLARIFICATION |

**Bài học truy vết:** `adb devices` nhận thiết bị sau reboot **không** xác minh unlock. Phải gắn phép đo `ro.boot.*` hoặc `device-info` với đúng boot/session và không áp kết quả của ảnh chụp cũ lên trạng thái hiện tại.

## 5. H164–H170 — baseline dump, giới hạn QFIL và phân tích handler

| ID | Công việc/kết luận được ghi ở nguồn | Trạng thái |
| --- | --- | --- |
| H164 | Kiểm kê DEVINFO và MISC đã lưu trong kho riêng từ 11/11; chỉ có baseline cũ | FILE INVENTORY |
| H165 | Đề xuất đọc lại DEVINFO/MISC để đối chiếu sau lệnh; **đề xuất không phải kết quả readback** | PLAN |
| H166 | Windows 7 nhận H01 ở Qualcomm 9008 và có phiên thử QFIL; không coi kết nối USB là thành công việc đọc/ghi | HOST OBSERVED / EDL OUTCOME LIMITED |
| H167 | So sánh AOSP quy định `get_unlock_ability` với trạng thái unlock thực tế; vẫn chưa PASS ở mốc này | RESEARCH |
| H168 | Kiểm tra đường dẫn/nguồn EDL, GPT và bản sao ABOOT/ABOOTBAK, ghi giới hạn provenance | SOURCE CROSS-CHECK |
| H169 | Kiểm tra trực tiếp cấu trúc và tính toàn vẹn một dump ABOOT được cung cấp | FILE STATIC VERIFIED |
| H170 | Lần dấu luồng handler và UI xác nhận ở disassembly; lý giải vì sao OKAY không đủ | STATIC ANALYSIS |

Các ghi chép về QFIL, EDL, FRP và bootloader nhằm **giải thích kết quả**, không phải công thức sửa metadata. Không đăng file programmer, patch DEVINFO, địa chỉ binary, chuỗi lệnh ghi hoặc các định danh được trích trong log.

## 6. Mốc về sau: H171 mới có PASS

**H171 (17–18/11/2026)** ghi nhận kết quả khác hẳn: sau quy trình riêng được chủ thiết bị chấp thuận, H01 báo `ro.boot.flash.locked=0`, `verifiedbootstate=orange` và giữ trạng thái này qua một lần reboot. Kết quả đó **không làm H142–H170 sai**; nó chỉ thuộc **thời điểm sau**. Không ngoại suy rằng unlock giữ qua factory reset/OTA hoặc mọi revision. [Báo cáo unlock](oem-unlock-research.md), [Magisk root](magisk-root-timeline.md).

## 7. Phần vẫn chưa được đánh dấu hoàn tất

Đây là **29 mục đã được đối chiếu ở cấp ý chính và thứ tự bằng chứng**, không phải kiểm kê byte-for-byte tất cả ảnh/video/TXT của 29 mục. Một số ảnh CMD, file ABOOT/DEVINFO và checksum trong nguồn là dữ liệu riêng hoặc binary OEM, nên cố ý không chuyển vào GitHub. Những điều còn mở gồm kết quả lâu dài sau cập nhật/reset, khả năng dùng Fastboot flash cho mọi phân vùng và quy trình phục hồi an toàn đầu-cuối.

**Điểm chốt:** lệnh `OKAY` ≠ unlocked; trạng thái main `locked` ngày **14/11** ≠ kết quả `unlocked` ngày **18/11**. Chỉ kết luận trên **đúng máy, đúng boot, đúng nguồn chứng cứ**.
