# Tình trạng đường âm thanh Android/ALSA

**Trạng thái: PAUSED / CHƯA KHẮC PHỤC.** Ghi chép nghiên cứu ngày 21/11/2026 yêu cầu tạm dừng thử nghiệm vá âm thanh.

## Kết quả khảo sát

- Video H.264 **không có audio** đã phát hình thành công trong cấu hình thử.
- Các mẫu H.264 + AAC 44,1/48 kHz thất bại, cả trường hợp thử loa Bluetooth.
- Hệ thống ghi lỗi `AudioTrack init failed` / `MediaCodecAudioRenderer error`.
- `/proc/asound/cards` trả `--- no soundcards ---` tại thời điểm thu thập; chưa thấy PCM output trong `/dev/snd`.
- Trong Device Tree runtime của máy khảo sát, `/soc/sound/status=disabled` đã được ghi nhận.

## Không nên suy diễn

- Không thể khẳng định nhà sản xuất cố ý khóa âm thanh chỉ từ những phát hiện trên.
- Driver có trong kernel không đồng nghĩa máy có codec/phần cứng phát tiếng hoàn chỉnh.
- Giả thuyết xung đột GPIO / pinmux và kế hoạch sửa Device Tree **chưa được xác minh**.
- **Chưa có** bản vá khôi phục âm thanh đã PASS; không flash boot/DTB thử nghiệm từ tài liệu này.

Nhánh này chỉ được tiếp tục khi có yêu cầu cụ thể và phương án kiểm tra chỉ đọc/rollback phù hợp.
