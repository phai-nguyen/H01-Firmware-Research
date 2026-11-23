# H01 — bằng chứng chi tiết DSDS, RIL2 và PCB hai đầu đọc

**Nguồn:** [Notion Dual SIM H01 (20/11/2026)](https://app.notion.com/p/41ec5d5277a9811a916cc87d0bac9d3b). **Trạng thái: firmware DSDS/RIL2 VERIFIED, hai SIM vật lý đồng thời CHƯA PASS.**

## Dữ liệu thực tế

- `persist.radio.multisim.config=dsds`; `gsm.sim.state=READY,ABSENT`; `gsm.network.type=LTE,Unknown`.
- `init.svc.ril-daemon=running` và **`init.svc.ril-daemon2=running`**.
- `persist.vendor.radio.msim.stackid_0=0`, `persist.vendor.radio.msim.stackid_1=1` (và cặp `stack_id_0/1` tương ứng).
- `ucloud.oem.conf.local_sim=true`, `uservice.control.slot0=true`; giá trị slot1 chưa có trong snapshot nguồn.
- Hai giá trị IMEI có trong getprop gốc đã được **loại bỏ** khỏi tài liệu công khai.

## Cấu hình init và các thành phần OEM

Vendor init khai báo RIL chính `/vendor/bin/hw/rild`. `init.qcom.rc` còn có `ril-daemon2 /vendor/bin/hw/rild -c 2`, socket `rild2`, và một stanza `ril-daemon3 ... -c 3`. Hai stanza có từ khóa `disabled` để tránh tự khởi chạy theo class; việc `ril-daemon2` xuất hiện **running** ở runtime có nghĩa đã được khởi động bằng cơ chế khác. **Stanza ril-daemon3 không chứng minh H01 có SIM thứ ba.**

Tài liệu UService ghi `slotId`, `subId`, `card.state`, `switch_m2_phy_mode`, `switch.vsim.plmn`; đây là bằng chứng **có code điều khiển**, không chứng minh broadcast đó dùng được hoặc an toàn.

## Hai đầu đọc trên bo mạch

Ảnh PCB thật do chủ H01 cung cấp thấy **hai cấu trúc đầu đọc thẻ kim loại**. Trong tài liệu thương mại Recharge WiFi H01 ver7 lại mô tả **Nano SIM slot ×1**; tài liệu ZEUS nêu khe SIM truy cập ngoài. Không thể khẳng định cả hai đầu đọc đều là Nano-SIM được nối điện đầy đủ chỉ từ hình ảnh. Chưa có phép thử mỗi vị trí và hai SIM đồng thời trong trang nguồn.

| Nhận định | Trạng thái |
| --- | --- |
| Firmware DSDS và hai RIL logic | **VERIFIED** |
| Hai đầu đọc kim loại vật lý | **Ảnh PCB** |
| Cả hai là SIM hoạt động | **Chưa kiểm tra điện/cơ** |
| Hai SIM dùng đồng thời | **Chưa thử** |
| Hai kết nối dữ liệu 4G đồng thời | **Không suy được từ DSDS** |

Không công khai dữ liệu ICCID, IMEI/IMSI, mã khóa SIM, SoftSIM/NV hoặc thử điều khiển radio trong đợt xuất bản. Xem [tổng quan DSDS](dual-sim.md).