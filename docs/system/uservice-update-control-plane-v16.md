# H01 — UService v16: ba luồng cập nhật, trigger dự kiến và giới hạn của audit runtime

**Nguồn:** [Notion OTA H01, mục 20 — “Nghiên cứu cơ chế cập nhật phần mềm v16” (22/11/2026)](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df). **STATIC VERIFIED từ Java/smali; chế độ update hiệu lực trên H01 chưa được đo.**

## Tách ba cơ chế

| Nhánh | Điều kiện/chuỗi code được phân tích | Phạm vi kết luận |
| --- | --- | --- |
| **Android FOTA** | ABUP `checkVersion` → policy/download `update.zip` → `RecoverySystem.installPackage()` | Đã có gói incremental lịch sử 81→87 và phép kiểm hash/chữ ký; **không cài trong nghiên cứu** |
| **UService APK update** | `GLOBAL_AUTO_UPDATE_MODE=1` → `VersionCheckAndDesc` → FTP → `com.ucloudlink.base.installservice` | Code path có mặt, **chưa chứng minh mode 1 đang chạy** |
| **UService binary update** | `GLOBAL_AUTO_UPDATE_MODE=2` → FTP → `binary_update.json` → chọn asset/binary khi khởi động ứng dụng | Có code quản lý binary, **chưa quan sát hot-update thành công** |

`DownConfigTask` tải **cấu hình chức năng**, không tự đồng nghĩa thay firmware Android, modem hoặc UService APK.

## Những trigger trong mã không phải lịch runtime được đo

Notion ghi các khoảng thời gian từ code:
- Khi Wi-Fi chuyển **CONNECTED**: logic trì hoãn khoảng **3 giây**.
- Đường cloud SIM: khoảng **120 giây**.
- Có handler định kỳ khoảng **1 giờ**, phụ thuộc đồng ý mạng, cấu hình và kết nối.
- Trong nhánh FOTA, giá trị fallback `CheckPeriod` được ghi là khoảng **25 giờ**, nhưng còn policy chu kỳ runtime.

Mode chung mặc định **0**; cấu hình trong nhánh MiFi có thể thành **1**, và giá trị runtime có thể bị OEM/cloud ghi đè. **Chưa có ảnh `getprop`/SharedPreferences runtime chứng minh mode cuối**; không suy tất cả lịch đã thực sự chạy.

## Metadata và một số điểm dễ suy diễn nhầm

- `VersionCheckAndDesc` tham chiếu các trường `MODEL`, `VER`, `SID`, `CFG`, `DID`; trong source, DID có đường tạo dựa vào định danh modem. **Không đăng request thật hoặc định danh**.
- `FTPParams` dùng `UDP`, `VER`, `MDVALUE`, `SIZE`, `FTP`. **Trường tên UDP là cờ update theo parser**, không chứng minh tải file bằng giao thức UDP.
- `FTPDownload` có hỗ trợ tải tiếp và kiểm kích thước/MD5. MD5 trong nhánh này **không tương đương chữ ký bất đối xứng của Android Recovery OTA**.
- `startUpdate` trả **0** có thể chỉ là mã trả về một bước trong logic; **không chứng minh đã cài APK xong**.
- `BinaryUpdateHelper` đọc/ghi `files/binary_update.json`, kiểm phiên bản/MD5, có fallback `lastVersion` và asset trong APK. **Không gọi trực tiếp helper như phép kiểm chỉ đọc**, vì có thể sửa JSON/xóa tệp.
- Trong tập code đã đọc **chưa tìm thấy kiểm chữ ký bất đối xứng riêng** của helper, nhưng chưa phủ mọi lớp và dịch vụ downstream nên **không thể kết luận cả hệ thống thiếu kiểm chữ ký**.

## Hệ quả đối với nghiên cứu H01

1. **Disable FOTA package không tự chứng minh UService APK/binary update đã dừng**.
2. Server cache/endpoint do bộ v15 thiết kế chỉ là dữ liệu cấu hình; **chưa có log thực địa v15**.
3. Muốn xác minh runtime một cách thận trọng phải phân biệt **mode hiệu lực, thời điểm lần kiểm gần nhất, dấu của `binary_update.json`, version APK/DEX đang dùng**. Trong nhiệm vụ xuất bản này **không thu hay sửa các dữ liệu trên máy**.
4. Gói OTA 81→87 thuộc nhánh Recovery; không phải QFIL package hay bản sao eMMC đầy đủ.

Không đăng `uc-asset0.bin`, `binary_update.json` riêng của máy, DEX OEM, SoftSIM, khóa, FTP credential, request URL hay chương trình tự kích hoạt cập nhật. Xem [phân nhóm v12–v16](uservice-update-channels-v12-v16.md), [cache v15](../firmware/ota-server-cache-v15-evidence.md), [FOTA](../firmware/fota-abup-internals.md).