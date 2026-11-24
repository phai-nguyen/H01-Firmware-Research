# H01 Root Control v1.1 — lỗi hash giả do trùng tên builtin mksh

**Nguồn:** [Notion H01 H184–H185, tháng 11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **HOST REPRODUCED + DEVICE READBACK REPORTED PASS**. Bản báo cáo chỉ lưu chẩn đoán và mốc xác minh, không phát hành script flash.

## Sự cố ban đầu

Một lần dùng công cụ kiểm boot in:

```text
h01_rootctl.sh[21]: alias: /dev/block/bootdevice/by-name/boot: invalid alias name
```

Hàm shell đặt tên **`hash`** va chạm với builtin/alias của **mksh Android**, khiến lệnh **không tính SHA-256**, giá trị kiểm tra trở thành rỗng rồi bị báo nhầm “boot không khớp”. **Không được hiểu log này là hash phân vùng boot đã sai**, hoặc là bằng chứng flash đã PASS.

## Bản sửa 1.1 và phép thử

- Nhóm nghiên cứu biên dịch **mksh R55** từ AOSP Android **8.1.0_r1** và tái hiện đúng lỗi `invalid alias name`.
- Đổi tên hàm thành `h01_sha256_file`, kiểm cả exit status của `sha256sum` lẫn chuỗi kết quả đúng **64 chữ số hex** trước khi so.
- Không sửa hai hash kỳ vọng hoặc hai ảnh boot trong gói. Báo cáo có **12 bài kiểm thử host** trên mksh R55 và `/bin/sh`, gồm lỗi đọc và hash sai dạng.
- Lúc gói 1.1 mới tạo, **chưa xác nhận chạy trên H01**. Chỉ sau khi có ảnh người dùng ở H185 mới chuyển kết quả thành **device reported PASS**.

## Kết quả mới hơn trên H01

Sau khi chủ thiết bị chạy gói v1.1: backup boot đủ **33.554.432 byte** và đối chiếu thành công, Fastboot báo Sending/Writing/Rebooting **OKAY**, Android `boot_completed=1` và `uid=0(root)`. Hash đọc **trực tiếp từ phân vùng boot** khớp ảnh Magisk 30.7 đã thử; boot ID mới khác phiên trước.

Bằng chứng này xác nhận bản sửa kiểm hash **đọc được trạng thái trên máy**. Không chứng minh factory reset, OTA, mất nguồn hoặc khôi phục một H01 hỏng boot.

**Nguyên tắc:** tách lỗi *measurement tool* khỏi lỗi image thực tế; không tuyên bố từ Fastboot OKAY một mình rằng đã phục hồi toàn bộ eMMC. Không đưa IMG/ZIP/script ghi boot, dữ liệu riêng hoặc lệnh flash lên GitHub.

Xem [Magisk compatibility](magisk-311-vs-307-boot-compatibility.md) và [recovery readiness](recovery-readiness.md).