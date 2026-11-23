# H01 — chi tiết dịch vụ ISms, Provider và quyền truy vấn Inbox

**Nguồn:** [Notion nghiên cứu SMS (19/11/2026)](https://app.notion.com/p/41dc5d5277a9814993b1e337bb0d8aa6). Biên soạn 24/11/2026. **SERVICE/PROVIDER OBSERVED; nhận/gửi SMS chưa kiểm chứng.**

Dữ liệu H01 lưu có `isms` (Binder `ISms`), `sms-sec`, `phone`, `telephony.registry`, `simphonebook`. Có `TelephonyProvider` (`com.android.providers.telephony`), `TeleService` (`com.android.phone`), `qcrilmsgtunnel` và `Dialer`.

Không tìm thấy một app giao diện SMS độc lập qua bộ lọc tên package **không chứng minh** modem không hỗ trợ SMS; `qcrilmsgtunnel` cũng không phải bằng chứng của ứng dụng SMS.

| Phép kiểm trong nguồn | Quan sát |
| --- | --- |
| `service check isms` | `Service isms: found` |
| `settings get secure sms_default_application` | `null` |
| `pm path com.android.providers.telephony` | Provider APK hiện diện |
| Shell thường truy vấn `content://sms/inbox` | **SecurityException**, thiếu READ_SMS/quyền liên quan |
| Magisk root truy vấn Inbox | Không còn Permission Denial, nhưng **`No result found`** |

**No result found** chỉ cho thấy lúc đó query không trả bản ghi Inbox; không chứng minh thiết bị không nhận SMS hoặc số điện thoại không có tin nhắn trong mạng. Chưa thực hiện thử nhận/gửi qua SIM, gửi SMSC/IMS/NAS, hai SIM đồng thời hoặc kiểm tra UI nhắn tin.

Không trích đăng số điện thoại, SMS/OTP, ICCID, IMEI, IMSI và log Telephony. Đợt này không tạo app Messages hay thực hiện thao tác trên máy. Xem [SMS tổng quan](sms.md), [Dual SIM](dual-sim-ril-pcb-evidence.md).