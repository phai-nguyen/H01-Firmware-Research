# H01 UService — từ DEX raw lỗi checksum đến dequickening 37.008/37.008

**Nguồn:** [Nhật ký Notion H01, mục 6 và 14 (10/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), đối chiếu phần cập nhật OTA/UService v12. **Phân tích tĩnh**, không kích hoạt loader, SoftSIM hay update trên máy.

## Hai mốc dễ bị nhầm

| Mốc nguồn | Nội dung |
| --- | --- |
| Mục 6 — ban đầu | `Uservice.vdex` v010 có DEX 035; trích bản raw **8.183.680 byte** còn quickening và checksum **không khớp**. Không dùng như DEX cuối |
| Mục 14 — cập nhật | Dequickening VDEX010 hoàn tất **37.008/37.008 records** và SHA-1/Adler-32 của DEX đã khôi phục **khớp** |
| Mục 15–16 trong nghiên cứu cập nhật 22/11 | Mẫu payload mã động `uc-asset0.bin` được kiểm riêng; **không đồng nhất với DEX VDEX ban đầu** |

## Chỉ số từ phép dequickening

| Loại | Số lượng |
| --- | ---: |
| Quickening records | **37.008/37.008** |
| Giá trị 16-bit tiêu thụ | **135.637** |
| Method có code-item | **53.229** |
| Opcode `return-void-no-barrier` khôi phục | **13.838** |
| Field accesses quickened khôi phục | **61.881** |
| Virtual invoke quickened khôi phục | **63.378** |
| NOP chuyển thành `check-cast` | **5.051** |
| NOP thường được giữ | **276** |
| Checksum Adler-32 sau khôi phục | **`0x34c4fe1d`** |

APK UService được ghi **23.449.980 byte**, VDEX **8.853.712 byte**, 1 DEX `035`, **7.291 class definitions** và **64.209 method IDs**.

Phép này chứng minh **bytecode container đã khôi phục tham chiếu có thể kiểm checksum**, nhưng **không** khẳng định decompile Java toàn bộ method body chính xác, tìm được mọi class được nạp sau này hoặc hiểu đầy đủ logic nghiệp vụ.

## Loader vẫn là mảng riêng

Các method `UServiceApplication.loadJars/loadLibraries`, `UcConnectCtrl.loadDex`, `LibDexload.loadUcClasses` và các đường `/files/code`, `assets/uc-asset0.bin`, `mini.dex` cho thấy đường nạp mã động. Một `libdexload.so` native có tham chiếu AssetManager, DexFile và routine đặt tên RC4. Ở **mục 14** đây là dấu vết tĩnh, không đủ kết luận thuật toán thực cho asset.

Báo cáo OTA **v12 sau này** có thêm thí nghiệm offline với payload xác định, nhưng phải tách khỏi mốc 10/11. Không công khai asset, DEX đã khôi phục, khóa giải mã, dữ liệu VSIM hoặc APK của OEM.

**Liên quan:** [UService loader](uservice-loader.md), [v12–v16 update channels](uservice-update-channels-v12-v16.md).