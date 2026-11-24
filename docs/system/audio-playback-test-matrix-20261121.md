# H01 — ma trận kiểm thử media và chuỗi lỗi AudioTrack (21/11/2026)

**Nguồn:** [Notion — AudioTrack, ALSA, HAL, 21/11/2026](https://app.notion.com/p/41fc5d5277a9814eb9e5f4324e25fba9), đối chiếu báo cáo ADB và Device Tree runtime. **REPORTED TESTS + STATIC/RUNTIME EVIDENCE; AUDIO STILL NOT WORKING.**

## Các bài thử người dùng đã thực hiện

| Cấu hình thử | Kết quả |
| --- | --- |
| H.264, 360p, **không có audio** | **PASS hình ảnh** |
| H.264 + AAC **44,1 kHz stereo** | **FAIL** |
| H.264 + AAC **48 kHz mono** | **FAIL** |
| H.264 + AAC **48 kHz stereo** | **FAIL** |
| Just Player **0.217** qua loa Bluetooth | **FAIL**, cùng đường lỗi âm thanh |
| NewPipe **0.29.1** và **0.29.3** | Mở UI/tìm kiếm được; **chưa xem YouTube thành công** |

**PASS video không âm thanh** chỉ cho thấy đường video trong phép thử đó hoạt động; không chứng minh mọi H.264/codec/video Android chạy được.

## Chứng cứ chia theo các lớp

| Báo cáo ADB được tham chiếu | Quan sát |
| --- | --- |
| `/proc/asound/cards` | `--- no soundcards ---` |
| `/proc/asound/devices` và `/dev/snd` | Có ALSA timer nhưng **không có PCM output node** |
| Audio Policy (trước/sau) | `Primary Output: 0`; output/input dump rỗng; các handle primary/a2dp/usb/r_submix là 0 |
| Audio Flinger | Không thấy playback thread/output hoạt động |
| Log AudioTrack | `Could not get audioflinger`, `Error -19`, `Error code -20`, `Cannot create AudioTrack` |
| Process/HAL | `audioserver` và audio HAL vẫn có tiến trình, **không chứng minh PCM output đã mở** |
| Audio policy XML | Có Speaker và Bluetooth A2DP route, **không chứng minh route mở được** |

Đối chiếu cấu hình Device Tree **đang chạy** trên K1: `/soc/sound/status=disabled` và `/proc/asound/pcm` trống. Đây là chứng cứ mạnh hơn giả thuyết “ứng dụng không hỗ trợ AAC”, nhưng chưa biết **nguyên nhân thiết kế phần cứng/driver**. Không thể kết luận hãng có sẵn bộ loa hoàn chỉnh và cố tình khóa.

## Trạng thái quyết định

Người dùng đã yêu cầu **tạm dừng nhánh sửa âm thanh**; không có bản vá boot/DTB đã PASS. Không thể suy rằng chỉ đổi `disabled` thành `okay` sẽ đăng ký ALSA card, vì còn codec, pinctrl, clock, regulator, ASoC, GPIO, amplifier, Audio HAL và thiết kế PCB. Không lấy DTB mẫu G4S/MTP để thay cho K1.

Không đăng bản H01 boot gốc, Device Tree OEM, RAR/log gốc hoặc module chỉnh sửa. Xem [tổng quan](audio.md) và [phân tích DTB](../hardware/k1-audio-device-tree-confirmation.md).