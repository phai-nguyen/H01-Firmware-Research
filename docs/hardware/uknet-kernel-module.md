# uknet.ko — module Netfilter / Generic Netlink của H01

**Nguồn:** Nhật ký Notion tổng H01, mục 19–24, nghiên cứu 10/11/2026. **Trạng thái: binary STATIC VERIFIED; kernel/sysfs OBSERVED; quan hệ runtime với daemon chưa xác minh hoàn chỉnh.**

## Mẫu đã khảo sát

| Thuộc tính | Giá trị theo bản phân tích |
| --- | --- |
| Đường dẫn firmware | `/system/lib/modules/uknet.ko` |
| Dung lượng | 34.616 byte |
| Định dạng | ELF32 ARM little-endian EABI5, relocatable |
| Metadata | `license=GPL`, `intree=Y`, `depends=` rỗng |
| Phiên bản riêng | `uknet_info: uv:1.0.0.6` |
| Vermagic của tệp | `3.10.49-gd0b9251-dirty SMP preempt mod_unload modversions ARMv7 p2v8` |
| Kernel runtime H01 | `3.18.71-perf-gd35e91f` (snapshot cùng đợt) |
| ELF section đáng chú ý | `__versions` chứa metadata CRC biểu tượng |

**Lưu ý:** Khác nhau giữa vermagic `3.10.49` và `uname -r` `3.18.71` **không tự chứng minh** file .ko tương thích hay không. Việc có `__versions` cần đối chiếu CRC/ABI/kernel build thực tế, không ép load để thử.

## Dấu hiệu chức năng từ symbols/strings

- Netfilter registration: `nf_register_hooks_i`, `nf_unregister_hooks_i`.
- Các hook IPv4/IPv6: `ukhook_event_v4`, `ukhook_event_v6` và các biến thể event khác.
- Tra socket/UID/metadata packet: `uksock_skb_lookup_sk_v4/v6`, `uksock_sk_get_uid`, helpers xử lý SKB và địa chỉ IP.
- Generic Netlink family: **`UCL_GENL`**; symbol `genl_register_family_with_ops_i`, `ugenl_init`, `uts_genl_doit`.
- Các thao tác/thống kê: `getstat`, `setuids`, `clsuids`, thống kê RX/TX theo interface hoặc UID.

**Đánh giá:** bằng chứng tĩnh phù hợp với module thống kê/chính sách lưu lượng mạng theo UID/interface. **Không tìm thấy bằng chứng đủ** để gọi đây là driver RF, QMI baseband hay chip Wi-Fi.

## Trạng thái runtime và giới hạn

Trong system init RC có action `on boot` gọi `insmod system/lib/modules/uknet.ko`. Trên thiết bị, `/sys/module/uknet` đã xuất hiện và chứa các mục `holders`, `notes`, `sections`, `taint`, `initstate`…, nhưng đọc `initstate` bị **Permission denied**. Điều này là bằng chứng kernel có module-name `uknet` đăng ký trong sysfs; chưa xác minh bản .ko trên disk trùng byte với instance kernel đang chạy hoặc đọc được trạng thái `live`.

`uc_netlink` là daemon được init khai báo, còn `UCL_GENL` là family string của module. Khả năng daemon này là userspace peer của uknet **là giả thuyết có căn cứ**, chưa có binary/trace Netlink chứng minh liên lạc thực tế.

## Kiểm tra chỉ đọc (Windows 7 CMD)

```bat
adb shell uname -r
adb shell ls -ld /sys/module/uknet
adb shell ls -l /system/lib/modules/uknet.ko
adb shell ls -la /sys/module/uknet
```

Không chạy `insmod`, `rmmod`, force-vermagic, can thiệp Netfilter hoặc tự gửi thông điệp Generic Netlink.

**Liên quan:** [init service map](../system/init-service-map.md), [daemon/socket](../network/ucloud-daemons-and-sockets.md), [quy tắc công bố](../security/publication-policy.md). File .ko gốc được lưu riêng; không đưa binary OEM lên GitHub.