# H01 — đối chiếu trực tiếp hệ tệp FOTA, kích thước và timestamp

**Nguồn trực tiếp:** Dropbox `H01-FOTA-files.txt` (bản liệt kê của `/system/app/FOTA`), đối chiếu [Notion H01 mục 4 — FOTA/ABUP](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Mức chứng cứ: FILE METADATA OBSERVED; không mở APK nhị phân, không chạy cập nhật.**

## Danh sách thực có trong file TXT

| Vị trí trong filesystem H01 | Kích thước `ls -l` | Mtime được in |
| --- | ---: | --- |
| `/system/app/FOTA/FOTA.apk` | **577.817 byte** | `2008-12-31 23:00` |
| `/system/app/FOTA/oat/arm/FOTA.odex` | **74.208 byte** | `2008-12-31 23:00` |
| `/system/app/FOTA/oat/arm/FOTA.vdex` | **2.865.228 byte** | `2008-12-31 23:00` |

Bản TXT cũng có hai thư mục `oat`, `oat/arm` với quyền và kích thước entry **4.096 byte** mỗi thư mục. Ba tệp đều được in quyền `-rw-r--r--` và owner/group `root:root`.

Các kích thước **khớp đúng** với ba dòng FOTA trong nhật ký Notion (mục 4) và [báo cáo phân tích APK/DEX](fota-abup-internals.md). Bản TXT là **dữ liệu do lệnh liệt kê filesystem trả về**: không chứa nội dung nhị phân, nên chưa có phép đối chiếu SHA-256 trên từng file trong lượt kiểm này.

## Không dùng năm 2008 làm ngày ra firmware

`2008-12-31 23:00` là **mtime mà filesystem in ra**, không phải ngày build Android, ngày đóng gói APK, ngày ký chứng thư hay ngày phát hành FOTA. Một số ảnh hệ thống Android có timestamp được giữ/đặt trước khi đóng gói; nguồn này **không đủ** để xác định nguyên nhân vì sao mtime là năm 2008.

Các mốc phải giữ độc lập:
- Mtime của ba tệp FOTA: **31/12/2008 23:00** theo bản liệt kê.
- Version firmware H01 đang được báo ở các log khác: họ build `K1_TSV3.1.005.001.240116`.
- Thời điểm nhật ký nghiên cứu và lấy tệp: **tháng 11/2026**.
- FOTA **đã chạy** trên H01 hay không: phải xem `init`/package state/process và log runtime, **không** suy từ việc APK tồn tại trong `/system/app`.

## Giới hạn và quan hệ với DEX

Notion mục 4 có phép phân tích VDEX version `vdex010`, phục hồi DEX `038` dài **2.540.284 byte**, 2.795 class definitions, 23.619 method IDs và **13.143 quickening records**. Đây là **một phép phân tích nhị phân đã ghi ở nguồn khác**, không phải kết quả mới của tệp TXT đang xét.

Bản liệt kê không có `update.zip`, không cho biết các phản hồi backend, không xác minh chữ ký OTA và không chứng minh firmware đang có bản cập nhật mới.

**Không đăng:** FOTA.apk, ODEX/VDEX OEM, DEX giải mã, mật khẩu/certificate riêng, request/backend có định danh, hoặc nội dung phân vùng H01. Xem [FOTA static](fota-vdex010-dequickening-evidence.md) và [FOTA runtime 10/11](fota-nov10-runtime-no-update-evidence.md).