# Cấu trúc boot.img H01/K1: header, kernel, DTB, ramdisk và dm-verity

**Nguồn trực tiếp:** [Nhật ký Notion H01 — mục H100, “Phân tích tĩnh boot.img – 11/11/2026”](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Mức chứng cứ: STATIC VERIFIED trên ảnh boot đã sao lưu, không phải phép boot lại hay kiểm tra chữ ký OEM tại thời điểm biên soạn.**

## Header và kernel

| Hạng mục | Giá trị ghi trong báo cáo nguồn |
| --- | --- |
| Tệp nghiên cứu | Ảnh phân vùng `boot` của H01, sao lưu ngày 11/11/2026 |
| Tổng kích thước phân vùng | **33.554.432 byte** (32 MiB) |
| Magic / header version | `ANDROID!` / Android boot image **v0** |
| Page size | **2.048 byte** |
| Kernel size / load address | **18.524.488 byte** / `0x80008000` |
| Ramdisk size / load address | **1.041.768 byte** / `0x81000000` |
| Second stage | **0 byte** |
| OS version field | Android **8.1.0**, patch metadata **2019-04** |
| Kernel | ARM32 Linux **3.18.71-perf-gd35e91f**, GCC 4.8, build timestamp **16/01/2024** |

Mốc patch metadata trong boot header **không đồng nghĩa** ngày biên dịch kernel, và string build trong các bản ghi khác nhau có biến thể `TSU`/`TSV`: không chuẩn hóa tên build của một mẫu bằng tên mẫu khác khi chưa đối chiếu trực tiếp.

Kernel command line trong ảnh có `androidboot.hardware=qcom`, `console=ttyHSL0,115200,n8`, `androidboot.bootdevice=7824900.sdhci`, `buildvariant=user`. Đây là **thông tin cấu hình tĩnh**, không phải bằng chứng UART đã giao tiếp thành công.

## Device Tree

Bộ kernel trong ảnh chứa **56 cấu trúc DTB/FDT**, được kiểm tra header và ranh giới không chồng lấn. Trong đó DTB số **50** có model:

```text
Qualcomm Technologies, Inc. MSM8909-PM8909 1GB MTP K1
```

DTB ứng viên K1 ghi PMIC **PM8909**, Board ID cặp `(0x8, 0x66)`; ngoài ra còn có FDT của biến thể G4S, RCM và reference boards. **Chỉ nhìn thấy DTB K1 trong ảnh boot không chứng minh bootloader chắc chắn chọn DTB đó khi chạy**. Báo cáo runtime âm thanh mới hơn đã đối chiếu model/board K1 từ Device Tree thực tế; xem [DTB âm thanh đang chạy](../hardware/k1-audio-device-tree-confirmation.md).

## Fstab trong DTB K1

| Partition | Filesystem / mount | fs_mgr flags |
| --- | --- | --- |
| `system` | ext4, `ro,barrier=1` | `wait,verify` |
| `vendor` | ext4, `ro,barrier=1,discard` | `wait,verify` |

Các đường block `/dev/block/platform/soc/7824900.sdhci/by-name/{system,vendor}` khớp tên thiết bị boot trong cmdline. `verify` chỉ nói **có cấu hình yêu cầu xác minh**, không chứng minh cả dm-verity chain, hash tree/FEC, signature đều đã được kiểm tra độc lập. Nghiên cứu OTA v11 trước đây xác định verity/FEC metadata ngoài ranh giới ext4 nhưng **chưa tính lại đầy đủ**.

## Ramdisk và phạm vi

Ramdisk gzip giải ra CPIO newc **1.729.280 byte**, **79 mục**, bao gồm `/init` ELF32 ARM và cấu hình Android/charger. Có đường `/sbin/charger` liên quan Charger Mode; xem [LK/PMIC](lk-pmic-charger-analysis.md). Dữ liệu sau chữ ký/đuôi boot chưa được phân loại hoàn chỉnh trong hồ sơ tĩnh, vì vậy **không nên giả định mọi byte sau ramdisk là rác hoặc có thể xóa**.

**Đã xác minh:** cấu trúc ảnh, kernel, bộ DTB, entry fstab và ramdisk trong ảnh đã lưu. **Chưa xác minh:** full secure boot fuse/verified boot runtime từ tệp một mình, việc phục hồi toàn bộ eMMC, hay khả năng thay DTB/boot trên phần cứng khác.

Không đăng ảnh `boot.img`, toàn bộ DTB, CPIO OEM, hash phân vùng riêng, hoặc script vá flash.