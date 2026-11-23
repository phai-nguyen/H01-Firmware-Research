# Launcher3 AutoHotspot — nguyên nhân lỗi API và các mốc v0.3.1–v0.4

**Nguồn:** [Notion AutoHotspot v0.4](https://app.notion.com/p/41ec5d5277a98185ac4cfc7813f9f8cf), 20–21/11/2026. Biên soạn 24/11/2026. **FAIL ở một số bản đầu, PASS thủ công v0.3.4 và tự chạy v0.4**.

Khi dùng GlocalmeHome, `MiniLauncherActivity.onResume()` có logic `WifiApUtil.isWifiApEnabled()` và `setWifiApEnabled(context,true)`. Chuyển sang Launcher3 khiến hotspot có thể duy trì khi đã bật, nhưng không tự bật lại từ trạng thái AP OFF.

| Bản | Kết quả theo log/thiết bị |
| --- | --- |
| v0.3.1 | `app_process` bị Killed (137), Soft AP vẫn OFF |
| v0.3.2 | `NoSuchMethodError`: bản gọi `IConnectivityManager.startTethering(int,ResultReceiver,boolean)` **3 tham số** không khớp H01 |
| v0.3.3 | Probe lấy được chữ ký thật `startTethering(int,ResultReceiver,boolean,String)` và `stopTethering(int,String)`; tham số bổ sung `callerPkg` |
| v0.3.4 | Dùng chữ ký **4 tham số** qua Binder/root, exit 0; có `SoftApState`, `wlan0 TetheredState`, `lastError=0`; iPhone kết nối được — **PASS thủ công** |
| v0.4 | Module Magisk `late_start` gọi lại logic sau Android boot; **PASS tự bật AP sau reboot** |

Log v0.4 ngày 20/11 ghi đợi **15 giây** sau `sys.boot_completed`, gửi yêu cầu tethering lần 1, `app_process exit=0`, `PASS: SoftApState is active`. Video boot cho thấy Launcher3 nhưng cũng xuất hiện hộp chọn HOME; **chưa khẳng định Always đã lưu** chỉ từ video.

Người dùng xác nhận thêm AutoHotspot v0.4 hoạt động trong tổ hợp cấp nguồn lạnh ngày 21/11. Chưa có thử nghiệm nhiều chu kỳ, không pin, mất điện, throughput LTE hoặc vận hành 24/7. Kết quả từng bản không được gộp thành một phép thử hoàn chỉnh.

Đợt công bố chỉ đưa báo cáo, không đưa JAR, APK, Magisk ZIP, script flash hoặc ảnh thử chưa rà quyền phân phối. Xem [tổng quan](autohotspot.md), [bằng chứng boot lạnh](../boot/auto-power-on-cold-boot-evidence.md).