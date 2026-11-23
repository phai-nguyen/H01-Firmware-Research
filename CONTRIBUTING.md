# Hướng dẫn đóng góp / Contributing

Dự án chào đón Pull Request và Issue bằng **tiếng Việt hoặc tiếng Anh**. Ưu tiên tài liệu kỹ thuật có thể tái kiểm chứng, công cụ chỉ đọc và bản vá có cơ chế hoàn tác.

## Trước khi gửi

1. Mở Issue mô tả vấn đề hoặc đề xuất, liên kết báo cáo có liên quan.
2. Ghi **mã máy, build Android, trạng thái bootloader/root, ngày thử, bước tái hiện, kết quả mong đợi và kết quả thực tế** (nếu an toàn để chia sẻ).
3. Đánh dấu rõ `PASS` (đã quan sát), `FAIL` (có bằng chứng lỗi), `PENDING` (chưa thử), `HYPOTHESIS` (giả thuyết), `PAUSED` (tạm dừng).
4. Bỏ IMEI, ICCID, IMSI, số điện thoại, MAC cá nhân, SSID/mật khẩu, IP/host riêng, token, khóa ký, chứng chỉ riêng, tài khoản, dữ liệu modem và mọi thông tin nhạy cảm khỏi log, ảnh và mã nguồn.
5. Không đưa lên Git **boot/system/vendor/userdata .img**, OTA gốc, APK hãng, keybox, `modemst*`, `fsg*`, recovery gốc hoặc ảnh NAND/eMMC.
6. Nếu có sửa lỗi tác động hệ thống, ghi rủi ro mất dữ liệu/brick, phương pháp backup và rollback đã kiểm chứng. Không được gắn nhãn PASS chỉ vì build thành công.

## Mẫu báo cáo

```text
Thiết bị và build:
Phương pháp:
Dữ liệu đầu vào (không nhạy cảm):
Kết quả / log đã ẩn thông tin riêng tư:
Trạng thái: PASS | FAIL | PENDING | HYPOTHESIS | PAUSED
Hạn chế / điều chưa xác minh:
```

Bằng việc đóng góp mã nguồn/tài liệu nguyên gốc, người đóng góp đồng ý cấp phép phần đó theo MIT/CC BY 4.0 tương ứng. Không sao chép tài sản bên thứ ba khi chưa đủ quyền.
