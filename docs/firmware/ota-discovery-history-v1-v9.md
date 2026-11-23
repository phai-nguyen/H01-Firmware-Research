# H01 — lịch sử tìm được OTA gốc, v1–v9

**Nguồn:** [Notion nghiên cứu OTA H01 (22/11/2026)](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), mục 2–12. **Chỉ lưu kết quả lịch sử; không công bố mã gọi backend có xác thực, credential hoặc cách vượt TLS.**

| Giai đoạn | Phát hiện |
| --- | --- |
| v1–v2 | Phân tích FOTA SDK xác định phiên bản gửi đi dùng `ro.fota.version`; yêu cầu kiểm tra gặp `SSLHandshakeException`. |
| v3 | Đối chiếu kho tin cậy gốc; nhận diện `CertificateExpiredException`. |
| v4 | Phép thử kiểm chứng tin cậy theo chứng thư cụ thể trong phạm vi riêng nhận HTTP 200 / `status=2101` đối với phiên bản thật — không có cập nhật. |
| v5 | Chuỗi phiên bản thấp được mô phỏng nhưng **không có chứng cứ là build từng phát hành**, server vẫn `2101`. |
| v6 | Log Recovery còn dấu vết phiên bản `K1_TSV3.1.004.012.210916_20210916-1758` sau khi reset. |
| v7 | Kiểm tra có kiểm soát với **phiên bản có dấu vết Recovery** nhận HTTP 200 / `status=1000` cùng metadata OTA. |
| v8 | Đã lấy gói để phân tích ngoại tuyến, xác định OTA tăng dần 81→87. |
| v9 | Xác minh hash vùng phân vùng sao lưu và chữ ký phù hợp Recovery, không cài gói. |

Firmware thật trên thiết bị ở mốc thử vẫn là `K1_TSV3.1.005.001.240116_20240116-1930`; không thay `ro.fota.version` thực, không hạ cấp hoặc flash OTA build 81. Phản hồi cho phiên bản lịch sử **không phải bằng chứng** máy build 87/root có thể cập nhật an toàn bằng gói đó.

## Ranh giới an toàn

Báo cáo chỉ cho biết TLS backend có vấn đề hết hạn chứng thư tại thời điểm khảo sát. Kiểm chứng chữ ký OTA/Recovery và xác thực HTTPS là **hai tầng bảo vệ khác nhau**. Không khuyến nghị tắt kiểm chứng TLS của ứng dụng thực hoặc tự phát lại yêu cầu chứa ID/secret của thiết bị.

Không đăng payload ZIP OEM, URL tải riêng, phản hồi máy chủ nguyên văn, phương thức dựng chữ ký thiết bị, deviceSecret, MID/IMEI, profile SoftSIM hoặc công cụ gửi request. Phần xác minh delta sau tải xem [v10](ota-delta-validation-v10.md), cùng [nhật ký 20/10–10/11](fota-update-history.md).