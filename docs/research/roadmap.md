# Lộ trình dự án

## v0.1 — Tài liệu cơ sở

- [x] README tiếng Việt và tiếng Anh.
- [x] Giấy phép tách mã nguồn và tài liệu.
- [x] Mốc kỹ thuật chính từ nguồn lưu trữ.
- [x] Chính sách không công bố firmware gốc / thông tin nhạy cảm.
- [x] Mẫu Issue và kiểm tra tệp public cơ bản.
- [x] Tạo repository GitHub Public và đưa 26 tệp tài liệu/công cụ lên nhánh `main` (23/11/2026).

## v0.2 — Chứng cứ và công cụ

- [x] Bảng GPT 42 phân vùng (không chứa GUID riêng của thiết bị) và kiểm tra tính nhất quán trong CI.
- [x] Mẫu báo cáo ADB read-only Windows 7 / Linux; cần kiểm thử thực tế trên H01.
- [x] Mở rộng bảng phân loại PASS/FAIL/PENDING; chứng cứ raw tiếp tục ở kho riêng.
- [x] Đã mở các chủ đề GPT, OTA, Dual SIM và App Control (liên kết trong Issues).

## v0.3 — Cộng đồng

- [ ] Hướng dẫn môi trường phát triển ứng dụng.
- [ ] Tự động kiểm tra Markdown, cấu trúc tài liệu và tệp đầu vào.
- [ ] Quy trình xây dựng Release có checksum, changelog và dấu mốc kiểm thử.
- [ ] Bản dịch tiếng Anh cho các tài liệu chính.

## Lô tổng hợp Notion → GitHub (23/11/2026)

- [x] Kiểm kê 15 trang Notion trong cây H01 và tài liệu đang có ở repo.
- [x] Chuyển 12 chuyên đề kỹ thuật có trạng thái và nguồn đối chiếu, bổ sung README/Changelog.
- [x] Lập [bảng độ phủ](notion-coverage.md) và [danh sách chưa hoàn tất](publication-backlog.md).
- [ ] Rà soát các báo cáo TXT/ZIP, ảnh, video từ kho riêng trước khi trích đăng.
- [ ] Trích biên soạn các nghiên cứu còn lại trong trang Notion tổng (không sao chép log nguyên văn).
- [ ] Kiểm tra links/CI và xây dựng GitHub Release tài liệu có checksum.

- [x] Đánh chỉ mục 207 mục H2 của trang Notion tổng vào [Master Index](notion-master-index.md) mà không đưa log/tệp OEM lên GitHub.

## Mở rộng kiến trúc và lưu trữ — 23/11/2026

- [x] Biên soạn bảy báo cáo kỹ thuật có nguồn FOTA/UService/daemon, Firehose, integrity eMMC, Boot Area, OEM Unlock.
- [x] Phân loại trạng thái mới nhất so với các mục lịch sử trong nhật ký.
- [ ] Bổ sung sơ đồ boot chain và init service map đầy đủ (cần đối chiếu snapshot).
- [ ] Đưa công cụ parser read-only và tài liệu tái lập phép kiểm tra ZIP/CRC/SHA-256 lên repo sau khi kiểm thử.

## Lô biên soạn kernel/init/boot — 23/11/2026

- [x] Phân tích và ghi chép kernel uknet, init Qualcomm, quyền mount /firmware, tối ưu PSS.
- [x] Phân biệt boot-image verification với Fastboot flash gates từ Notion mục 107 (đã hiệu chỉnh).
- [x] Tài liệu hóa Magisk 30.7 qua boot RAM rồi root cố định, ghi chú giới hạn kiểm thử.
- [x] Tạo checklist cứu hộ mà không phát hành script flash OEM.
- [ ] Rà soát các báo cáo TXT/ZIP của kernel và công cụ cứu hộ tự viết để phát hành có nguồn, tests và giấy phép.

## Chốt phạm vi theo yêu cầu chủ dự án — 23/11/2026

- [x] Chuyển trọng tâm sang **đưa toàn bộ kết quả nghiên cứu H01 lên GitHub**.
- [x] Bổ sung bảy tài liệu nghiên cứu lịch sử còn thiếu, cập nhật README/Changelog/bảng đối chiếu.
- [ ] Tiếp tục chuyển nội dung các mục nghiên cứu khác trong Notion/kho tệp thành báo cáo kỹ thuật đã lọc, không xem chỉ mục 207 tiêu đề là đã hoàn tất toàn bộ.
- [ ] Không tạo app, script, bộ kiểm thử hoặc yêu cầu thử thiết bị mới khi nhiệm vụ hiện tại chỉ là **lưu hồ sơ nghiên cứu**.
