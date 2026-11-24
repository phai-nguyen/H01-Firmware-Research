# H01 — đối chiếu MMC host, block device và quyền DAC/SELinux (14/11/2026)

**Nguồn:** Dropbox `H01-mmc-inspect-20261114.txt`, `H01-mmc-nodes-20261114.txt`, `H01-sysfs-mmc-attrs-20261114.txt`. Kết quả có từ snapshot Android 8.1 trên H01; báo cáo đã loại serial, thông tin eMMC nhận dạng và dữ liệu cá nhân.

## MMC topology quan sát từ sysfs

| Thành phần | Kết quả |
| --- | --- |
| `mmc0` | Host tại controller Qualcomm `7824900.sdhci`, có card `mmc0:0001` |
| `mmc1` | Host tại controller `7864900.sdhci`; **không suy ra đã lắp card** chỉ từ host |
| User Area block | `/sys/block/mmcblk0` |
| RPMB block | `/sys/block/mmcblk0rpmb` |
| `/proc/partitions` | Có các `mmcblk0p1` đến `mmcblk0p42` |
| User Area size | `7.634.944` KiB trong `/proc/partitions`, tương đương **7.818.182.656 byte** |
| Kernel | **3.18.71-perf-gd35e91f** |
| Build fingerprint ở phiên | Android 8.1, build SDK `87`, `release-keys` |

Tên `mmcblk0rpmb` và các entry `p1–p42` là dấu hiệu kernel nhận diện vùng RPMB và **42 phân vùng ở User Area**. Nó **không** chứng minh RPMB có thể đọc/ghi authenticated theo quyền shell hoặc Boot1/Boot2 vật lý đã trống.

## Quyền truy cập thực tế

- ADB `uid=2000(shell)`, context `u:r:shell:s0`.
- `/dev/block/mmcblk0` và nhiều partition node được quan sát có owner `root:root`, mode **`brw-------`** (0600). Chỉ nhìn tên partition qua sysfs không nghĩa shell có quyền đọc raw device.
- `/sys/kernel/debug` và cây MMC debugfs có các hạn chế, lệnh liệt kê/đọc gặp **Permission denied**.
- Những attribute `raw_rpmb_size_mult`, `enhanced_rpmb_supported`, `cid`, `csd`, `name`, `manfid`, `oemid` được thử đọc qua ADB, tất cả **Permission denied** trong snapshot.
- Báo cáo SELinux cùng ngày ghi AVC từ chối `read/getattr` đối với MMC sysfs/debugfs. **DAC mode 0600 trên block node và SELinux AVC thuộc hai cơ chế kiểm soát riêng**, không tự gán mọi thất bại cho một nguyên nhân.

## Chưa xác nhận

- Không có bản đọc EXT_CSD nguyên vẹn **512 byte** trong các báo cáo này.
- Không xác minh `BOOT_SIZE_MULT`, `PARTITION_CONFIG` hay kích thước Boot Area bằng đường MMC độc lập.
- Không diễn giải `mmc1` thành eMMC thứ hai.
- Không đọc/tạo key RPMB, không ghi thiết bị block hoặc chỉnh SELinux.

Báo cáo công khai chỉ giữ topology và giới hạn quyền, **không chứa CID/CSD/serial eMMC**. Xem [EXT_CSD research](../firmware/mmc-extcsd-access-investigation.md) và [GPT](../firmware/gpt-layout.md).