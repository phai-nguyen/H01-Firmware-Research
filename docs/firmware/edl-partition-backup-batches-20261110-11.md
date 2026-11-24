# H01 — nhật ký sao lưu EDL theo từng nhóm (10–11/11/2026)

**Nguồn:** [Nhật ký H01 các mục H035–H087](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd). **Đây là bản tổng hợp kết quả đã lưu, không phải hướng dẫn thao tác trên thiết bị.**

## Các đợt READ

| Thời gian | Nhóm | Bằng chứng |
| --- | --- | --- |
| 10/11 | `splash` | Firehose READ 100%, **10.485.760 byte** |
| 10/11 | `sbl1/sbl1bak` | Mỗi tệp **524.288 byte**, ảnh đã chuyển sang iPhone |
| 10/11 | `aboot/abootbak` | Mỗi tệp **1.048.576 byte** |
| 10–11/11 | `rpm/rpmbak` | Mỗi tệp **524.288 byte** |
| 10–11/11 | `tz/tzbak` | Mỗi tệp **2.097.152 byte** |
| 11/11 | Boot-security | Batch 5 phân vùng: `devcfg`, `cmnlib`, `cmnlibbak`, `keymaster`, `keymasterbak` |
| 11/11 | Misc | `apdp`, `pad`, `misc` |
| 11/11 | OEM | `oem`, `config` |
| 11/11 | Hệ thống | `vendor`, `system`, dump kích thước khớp GPT |
| 11/11 | Product/boot | `productinfo` **64 MiB**, `boot/persist/recovery` **32 MiB mỗi ảnh** |
| 11/11 | Radio/security | 15 phân vùng, gồm `modem`, `DDR`, các vùng `fsg*`, `modemst*`, `sec`, `fsc`, `ssd`, `keystore` |
| 11/11 | Cache | **115.343.360 byte**, kiểm SHA-256/ZIP |
| 11/11 | Userdata | **5.440.510.464 byte**, 10.625.997 sector; SHA-256 `OK`, chuyển iPhone |

Mã nguồn EDL V3.62 hỗ trợ **đọc tuần tự nhiều partition trong một phiên kết nối**, không phải chụp snapshot atomic. Các báo cáo READ 100% chứng minh công cụ đọc đủ số sector dự kiến, **không chứng minh chính xác mọi byte firmware OEM hoặc khả năng khôi phục**.

## Lưu trữ antiX

Thư mục `~/edl` ban đầu nằm trên **overlay/RAM** của antiX Live (~1,5 GiB), không bền qua reboot. Chủ thiết bị đã chấp thuận dành một phân vùng HDD **ext4 ~9,8 GiB** làm kho lưu, xác minh mount và quyền ghi. Đây là điều kiện quan trọng trước khi đọc `system` và `userdata`. Các bước format HDD đã xảy ra trong lịch sử, **không phải hướng dẫn chạy lại**.

## Kết quả

Nguồn tổng hợp ngày 11/11 ghi **42/42 phân vùng GPT có ảnh và sidecar**, nhưng số IMG có thể vượt 42 khi tính cả ảnh GPT metadata và các thế hệ dump. Không đăng ảnh OEM, userdata, dữ liệu SIM/NV hoặc đường dẫn riêng.

Xem [đối chiếu ZIP/iPhone](emmc-iphone-gpt-integrity-timeline.md), [GPT gaps](gpt-unallocated-regions-and-integrity.md).