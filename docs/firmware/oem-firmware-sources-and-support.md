# Truy tìm nguồn firmware ZEUS H01 và phản hồi hỗ trợ OEM

**Nguồn:** nhật ký Notion H01, mục 26–31, ngày 10/11/2026. **Phân loại: tổng hợp nguồn nghiên cứu lúc đó và nội dung phản hồi hỗ trợ đã ghi; chưa tự xác minh lại trạng thái website hiện tại.**

## Đối chiếu thiết bị

- Tài liệu sản phẩm ZEUS WiFi Nhật Bản nêu thiết bị **H01**, màn hình cảm ứng, nguồn USB-C, khe SIM và giao diện kiểm tra cập nhật.
- Một bài đánh giá kỹ thuật được trích trong nhật ký nêu H01 dùng Qualcomm MSM8909 và liên quan uCloudlink; điều này phù hợp snapshot thiết bị H01: Android 8.1, `msm8909`, model nội bộ `K1`.
- Tài liệu ZEUS công khai tại thời điểm khảo sát **không xác nhận** đúng mã bo mạch/phiên bản nội bộ và build của từng H01. Không chọn ROM chỉ vì trùng tên `K1`.
- Nhật ký có đề cập HUMAN LIFE là pháp nhân vận hành ZEUS WiFi Nhật Bản sau quá trình chuyển đổi doanh nghiệp; thông tin đơn vị vận hành không thay thế quyền cấp firmware gốc từ uCloudlink.

## Tình trạng tìm firmware theo bản ghi ngày 10/11

Đã rà đúng chuỗi build, internal model K1, Qualcomm MSM8909 và các danh mục firmware công khai, nhưng **không tìm được factory ROM/recovery ZIP/manifest chính thức có thể chứng minh tương thích với mẫu nghiên cứu**. Các tệp mang chữ K1 của thiết bị không liên quan phải được loại trừ.

Các thông báo dịch vụ ZEUS WiFi Nhật Bản mà báo cáo ngày 10/11 dẫn lại bao gồm kế hoạch và kết thúc dịch vụ cho thiết bị H01 cũ đầu năm 2026. **Đó là vòng đời nhà mạng/nhà khai thác, không phải bằng chứng phần cứng H01 không còn chạy LTE hoặc firmware không thể dùng với mạng khác.**

## Phản hồi từ uCloudlink trong hồ sơ

Trong ngày 10/11/2026, tài khoản hỗ trợ `service@ucloudlink.com` trả lời yêu cầu factory/recovery firmware. Theo hồ sơ lưu lại:

- Factory firmware, full recovery package, partition manifest, EDL/Firehose tool và thông tin chữ ký **không sẵn có để phân phối ra ngoài**.
- Hãng **không hỗ trợ tự flash firmware** và hướng khách hàng có sự cố sang dịch vụ hậu mãi.
- Bộ phận hỗ trợ đề nghị gửi IMEI để nhận diện/hỗ trợ thiết bị; **không xuất IMEI, thread ID, email riêng hoặc phần đính kèm** lên GitHub.

Cần phân biệt: “không phân phối ra bên ngoài” **không có nghĩa OEM không giữ bản nội bộ**. Không có file flash, Firehose loader, signing material hoặc link factory image hợp lệ được cung cấp từ thư phản hồi này.

## Kết luận cho dự án

Đường firmware chính thức chưa được xác nhận có tài nguyên tải công khai cho chính mẫu H01. Vì vậy kho [sao lưu eMMC](emmc-backup-verification.md) có giá trị nghiên cứu, nhưng **không được đóng nhãn “factory ROM chính hãng”** và cũng chưa có quy trình [cứu hộ đầu-cuối](../boot/recovery-readiness.md).

Tài liệu không tiết lộ IMEI, cấu hình SoftSIM, ticket hỗ trợ, token, đường dẫn tải riêng hoặc binary có điều kiện phân phối.