# H01 — bảng đối chiếu nguồn Notion chuyên đề (24/11/2026)

**Phạm vi:** 17 trang H01 được trả về khi tìm kiếm theo từ khóa "H01" trong Notion, gồm **1 trang tổng với 207 đề mục** và **16 trang chuyên đề**. Đây là kết quả tìm kiếm tại thời điểm khảo sát, **không xác nhận đã tìm được mọi tài liệu H01 trong toàn bộ workspace**.

Bảng dưới đây cho biết **đã có báo cáo GitHub liên quan** cho từng trang, **không có nghĩa toàn văn trang và mọi đính kèm đã được chuyển**. Báo cáo công khai là bản biên soạn, giữ nguyên các cấp độ VERIFIED / REPORTED PASS / OPEN và tình trạng đã tạm dừng khi phù hợp.

| # | Trang nghiên cứu nguồn | Báo cáo GitHub liên quan |
| ---: | --- | --- |
| 1 | [Tự khởi động USB-C / LK / charger](https://app.notion.com/p/41ec5d5277a9815799c4d61fba41a3ea) | [Xem tài liệu](../boot/auto-power-on-cold-boot-evidence.md) |
| 2 | [Biểu tượng 4G slot 0 / SystemUI](https://app.notion.com/p/41ec5d5277a9813fbeebe77a1c3617f2) | [Xem tài liệu](../system/4g-slot0-systemui-evidence.md) |
| 3 | [AudioTrack / ALSA / Audio HAL](https://app.notion.com/p/41fc5d5277a9814eb9e5f4324e25fba9) | [Xem tài liệu](../system/audio-playback-test-matrix-20261121.md) |
| 4 | [Sao lưu boot / tái sử dụng cấu hình](https://app.notion.com/p/41ec5d5277a98103978ce6392e948073) | [Xem tài liệu](../firmware/boot-image-reuse-limitations.md) |
| 5 | [PIN LockSet / High contrast text](https://app.notion.com/p/41dc5d5277a98195a387cbc89b6c1a81) | [Xem chi tiết](../system/lockset-high-contrast-ui-validation.md) |
| 6 | [OTA / Recovery / server cache / v16](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df) | [Xem tài liệu](../firmware/ota-server-cache-v15-evidence.md) |
| 7 | [Mã kỹ thuật 2846 / Log Tools](https://app.notion.com/p/421c5d5277a98192b864cbdb37b94203) | [Xem tài liệu](../system/assistant-2846-log-tools-safety-evidence.md) |
| 8 | [Nhật ký tổng (207 đề mục)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd) | [Xem tài liệu](../research/notion-207-routing-map.md) |
| 9 | [Launcher3 AutoHotspot v0.4](https://app.notion.com/p/41ec5d5277a98185ac4cfc7813f9f8cf) | [Xem tài liệu](../projects/autohotspot-api-history.md) |
| 10 | [Chức năng ẩn / manifest / DEX](https://app.notion.com/p/41dc5d5277a981db8ad1fff1aca10bc5) | [Xem tài liệu](../system/hidden-scanner-parser-failure-and-recovery.md) |
| 11 | [H01 máy B / Magisk / IME / xoay](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2) | [Xem tài liệu](../research/h01-device-b-comparison-20261124.md) |
| 12 | [SMS / TelephonyProvider](https://app.notion.com/p/41dc5d5277a9814993b1e337bb0d8aa6) | [Xem tài liệu](../network/sms-telephony-permission-evidence.md) |
| 13 | [Dual SIM / PCB / RIL](https://app.notion.com/p/41ec5d5277a9811a916cc87d0bac9d3b) | [Xem tài liệu](../network/dual-sim-ril-pcb-evidence.md) |
| 14 | [Android Keyguard / SystemUI](https://app.notion.com/p/41ec5d5277a9815e9ab9ee60633cfa9b) | [Xem tài liệu](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| 15 | [Keyguard mặc định bị vô hiệu hóa](https://app.notion.com/p/41ec5d5277a981879644efda02037161) | [Xem tài liệu](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| 16 | [Crash BackKeyManager/LockScreen](https://app.notion.com/p/41dc5d5277a98151bda6fc8ec359addd) | [Xem tài liệu](../system/backkeymanager-lock-crash.md) |
| 17 | [UCloud Keyguard / K1,K2 / sleep](https://app.notion.com/p/41ec5d5277a981feaf8ede50c6148510) | [Xem tài liệu](../system/keyguard-framework-vdex-ucloud-sleep.md) |

## Báo cáo chéo từ cùng nguồn

- Trang **OTA** còn có [dấu vết bản cũ trong Recovery và phân loại xác thực OTA](../firmware/ota-recovery-version-trace-and-trust-levels.md). Lịch sử nhận gói 81→87 không phải thông báo có cập nhật mới cho build 87 đang chạy.
- Trang **PIN LockSet** được ghi cụ thể tại [báo cáo High Contrast](../system/lockset-high-contrast-ui-validation.md), không chuyển từ PASS giao diện thành PASS khóa PIN.

## Phần chưa thể kết luận hoàn tất

- **Notion:** 207/207 đề mục tổng đã có trong chỉ mục; mỗi mục có một tuyến liên kết báo cáo liên quan, không phải 207/207 bài đã biên soạn hết.
- **Trang chuyên đề:** 16/16 trang tìm thấy đã có ít nhất một bản tóm tắt công khai liên quan; nhiều trang có nhiều phần, tài liệu gốc, ảnh, tệp TXT hoặc RAR chưa được đối chiếu hết ở cấp chứng cứ.
- **Dropbox/đính kèm:** đã đọc chọn lọc các TXT kỹ thuật; toàn bộ các bản sao ảnh eMMC, firmware OEM, log nhạy cảm và dữ liệu SIM không thuộc nội dung công khai.
- **Chất lượng:** hiệu lực firmware, runtime thực tế và khả năng phục hồi phải phân biệt rõ với kết luận chỉ đọc bytecode, manifest hoặc hash.

**Tiêu chí để đánh dấu một mục là đã di chuyển đầy đủ:** đã đọc đủ phần nguồn và những đính kèm dùng làm chứng cứ, xác minh mốc PASS/FAIL có kế thừa đúng theo thời gian, đối chiếu báo cáo công khai bao quát các kết luận chính, và kiểm tra không rò rỉ thông tin riêng. Hiện **chưa có đánh giá hoàn tất 100% theo tiêu chí này**.

Tham khảo [bảng 207 mục](notion-207-routing-map.md), [coverage](notion-coverage.md), [backlog](publication-backlog.md), [chính sách công bố](../security/publication-policy.md).
