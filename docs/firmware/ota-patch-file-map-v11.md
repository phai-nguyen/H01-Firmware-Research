# H01 OTA v11 — vùng bsdiff/new giao với các tệp ext4

**Nguồn:** [Notion OTA H01](https://app.notion.com/p/420c5d5277a981ddbe17ca37e72e91df), mục 14, ngày 22/11/2026. **Trạng thái: phân tích chỉ đọc ảnh system/vendor build 87.**

Báo cáo ánh xạ vùng block `bsdiff/new` sang tệp: **17 tệp thường ở system và 1 tệp thường ở vendor** có dữ liệu giao vùng vá. Đây là giao vùng, **không chứng minh toàn bộ tệp đổi** hoặc bản vá đã được thực thi trên máy.

| Nhóm | Tệp được nhận diện |
| --- | --- |
| UService | `Uservice.apk`, `libJniUcst.so`, ODEX/VDEX |
| Dịch vụ Android | `services.art`, `services.odex`, `services.vdex`, `services.jar.prof` |
| UCloud / ADB | `adbd`, `uC_MsgRouter`, `uC_WebServer` |
| Cấu hình | `system/build.prop`, `etc/prop.default`, `vendor/build.prop` |
| Recovery | `install-recovery.sh`, `recovery-from-boot.p` |
| Khác | `cdrom_install.iso`, `ucloud/git.log` |

Phân tích này **chưa bao gồm các lệnh move**. Chỉ thấy các vùng thư mục liên quan FOTA/GlocalmeHome, không thấy byte APK/DEX giao vùng bsdiff/new của hai app; **không được nói hai app không thay đổi** vì không xét mọi cơ chế delta.

Bản đích có `ro.secure=1`, `ro.adb.secure=0`, `ro.debuggable=0`, `ro.ukl.open.adb.root=true`, `ro.sys.usb.default.config=diag,serial_smd,serial_tty,adb`. Đây là giá trị **ảnh đích**, không chứng minh những cờ này được thêm mới từ bản 81 hoặc adbd thật chạy UID 0.

`install-recovery.sh` liên quan vùng đầu Recovery **22.381.868 byte**, báo cáo so SHA-1 của vùng đó đạt. Hai ảnh còn có verity/FEC metadata ngoài ext4; **chưa kiểm tra lại cây hash/FEC hoặc chữ ký verity**. Bộ báo cáo trích 18 tệp thường và đối chiếu SHA-256; parser ext4 có kiểm tra ranh giới nhưng **chưa so bằng parser độc lập**.

Không công khai dữ liệu từng tệp OEM đã trích, ODEX/VDEX, image hoặc bản vá. Đây là bản ghi phân tích đã có, không phải gói sửa firmware.

Xem [v10 integrity](ota-delta-validation-v10.md), [UService](../system/uservice-loader.md).