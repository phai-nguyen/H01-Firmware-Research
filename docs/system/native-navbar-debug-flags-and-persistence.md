# H01 — thanh Back/Home/Recents Android gốc: thử tạm, rồi module giữ qua reboot

**Nguồn:** [Notion tổng H01 H183–H186 (18/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). Phân biệt **STATIC CODE**, **USER UI PASS**, **MODULE PERSISTENCE PASS** và những thao tác chưa được xác minh.

## Cơ chế OEM

`SystemUI.StatusBar.createNavigationBar()` trên K1 có điều kiện factory/debug để tạo thanh phím; `panelsEnabled()` đọc điều kiện tương tự. `PhoneWindowManager.setInitialDisplaySize()` đọc `qemu.hw.mainkeys`. Các resource `NavigationBarFragment`/`NavigationBarView` **còn trong SystemUI nguyên bản**.

Hai thuộc tính đã dùng trong phiên nghiên cứu là:

```text
qemu.hw.mainkeys=0
persist.select.launcher.debugmode=true
```

Debug flag cũng ảnh hưởng bảng thông báo; **không** chỉ dùng cho ba phím. Bản thử ban đầu tạm đặt các thuộc tính với cơ chế hoàn tác trong **cùng boot**, không sửa APK/JAR system hoặc boot image.

## Mốc kiểm chứng

| Mốc | Trạng thái đúng theo nguồn |
| --- | --- |
| Preflight ban đầu | 5 tình huống **HOST MOCK PASS**, chưa phải máy thật |
| Sau khi người dùng thử trên H01 | Ba phím Back/Home/Recents hiển thị, mở được màn Recents có các thẻ ứng dụng; người dùng báo **phím hoạt động tốt** |
| Root cố định H185 | Root và boot hash PASS nhưng **module=not_installed** — chưa chứng minh nạp tự động |
| Sau reboot H186 | `module=enabled`, `boot_completed=1`, `mainkeys=0`, `debug=true`, WindowManager hiển thị cửa sổ **NavigationBar** |
| Thử chạm các phím sau module | Snapshot H186 **không chứng minh tất cả phím đã bấm thử lại** |

Giữa H185 và H186 có **boot ID khác**, root Magisk 30.7 và boot hash vẫn giữ. Module `h01_navbar_native` dùng `system.prop` nạp trước Zygote, không có polling; `skip_mount` không chặn đường xử lý system.prop được ghi trong nghiên cứu. **PASS persistence** không tương đương **PASS qua factory reset/OTA**.

Snapshot cuối H186 có density ép **120** (không phải DPI mặc định **160**) và màn vật lý **240×320**. Giao diện NavBar nằm cạnh trái khi xoay ngang ở mốc thử tạm. Không đồng nhất việc **bật thanh phím** với nghiên cứu **ẩn thanh khi IME mở**, đó là hai nhánh riêng.

Không đăng module cá nhân, ảnh boot OEM/Magisk, JAR/DEX hệ thống đã sửa hay tệp CMD tác động firmware. Xem [IME policy](ime-nav-policy-window-evidence-v01-v03.md) và [Magisk timeline](../boot/magisk-root-timeline.md).