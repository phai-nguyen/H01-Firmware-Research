# Nguồn gốc thông tin / Evidence provenance

Các ghi chép nguồn hiện nằm trong **Notion riêng của người nghiên cứu** và bản sao **Dropbox `/H01/EMMC`**; đây **không phải nguồn tải công khai**. Không thêm liên kết chia sẻ cá nhân, thông tin nhận dạng thiết bị, mã khóa hoặc tập tin OEM trước khi rà soát.

## Tài liệu gốc đã đối chiếu khi soạn v0.1.0

| Nguồn | Ngày / nội dung | Đã chuyển thành |
| --- | --- | --- |
| Notion — "H01 – Nghiên cứu firmware GlocalMe K1 / Qualcomm MSM8909" | ghi chép tổng quan, boot, phân vùng, root (cập nhật đến 21/11) | hardware, firmware, boot |
| Notion — "H01 — Nghiên cứu OTA, cách lấy firmware gốc và kiểm chứng bản sao" | 22/11/2026 | firmware/ota |
| Notion — "H01 — Bằng chứng Dual SIM trong firmware và PCB" | 20/11/2026 | network/dual-sim |
| Notion — "H01 — Báo cáo lỗi AudioTrack, ALSA và Audio HAL" | 21/11/2026 | system/audio |
| Notion — "H01 — Launcher3 AutoHotspot v0.4 PASS sau reboot" | 20–21/11/2026 | projects/autohotspot |
| Dropbox — `/H01/EMMC` | nhiều bản `.img`, `.sha256`, báo cáo và CSV nội bộ | chỉ dùng kiểm kê **không xuất tệp gốc** |
| GitHub — `phai-nguyen/H01`, `H01-Display-Control`, `H01-Hidden-Settings` | README các dự án đang phát triển | projects/index |

Đây là **bản tổng hợp** từ nhật ký nguồn, chưa phải quy trình kiểm thử tái lập độc lập trên một H01 khác. Các tài liệu gốc Notion có thể chứa nhiều phiên bản/mốc lịch sử; lấy kết luận cập nhật nhất và ghi rõ giới hạn. Khi công bố log minh chứng, phải kiểm tra thủ công từng dòng và ảnh đính kèm.

## Đối chiếu bổ sung v0.2.0

- `/H01/EMMC/H01-partitions-20261111.csv`: bản kê 42 phân vùng có GUID; GitHub **chỉ chứa** các cột thứ tự, tên, LBA, sectors và bytes.
- `/H01/EMMC/H01-GPT-map-20261111.txt`: kiểm tra CRC/backup GPT, đếm 42/44 entry; không tái xuất DiskGUID hay UniqueGUID.
- Sidecar `H01-system-20261111.sha256`, `H01-boot-20261111.sha256`: xác nhận định dạng `sha256sum` cho công cụ offline; không sao chép hash thật lên GitHub.
- Công cụ v0.2.0 mới được kiểm tra bằng unit test và kiểm tra tĩnh; **chưa ghi nhận PASS khi chạy trên H01 thực tế**.
