# H01 Magisk 30.7 — công cụ máy tính từ nguồn Notion

**Nguồn:** [Notion nhật ký H180–H186 (18/11/2026)](https://app.notion.com/p/414c5d5277a981898f7be2712da8f7cd), gói lịch sử `H01-Root-Co-Dinh-20261118.zip` (v1.1) và [Notion H01 máy B](https://app.notion.com/p/421c5d5277a981b3a9b9cc0582dcf9d2). Công cụ Python này tổng quát hóa quy tắc an toàn và thứ tự kiểm tra từ bộ CMD + `h01_rootctl.sh` đã ghi Notion. **Bản công khai là phiên bản chuyển sang Python, chưa được chạy trên H01 thật**, không gọi là bản đã PASS thực địa.

## Công cụ dùng để làm gì?

- `check`: kiểm 2 ảnh boot **của đúng máy** dài 32 MiB và SHA-256 tương ứng, không cần cắm H01.
- `boot-ram`: kiểm Fastboot đang mở khóa rồi thực hiện **`fastboot boot`**, không ghi phân vùng boot.
- `root-status`: kiểm model K1/MSM8909/SDK27, quyền `su`, Magisk 30.7 và hash boot trên máy.
- `backup`: sao lưu vùng `boot` sang `private-backup/boot-before.img` trên PC, từ phiên Android đang có root; không ghi đè bản sao trước đó.
- `flash-root`: có **cụm xác nhận riêng**, đòi hỏi root RAM `uid=0`, hash boot trên thiết bị đang khớp **ảnh stock**, backup đã đối chiếu và unlock Fastboot được xác minh **trước khi ghi**. Chỉ ghi phân vùng `boot`.
- `restore-stock`: chỉ thực hiện trên chính máy đã xác minh, có cụm xác nhận riêng và ảnh gốc đúng hash; đòi hỏi Fastboot đã mở khóa.

**⚠️ Flash hoặc restore có thể brick/mất dữ liệu.** Lệnh mặc định không ghi flash; lệnh ghi cần có ảnh gốc, đường cứu hộ thực tế và sự chủ động của chủ máy. **Không chạy trên máy H01 đã mất boot** khi chưa có kế hoạch phục hồi riêng.

## Cần chuẩn bị

1. Máy tính Windows 7 SP1 64-bit chạy **Python 3.8**, hoặc antiX Linux với Python 3.8+.
2. Android Platform Tools `adb` và `fastboot` chính hãng trong `PATH`, driver USB làm việc ổn định.
3. Bootloader H01 **đã mở khóa thật**. Giữ ảnh `boot-goc.img` của **chính H01** và ảnh vá từ ảnh đó bằng **Magisk 30.7**. Không dùng ảnh root của H01 khác, dù cùng firmware.
4. Sao chép `config.example.json` thành `config.local.json`, điền serial, hash gốc, hash vá được tạo/kiểm trên chính máy. `config.local.json`, ảnh IMG và sao lưu trong `private-backup/` đã được `.gitignore` chặn.
5. Luôn giữ bản gốc bất biến ở nơi khác ngoài thư mục làm việc và có phương án vào Fastboot/EDL.

## Cách chạy

Thực thi trong thư mục `tools/h01_root`:

```sh
python root_tool.py check --config config.local.json
python root_tool.py boot-ram --config config.local.json
```

Sau khi Android khởi động lại từ RAM và cấp quyền root cho **Shell** trong Magisk:

```sh
python root_tool.py root-status --config config.local.json
python root_tool.py backup --config config.local.json
```

Chỉ khi **boot RAM đã PASS** và đã xác minh có backup trên PC, bước ghi cố định mới có ý nghĩa:

```sh
python root_tool.py flash-root --config config.local.json --confirm I-CONFIRM-ROOT-FLASH-ON-MY-H01
```

Tool sẽ ghi `boot` nhưng **không tự reboot** sau flash: đọc output thành công trước, chủ máy chủ động reboot, rồi chạy `root-status` lần nữa. Nếu cần khôi phục tại Fastboot và chỉ khi ảnh stock đúng máy đã xác minh:

```sh
python root_tool.py restore-stock --config config.local.json --confirm I-CONFIRM-STOCK-RESTORE-ON-MY-H01
```

## Ranh giới chứng cứ và phát hành

- Bộ gốc v1.1 có `boot-goc.img`, `boot-root.img` đã vá cho một máy cụ thể, script CMD và module navbar riêng. **Không phát hành 2 boot image, khóa hay serial/hashes của máy thử**.
- Bộ máy B có ảnh root A được **thử tạm qua RAM**, nhưng image root cố định trên B được **vá riêng từ boot B**; đây là điểm an toàn bắt buộc của bản công khai.
- Script này đã có **kiểm thử offline** cho validate hash/logic (xem test repo), nhưng chưa có thử nghiệm máy thật sau khi chuyển từ CMD sang Python. Mọi kết quả PASS lịch sử thuộc script/bộ gốc, **không** thuộc phiên bản chuyển đổi này.
- Không tích hợp Magisk APK hoặc IMG OEM; tải Magisk từ [nguồn phát hành chính thức](https://github.com/topjohnwu/Magisk/releases/tag/v30.7).

Xem [báo cáo root](../../docs/boot/h01-magisk-root-notion-procedure-20261124.md), [bootloader unlock](../h01_unlock/README.md) và [chính sách Notion-only](../../docs/research/notion-only-publication-policy-20261124.md).
