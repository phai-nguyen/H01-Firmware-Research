# H01 — Magisk 31.1 lỗi unpack, Magisk 30.7 boot RAM và root thành công

**Nguồn trực tiếp:** [Notion H01 H179–H182, 18/11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Bằng chứng: phân tích ảnh boot đã sao lưu và người dùng xác nhận trên một H01 thật**. Đây không phải tuyên bố hai phiên bản Magisk hoạt động giống nhau trên mọi máy MSM8909.

## Trình tự kiểm chứng

| Phép thử | Kết quả |
| --- | --- |
| Boot RAM ảnh boot gốc H01 (32 MiB) | Fastboot báo Booting OKAY, Android `sys.boot_completed=1` |
| Boot RAM ảnh có marker cmdline | `ro.boot.h01_ramtest=ram-20261118`, Android boot thành công; **chưa có root** |
| Magisk 31.1 unpack cùng boot gốc | **FAIL: Unable to unpack boot image** |
| MagiskBoot 30.7 unpack ảnh boot đó | **PASS** |
| Vá boot bằng Magisk 30.7 **trên H01** | Đã tạo ảnh Magisk, so static với bản gốc |
| `fastboot boot` ảnh Magisk 30.7 | Android boot completed, ban đầu `su` bị từ chối vì chưa cấp Superuser |
| Sau cấp quyền Shell trong Magisk | Hai lần `su -c id` báo **uid=0(root)** — **ROOT RAM PASS** |

Phép phân tích độc lập của 31.1 phát hiện chuỗi gzip kernel thật ở **offset 16.495**, không căn 4 byte; bản thử chọn nhầm chuỗi giống gzip legacy ở offset **246.304**, sau đó `invalid gzip header`. Đây là **chẩn đoán phù hợp ảnh boot H01 đang dùng**, không chứng minh lỗi chung của mọi ảnh ARM32 hoặc mọi phát hành Magisk 31.1.

## Giới hạn của phép so boot

Báo cáo ảnh Magisk 30.7 dài **33.554.432 byte**: kernel/DTB giữ từng byte; ramdisk thay `init` và thêm 9 entry Magisk, 77 entry OEM khác giữ nguyên nội dung/quyền. Header đổi `ramdisk_size` và ID; các load address, page size, cmdline không đổi theo phép so. Bản Magisk **không giữ toàn bộ đuôi dữ liệu dư của boot gốc**. `KEEPVERITY=true`, `KEEPFORCEENCRYPT=false` **không tự chứng minh trạng thái /data encryption**. AVB1 tool trả 0 **không chứng minh OEM đã ký lại ảnh vá**.

Các mục Notion H179–H182 dừng ở **root trong phiên boot RAM**. Kết quả **root cố định sau flash và reboot** được ghi riêng ở H185–H186, không được gán ngược cho bước thử này.

**Không đăng:** ảnh boot gốc/đã vá, checksum theo máy, ZIP Magisk riêng, serial/định danh hoặc lệnh ghi flash. Xem [root timeline](magisk-root-timeline.md), [lỗi kiểm tra mksh](rootctl-mksh-hash-alias-regression.md).