# ZEUS H01 — quy trình root Magisk 30.7 theo nhật ký Notion đã PASS

**Nguồn duy nhất:** [Notion H01 H179–H186](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), ngày 18/11/2026, và [H01 máy B](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2) ngày 23–24/11. **Trạng thái:** root qua boot RAM và root cố định sau flash đều **REPORTED PASS trên các máy đã thử**. Tài liệu không bảo đảm tương thích với toàn bộ H01 hoặc cập nhật mới.

**Điều kiện bắt buộc:** bootloader đã thực sự mở khóa, có bản sao `boot.img` **của đúng máy**, ảnh gốc/khôi phục được bảo quản và có phương án xử lý bootloop. Tuyệt đối không flash boot của H01 máy A lên máy B: Notion ghi hai ảnh boot gốc **khác hash** dù cùng dòng máy/firmware.

## 1. Xác nhận trạng thái và sao lưu trước root

Trên Windows 7/antiX đang cài ADB/Fastboot và lúc H01 chạy Android, dùng các lệnh **chỉ đọc**:

```sh
adb devices
adb shell getprop ro.build.display.id
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.verifiedbootstate
adb shell getprop sys.boot_completed
```

Trong các lượt Notion, điều kiện trước patch là `flash.locked=0`, `verifiedbootstate=orange`, Android boot hoàn tất và máy được nhận ở ADB. Lưu `boot.img` nguyên bản từ **chính H01 đang dùng**, kích thước/ký hiệu phân vùng và hash SHA-256; giữ cả bản `recovery` và đường quay về Fastboot/EDL. Không coi ảnh boot 32 MiB từ máy khác là tương thích chỉ vì kích thước trùng.

## 2. Tại sao chọn Magisk 30.7?

| Phép thử trên boot H01 trong Notion | Kết quả |
| --- | --- |
| Magisk 31.1 — unpack ảnh boot thực tế | **FAIL**: `Unable to unpack boot image`, `invalid gzip header` |
| MagiskBoot 30.7 — unpack cùng ảnh | **PASS** |
| Magisk 30.7 — vá boot ngay trên H01 | Đã tạo ảnh `magisk_patched-30700_*.img` |
| `fastboot boot` ảnh vá | Android khởi động và cấp root `uid=0` sau khi cho phép Shell |
| Flash boot vá từ **đúng ảnh gốc máy thử** | REPORTED PASS, root sau reboot |

