# H01: MMI SecretCodeReceiver — khôi phục tham chiếu trong VDEX 010

**Ngày:** 23/11/2026  
**Tình trạng:** Đã kiểm tra ngoại tuyến trên bản `MMI.vdex` gốc của một ZEUS H01 / GlocalMe K1. Không chạy hoặc gửi broadcast đến thiết bị thật.  
**Phân biệt:** Mã nhập trong **About** của GlocalmeHome và receiver của MMI là **hai nhánh được phân tích độc lập**.

## Phát hiện đã đối chiếu

- Container `MMI.vdex` dùng định dạng `vdex010` của Android 8.1, chứa **một DEX** và vùng quickening của ART.
- Class `com.ukelink.dusk.mmi.MySecretCodeReceiver` có hai method được phân tích: `<init>()` và `onReceive(Context, Intent)`.
- Constructor gán chuỗi `2846` vào trường instance `SECRETCODE`.
- `onReceive` trước hết lấy `intent.getAction()`; nếu action không đúng `android.provider.Telephony.SECRET_CODE` thì thoát.
- Với action đúng, mã gọi `intent.getData().getHost()` và so sánh host với `SECRETCODE` qua `String.equals(Object)`; nếu không khớp thì thoát.
- Nếu cả hai phép so sánh đều đúng, method tạo `Intent`, chọn `com.ukelink.dusk.mmi.MainActivity` bằng `Intent.setClass(context, MainActivity.class)`, đặt cờ `0x10000000` (`FLAG_ACTIVITY_NEW_TASK`) rồi gọi `Context.startActivity(intent)`.

### Mức khôi phục

- Constructor: **1/1** tham chiếu quickening được đối chiếu với trường `SECRETCODE`.
- `onReceive`: **9/9** tham chiếu quickening được khôi phục về tên method/field tương ứng từ bảng DEX.
- **8/8 kiểm tra ngữ nghĩa** chạy PASS trên bản mẫu lưu riêng; **5/5 bài kiểm thử với dữ liệu giả** PASS.
- Mức xác minh là **cấu trúc bytecode và đích lời gọi** trên bản VDEX được cung cấp, **không phải** thử thành công broadcast thực tế hay chứng minh launcher About gửi broadcast này.

## Tách biệt hai đường truy cập

**Đường 1 — mật khẩu trong About (đã đối chiếu từ `GlocalmeHome.apk`, video và Activity thực tế):**

`MiniAboutActivity` → nhấn **Version No. 5 lần** → nhập `2846` → `ARouter` `/minilauncher/assistant` → `AssistantActivity` → nút **MMI** → `com.ukelink.dusk.mmi.MainActivity`.

**Đường 2 — BroadcastReceiver trong MMI (đã đối chiếu bytecode VDEX):**

`Intent` action `android.provider.Telephony.SECRET_CODE` + URI host `2846` → `MySecretCodeReceiver.onReceive()` → `MainActivity` với `NEW_TASK`.

**Không suy luận** rằng Đường 1 phải gọi `MySecretCodeReceiver` vì đường chuyển UI qua `AssistantActivity` đã được ghi nhận riêng.

## Công cụ tự viết và thử nghiệm

- [`tools/inspect_2846.py`](../../tools/inspect_2846.py): kiểm tra đường mật khẩu/About trong GlocalmeHome.apk; **6/6 kiểm tra trên mẫu gốc**.
- [`tools/inspect_mmi_vdex.py`](../../tools/inspect_mmi_vdex.py): đọc VDEX 010, tìm bảng quickening theo code-item, kiểm tra constructor và `onReceive()` mà **không xuất mã OEM**.
- [`tests/test_mmi_vdex.py`](../../tests/test_mmi_vdex.py): 5 bài kiểm thử với fixture tự tạo, không chứa firmware.

Chạy ngoại tuyến với tệp do người nghiên cứu đang sở hữu:

```sh
python3 tools/inspect_mmi_vdex.py /path/to/MMI.vdex
python3 -m unittest discover -s tests -v
```

**Không có** APK/VDEX nguyên bản, bản DEX đã khôi phục, IMEI, IMSI hoặc dữ liệu người dùng trong repository.

## Đối chiếu định dạng

- [VdexExtractor — triển khai backend VDEX 010, giấy phép Apache 2.0](https://github.com/anestisb/vdexExtractor/blob/master/src/vdex/vdex_backend_010.c)
- [Android ART — bảng mã lệnh quickened](https://android.googlesource.com/platform/art/+/a77f3c91ad7bd46fff8e98f582eef216892219b9/runtime/dex_instruction_list.h)
- [Luồng About / 2846 trên H01](glocalmehome-about-secret-code-2846.md)

**Việc tiếp theo:** Nếu muốn kiểm tra độc lập trên một bản firmware H01 khác, chạy cùng checker với `MMI.vdex` tương ứng và so sánh kết quả. Không cần bật `ADB ROOT`, Factory Mode hoặc khởi chạy receiver qua lệnh broadcast.
