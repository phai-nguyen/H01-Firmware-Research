# H01 — OEM Unlock: các lệnh Fastboot OKAY nhưng vẫn locked (14/11), rồi PASS (17–18/11)

**Nguồn trực tiếp:** [Notion nhật ký H142–H172](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), các mốc 14–18/11/2026. **Lịch sử điều tra đã hoàn tất trong hồ sơ**, không khuyến nghị thực hiện lại lệnh unlock, can thiệp ABOOT/DEVINFO hay bỏ qua xác minh trên thiết bị mới.

## Diễn biến theo thời gian

| Mốc | Kết quả | Điều đã chứng minh |
| --- | --- | --- |
| Trước 14/11 | `fastboot flashing get_unlock_ability=1`; `Device unlocked=false`; `Device critical unlocked=true` | Quyền **yêu cầu** mở khóa có, main unlocked **chưa có** |
| 14/11 | `fastboot oem unlock`, `oem unlock-go` đều trả **OKAY**; thiết bị về setup sau Recovery wipe | Lệnh được tiếp nhận, có xóa dữ liệu |
| 14/11 sau khởi động | `fastboot getvar unlocked: no`, `device-info unlocked=false`, `get_unlock_ability=1` | **Main unlock FAILED** dù OKAY |
| Phân tích ABOOT 14–17/11 | Nhận diện handler/các nhánh device-info OEM khác đường Android chuẩn | Cơ chế kiểm tra/cờ persistent **khác với suy luận ban đầu** |
| 17–18/11 | Báo cáo bản ghi/thử nghiệm riêng có xác nhận chủ máy và readback | **Bằng chứng trên H01**, không phải chỉ mô phỏng |
| 18/11 sau Android reboot | `ro.boot.flash.locked=0`, `verifiedbootstate=orange` vẫn giữ | **REPORTED PASS** trên máy được thử |

**Không đảo ngược thứ tự:** câu “vẫn locked” ở 14/11 là đúng **cho phiên trước**, không phải kết luận cho mốc sau 18/11. `Critical unlocked=true` **không đồng nghĩa main unlocked=true**.

## Call graph và các điểm dễ hiểu sai

Trong bản ABOOT phân tích, alias `oem unlock` và `flashing unlock` có cùng handler; `oem unlock-go` đi qua nhánh khác. Luồng callback chuẩn có đường gọi **UI xác nhận**, điều này giải thích vì sao cần phân biệt yêu cầu unlock, prompt, xác nhận và ghi trạng thái. Một số ảnh/video lúc đó chưa xuất hiện prompt vì thiết bị có vấn đề phím âm lượng; không được coi im lặng ở màn hình là giao thức tự động chấp thuận.

Cờ `get_unlock_ability` liên quan FRP/Persistent Data Block `config`, không phải trường main-unlocked trong `devinfo`. Android 8.1 kiểm cờ và digest của vùng Persistent Data Block theo luật riêng. Chỉnh cờ/getprop ngoài luồng hoặc giữ metadata không nhất quán có thể làm thay đổi dữ liệu/khóa thiết bị.

Phân tích muộn tìm hai nhánh diễn giải trạng thái device-info OEM, giải thích việc chỉ sửa một cờ mà giữ metadata khác **không được giữ trạng thái unlock**. Không công bố offset/byte thay đổi, image DEVINFO thử, hoặc lệnh ghi thực nghiệm, bởi đây là phương pháp thay thế metadata bootloader có rủi ro brick, xóa dữ liệu và sai khác giữa board.

## Bằng chứng và giới hạn

Bản ghi 18/11 có **readback từ eMMC** phù hợp ảnh thử đã được chủ sở hữu cho phép, sau đó Android báo `0/orange` cả trước và sau reboot. Chưa chứng minh giữ trạng thái sau factory reset/OTA, chưa xác minh mọi Fastboot flash gate đã mở, chưa thử trên mọi revision khác. Một hồ sơ H01 khác ngày 23–24/11 cũng có kết quả unlock/root riêng, được ghi ở [máy B](device-b-unlock-root-evidence.md), không trộn dữ liệu giữa hai máy.

**Tài liệu liên quan:** [khái quát OEM Unlock](oem-unlock-research.md), [Root](magisk-root-timeline.md), [ABOOT verifier](boot-verification-chain.md). Không đăng binary, khóa, DEVINFO hoặc trace chứa định danh.