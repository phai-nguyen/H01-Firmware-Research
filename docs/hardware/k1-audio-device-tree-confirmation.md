# H01 K1 — Device Tree âm thanh và ALSA đã xác minh trên máy thật

**Nguồn:** [Notion H01 AudioTrack, ALSA, HAL (21/11/2026)](https://app.notion.com/p/41fc5d5277a9814eb9e5f4324e25fba9), phần cập nhật đối chiếu runtime và boot gốc. **Trạng thái: kết quả chỉ đọc đã kiểm chứng, âm thanh CHƯA SỬA.**

## DTB đang chạy

| Thuộc tính | Kết quả báo cáo |
| --- | --- |
| Model Device Tree | `Qualcomm Technologies, Inc. MSM8909-PM8909 1GB MTP K1` |
| Board ID u32 | `(0x8, 0x66)` |
| `/soc/sound/status` | **`disabled`** |
| `/soc/sound/compatible` | `qcom,msm8952-audio-codec` |
| `/soc/sound/qcom,model` | `msm8909-snd-card` |
| `/proc/asound/cards` | `--- no soundcards ---` |
| `/proc/asound/pcm` | Trống |
| `/dev/snd` | Chỉ có timer, **không có PCM node** |

Bản sao boot gốc có nhiều FDT; DTB mang model và board ID K1 cũng ghi `/soc/sound/status=disabled`. DTB MTP tiêu chuẩn và G4S không có cùng thiết kế, khác cấu hình GPIO/micbias/pinctrl, **không thể dùng để thay thế DTB K1 theo suy đoán**.

## Liên hệ kết quả phát media

Mẫu H.264 không có audio đã hiện hình; mẫu AAC 44,1 kHz/48 kHz gặp `AudioTrack init failed`, kể cả đường Bluetooth. Audio Policy còn khai báo Speaker/A2DP, nhưng báo cáo thấy `Primary Output: 0`, không có ALSA sound card/PCM node. Điều này ủng hộ lỗi tại lớp dưới UI, **không phải chỉ thiếu nút âm lượng**.

**Không được kết luận:** hãng cố tình giấu phần cứng âm thanh; chỉ cần thay `disabled` thành `okay` sẽ có tiếng; Bluetooth/USB chắc chắn hoạt động sau khi thay DTB. Những việc đó còn liên quan codec/clock/driver/GPIO/Audio HAL và phần cứng.

**Trạng thái giữ nguyên:** chưa có boot patch hoặc sửa âm thanh đã PASS; nhánh thử nghiệm tạm dừng. Không phát hành DTB, boot IMG hay APK/driver OEM. Xem [báo cáo audio tổng](../system/audio.md).