# H01 App Control — nghiên cứu quản lý ứng dụng và dịch vụ

**Trạng thái: PROPOSED / PARTIAL.** Chưa có bằng chứng một ứng dụng có thể bật/tắt **toàn bộ** dịch vụ OEM an toàn.

Mục tiêu: quản lý package hệ thống, ứng dụng ẩn, ứng dụng tự cài và trạng thái thực thi. Cần phân biệt:

1. `PackageManager`: package đã cài, `enabled` và `hidden`.
2. `ActivityManager`: Activity/Service/Process đang chạy.
3. `init.rc`: dịch vụ native của Android/OEM.
4. Root Magisk: quyền thực thi, **không tự động biết phụ thuộc giữa dịch vụ**.

Cơ sở: [kiểm kê 473 component](../system/hidden-feature-inventory.md), [Hidden Settings](https://github.com/phai-nguyen/H01-Hidden-Settings), các báo cáo thử tối ưu RAM/FOTA/GlocalMe Feedback và công cụ ADB chỉ đọc.

Điều kiện triển khai: phân nhóm rủi ro, xác minh mỗi hành động, lưu trạng thái trước/sau, hạn chế các service mạng/modem/OTA, và có phương án bật lại qua ADB nếu UI mất. Không làm nút “Tắt tất cả” hay ẩn GlocalmeHome/Launcher3 mù.

**Nguồn:** chủ đề nghiên cứu App Control và tối ưu RAM H01 ngày 17–21/11/2026; chưa phải ứng dụng hoàn thiện.