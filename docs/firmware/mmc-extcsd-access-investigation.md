# H01 eMMC EXT_CSD, RPMB và Boot Areas — các giới hạn quyền đã kiểm chứng

**Nguồn trực tiếp:** [Notion H01 H127–H141, 14/11/2026](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Trạng thái: runtime/Firehose metadata OBSERVED, EXT_CSD nguyên bản CHƯA ĐỌC ĐƯỢC.**

## Tầng Android

Hồ sơ về MMC host cho thấy H01 có eMMC, node RPMB riêng và một số sysfs liên quan card. Trên Android, `u:r:shell:s0` bị AVC **SELinux Enforcing** từ chối `read/getattr` đối với MMC sysfs/debugfs. Trong một số kiểm tra khác còn có hạn chế DAC/permission của file root-only; phải giữ riêng hai nguyên nhân, không gộp mọi `Permission denied` thành SELinux.

Đã thấy tên attribute `raw_rpmb_size_mult` trong sysfs nhưng shell **không đọc được giá trị thật**. Sự có mặt của node không đồng nghĩa đã đọc `BOOT_SIZE_MULT`, `PARTITION_CONFIG`, `RPMB_SIZE_MULT` hoặc EXT_CSD raw 512 byte. Trong snapshot Android, `mmcblk0boot0` và `mmcblk0boot1` **không xuất hiện**; điều đó **không chứng minh Boot Area không tồn tại trên chip**.

Kernel/runtime còn có log `qseecomd` RPMB listener; đó là **dịch vụ của hệ bảo mật**, không tương đương Linux cung cấp truy cập RPMB bằng block I/O chuẩn.

## Tầng Firehose

| Physical partition theo phản hồi Firehose | Sector | Sector size | Dung lượng |
| --- | ---: | ---: | ---: |
| **PPN 0** — User Area | **15.269.888** | 512 byte | 7.818.182.656 byte |
| **PPN 1** — ứng viên Boot1 | **8.192** | 512 byte | 4.194.304 byte |
| **PPN 2** — ứng viên Boot2 | **8.192** | 512 byte | 4.194.304 byte |

Ở hai lượt GetStorageInfo đầu tiên, client từng probe **4.096 byte/sector** khi đoán UFS và bị NAK. Sau khi nhận đúng `MemoryName=eMMC`, cả PPN 1 và 2 trả **ACK** với geometry 8.192×512. Đây là **metadata**, không phải dữ liệu vùng boot.

Những lượt READ sau trong hồ sơ báo **payload 4 MiB đều toàn `0x00`**, có đối chiếu ảnh/sidecar; cần giữ kết luận hẹp: **programmer đã trả các byte zero**, chưa loại trừ ánh xạ/logic generic programmer trả zero. Không được gắn tên “Boot Area vật lý trống” chỉ vì payload toàn zero.

## RPMB / EXT_CSD vẫn chưa hoàn tất

Một log Android QSEE từng ghi RPMB `Mult=1024`, suy ra 512 KiB **theo đơn vị log**. Điều đó **chưa phải** đọc EXT_CSD chuẩn qua MMC command và chưa đủ để chứng nhận cấu hình secure hardware partition.

Không thay SELinux, không `setenforce 0`, không viết MMC sysfs, không thay `PARTITION_CONFIG`/boot selection và **không thử bất kỳ thao tác ghi hay provision key RPMB**.

## Kết luận

- **Đã có:** chứng cứ eMMC User Area + PPN1/2 geometry và các payload trả về, RPMB node/listener, lỗi permission có AVC.
- **Chưa có:** raw EXT_CSD 512 byte, khả năng truy cập RPMB an toàn, kiểm chứng nội dung Boot1/Boot2 bằng đường độc lập, kết quả phục hồi đầu-cuối.

Xem [Boot areas](emmc-boot-areas.md), [Firehose timeline](edl-sahara-firehose-failure-to-success.md).