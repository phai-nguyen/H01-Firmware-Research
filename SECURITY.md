# Chính sách bảo mật và công bố dữ liệu

**Không mở Public, đăng Issue hoặc gửi Pull Request chứa các dữ liệu sau:**

- Firmware nguyên bản, bản dump eMMC/NAND, `userdata`, `persist`, `modemst`, `fsg`, `keystore`, tệp OTA nguyên gốc chưa có quyền phân phối.
- IMEI, MEID, IMSI, ICCID, eSIM/SoftSIM profile, địa chỉ/định danh thuê bao, số điện thoại, MAC riêng, mật khẩu Wi-Fi, token, cookie, tài khoản, mật khẩu, khóa ký hay chứng thư riêng.
- Log hệ thống chưa được ẩn danh; ảnh chụp màn hình có dữ liệu cá nhân.

Nếu phát hiện lộ dữ liệu: **ngừng chia sẻ, thu hồi/vô hiệu hóa khóa có thể thu hồi**, và liên hệ chủ repository qua kênh GitHub bảo mật trước khi công khai lỗi. Xóa một commit không bảo đảm xóa bản sao hoặc lịch sử.

Các báo cáo lỗ hổng bảo mật nên dùng **GitHub Private Vulnerability Reporting** nếu repository bật tính năng đó; không đăng thông tin khai thác nhạy cảm trong issue công khai.

Các script kiểm tra tự động chỉ giúp phát hiện một phần rủi ro; **không thay cho rà soát thủ công**.
