# H01 — kiểm toán 16 trang Notion chuyên đề (chỉ công bố nội dung đã ghi)

**Nguồn duy nhất:** [Trang tổng H01 trên Notion](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd) và **16 trang chuyên đề con được tìm thấy khi tìm từ khóa H01, kiểm lại ngày 24/11/2026**. Danh sách này là phạm vi tìm kiếm hiện có, **không** chứng minh toàn workspace Notion không còn trang H01 khác. Không trích xuất IMG/APK/đính kèm riêng và không công bố kết quả chỉ mới xuất hiện trong cuộc trò chuyện nhưng **chưa ghi vào Notion**.

## Từng trang nguồn và kết quả đã được Notion ghi lại

| # | Trang Notion | Kết quả có thể công bố | Báo cáo chi tiết trên GitHub |
| ---: | --- | --- | --- |
| 1 | [Tự khởi động USB-C](https://app.notion.com/p/41ec5d5277a9815799c4d61fba41a3ea) | Auto Power-On v0.6 qua cold USB-C, AutoHotspot v0.4, 4G AutoShow v1.1 đều được người thử báo PASS trong một chuỗi boot; không chứng minh vận hành không pin hay lâu dài | [Báo cáo Auto Power-On](../boot/auto-power-on-cold-boot-evidence.md) |
| 2 | [Biểu tượng 4G SIM 1](https://app.notion.com/p/41ec5d5277a9813fbeebe77a1c3617f2) | One-shot AutoShow v1.1 đặt cờ slot0 sau boot; icon và cờ trong log được ghi PASS; không khẳng định sửa được mọi trường hợp RIL | [4G slot0](../system/4g-slot0-systemui-evidence.md) |
| 3 | [Âm thanh/ALSA/Audio HAL](https://app.notion.com/p/41fc5d5277a9814eb9e5f4324e25fba9) | AudioTrack/HAL lỗi; âm thanh H01 chưa PASS; Sound Device Tree báo disabled, chưa có patch boot và test phát tiếng được xác minh | [Audio matrix](../system/audio-playback-test-matrix-20261121.md) |
| 4 | [Sao lưu boot và dùng cho H01 khác](https://app.notion.com/p/41ec5d5277a98103978ce6392e948073) | Boot đã vá Magisk không chứa tất cả tùy biến app/module; chỉ là một thành phần, không phải factory firmware hay bản sao toàn máy | [Giới hạn boot reuse](../firmware/boot-image-reuse-limitations.md) |
| 5 | [PIN LockSet / tương phản cao](https://app.notion.com/p/41dc5d5277a98195a387cbc89b6c1a81) | Menu khóa/PIN và High Contrast UI từng mở PASS, nhưng PIN/Swipe ngủ–thức–reboot chưa có PASS; nhiều nhánh tạm dừng | [High Contrast](../system/lockset-high-contrast-ui-validation.md) |
| 6 | [OTA, cache, firmware nguồn](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df) | Đã kiểm gói incremental 81→87 và chữ ký trong phạm vi báo cáo; `data.sha256` máy chủ còn chưa giải thích; cache v15 là host thử, chưa có factory ROM | [OTA V10](../firmware/ota-delta-validation-v10.md) |
| 7 | [Mã 2846/Assistant Function](https://app.notion.com/p/421c5d5277a98192b864cbdb37b94203) | Tuyến About → Assistant Function → MMI được xác nhận bằng ADB/video; Log Tools chỉ quan sát giao diện, không kích hoạt modem log/cfg | [MMI 2846](../system/glocalmehome-about-secret-code-2846.md) |
| 9 | [Launcher3 AutoHotspot](https://app.notion.com/p/41ec5d5277a98185ac4cfc7813f9f8cf) | v0.4 tự bật hotspot sau reboot được báo PASS; chưa có soak test/đánh giá nhiều biến thể | [AutoHotspot](../projects/autohotspot-api-history.md) |
| 10 | [Tính năng ẩn APK/ODEX/VDEX](https://app.notion.com/p/41dc5d5277a981db8ad1fff1aca10bc5) | Đã quét 8 APK + 7 ODEX + 7 VDEX, ghi 473 component và 393 Activity/Alias; không đồng nghĩa 473 chức năng hoạt động | [Feature inventory](../system/hidden-activity-and-oem-flags.md) |
| 11 | [H01 mới cùng firmware](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2) | Trang ghi thiết bị B khác máy nghiên cứu cũ; unlock/root/Launcher3/IME/xoay có bằng chứng trên máy B ở từng mốc, không sao chép kết quả A sang B | [Máy B](h01-device-b-comparison-20261124.md) |
| 12 | [SMS / TelephonyProvider](https://app.notion.com/p/41dc5d5277a9814993b1e337bb0d8aa6) | Android có dịch vụ SMS và TelephonyProvider, root có thể đọc provider theo log; chưa có thử nhận/gửi SMS thực tế PASS | [SMS](../network/sms-telephony-permission-evidence.md) |
| 13 | [Dual SIM / PCB / RIL2](https://app.notion.com/p/41ec5d5277a9811a916cc87d0bac9d3b) | DSDS và RIL2 runtime ghi nhận, PCB thấy hai cấu trúc đầu đọc; chưa xác minh hai SIM vật lý dùng đồng thời | [Dual SIM](../network/dual-sim-ril-pcb-evidence.md) |
| 14 | [SystemUI / Keyguard bytecode](https://app.notion.com/p/41ec5d5277a9815e9ab9ee60633cfa9b) | Khảo sát SystemUI DEX/ODEX có quickening; nhánh `doKeyguardLocked()` trả sớm trong mẫu, chưa có patch khóa màn hình an toàn | [Keyguard](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| 15 | [Keyguard mặc định tắt](https://app.notion.com/p/41ec5d5277a981879644efda02037161) | Tệp framework-res chứa `config_disableLockscreenByDefault=true`; điều này lý giải chính sách mặc định, không chứng minh bật Swipe sẽ chạy ổn | [Keyguard default](../system/keyguard-framework-vdex-ucloud-sleep.md) |
| 16 | [Crash BackKeyManager](https://app.notion.com/p/41dc5d5277a98151bda6fc8ec359addd) | NullPointerException khi `BackKeyManager.monitor()` gọi handler chưa được khởi tạo; launcher OEM có nhánh phục hồi về Init/MiniLauncher; chưa vá APK | [BackKeyManager](../system/backkeymanager-lock-crash.md) |
| 17 | [UCloud Keyguard K1/K2 / sleep](https://app.notion.com/p/41ec5d5277a981feaf8ede50c6148510) | SystemUI có nhánh model K1/K2 và delay 50/200 ms trong bytecode; target String.equals vẫn chịu hạn chế dequickening; chưa có thử khóa vuốt tự động | [UCloud lock/sleep](../system/keyguard-framework-vdex-ucloud-sleep.md) |

## Các điều kiện giữ trạng thái chính xác

- `REPORTED PASS` là bằng chứng thuộc **một lần thử, một phiên bản, một thiết bị**. Ví dụ AutoHotspot PASS sau reboot không tự chứng minh chạy liên tục 24 giờ, và thiết bị B không được mặc định có tất cả tính năng đã PASS trên thiết bị A.
- `STATIC VERIFIED` chỉ phản ánh mã bytecode/manifest/config trong mẫu: không biến **473 component**, **hai RIL**, **audio HAL** hoặc **Keyguard method** thành bằng chứng chức năng phần cứng đã hoạt động.
- `OPEN/PAUSED/FAIL` giữ nguyên: âm thanh chưa phát PASS; SIM2 chưa có hai SIM vật lý hoạt động đồng thời; SMS chưa gửi/nhận PASS; PIN/Swipe chưa qua kiểm thử đầy đủ; gói factory full restore chưa tồn tại trong kết quả hiện có.
- Một kế hoạch hoặc một bộ ZIP công cụ đã dựng **không** đồng nghĩa đã chạy trên H01. Thử synthetic/host phải được phân biệt với log Android và xác nhận thiết bị thật.

## Ngoài phạm vi đợt công bố này

- Vấn đề Wi-Fi 5 GHz và hiện tượng chọn băng tần làm tắt hotspot đang được nghiên cứu nhưng **không tìm thấy ghi chép tương ứng trong 17 trang Notion H01 kiểm tra**. Không đưa thành báo cáo Notion-only; nếu sau này ghi nhận vào Notion và có bằng chứng mới, mới đưa vào danh sách chờ kiểm duyệt.
- Không công bố firmware OEM, programmer, APK/ODEX/VDEX/ELF, dữ liệu SIM/NV/SoftSIM, IMEI/serial, mật khẩu hotspot, log chứa danh tính, token, ảnh/tệp riêng hoặc script ghi/xóa flash chưa kiểm chứng.

## Trạng thái chuyển giao

**Đã có:** 207 đề mục cấp hai trong nhật ký tổng và 16 trang chuyên đề có bản đồ đến báo cáo GitHub. Báo cáo này kiểm kê 16 trang ở mức **kết luận chính**.

**Chưa có chứng nhận:** 100% mọi đoạn, mỗi ảnh/video, TXT, RAR, ZIP và gói nhị phân đã được soát quyền công bố. Chúng **không** được tự upload theo mục tiêu Notion-only và quy định an toàn. Xem [nguồn & phạm vi](source-boundaries-and-coverage.md), [chính sách](../security/publication-policy.md).
