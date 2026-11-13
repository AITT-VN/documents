# 6. Module phát nhạc - Sound Player
![nhac.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.1.png)


- Module phát nhạc Sound Player là một module có khả năng phát âm thanh. Bạn có thể ứng dụng chúng vào các ứng dụng vui nhộn sáng tạo như phát các đoạn nhạc ngắn, phát ra âm thanh báo động,…

- Dựa vào tính năng này, chúng tôi sẽ đưa ra hướng dẫn Sound Player cơ bản, để bạn có thể phát ra âm thanh mà mình thích. Bạn có thể ứng dụng chúng vào để biến Yolo:Bit thành một hướng dẫn viên du lịch tài năng, một giáo sư giảng dạy cho học sinh hoặc đơn giản chỉ cần là một cỗ máy thông báo thông minh cho người dùng, bằng cách ghi âm sẵn âm thanh mình cần hoặc tạo ra giọng đọc bằng phần mềm.

## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/dieu-khien-dong-ngat/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật của Sound Player:**

    + USB giao tiếp: 2.0.
    + Giao tiếp UART: TTL.
    + Điện áp đầu vào: 3.3V
    + Dòng làm việc : 10mA.
    + Nhiệt độ Làm Việc: -40°C ~ 85°C
    
## **3. Hướng dẫn tạo file MP3 bằng giọng nói tiếng Việt**
Trong một số dự án như tạo ra các thiết bị cảnh báo, chào khách hàng, thông báo hướng dẫn,… chúng ta cần phát ra một âm thanh giọng nói. OhStem Education sẽ hướng dẫn các bạn tạo một file MP3 giọng nói từ một đoạn văn bản nhé!

- **Bước 1:** Từ trình duyệt Web, các bạn truy cập vào địa chỉ sau: [https://soundoftext.com/ ](https://soundoftext.com/)
    
Trang web này cho phép chúng ta tạo ra các âm thanh giọng đọc của con người từ văn bản bất kỳ với đa dạng các ngôn ngữ trên thế giới, trong đó có tiếng Việt.
![nhac.9](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.9.png)

- **Bước 2:** Nhập câu nói mà bạn muốn tạo vào ô **“Text”.** Ở đây, mình sẽ tạo thử một câu **“Xin chào các bạn”**
![nhac.10](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.10.png)

- **Bước 3:** Chọn ngôn ngữ bạn muốn tại ô **“Voice”**. Ở đây mình cần tạo giọng đọc tiếng Việt nên mình sẽ chọn **“Vietnamese”**
![nhac.11](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.11.png)

- **Bước 4:** Nhấn **“Submit”** để hệ thống tự động tạo câu nói bạn muốn. Sau đó tải file âm thanh về máy tính.

> **Lưu ý:** Sau khi tải file MP3 về máy tính, bạn cần **đổi tên file theo số thứ tự** (ví dụ: `1.mp3`, `2.mp3`, `3.mp3`,…) trước khi lưu vào module Sound Player để chương trình có thể gọi đúng bài hát theo số thứ tự.
    
## **4. Lưu file MP3 vào Sound Player:**
- **Bước 1:** Kết nối module Sound Player (cổng lưu file được khoanh đỏ như hình bên dưới) với máy tính bằng dây cáp USB type C.
![nhac.2](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.2.png)


- **Bước 2**: Bộ nhớ lưu trữ của module sẽ xuất hiện như hình, trong ví dụ là USB Drive (E:):
![nhac.3](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.3.png)


OhStem Education đã chuẩn bị sẵn 1 số tập tin MP3 có sẵn trong Module. Bạn có thể sao chép các file MP3 bạn muốn vào đây. Chúng tôi đề xuất bạn đặt tên tập tin MP3 của bạn theo số thứ tự như hình trên.
    
**Bạn có thể tải thêm một số mẫu có sẵn tại đây:** [https://github.com/AITT-VN/yolobit_extension_sound_player ](https://github.com/AITT-VN/yolobit_extension_sound_player)
    
- **Bước 3:** Ngắt kết nối module Sound Player với máy tính và thực hiện các bước như chương tiếp theo.

> **Lưu ý:**
> - Module Sound Player có **2 cổng USB-C** — một cổng dùng để **lưu file** (kết nối với máy tính), một cổng dùng để **cấp nguồn**. Hãy chắc chắn dùng đúng cổng khi lưu file.
> - Chỉ sử dụng định dạng **MP3** — các định dạng khác (WAV, AAC,...) sẽ không được phát.
> - Không nên lưu quá nhiều file cùng lúc để tránh nhầm lẫn thứ tự bài hát trong chương trình.

## **5. Kết nối**

| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/dieu-khien-dong-ngat/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/dieu-khien-dong-ngat/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![nhac.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.1.png) | Module phát nhạc (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/sound-player/) |
    
    
- **Bước 1**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 2**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 3**: Kết nối Sound Player với **P14/P15 trên mạch mở rộng**.
![nhac.4](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.4.png)


## **6. Hướng dẫn lập trình:**
- **Bước 1**: Tải thư viện Sound Player, bằng cách dán đường link sau [https://github.com/AITT-VN/yolobit_extension_sound_player.git ](https://github.com/AITT-VN/yolobit_extension_sound_player.git) vào phần tìm kiếm thư viện.

Xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![nhac.5](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.5.png)

Sau khi thực hiện xong phần hướng dẫn Sound Player cơ bản này, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:
![nhac.6](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.6.png)

Để làm việc với module Sound Player, bạn cần sử dụng câu lệnh sau để khai báo chân được sử dụng trong chương trình:
![nhac.7](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.7.png)

- **Bước 2**: Gửi chương trình sau vào Yolo:Bit:
![nhac.8](/wiki-assets/images/module/dieu-khien-dong-ngat/images/nhac.8.png)


> **Ghi chú:** **Giải thích chương trình:**

Sau khi gửi chương trình xuống Yolo:Bit, bài nhạc số 1 sẽ được phát ra, âm lượng bạn có thể tùy chỉnh từ 0-30. Khi bạn nhấn nút A, bài hát đang phát sẽ dừng lại để chuyển sang bài kế tiếp. Tương tự với nút B.