Tài liệu nguồn mô tả bản 31.1 chọn nhầm gzip marker trong kernel trên ảnh cụ thể của H01; **không** khẳng định toàn bộ bản 31.1 lỗi trên tất cả thiết bị Android 8.1. [Magisk 30.7 chính thức](https://github.com/topjohnwu/Magisk/releases/tag/v30.7). Không sử dụng bản APK có nguồn không rõ hoặc image patched sẵn từ mạng.

## 3. Vá ảnh boot trên đúng H01

Theo H182/H180 của Notion, đường dùng thành công là:

1. Đặt **boot gốc đã sao lưu của đúng máy** vào bộ nhớ nội bộ để ứng dụng Magisk mở được.
2. Cài **Magisk 30.7** bằng đường cài APK được firmware H01 cho phép. Ở máy đã thử, cơ chế **InstallService/H01 Home** đã được nghiên cứu riêng; không suy mọi APK installer đều được phép.
3. Trong Magisk chọn **Install → Select and Patch a File**, trỏ tới boot gốc. Kiểm tệp đầu ra `magisk_patched-30700_*.img` và chép an toàn sang máy tính.
4. Kiểm kích thước/hash tệp trước khi thử. Bản root cụ thể ngày 18/11 có kích thước **33.554.432 byte**; **không** dùng hash của máy A làm hash chuẩn cho mọi H01. Ảnh root sẽ có ramdisk khác ảnh gốc do Magisk.

**Không chọn ảnh boot marker** của thử nghiệm H180 làm đầu vào patch. Không đưa `magisk_patched.img`, boot OEM hoặc khóa riêng lên GitHub.

## 4. Kiểm root tạm qua RAM — ưu tiên trước khi ghi flash

Notion H180 ghi thử `fastboot boot` boot gốc/marker; H182 thử ảnh Magisk 30.7 đã patch thành công. Sau khi vào Fastboot từ Android:

```sh
adb reboot bootloader
fastboot devices
fastboot boot magisk_patched-30700.img
```

**Tên `magisk_patched-30700.img` ở trên là tên ví dụ do người dùng tự đặt cho ảnh đúng máy sau khi đối chiếu; không phải file được cung cấp ở repo.** Nếu cần, dùng tên thực tế của file đã được Magisk tạo, không dùng ảnh của H01 khác.

Khi Android lên:

```sh
adb devices
adb shell getprop sys.boot_completed
adb shell su -c id
```

Ở mốc H182, Fastboot báo `Sending` và `Booting OKAY`, Android `sys.boot_completed=1`. Lần đầu `su` báo `Permission denied`; sau khi **cấp quyền Superuser cho Shell trong Magisk**, kết quả thực tế là:

```txt
uid=0(root) gid=0(root) groups=0(root) context=u:r:magisk:s0
```

**Đây mới là ROOT RAM PASS.** `fastboot boot` không ghi phân vùng boot, nhưng Android/Magisk trong lúc chạy có thể ghi `/data`. Không nhầm `Permission denied` do chưa cấp quyền với lỗi Magisk patch.

## 5. Root cố định sau reboot — bước đã thực thi trên máy thử, KHÔNG phải lệnh flash dùng chung

Notion H184–H185 ghi lần thử đã chốt bằng gói **H01-Root-Co-Dinh v1.1** trên Windows 7. Công việc đã diễn ra:

1. Công cụ xác nhận **root RAM hiện có**, serial/firmware và **hash ảnh boot đang nằm trong phân vùng** thuộc danh mục stock/root của đúng máy.
2. Sao lưu boot hiện tại từ máy H01 sang máy tính trước khi ghi, kiểm size/hash; nếu nguồn không khớp thì **dừng**.
3. Chuyển sang Fastboot, xác nhận máy đang unlocked, rồi **ghi vào phân vùng `boot` duy nhất** bằng đúng ảnh Magisk 30.7 đã boot RAM PASS. Không thay `system`, `vendor`, `recovery`, `modem`, `aboot` hoặc `devinfo` trong bước root này.
4. Sau khi reboot vào Android, kiểm `boot_completed=1`, `su -c id` trả `uid=0(root)` và **hash đọc lại trực tiếp từ phân vùng boot khớp ảnh root đã dùng**. So sánh `boot_id` với lần trước để tránh nhầm kết quả của cùng phiên cũ.

Gói v1.0 trước đó có lỗi kiểm checksum do tên hàm shell `hash` đụng built-in/alias của `mksh`; bản **v1.1** đổi sang hàm `h01_sha256_file` và đã đo đúng trên H01 thật. **Không dùng output false mismatch của bản v1.0** làm bằng chứng boot hỏng.

**Kết quả H185:** Fastboot `Sending/Writing/Rebooting OKAY`, Android boot hoàn tất, `su` có `uid=0`, ảnh boot sau ghi khớp ảnh root của **đúng máy thử**. H186 ghi root và module thanh điều hướng tiếp tục hoạt động qua thêm một reboot. Chưa có kiểm thử factory reset, OTA, hoặc mọi trường hợp mất nguồn.

### Kiểm tra sau khởi động (chỉ đọc)

```sh
adb devices
adb shell getprop sys.boot_completed
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.verifiedbootstate
adb shell su -c id
```

Các lệnh đọc trạng thái trên **không thay thế** phép băm partition boot và kiểm bản sao như trong H185. Không flash nếu thiếu bản stock/rollback, USB không ổn định, hoặc không thể xác minh đúng máy.

## 6. Khôi phục và các nhánh độc lập

- Nếu bootloop hoặc root không đúng, cần dùng **ảnh boot gốc của chính máy** và đường rollback đã được chuẩn bị trước. Notion H184 ghi gói v1.1 có nhánh `5_PHUC_HOI_BOOT_GOC.cmd` để thực hiện khi máy đã ở Fastboot; không tự chạy trên firmware/biến thể khác.
- Thanh Back/Home/Recents tự khởi động là **module khác**, không phải điều kiện để root. H186 mới xác nhận module `h01_navbar_native` và cửa sổ `NavigationBar` xuất hiện sau reboot.
- Với **máy B**, Notion ghi ảnh boot gốc B khác A; root qua RAM có thể kiểm trước, nhưng ảnh root cố định phải **được vá từ boot của B**. Không dùng chung file vá hay checksum giữa hai thiết bị.
- Tập IMG sao lưu chưa được chứng minh là bộ factory recovery đầu-cuối; do đó điều kiện khôi phục phải được đánh giá trên **đúng máy** trước mọi thao tác ghi.

## 7. Tóm tắt nghiệm thu

| Mức | Bằng chứng bắt buộc | Notion H01 |
| --- | --- | --- |
| `BOOT-RAM PASS` | Android boot hoàn chỉnh từ `fastboot boot` | H180 |
| `ROOT-RAM PASS` | `su -c id` có `uid=0(root)` khi boot RAM ảnh Magisk 30.7 | H182 |
| `ROOT-PERSISTENT PASS` | Boot partition hash khớp ảnh đã thử, Android lên bình thường và `uid=0` sau reboot | H185 |
| `MODULE-PERSISTENCE PASS` | Module bật lại và UI phím Android xuất hiện sau reboot khác | H186 |

**Ranh giới công bố:** đây là quy trình **rút từ Notion**, không chứa boot image OEM/patched, khóa hoặc serial máy. Các bước ghi flash được mô tả để phân biệt bằng chứng đã PASS và điều kiện an toàn, **không** cung cấp ảnh dùng chung hoặc lệnh flash một lần có thể áp dụng mù. Xem [mở khóa bootloader](h01-bootloader-unlock-notion-procedure-20261124.md), [root timeline](magisk-root-timeline.md), [H01 máy B](device-b-unlock-root-evidence.md), [chính sách Notion-only](../research/notion-only-publication-policy-20261124.md).

## Công cụ mã nguồn công khai

- [`tools/h01_root/root_tool.py`](../../tools/h01_root/README.md): dùng ADB/Fastboot với hình ảnh gốc/ảnh vá **của đúng H01** để thử RAM, kiểm quyền root, sao lưu, hoặc ghi boot có xác nhận. Không kèm IMG, Magisk APK hoặc thông số máy A/B. Bản này được viết lại từ trình tự đã lưu trên Notion; **chưa có chứng cứ kiểm thử H01 thật sau khi tổng quát hóa**.
