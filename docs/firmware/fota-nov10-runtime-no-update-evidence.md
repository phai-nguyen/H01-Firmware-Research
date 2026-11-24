# H01 — hai lượt kiểm tra FOTA ngày 10/11/2026, trạng thái 2101

**Nguồn:** Dropbox `H01-ota-check-current.txt`, đoạn log H01 có **hai lần checkVersion thực sự** trong ngày 10/11/2026. Đây là **RUNTIME HISTORICAL OBSERVED**, không phải truy vấn backend mới khi viết báo cáo.

| Thời điểm trong log | Quan sát |
| --- | --- |
| 09:46:26 | `iportOtaAgentPolicy` init FOTA |
| 09:47:12–09:47:13 | Đã gọi `checkVersion`; phản hồi **status 2101**, `No new updates were found`, `data=null` |
| 09:47:12 | `iportUpdateEngine` ghi `ota processing status: false` |
| 17:05:18 | Lần gọi `checkVersion` thứ hai; phản hồi **status 2101**, `No new updates were found`, `data=null` |

Cả hai lần đều liên quan build đang chạy **K1_TSV3.1.005.001.240116_20240116-1930** và network type **4G** theo nguồn. Trong **tệp log này** không có URL tải gói OTA hoặc báo cài firmware thành công. Không có update trong hai lần hỏi không có nghĩa server vĩnh viễn không cấp bản update cho mọi thiết bị.

## Ranh giới dữ liệu được công khai

Log gốc có product/device registration URL, `mid`, `cid/lac/mcc/mnc`, timestamp và chữ ký request. Các giá trị nhận dạng và chữ ký này **không được trích nguyên văn** vì không cần thiết cho kết luận về phiên bản. Không phát lại request, gọi endpoint, thay TLS hay cài OTA.

**Không đồng nhất với nghiên cứu OTA incremental 81→87:** gói đó được tìm qua **phiên bản cũ có dấu vết trong Recovery** ở mốc khảo sát khác, không phải được cấp trong hai lượt ngày 10/11 này. OTA delta cũng không phải factory ROM.

Xem [lịch sử FOTA](fota-update-history.md) và [Recovery OTA 81→87](ota-recovery-version-trace-and-trust-levels.md).