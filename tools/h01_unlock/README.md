# H01 bootloader unlock — công cụ kiểm tra DEVINFO ngoại tuyến

**Nguồn lịch sử:** [Notion H171 (18/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd) và [Notion máy H01 thứ hai](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2). Bản script được biên soạn lại từ `kiem_tra_ngoai_tuyen.py` / `kiem_tra.py` của gói nghiên cứu đã được ghi trong Notion. **Script công khai đã sửa để không chứa hash/định danh máy; chưa kiểm thử trực tiếp trên H01 sau khi tổng quát hóa.**

## Công dụng

`offline_devinfo.py` đọc **bản sao riêng của ABOOT và DEVINFO** trên máy tính, xác minh kích thước/hashes được chủ thiết bị cung cấp, kiểm tra magic/field và so đúng **12 byte thay đổi** giữa nhãn `ANDROID-BOOT!` và `GLOCALME-BOOT`. Chế độ `verify` chỉ kiểm file candidate có sẵn; `prepare` tạo **một candidate ngoài thiết bị** sau xác nhận rõ ràng.

**Không có lệnh giao tiếp ADB/EDL, `edl.py w`, flash, erase hoặc đọc/ghi phân vùng thật trong tool này.** Candidate không phải firmware, không có tác dụng mở khóa cho đến khi thực nghiệm riêng được đánh giá và chấp thuận trên đúng máy. Chỉ dùng với bản ABOOT có **cơ chế OEM metadata đã được kiểm chứng riêng bằng phân tích**, không chỉ vì có cùng SoC MSM8909.

## Điều kiện

- Python 3.8+ (antiX Linux hoặc Windows 7 có Python 3.8).
- Hai ảnh **ABOOT và DEVINFO của chính H01**, SHA-256 đối chiếu **độc lập** và bản sao lưu bất biến ngoài thiết bị.
- Không dùng bản DEVINFO/ABOOT hoặc hash từ một chiếc H01 khác; không lấy từ repo này vì **repo không phát hành chúng**.

## Ví dụ cú pháp (điền thông số từ bản sao RIÊNG)

Chế độ kiểm một candidate đã tồn tại:

```sh
python3 offline_devinfo.py verify --aboot ./aboot-goc.img --expected-aboot SHA256_ABOOT_CUA_ANH --devinfo ./devinfo-goc.img --expected-devinfo SHA256_DEVINFO_CUA_ANH --candidate ./candidate-rieng.img
```

Chuẩn bị candidate **chỉ trên ổ đĩa máy tính**:

```sh
python3 offline_devinfo.py prepare --aboot ./aboot-goc.img --expected-aboot SHA256_ABOOT_CUA_ANH --devinfo ./devinfo-goc.img --expected-devinfo SHA256_DEVINFO_CUA_ANH --candidate ./candidate-rieng.img --confirm PREPARE-MY-OWN-H01
```

Lệnh trên chỉ hoạt động khi thay đúng chuỗi SHA-256 dài 64 ký tự, hình ảnh đúng 1 MiB và đầu vào phù hợp chính xác. Tool không ghi đè file candidate đã có. Đọc kết quả `offline_verified=true` là **kiểm tra offline PASS**, **không đồng nghĩa bootloader unlock PASS**.

## Không nằm trong repo

- Ảnh `devinfo-goc.img`, `devinfo-...-GLOCALME.img`, `aboot-goc.img`, Firehose programmer, hash riêng máy, dữ liệu SIM/SoftSIM, script ghi EDL.
- Phương pháp flash ứng viên trên mọi thiết bị, khôi phục cuối-đầu hoặc bảo đảm không brick.

Xem [hướng dẫn nghiên cứu unlock H01](../../docs/boot/h01-bootloader-unlock-notion-procedure-20261124.md), [trạng thái boot/recovery](../../docs/boot/root-and-recovery.md). Quy tắc công bố dự án: **chỉ công bố nội dung đã có trên Notion**.
