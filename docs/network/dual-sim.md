# Dual SIM: firmware DSDS và phần cứng chưa rõ

**Nguồn:** trang nghiên cứu Notion 20/11/2026, đối chiếu snapshot getprop và ảnh PCB.

## Đã quan sát

- `persist.radio.multisim.config=dsds`.
- Trạng thái snapshot `gsm.sim.state=READY,ABSENT`.
- `ril-daemon` và `ril-daemon2` đều được báo cáo là đang chạy; hệ thống có hai kênh telephony logic.
- PCB máy nghiên cứu có hai đầu đọc thẻ kim loại; ảnh không chứng minh mọi tiếp điểm được đấu nối cho hai Nano-SIM.

## Chưa xác minh

- Cả hai đầu đọc đều là khe Nano-SIM vật lý hoạt động.
- Có thể dùng cùng lúc hai SIM vật lý hoặc hai kết nối dữ liệu 4G.
- Chuyển SIM qua service OEM/SoftSIM có an toàn trên máy thực hay không.

## Hướng thử nghiệm

Bắt đầu bằng kiểm tra chỉ đọc các thuộc tính DSDS, trạng thái RIL và trạng thái SIM **sau khi loại bỏ IMEI/IMSI/ICCID**. Không phát broadcast OEM, không sửa modem NV hay thay đổi chế độ SIM bằng phỏng đoán.
