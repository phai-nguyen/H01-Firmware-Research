# UService H01: phân biệt ba cơ chế cập nhật (v12–v16)

**Nguồn:** [Notion OTA/UService ngày 22/11/2026](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), mục 15 và 20. **Trạng thái: STATIC VERIFIED, các mode runtime còn mở.**

## V12: mã DEX động

Báo cáo nêu `UServiceApplication` dùng AppLibs và `libdexload.so` để nạp `assets/uc-asset0.bin`; native xử lý payload từ offset `0x124` qua routine RC4. DEX sau giải mã **8.226.048 byte** đạt kiểm magic, file size, SHA-1, Adler-32. Điều này bổ sung kết quả ban đầu trong [UService loader](uservice-loader.md) vốn mới phát hiện routine từ static strings; **không chứng minh mọi phiên bản và asset đều tương tự**.

Kết quả Jadx có lỗi, một số method phải đối chiếu bằng bytecode/smali. Không coi Java được dịch ngược là source nguyên bản.

## Ba đường cập nhật

| Nhánh | Cơ chế tìm trong mã | Bằng chứng |
| --- | --- | --- |
| Firmware FOTA | ABUP → gói Android OTA → `RecoverySystem.installPackage` | Đã có gói thật build **81 → 87** và kiểm chứng chữ ký/khối |
| UService APK | `GLOBAL_AUTO_UPDATE_MODE=1` → `VersionCheckAndDesc` → FTP → InstallService | STATIC, chưa xác nhận chạy runtime |
| UService binary nghiệp vụ | `GLOBAL_AUTO_UPDATE_MODE=2` → FTP → `binary_update.json` và asset trong vòng khởi động ứng dụng | STATIC, chưa đo runtime |

Một nhánh `DownConfigTask` tải **cấu hình chức năng**, không mặc nhiên là cập nhật firmware. `GLOBAL_AUTO_UPDATE_MODE` có mặc định 0, nhánh MiFi có giá trị 1; **mode hiệu lực thực tế trên H01 chưa được đo**.

Nhánh APK đi qua `com.ucloudlink.base.installservice` nhưng chưa phủ đầy đủ kiểm tra chữ ký/quyền. Giá trị `return 0` của `startUpdate` không chứng minh đã cài APK. `BinaryUpdateHelper` có thể ghi JSON, xóa file và chọn fallback asset, **không gọi như audit chỉ đọc**.

Trong nhánh helper đã đọc không tìm thấy một bước kiểm ký bất đối xứng riêng, nhưng chưa khảo sát toàn bộ các lớp khác, **không kết luận hệ thống thiếu cơ chế ký**. Tên trường `UDP` trong metadata FTP là cờ logic theo parser, không đủ chứng minh truyền tải qua UDP.

V12 còn tìm được logic binary `adbd` đọc `sys.ukl.adb.auth.disable`; đó là kiểm **xác thực ADB**, không tương đương quyền root của tiến trình. Giá trị `ro.ukl.open.adb.root=true` trong ảnh vendor **không chứng minh adbd UID 0**.

**Giữ riêng:** payload DEX/asset, SoftSIM, mã khóa, endpoint có xác thực, APK OEM và dữ liệu định danh; không gửi request hay bật update tự động trong lần xuất bản tài liệu.