# Tổng quan phần cứng H01

**Nguồn:** bản ghi nghiên cứu Notion "H01 – Nghiên cứu firmware GlocalMe K1 / Qualcomm MSM8909" (dữ liệu thu thập trên thiết bị, cập nhật 18–21/11/2026). Chưa xác minh độc lập cho các biến thể khác.

| Thành phần | Ghi nhận |
| --- | --- |
| Model | ZEUS H01; máy thử nhận dạng nền tảng GlocalMe K1 |
| Chipset | Qualcomm MSM8909, 4 nhân ARMv7 Cortex-A7 |
| OS | Android 8.1.0, API 27 |
| Kernel snapshot | nhánh 3.18.71-perf |
| RAM snapshot | MemTotal khoảng 929.480 kB |
| Storage | eMMC hạng 8 GB |
| Màn hình | 240×320 ở cấu hình UI nghiên cứu |
| Kết nối | USB-C; giao diện Wi-Fi hotspot; đường modem Qualcomm |

## PCB, UART, test pad

Trên ảnh bo mạch có ký hiệu `CSMF1_MB_VA` và các nhãn như `GND`, `RX`, `TX`, `VIO`, `BOOT`. **Tên in không phải sơ đồ pinout đáng tin cậy**. Chưa xác nhận đầy đủ các điểm cấp nguồn, UART/EDL hoặc mức điện áp an toàn; không nối tắt các pad dựa trên nhãn.

## Các câu hỏi còn mở

- Sự tương đồng giữa biến thể H01, GlocalMe K1 và các thiết bị ZEUS khác.
- Sơ đồ phần cứng, khả năng dùng SIM thứ hai, tuyến âm thanh và cấu trúc nguồn.
- Khác biệt phiên bản PCB/GPT theo lô sản xuất.
