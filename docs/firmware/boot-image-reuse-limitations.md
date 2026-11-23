# H01 — ảnh boot Magisk và giới hạn kế hoạch nhân bản sang máy khác

**Nguồn:** [Notion kế hoạch sao lưu boot / máy H01 thứ hai](https://app.notion.com/p/41ec5d5277a98103978ce6392e948073), 20/11/2026. Biên soạn 24/11/2026. **Đây là kế hoạch lịch sử, chưa có phép thử H01 thứ hai PASS; chủ dự án hiện không có máy thứ hai.**

Báo cáo đã so ảnh boot Magisk đang chạy với ảnh cứu hộ bằng FC, kích thước **33.554.432 byte**, kết quả **no differences encountered**. Ảnh đã vá Magisk **không phải boot xuất xưởng** và là ảnh được chụp **trước khi thử Auto Power-On v0.6**.

| Thành phần | Có trong ảnh boot Magisk được so? |
| --- | --- |
| Kernel, ramdisk và init Magisk | Có |
| Launcher3, H01 Home, ứng dụng trong system | **Không** |
| Module Magisk AutoHotspot, cài đặt Home, dữ liệu Wi-Fi | **Không** — nằm tại các nguồn khác, thường userdata |
| Firmware modem/system/vendor và dữ liệu người dùng | **Không** |
| Thay đổi Auto Power-On v0.6 sau đó | **Không có trong ảnh BEFORE-v06** |

Kế hoạch nguồn đề xuất đối chiếu board, firmware, GPT, lock state và tạo backup riêng từng máy trước khi cân nhắc tái tạo. **Không được gọi đây là quy trình đã chạy được trên máy thứ hai**, và không biến bộ ảnh của một thiết bị thành factory ROM chung.

Đặc biệt không dùng các phân vùng riêng `modemst1/2`, `fsg`, `persist`, `userdata`, `keystore/keymaster`, `productinfo`, `devinfo` hoặc dữ liệu SoftSIM/NV từ H01 này để ghi mù vào máy khác.

**Theo quyết định hiện tại, nhánh thử máy thứ hai đã dừng vì không có máy.** Đợt này chỉ ghi tài liệu, không tạo gói clone/script flash hay yêu cầu mượn thêm H01. Xem [tổng quan sao lưu](backup-and-reconstruction.md), [mốc boot lạnh](../boot/auto-power-on-cold-boot-evidence.md).