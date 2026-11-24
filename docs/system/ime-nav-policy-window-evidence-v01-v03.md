# H01 — vì sao immersive.navigation mất hiệu lực với IME, tiến trình v0.1–v0.3

**Nguồn:** [Nhật ký Notion H01, H192–H197](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Runtime/log VERIFIED theo các lượt thử; không khẳng định nhánh thông báo hoặc 5 giây chính xác đã PASS**.

## Quyết định bỏ yêu cầu tự ẩn đúng 5 giây

Ban đầu người dùng muốn Back/Home/Recents ẩn sau **5 giây**. Dịch ngược `SystemUI.StatusBar` của firmware ghi các timer:

| Method/nhánh | Thời gian | Mục đích |
| --- | ---: | --- |
| `scheduleAutohide()` | **2.250 ms** | Ẩn khi đủ điều kiện |
| `userAutohide()` sau `ACTION_OUTSIDE` | **350 ms** | Ẩn sớm khi thao tác bên ngoài |
| `touchAutoDim()` | **2.250 ms** | **Giảm sáng**, không phải ẩn thanh |

Người dùng đã **chọn dùng timing mặc định**, không tiếp tục sửa thành đúng 5 giây. Đặt immersive.navigation có thể ẩn trong nhiều ứng dụng nhưng **không** giải quyết ngoại lệ IME và bảng thông báo.

## Hai báo cáo runtime trước vá

| Trạng thái | Flags/Window chứng minh điều gì |
| --- | --- |
| Bàn phím đang mở | `mForcingShowNavBar=true`, `mLastSystemUiFlags=0xb618`, **HIDE_NAVIGATION bit 0x2 bị xóa**, NavigationBar **SHOWING** |
| Mở bảng thông báo | Focus `StatusBar`, `mLastSystemUiFlags=0x960a`; **HIDE_NAVIGATION vẫn tồn tại** nhưng NavigationBar **SHOWING** do policy layout |

Với thanh phím ở mép trái **36 px**, snapshot bàn phím có `mRestrictedScreen=(36,0) 284x240` dù màn là **320×240**. Hai triệu chứng có **nguyên nhân chính sách khác nhau**; không thể sửa cả hai bằng thay một timeout hoặc một cờ.

## Căn cứ sửa đúng nhánh IME

Phân tích `PhoneWindowManager.updateSystemUiVisibilityLw()`: nhánh `mForcingShowNavBar` loại bỏ các bit clearable gồm **LOW_PROFILE=1, HIDE_NAVIGATION=2 và FULLSCREEN=4**. Bản nghiên cứu IME giữ logic cho bit 1/4 nhưng không cho clear **bit 2** ở đúng call site. Đó là một thay đổi cục bộ **khi cờ HIDE_NAVIGATION đã được yêu cầu từ trước**, không ép mọi app ẩn thanh. Không sửa `StatusBar`, touchAutoDim, phần bảng thông báo hoặc module bật thanh phím.

### Các mốc theo từng gói thử

| Giai đoạn | Bằng chứng | Độ tin cậy |
| --- | --- | --- |
| v0.1 kiểm bytecode | Hai tiến trình ART độc lập, stock/candidate mỗi bên **2.533 PASS**, marker `PREFLIGHT_PASS_NOT_INSTALLED` | **PASS preflight**, không đổi giao diện |
| v0.2 thử tạm | Host checks, `dex2oat EXIT=0`, bind candidate vào namespace init; `system_server` đổi PID, bộ hẹn ~300 giây | **Applied trong một boot**, không cố định |
| v0.2 sau mở IME | `mForcingShowNavBar=true`, `mLastSystemUiFlags=0xb61a` có HIDE_NAVIGATION; NavigationBar **HIDDEN**, màn usable **320 px** | **IME real-device PASS**, người dùng xác nhận |
| v0.3 Magisk | Giữ đúng candidate đã PASS, đăng ký module để nạp sau boot | Gói phát triển/host tests, ban đầu **chưa xác nhận cold boot** |
| v0.3 sau reboot | `MODE=persistent`, `NEXT_BOOT_ENABLED=true`, bootID mới, `service.ready` cùng boot, candidate services được nạp; thanh phím HIDDEN trên Launcher3 | **Persistence PASS**, nhưng snapshot này **không mở IME** |

**Quan trọng:** v0.3 sau reboot có Launcher3 foreground, không có `mForcingShowNavBar=true`. Phép chứng minh IME mở/HIDDEN là ở **v0.2**, không được lấy ảnh v0.3 làm bằng chứng cả hai điều trong cùng snapshot. Watchdog log từ boot thử cũ không đồng nghĩa watchdog còn đang chạy persistent.

## Giới hạn hiện hành

Đợt này chỉ bảo tồn nghiên cứu, không phát hành services JAR/DEX đã vá, offsets/byte patch, module Magisk hoặc script restart `zygote`. **Bảng thông báo còn mở**, và không có chứng cứ “ẩn đúng sau 5 giây ở mọi Activity” đã PASS.

Xem [tóm tắt IME](ime-navigation-research-timeline.md) và [đoạn khảo sát máy B](device-b-launcher-ime-evidence.md).