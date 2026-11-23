# ZEUS H01 — hồ sơ so sánh thiết bị A/B ngày 23–24/11/2026

**Nguồn:** trang Notion “H01 MÁY MỚI #2 — cùng firmware: mở khóa, root, Launcher3, IME và xoay PASS (23–24/11/2026)”. **Bản tổng hợp từ nhật ký**, không đo mới trên thiết bị. **Thiết bị A** là mẫu được nghiên cứu trước; **B** là mẫu được ghi nhận trong hồ sơ này. Không công khai serial, Sahara HWID/PK_HASH hoặc số định danh khác.

## Phần được xác nhận

| Thuộc tính/đặc điểm | Kết quả theo nhật ký |
| --- | --- |
| Nền tảng | ZEUS H01/GlocalMe K1, MSM8909, Android 8.1/API 27 |
| Build hiển thị máy B | `K1_TSV3.1.005.001.240116` |
| GPT B | Đã đọc được 42 phân vùng qua EDL |
| ABOOT A so với B | Có **hash trùng nhau** trong hai ảnh khảo sát |
| Boot nguyên bản A so với B | **Hash khác nhau**; không dùng mù ảnh boot máy khác |
| Bootloader B | Từ locked/green sang unlocked/orange, giữ qua một lần reboot |
| Magisk B | Boot RAM rồi vá boot riêng của B; root cố định PASS theo log |
| Giao diện B | H01 Home, Launcher3, thanh phím Android, IME và xoay có các mốc PASS riêng |

**Không áp dụng mặc định kết quả của A cho B:** Auto Power-On v0.6, AutoHotspot, AutoShow 4G, SIM 2, logo boot và các ứng dụng OEM khác chưa có bằng chứng PASS trên B từ trang này. Share Server/J2ME Loader mới chỉ có bộ cài được gửi tới B, **chưa có xác nhận chạy chức năng riêng trên B**.

## Nguyên tắc phân biệt hồ sơ

Những hướng dẫn và ảnh boot của A thuộc mốc lịch sử trước; sau khi có bản sao riêng, ảnh boot Magisk của B được vá từ **boot gốc của B**. Không coi ảnh hoặc checksum của A là bản phục hồi dùng chung. Cũng không gọi các ảnh đã sao lưu thành **factory firmware**, và không gộp các khóa/hiệu chuẩn/SoftSIM/NV của hai máy.

Đây là **bản biên soạn đã lược bỏ định danh**: giữ riêng các file IMG, thông tin EDL, serial, log riêng và liên kết tới kho cá nhân. Xem [Boot/root B](../boot/device-b-unlock-root-evidence.md), [IME B](../system/device-b-launcher-ime-evidence.md), [xoay B](../system/device-b-rotation-evidence.md).