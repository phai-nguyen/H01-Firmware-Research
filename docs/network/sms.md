# SMS trên H01 — dịch vụ có, khả năng gửi/nhận chưa xác minh

**Trạng thái: SERVICE OBSERVED, RUNTIME SEND/RECEIVE OPEN.** Snapshot ngày 19/11/2026.

| Khảo sát | Kết quả |
| --- | --- |
| `service check isms` | `Service isms: found` |
| TelephonyProvider | `com.android.providers.telephony` tồn tại |
| TeleService | `com.android.phone` tồn tại |
| SMS app mặc định | `sms_default_application=null` trong phép thử |
| Shell thường đọc `content://sms/inbox` | Bị từ chối READ_SMS |
| Magisk root đọc Inbox | `No result found.` |

Có `isms` và Provider **không** chứng minh H01 nhận SMS từ mạng, có inbox thực tế hoặc gửi được SMS; `No result found` chỉ cho biết lúc kiểm tra chưa có hàng dữ liệu trả về. `qcrilmsgtunnel` là thành phần RIL Qualcomm, không phải bằng chứng của ứng dụng tin nhắn.

Nhiệm vụ còn mở: gửi một tin nhắn thử thông thường **không chứa OTP** vào SIM, xác minh modem → TelephonyProvider, sau đó mới xem xét ứng dụng H01 Messages. Không đăng số thuê bao, IMEI/IMSI/ICCID, nội dung SMS/OTP và log Telephony thô.

**Nguồn:** Notion “H01 – Nghiên cứu tính năng SMS và hộp thư tin nhắn (19-11-2026)”. Xem [Dual SIM](dual-sim.md).