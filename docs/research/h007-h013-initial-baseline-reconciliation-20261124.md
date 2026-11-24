# H01 — đối chiếu 7 mục nền tảng H007–H013 với kết quả đến 24/11/2026

**Nguồn gốc:** [Nhật ký Notion tổng H01](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), các đề mục **7–13** ở giai đoạn đầu 10/11/2026. **Mục đích:** hoàn thiện bảy tuyến truy vết từng trỏ chung tới `firmware/overview.md`; **không** coi nhận định lịch sử ngày 10/11 là kết quả hiện tại. Chỉ công bố nội dung biên soạn, không đính kèm dữ liệu riêng, binary hãng hay log thô.

## H007 — Tiến trình UCloudlink và các dịch vụ nền

Bản chụp process ban đầu liệt kê `uc_MsgRouter` (nhận tham số `-c /system/etc/mosquitto.conf`), `uC_WebServer`, `unet`, `uc_qmi_clnt`, `uc_netlink`, `uc_kglogd`, `com.ucloudlink.uservice` và `com.abupdate.fota_demo_iot`. Đây là **OBSERVED AT SNAPSHOT**: PID chỉ áp dụng thời điểm thu thập, không dùng số PID lịch sử để thao tác `/proc` ở phiên khác.

Lệnh `readlink /proc/PID/exe` ở ảnh gốc chưa cho bằng chứng đường dẫn cho mọi process. Các dòng `cmdline` cho biết tên executable của bốn daemon; ADB thường chưa có quyền kéo các binary hệ thống. `mosquitto.conf` có ghi chỉ thị `user root` trong phần cấu hình không comment, nhưng không chứng minh tài khoản MQTT, topic, listener hay server cloud thực tế. **Diễn biến về sau:** snapshot port/socket và sơ đồ init cung cấp chi tiết bổ sung, nhưng không chứng minh truy cập từ WAN. Xem [daemon/socket](../network/ucloud-daemons-and-sockets.md), [v13/v14](../network/ucloud-live-sockets-v13-v14.md) và [init map](../system/init-service-map.md).

## H008 — Ứng dụng hệ thống và nhánh OEM

Hồ sơ ban đầu nhận diện các APK/dịch vụ: FOTA, UService, GlocalmeHome, GlocalMeFeedback, InstallService, UKL Factory và MMI. Đây là **kiểm kê tệp/package**; sự hiện diện không khẳng định service đang chạy, khả năng gỡ an toàn hoặc phụ thuộc runtime. Tên adapter chứa `sprd` trong mã UService **không thay đổi** thông tin SoC MSM8909 quan sát trên thiết bị. Xem [ma trận ứng dụng hệ thống](../system/system-app-dependency-baseline-20261124.md), [package state](../system/package-install-and-fota-feedback.md).

## H009 — Các kết luận “chưa có” đã bị kết quả sau thay thế

| Nhận định ban đầu 10/11 | Kết luận đến 24/11 | Mức bằng chứng |
| --- | --- | --- |
| Chưa có gói OTA thật, không biết full hay delta | Đã phân tích incremental **81→87**, không phải factory ROM | OFFLINE VERIFIED BY SOURCE REPORT |
| Firehose/EDL chưa được xác nhận | Có nhật ký READ/GPT/NOP và bộ ảnh phân vùng được kiểm kê | REPORTED PASS; không suy restore |
| Chưa đọc boot/system/vendor, chưa có eMMC dump | Có bản sao ứng viên **42/42** tên phân vùng; vẫn chưa có ảnh User Area thô nguyên dải | COPY INTEGRITY REPORTED; full clone OPEN |
| UService DEX chưa dequickening đủ | Báo cáo sau xử lý **37.008/37.008** quickening records, kiểm checksum cấu trúc | STATIC VERIFIED IN REPORT |
| Bootloader chưa biết có thể unlock | 18/11 ghi nhận unlocked sau reboot, sau đó Magisk 30.7 root | REPORTED PASS trên máy thử |
| Chưa xác minh IPC/daemon, UART pinout | Có socket/process evidence từng phần; UART/pad chính xác và mọi IPC còn mở | PARTIAL / OPEN |

