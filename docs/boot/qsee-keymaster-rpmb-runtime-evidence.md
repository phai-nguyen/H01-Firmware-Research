# H01 — phân biệt QSEE/Keymaster TA, RPMB/SSD listener và boot property

**Nguồn trực tiếp:** [Nhật ký Notion H01 — H110–H114 (11/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), bao gồm ABOOT keystore, chữ ký image và log runtime QSEE/Keymaster. **Phân loại: STATIC VERIFIED + LOG RUNTIME OBSERVED; các thao tác Root of Trust/attestation chưa được xác minh đầu-cuối.**

## Keystore nằm trong ABOOT khác với Keymaster TA

Phân tích ABOOT tìm **object ASN.1 DER 1.619 byte** được đưa qua parser của boot-verifier. Nội dung gồm keystore/keybag chứa **RSA public key 2048 bit** với exponent 65537, certificate X.509 và object chữ ký. Authenticated inner DER dài **298 byte** được đối chiếu với trường declared length; bài kiểm tra OpenSSL trong hồ sơ ghi chữ ký inner keystore **hợp lệ với public key đi kèm**.

Bằng chứng này chỉ chứng minh **mối quan hệ mật mã nội bộ** của object được phân tích, **không chứng minh** private key của hãng, fuse SoC, hoặc nguồn tin cậy phần cứng đã xác minh toàn chuỗi. Một số chuỗi certificate dùng nhãn Android generic, không thể tự coi là keystore riêng do ZEUS phát hành.

Đối chiếu với source họ Qualcomm LK: ký image sử dụng **SHA-256 + RSA PKCS#1 v1.5** và kiểm tra DigestInfo dài **51 byte**; verify image còn kiểm target và length. Tuy nhiên source-family **không phải** mã nguồn hãng đã được cung cấp, nên các diễn giải từ source chỉ được gắn nhãn đối chiếu, không phải chứng minh C-level byte-for-byte.

## Log Android: có TA và listener, không chứng minh lệnh bảo mật thành công

| Bằng chứng từ log H01 | Giải thích chính xác |
| --- | --- |
| QSEECom ban đầu báo `keymaster.mdt` không tìm được trong `/firmware/image` | Một đường tự nạp TA thất bại |
| Lượt kế tiếp báo `App is already loaded QSEE` với app ID 1 | Keymaster TA **được nhận diện là đã nạp** ở thời điểm retry |
| KeymasterUtils nhận API **3.0**, TA version **3.120** | TA đáp ứng truy vấn phiên bản |
| `android.hardware.keymaster@3.0` đăng ký `IKeymasterDevice/default` | Android HAL đã đăng ký được |
| `librpmb.so` / listener ID **0x2000** và `libssd.so` / ID **0x3000** | Dịch vụ QSEE RPMB/SSD đã khởi tạo/started |
| RPMB log `Mult=1024`, sector 512 byte | Phép tính theo log là **512 KiB**, chưa thay thế đọc EXT_CSD thực |

Việc Keymaster TA đã loaded sau khi thử tìm file bị lỗi **không đủ** để khẳng định ABOOT chính là thành phần nạp TA. Listener RPMB/SSD trả init/start thành công **không chứng minh** authenticated RPMB read/write, provisioning key, attestation hoặc secure-storage nghiệp vụ đã hoạt động.

## Cảnh báo về boot properties

Snapshot có:

```text
ro.boot.keymaster=1
ro.boot.authorized_kernel=true
ro.boot.verifiedbootstate=green
ro.boot.veritymode=enforcing
```

`ro.boot.keymaster=1` là bootloader property truyền vào Android, **không phải phiên bản TA** hoặc chứng cứ Keymaster đã xác minh Root of Trust. `ro.boot.verifiedbootstate=green` ở mốc cũ cũng không mâu thuẫn với `orange` sau khi người dùng mở khóa ở mốc mới hơn. Tham khảo [Boot verification](boot-verification-chain.md) và [timeline unlock](oem-unlock-failed-attempts.md).

**Không công bố** DER blob, khóa công khai nhúng của OEM, định danh/khóa thiết bị, raw keymaster logs, dữ liệu RPMB, image QSEE hoặc hướng dẫn sửa unlock/keystore.