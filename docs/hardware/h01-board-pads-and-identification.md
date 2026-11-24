# ZEUS H01 / GlocalMe K1 — nhận dạng bo mạch và các pad chưa xác minh

**Nguồn:** [Nhật ký Notion H01, H001–H003](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), thu thập ban đầu tháng 11/2026. **Trạng thái: BOARD LABELS OBSERVED, pinout UART/EDL NOT VERIFIED.**

## Nền tảng

| Thuộc tính | Phép đọc / nhận dạng |
| --- | --- |
| Thiết bị thương mại | ZEUS H01 |
| Nhận dạng Android/OEM | GlocalMe K1, Qualcomm **MSM8909** |
| Android / ABI | **8.1 Oreo**, API 27, ARMv7 / `armeabi-v7a` |
| CPU | 4 nhân Cortex-A7 theo snapshot `/proc/cpuinfo` |
| Kernel | **3.18.71-perf-gd35e91f** trong mốc dump |
| RAM Android | `MemTotal=929.480 kB` (không phải lượng RAM free) |
| eMMC User Area | Báo cáo EDL sau này ghi **15.269.888×512 byte** (~7,82 GB thập phân) |

Trong ghi chép đầu có chuỗi `K1_TSU3.1.005.001.240116_20240116-1930`; các lần `ro.build.display.id` về sau cũng ghi biến thể `TSV`. **Không coi TSU và TSV chắc chắn là một build duy nhất** cho tới khi có bản dump thuộc tính cùng thiết bị/đợt.

## PCB

Ảnh mặt bo cho thấy ký hiệu **`CSMF1_MB_VA`**, **`2209 BW7`** và **`05-01`**. Các pad được in nhãn:

```text
GND · VPH · BOOT · VIO · RX · TX · TEMP · ID · PWR
USB DM · DP · VBUS
```

Đây là **nhãn quan sát trên ảnh PCB**. **Chưa có sơ đồ pinout chính thức, mức logic được xác nhận cho mọi pad, chức năng BOOT/EDL hoặc nối tương ứng tới SoC** trong mục nguồn ban đầu. Không cấp nguồn trực tiếp vào `VPH/VIO`, nối tắt `BOOT`, hoặc gắn USB-UART vào RX/TX chỉ vì tên in trên bo.

## Phạm vi nghiên cứu

- Android 8.1, MSM8909, GPT/eMMC và boot chain là các mảng có bằng chứng từ Android + Firehose.
- Modem LTE, SIM vật lý, chân test/JTAG/UART vẫn cần giữ phân biệt **hình ảnh/chuỗi** với **phép đo điện đã kiểm chứng**.
- Không phát hành ảnh bo chứa serial/QR/định danh hoặc tài liệu có thể định danh máy.

Xem [hardware overview](overview.md), [Dual SIM/PCB](../network/dual-sim-ril-pcb-evidence.md) và [eMMC](../firmware/gpt-layout.md).