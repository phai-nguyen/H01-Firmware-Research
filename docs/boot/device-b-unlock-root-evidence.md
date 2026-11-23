# H01 máy B — EDL, bootloader và Magisk 30.7: mốc kiểm chứng

**Nguồn:** trang Notion “H01 MÁY MỚI #2”, mục 2–7, 23–24/11/2026. **REPORTED PASS theo log trên một máy B**; không phải hướng dẫn flash cho công chúng.

## EDL và bản sao riêng

Trong phiên antiX Live, đã thiết lập lại công cụ EDL sau khi thư mục phiên cũ không còn. Giao diện USB Qualcomm 9008 xuất hiện, Firehose đọc GPT có **42 phân vùng**. Có backup `aboot`, `devinfo` và boot **riêng máy B**, kiểm tra kích thước/hash. Ảnh ABOOT được báo trùng hash với A, còn boot gốc **khác hash**. Nhật ký đính chính một nhận định offset DEVINFO “khác máy A”: sau quy đổi LBA × 512, vị trí thực tế tương ứng trùng, không được ghi kết luận ban đầu là đúng.

## Mở khóa: kiểm tra trạng thái trước và sau

- Lúc đầu: `ro.boot.flash.locked=1`, `ro.boot.verifiedbootstate=green`.
- Hồ sơ lưu một thử nghiệm có kiểm tra byte, write/readback riêng cho metadata DEVINFO của B; ghi và đọc lại có báo cáo PASS. **Không xuất bản tệp DEVINFO đã sửa hoặc thao tác ghi/từng byte** vì có thể làm hỏng khóa thiết bị khác.
- Sau đó thuộc tính Android báo `flash.locked=0` và `verifiedbootstate=orange` **trước và sau một lần ADB reboot** — mức chứng cứ PASS của nhật ký.
- Sau lệnh reset EDL từng có cảnh báo USB disconnected/cleanup; ảnh readback đã khớp và Android chạy. Không suy tất cả lần USBError vô hại.

## Root Magisk 30.7

1. Ảnh boot Magisk từ A từng được **nạp tạm** qua Fastboot RAM. Lần đầu lệnh `su` bị từ chối vì Shell chưa có quyền; không suy đây là lỗi nạp boot.
2. Sau khi cài Magisk 30.7 qua installer được firmware cho phép và cấp quyền Shell, `su` trả `uid=0(root)`.
3. Boot gốc 32 MiB được sao lưu từ **B**. Một lần kéo bản sao tạm bị lỗi quyền, sau đó được xử lý và đối chiếu hash; không coi bản lỗi là ảnh chuẩn.
4. Vì boot gốc B khác A, ảnh Magisk được vá **từ boot B**, với kernel/cmdline giữ nguyên và ramdisk bổ sung Magisk. Boot RAM ảnh mới PASS, cảm ứng/Wi-Fi được người dùng xác nhận.
5. Sau khi ghi ảnh B trong phiên thử được chấp thuận và reboot, Android có `uid=0`, checksum phân vùng boot khớp ảnh B đã vá — **root cố định REPORTED PASS**.

**Giới hạn:** chưa có thử nghiệm factory reset, OTA, nhiều chu kỳ nguồn hoặc phục hồi sự cố boot thật. Không công khai serial, HWID/PK_HASH, ảnh DEVINFO/boot, hash thiết bị, metadata unlock, lệnh EDL ghi hay file riêng. Xem [so sánh A/B](../research/h01-device-b-comparison-20261124.md) và [Magisk A](magisk-root-timeline.md).