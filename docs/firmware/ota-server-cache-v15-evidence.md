# H01 OTA v15 — khảo sát bảng cache máy chủ, chưa chạy trên máy thật

**Nguồn:** [Notion — OTA H01 22/11/2026, mục 18–20](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df). **STATIC VERIFIED / HOST FIXTURE PASS; DEVICE TEST NOT DONE.**

## Vì sao cần bộ v15?

Bộ lấy mẫu network v14 đã báo **ba FD_MAP_END và READ_ONLY_DONE**, đủ ba snapshot cách nhau 12–13 giây. Mỗi mẫu có 8 dòng socket liên kết PID/UID: 5 listener, 2 đầu nối MQTT loopback và 1 DHCP UDP. Tuy nhiên, dòng **CACHE_ENDPOINTS_NOT_COLLECTED_AWK_UNAVAILABLE** nói rõ bộ lọc `awk` không tồn tại trong PATH; nó **không chứng minh cache rỗng**. V14 ghi nhận listener cục bộ, không xác định server Internet nào đang được sử dụng.

## Đối tượng v15 dự kiến đọc

| Nguồn trong UService | Loại thông tin theo phân tích tĩnh |
| --- | --- |
| `system_config.xml` (SharedPreferences) | Cấu hình hệ thống/ASS/RC |
| `restore_record.xml` | Trạng thái chế độ và thông tin đã khôi phục |
| `/productinfo/ucloud/downcfg_server_ip.cfg` | Bảng IP/server dự phòng của thiết bị |

Mã UService có các kiểu cấu trúc `RunningStates`, `RouteTableAddress`, `IP_MODE` và các nhóm địa chỉ tương ứng business, SaaS, factory. Công cụ v15 được thiết kế **chỉ đọc tên khóa, trạng thái, mode và endpoint đã lược thông tin riêng**, không tải toàn XML ra báo cáo, không gửi DNS/HTTP hay sửa cache. Bộ lọc bỏ URL path/query/fragment và từ chối userinfo.

## Mức thử nghiệm đã thực hiện

- **PASS tại host:** các fixture cho XML entities, array route, IPv4/IPv6, lọc secret, bỏ query, từ chối DTD/userinfo; DEX build min API 27 và ZIP CRC/header checks theo báo cáo.
- **Chưa chạy trên H01:** Notion ghi rõ v15 chưa được thực thi trực tiếp trên H01/Windows; không có `STATUS` của tập tin cache thật và không có endpoint xác nhận.
- **Không thể suy từ source:** danh sách server chính/phụ đã được lựa chọn, endpoint có đang được dùng, hoặc chế độ cập nhật runtime đang bật.

Tên tệp/đường dẫn được ghi để chỉ ra **vị trí nghiên cứu tĩnh**, không phải khuyến nghị gọi root đọc hoặc trích xuất dữ liệu trực tiếp lên GitHub. Không xuất bản JAR/tool thử nghiệm, khóa, tài khoản, host cá nhân, nội dung XML hoặc URL được gắn token.

Tham khảo [network v13–v14](../network/ucloud-live-sockets-v13-v14.md) và [ba kênh cập nhật UService v12–v16](../system/uservice-update-channels-v12-v16.md).