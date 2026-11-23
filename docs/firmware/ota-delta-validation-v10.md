# H01 OTA 81 → 87 — đối chiếu chữ ký và vùng đích v10

**Nguồn:** [Notion nghiên cứu OTA H01 22/11/2026](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), mục 7–9 và cập nhật v10. **Trạng thái: ngoại tuyến; không cài OTA.**

## Thông tin gói

- OTA **block-based incremental**, pre-build Android 8.1 build 81, post-build 87; bản đích `K1_TSV3.1.005.001.240116_20240116-1930`.
- Dung lượng **44.118.207 byte**, cache yêu cầu theo metadata **56.673.792 byte**; có `system.patch.dat`, `vendor.patch.dat`, `patch/boot.img.p`, cùng delta bootloader/modem.
- `system.new.dat` và `vendor.new.dat` chỉ 4.096 byte theo báo cáo; **không phải ảnh phân vùng đầy đủ**.

## Toàn vẹn và chữ ký

Theo v8–v9, MD5, SHA-1 và **9 segmentMd5** của gói khớp metadata; ZIP CRC không lỗi. Chữ ký **CMS toàn gói** được OpenSSL xác minh ở mức mật mã. Public key Recovery `res/keys` khớp khóa RSA signer; chứng thư `META-INF/com/android/otacert` khớp signer CMS. Việc dùng `-noverify` **không xác minh chuỗi tin cậy CA**, và chữ ký OTA độc lập với chứng thư HTTPS Adups.

**Còn mở:** giá trị `data.sha256` máy chủ trả **không khớp SHA-256 toàn ZIP** do nhóm phân tích tính. Chưa biết trường server hash phần nào, không kết luận nó đã PASS.

## Đối chiếu bản sao build 87

V9: vùng đầu đúng chiều dài mà OTA kiểm tra của `boot`, `aboot`, `sbl1`, `rpm`, `modem` đã khớp hash **đích build 87**; không khớp hash **nguồn build 81**. Không suy rộng thành đã kiểm mọi byte eMMC.

V10 kiểm tra `system`: **2.102/2.102** lệnh đích (2.063 move, 30 bsdiff, 1 new, 8 zero); **145.776 block duy nhất** tương ứng **597.098.496 byte (~46,34% ảnh)**.

V10 kiểm `vendor`: **11/11** lệnh (6 bsdiff, 1 new, 4 zero); **5.818 block duy nhất**, **23.830.528 byte (~4,55% ảnh)**. `abootbak/sbl1bak/rpmbak` cũng khớp các vùng đích theo yêu cầu OTA.

- `move/bsdiff`: đối chiếu hash đích của lệnh.
- `new`: so byte với dữ liệu `new.dat`.
- `zero`: so byte zero.
- `erase` không định nghĩa giá trị byte cố định; `stash/free` là quản lý khối nguồn.
- Một số hash trong điều kiện trước cập nhật thuộc **build 81**, không dùng chúng để phán đoán ảnh đích build 87 sai.

## Giới hạn

**Không xác minh toàn ảnh system/vendor hoặc mọi phân vùng**, chưa có factory firmware đầy đủ hay thử khôi phục OTA. Không công khai ZIP OTA OEM, URL tải có credential, token, ID SIM, raw partitions hay script can thiệp TLS. Xem [bản đồ file v11](ota-patch-file-map-v11.md), [OTA tổng quan](ota.md).