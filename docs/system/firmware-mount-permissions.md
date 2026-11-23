# Phân vùng modem mount tại /firmware — chứng cứ quyền truy cập

**Nguồn:** Notion H01 mục 22–24 (10/11/2026), `init.target.rc`, `/proc/mounts`, ảnh CMD `ls -ld` và `getenforce`. **Trạng thái: mount & quyền OBSERVED; chưa trích xuất file từ thư mục này.**

## Dữ liệu đối chiếu

- Init khai báo `/dev/block/bootdevice/by-name/modem` được mount VFAT tại `/firmware` với cờ `ro`.
- `/proc/mounts` trên thiết bị xác nhận mount thực tế: `modem → /firmware`, `vfat`, `ro`, `uid=1000,gid=1000`, `fmask=0337,dmask=0227`, label `u:object_r:firmware_file:s0`.
- `ls -ld /firmware` trả permission **`dr-xr-x---`**, owner/group **`system:system`**; `getenforce` trả `Enforcing`.
- ADB shell chạy UID 2000, **không thuộc group system** trong snapshot, nên **DAC mode 0550 đã đủ giải thích Permission denied** khi liệt kê. Không khẳng định SELinux là nguyên nhân trực tiếp chỉ từ lỗi này.

`ro` chỉ là *mount read-only* — không tự cấm đọc. Trong trường hợp này, quyền traverse/list thư mục là rào cản thấy được.

## Điểm cần phân biệt

- **Có mount**: được xác minh từ `/proc/mounts`.
- **Không liệt kê được file qua shell thường**: được xác minh từ lệnh ADB; không có nghĩa hệ thống không chứa file modem.
- **Chưa pull được file bên trong `/firmware`**: không tuyên bố đã sao lưu các file đó ở nhánh này.
- Bản dump raw partition modem qua EDL là *nguồn thu thập khác*, không đồng nghĩa lệnh `ls /firmware` chạy thành công.

## Kiểm tra lại chỉ đọc

```bat
adb shell ls -ld /firmware
adb shell getenforce
adb shell cat /proc/mounts > H01-proc-mounts.txt
findstr /I " /firmware " H01-proc-mounts.txt
```

Không dùng `su` để vượt quyền cho mục tiêu này, không `chmod/chown/chcon`, không `setenforce`, không mount RW, không tìm kiếm dữ liệu SoftSIM theo đường dẫn suy đoán.

**Liên quan:** [init map](init-service-map.md), [EDL/GPT](../firmware/edl-firehose-diagnostics.md), [backup](../firmware/backup-and-reconstruction.md).