Cần giữ mốc cũ để hiểu **quá trình phát hiện**, không ghi đè bằng kết quả mới. Các vùng eMMC ngoài partition còn thiếu **158.953.472 byte theo bản kiểm 18/11**, không thể gọi bộ ảnh là restore image hoàn chỉnh. Khả năng đăng ký cloud, khóa/secret, nội dung SoftSIM, vai trò đầy đủ của asset động và hiệu lực thao tác OTA runtime vẫn không được xác nhận trong tài liệu công khai.

Nguồn cập nhật: [OTA delta](../firmware/ota-delta-validation-v10.md), [Firehose](../firmware/edl-firehose-diagnostics.md), [backups](../firmware/emmc-backup-verification.md), [gaps](../firmware/user-area-reconstruction-overlap-and-gaps.md), [UService](../system/uservice-loader.md), [unlock](../boot/oem-unlock-research.md), [Magisk](../boot/magisk-root-timeline.md).

## H010 — Đánh giá lại kế hoạch ban đầu

- **Phân tích tĩnh FOTA/UService:** đã bổ sung VDEX, loader, ba kênh cập nhật; mode chạy hiệu lực và payload động chưa được chứng minh hoàn toàn.
- **IPC/runtime:** đã có các snapshot socket, một số mapping port/PID; còn thiếu đồ thị phụ thuộc đầy đủ, đối chiếu theo một boot thống nhất.
- **Firmware phục hồi:** đã có GPT/partition images, báo cáo SHA/CRC; **chưa đạt** cứu hộ end-to-end và chưa có factory image có thể công bố.
- **Linux thay thế:** vẫn ở mức đánh giá giả thuyết; không có Linux/GSI tương thích đã boot PASS trên H01 trong nguồn đối chiếu.

Không lặp lại thao tác ghi flash, unlock, kích hoạt FOTA hay thăm dò khóa/SoftSIM chỉ để nâng mức báo cáo.

## H011 — Danh mục chứng cứ ban đầu

Tài liệu gốc ghi các **nhóm tệp** thay vì xác nhận mọi byte đã nằm trong Notion: APK/ODEX/VDEX FOTA và UService; thư viện UCloudlink; cấu hình Mosquitto; các báo cáo `getprop`, `ps`, `services`, `packages`, danh sách system binary/library; APK InstallService. Một số file raw và gói nén lưu riêng ở nơi khác, **không tự động trở thành đính kèm Notion hoặc tệp GitHub**. Không đăng lại các tệp OEM, hash cá nhân hoặc đường dẫn chứa credential. Xem [bảng nguồn và ranh giới](source-boundaries-and-coverage.md).

## H012 — Quy tắc thu thập và công bố

Trong giai đoạn đầu, ADB shell là UID 2000 và nhiều thao tác đọc bị từ chối. Các phiên sau có root trên máy thử, nhưng **quyền root không khiến lệnh tác động hệ thống trở thành an toàn**. Vẫn ưu tiên lệnh chỉ đọc, không thay đổi cấu hình modem, MQTT, OTA, init hay SELinux để kiểm thử độ phủ. Che IMEI/IMSI, serial, địa chỉ mạng, mật khẩu, token, SoftSIM/NV, dump firmware và ảnh nhận dạng trước công bố. Xem [chính sách xuất bản](../security/publication-policy.md).

## H013 — Nhật ký kết luận chính: lịch sử so với hiện trạng

Mục H013 từng kết luận dự án mới ở giai đoạn lập bản đồ, chưa đọc phân vùng, chưa unlock/flash. **Đây là phát biểu đúng ở thời điểm đầu**, nhưng **không phải trạng thái ngày 24/11**. Đến mốc 24/11 đã có tài liệu khử định danh về GPT 42 phân vùng, các lần sao lưu, fastboot unlock/root trên máy thử và OTA incremental đã đối chiếu. Vẫn **không** có bằng chứng factory restore end-to-end hay khả năng áp dụng trên mọi H01.

## Ranh giới xác nhận

Báo cáo này bổ sung đầy đủ **trình tự kết luận và nguồn tham chiếu cho bảy mục H007–H013**, không chứng nhận mọi ảnh/ZIP và mọi dòng Notion đã được kiểm duyệt. Không coi **7 mục có báo cáo chi tiết** là 7/207 mục đã chuyển toàn bộ đính kèm. Các mốc `REPORTED PASS` và `OPEN` giữ nguyên mức tin cậy từ nguồn.
