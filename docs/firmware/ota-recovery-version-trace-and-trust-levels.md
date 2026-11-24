# H01 — dấu vết bản cũ trong Recovery và hai lớp xác thực OTA

**Nguồn:** [Notion nghiên cứu OTA 22/11/2026](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), các mục 4–10. **Đây là kết quả lịch sử từ H01 đã nghiên cứu; không phải thao tác yêu cầu cập nhật hiện tại.**

## Vì sao tìm được thông tin OTA sau factory reset?

Chủ thiết bị từng cập nhật rồi reset xóa dữ liệu, nên log ứng dụng FOTA trong vùng userdata không được giả định còn đầy đủ. Trong nhánh v6, tài liệu ghi **Recovery vẫn có hai bản `last_log.6` và `last_log.7`**, chứa chuỗi bản cũ:

```text
K1_TSV3.1.004.012.210916
K1_TSV3.1.004.012.210916_173207
K1_TSV3.1.004.012.210916_20210916-1758
```

Chuỗi thứ ba có dạng đầy đủ tương ứng trường `ro.fota.version`. Tại thời điểm đó, chỉ có **dấu vết version trong Recovery**; không đủ để chứng minh đây là đúng bản nguồn của lần nâng cấp gần nhất trước khi có phản hồi OTA và kiểm chứng phân vùng.

## Các mốc backend và gói incremental

| Phép kiểm trong hồ sơ | Kết quả |
| --- | --- |
| v1–v3 | Phân tích FOTA SDK, gặp `SSLHandshakeException` và xác định lỗi chứng thư hết hạn |
| v4 | Kiểm tra có giới hạn trong môi trường thử riêng: HTTP 200, `status=2101` với build thực — **không có bản cập nhật** |
| v5 | Chuỗi phiên bản thấp mô phỏng không có chứng cứ từng phát hành, server vẫn `2101` |
| v6 | Tìm được ba chuỗi bản 2021 trong Recovery |
| v7 | Truy vấn lịch sử với bản có dấu vết Recovery: HTTP 200, `status=1000`, trả metadata gói |
| v8–v9 | Lấy gói OTA, so hash/chữ ký/Recovery key theo phạm vi báo cáo; **không cài OTA** |

Gói đã thu là **incremental build 81 → 87**, dung lượng **44.118.207 byte**. Hai phiên kiểm tra ứng dụng FOTA trước đó từ log tháng 10/2026 cũng trả `2101` cho build 87 đang chạy. **Có gói cho bản cũ không đồng nghĩa firmware build 87 hiện tại cần cập nhật hoặc gói phù hợp để tự flash.**

## Hai cơ chế tin cậy không thể gộp

1. **TLS của máy chủ:** nghiên cứu nhận diện chứng thư cũ hết hạn và có phép thử tương thích chỉ trong công cụ riêng. Chứng thư hết hạn **vẫn là chứng thư hết hạn**; đây không phải lý do tắt kiểm chứng TLS của FOTA trên máy.
2. **Chữ ký Android OTA:** chữ ký CMS toàn gói được kiểm ở mức mật mã, signer RSA khớp key Recovery trên ảnh mẫu, và ZIP/segment hashes khớp trong các mốc đã nêu. Phép kiểm OpenSSL với tùy chọn bỏ qua CA **không xác nhận chuỗi chứng chỉ CA**, và metadata `data.sha256` của backend từng **không khớp SHA-256 toàn ZIP**; ý nghĩa trường đó còn mở.

OTA 81→87 là **delta**: chứa lệnh biến đổi block và các bản vá; **không phải factory ROM đầy đủ hoặc bản sao User Area eMMC**. Bộ sao lưu 42 phân vùng của H01 là một nguồn khác và chưa được chứng minh phục hồi end-to-end.

Không công bố địa chỉ tải có xác thực, body API, thiết bị ID, deviceSecret, khóa ký, request signature, công cụ hạ tiêu chuẩn TLS hoặc OTA ZIP OEM.

**Liên quan:** [dòng thời gian v1–v9](ota-discovery-history-v1-v9.md), [chữ ký/khối v10](ota-delta-validation-v10.md), [OTA tổng quan](ota.md).