# Dòng thời gian sao lưu eMMC H01 — 10–14/11/2026

**Nguồn:** Notion trang tổng H01, các mục 32–98, 114–138. **Phân loại:** nhật ký thao tác sao lưu và kiểm tra từ các phiên khác nhau; không phải phép đọc lại mới, không phải quy trình flash.

## 10/11 — từ GPT đến boot chain

Sau khi Firehose handshake thành công và đọc GPT 42 phân vùng của eMMC User Area, dự án tiến hành sao lưu từng nhóm. Nhật ký ghi các mốc đã có ảnh chuyển và kiểm chứng:

- `splash`, `boot`, `recovery`: mỗi ảnh được xuất và chuyển từ máy tính sang iPhone theo từng mốc.
- Các phân vùng khởi động: `sbl1/sbl1bak`, `aboot/abootbak`, `rpm/rpmbak`, `tz/tzbak`.
- Chỉ khi báo cáo đọc hoàn tất và kích thước trùng GPT mới đánh dấu một phân vùng đã được sao lưu; ảnh chụp client đang “waiting for device” **không tính PASS**.

## 11/11 — batch và nơi lưu bền vững

Ban đầu `~/edl` của antiX Live nằm trên lớp overlay trong RAM, không an toàn để làm kho lớn. Sau đó chủ thiết bị đã phê duyệt sử dụng phân vùng HDD riêng, tạo và mount **ext4 ~9,8 GiB**, đường làm việc `/mnt/H01-DATA/H01-backup`. Kiểm tra quyền ghi đã PASS. Việc mount phải thực hiện lại ở phiên Live mới; điều này đã được ghi trong nhật ký.

Sau khi ổ lưu được xác nhận, các batch được ghi nhận hoàn tất theo thứ tự:

| Nhóm | Phạm vi |
| --- | --- |
| Boot-security | `devcfg`, `cmnlib`, `cmnlibbak`, `keymaster`, `keymasterbak` |
| Small misc | `apdp`, `pad`, `misc` |
| OEM/config | `oem`, `config` |
| Images lớn | `vendor`, `system` |
| Product/boot | `productinfo`, `boot`, `persist`, `recovery` |
| Modem/radio/security | 15 phân vùng thuộc nhóm `modem`, `fsg*`, `modemst*`, `sec`, `fsc`, `ssd` và các thành phần liên quan |
| Các mục còn lại | `cache`, `userdata`, các vùng metadata GPT |

Nhật ký ghi các bước đóng ZIP, sidecar SHA-256 và chuyển bản sao sang iPhone; bản `userdata` kích thước **5.440.510.464 byte** được lưu ngoài ZIP vì dung lượng lớn. **Bản sao dữ liệu radio, SoftSIM và userdata không thuộc phạm vi công bố GitHub.**

## Kiểm tra hoàn chỉnh trên iPhone

Hai bản ghi kiểm tra mang số khác nhau, **không mâu thuẫn về GPT**:

| Mốc báo cáo | ZIP | IMG trong ZIP | IMG độc lập | Kết quả |
| --- | ---: | ---: | ---: | --- |
| Mục 95 (trước) | 18 | 41 | 1 | 42/42 SHA-256 MATCH |
| Mục 98 (bổ sung) | 19 | 45 | 1 | 46/46 SHA-256 MATCH |

Đến mốc sau, bộ kiểm kê đã chọn được ứng viên tương ứng **42/42 phân vùng GPT**, trong khi 46 đối tượng còn gồm ảnh GPT metadata và những bản dump boot/recovery khác thế hệ. Kiểm tra các bản sao với sidecar và CRC ZIP **không chứng minh** ảnh gốc được đọc đúng LBA, không chứng minh tính xác thực của OEM và không bảo đảm có thể restore.

## 14/11 — kiểm tra những vùng ngoài User Area

Đợt Firehose PPN 1/2 trả hai payload **4 MiB toàn `0x00`**; chưa xác minh đó là dữ liệu thật của Boot1/Boot2 vật lý. Các log eMMC/RPMB chịu giới hạn SELinux/DAC trên Android. Không đánh đồng hai ảnh zero-filled với boot chain đã sao lưu. Xem [Boot Area](emmc-boot-areas.md).

## Trạng thái hiện tại của ghi chép

- Tài liệu này là lịch sử công việc **đã làm**, không phải hướng dẫn thực thi lại EDL.
- Bản sao phân vùng gốc, ZIP, IMG, sidecar và full log **để riêng**; chỉ số lượng, phân loại và kết luận được công khai.
- Chưa có [factory package](oem-firmware-sources-and-support.md) hoặc [restore đầu-cuối](../boot/recovery-readiness.md) được kiểm chứng.