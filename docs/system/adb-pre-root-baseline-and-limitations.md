# H01 — baseline ADB trước root, quyền shell và giới hạn khảo sát

**Nguồn:** [Notion H01, H003 và H015–H018](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), tháng 11/2026. **Trạng thái: quan sát trước khi thiết bị được root ở các mốc sau.**

## Phân biệt shell và root

Trong firmware production ban đầu:

```text
adb shell id → uid=2000(shell), u:r:shell:s0
adb root → adbd cannot run as root in production builds
```

ADB shell **không phải UID root** dù tiến trình `uc_MsgRouter`, `uC_WebServer`, `unet`, `uc_qmi_clnt`, `uc_netlink` có thể chạy UID 0. Quyền root của một daemon không được ADB thừa hưởng.

Ở snapshot trước root, đọc symlink `/dev/block/bootdevice/by-name` được, nhưng đọc raw `boot/system/vendor` qua block device bị chặn. Các nơi khác như `/proc/cmdline` hoặc tham số kernel DLOAD cũng có báo Permission denied. **Liệt kê tên phân vùng khác với đọc được nội dung phân vùng**. Bộ GPT 42 partition được xác minh **sau này** qua Firehose, không được gán nhầm vào thời điểm chỉ mới có symlink.

## Procfs FD và chủ socket

Snapshot `ps` có các daemon OEM, nhưng cố đọc `/proc/<PID>/fd` của `uc_MsgRouter` bằng shell thường bị Permission denied. Tại mốc này **chưa thể map inode port 1883 sang PID**. Sự cố có thể do procfs DAC hoặc SELinux, **ảnh không phân biệt hoàn toàn**.

Do vậy nhóm chuyển sang đọc cấu hình `init.rc`, `/proc/net/tcp`, `/proc/net/unix`, `netstat` chỉ đọc. Sau đó **ngày 22/11**, phương án snapshot khác đã gán PID/UID từ FD map ở v14; [báo cáo runtime mới](../network/ucloud-live-sockets-v13-v14.md) **supersede giới hạn mốc cũ**, không xóa lịch sử thất bại.

## Tính thời điểm của kết luận

- Đến ngày 18/11 trong hồ sơ thử nghiệm, **Magisk 30.7 root đã PASS** trên một H01.
- Những mệnh đề “chưa có quyền root”, “chưa đọc được block”, “chưa có Firehose” trong mục H003/H013 **là ảnh chụp tiến độ ban đầu**, không phải trạng thái chung sau root/EDL.
- Dù có Magisk root, không được tự coi `adb root` sẽ chuyển sang root hoặc tất cả các SELinux domain đều được mở.

Không công bố log gốc có ID máy, MAC, IP WAN, tên tệp của người dùng. Tham khảo [lịch sử root](../boot/magisk-root-timeline.md), [init services](init-service-map.md).