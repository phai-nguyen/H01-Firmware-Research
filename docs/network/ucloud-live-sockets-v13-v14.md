# H01 — mạng UCloudlink thực đo: ba snapshot v14

**Nguồn:** [Notion OTA/Network H01](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), mục 17–19 ngày 22/11/2026. **Trạng thái: RUNTIME OBSERVED tại thời điểm thu, không phải kiểm thử WAN exposure.**

## Từ v13 sang v14

V13 có **hai mẫu** socket, cách nhau khoảng **165 giây**; việc map FD bị dừng nên chưa có mẫu ba và không có marker hoàn tất. UID trong bảng socket owner rỗng; PID phải ghép thêm với danh sách process.

V14 sửa phương thức thu FD, báo cáo **24.614 byte**, đầy đủ ba `FD_MAP_END` và `READ_ONLY_DONE`. Ba thời điểm ghi **22:10:48, 22:11:00, 22:11:13**; mỗi mẫu có 8 dòng socket, gồm 5 listener, 2 đầu cùng một kết nối MQTT loopback và DHCP UDP. Tại v14 đã ghép được PID và UID.

| Socket quan sát | Owner | Ý nghĩa |
| --- | --- | --- |
| TCP 80, 443, IPv6 wildcard | `uC_WebServer` (UID 0) | LISTEN trên H01 |
| TCP 1883, IPv4/IPv6 | `uC_MsgRouter` (UID 0) | Broker/router MQTT |
| TCP 1989, IPv6 wildcard | `com.ucloudlink.uservice` (UID radio) | LISTEN, phù hợp class `SocketServer.init()` |
| 127.0.0.1:1883 | WebServer ↔ MsgRouter | **ESTABLISHED** nội bộ |
| DHCP `wlan0` | Gateway hotspot iPhone | Mạng nội bộ phù hợp kết nối đã dùng |

**Quan trọng:** wildcard listener không chứng minh cổng truy cập từ WAN. Không có phép đo firewall, v6only/dual-stack hoặc kiểm thử client bên ngoài. Trong ba snapshot v14 **không thấy kết nối Internet**, nhưng điều đó không chứng minh thiết bị không bao giờ gọi cloud. V13 từng thấy một socket TIME_WAIT ra ngoài chưa xác định owner; không thể gán cho UService.

Bản v14 báo `CACHE_ENDPOINTS_NOT_COLLECTED_AWK_UNAVAILABLE` nghĩa là **bảng cache chưa được thu thập** vì môi trường thiếu awk, **không phải cache rỗng**. Bộ đọc v15 chỉ mới được kiểm thử bằng fixture ở Notion, chưa có PASS runtime.

Đây là bằng chứng **mới hơn** so với [mốc socket 10/11](ucloud-daemons-and-sockets.md), vốn chưa ghép owner theo inode/FD. Không đăng IP WAN, dữ liệu packet, endpoint/host riêng, thông tin tài khoản hoặc SoftSIM.