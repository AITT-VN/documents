# 3. Thiết lập phát nhạc cho module Sound Player

![nhac.1](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.1.png)


- Module phát nhạc Sound Player là một module có khả năng phát âm thanh. Bạn có thể ứng dụng chúng vào các ứng dụng vui nhộn sáng tạo như phát các đoạn nhạc ngắn, phát ra âm thanh báo động,…

- Dựa vào tính năng này, chúng tôi sẽ đưa ra hướng dẫn Sound Player cơ bản, để bạn có thể phát ra âm thanh mà mình thích. Bạn có thể ứng dụng chúng vào để biến Yolo:Bit thành một hướng dẫn viên du lịch tài năng, một giáo sư giảng dạy cho học sinh hoặc đơn giản chỉ cần là một cỗ máy thông báo thông minh cho người dùng, bằng cách ghi âm sẵn âm thanh mình cần hoặc tạo ra giọng đọc bằng phần mềm.


## **1. Hướng dẫn tạo file MP3 bằng giọng nói tiếng Việt**
Trong một số dự án như tạo ra các thiết bị cảnh báo, chào khách hàng, thông báo hướng dẫn,… chúng ta cần phát ra một âm thanh giọng nói. OhStem Education sẽ hướng dẫn các bạn tạo một file MP3 giọng nói từ một đoạn văn bản nhé!

    - **Bước 1:** Từ trình duyệt Web, các bạn truy cập vào địa chỉ sau: [https://soundoftext.com/ ](https://soundoftext.com/)
    
Trang web này cho phép chúng ta tạo ra các âm thanh giọng đọc của con người từ văn bản bất kỳ với đa dạng các ngôn ngữ trên thế giới, trong đó có tiếng Việt.
![nhac.9](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.9.png)

    |
    
    - **Bước 2:** Nhập câu nói mà bạn muốn tạo vào ô **“Text”.** Ở đây, mình sẽ tạo thử một câu **“Xin chào các bạn”**
![nhac.10](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.10.png)

    |
    
    - **Bước 3:** Chọn ngôn ngữ bạn muốn tại ô **“Voice”**. Ở đây mình cần tạo giọng đọc tiếng Việt nên mình sẽ chọn **“Vietnamese”**
![nhac.11](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.11.png)

    |
    
    - **Bước 4:** Nhấn **“Submit”** để hệ thống tự động tạo câu nói bạn muốn. Sau đó tải file âm thanh về máy tính
    
    
## **2.  Lưu file MP3 vào Sound Player:**
- **Bước 1:** Kết nối module Sound Player (cổng lưu file được khoanh đỏ như hình bên dưới) với máy tính bằng dây cáp USB type C.
![nhac.2](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.2.png)


- **Bước 2**: Bộ nhớ lưu trữ của module sẽ xuất hiện như hình, trong ví dụ là USB Drive (E:):
![nhac.3](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.3.png)


- **Bước 3:** Ngắt kết nối module Sound Player với máy tính và thực hiện các bước như chương tiếp theo.


## **3. Hướng dẫn lập trình:**
- **Bước 1**: Tải thư viện Sound Player trong mục MỞ RỘNG:
![nhac.5](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.5.png)

    |
    
    Sau khi thực hiện xong phần hướng dẫn Sound Player cơ bản này, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:
![nhac.6](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.6.png)

    |
    
    Để làm việc với module Sound Player, bạn cần sử dụng câu lệnh sau để khai báo chân được sử dụng trong chương trình (dự án này dùng chân D3-D4):
![nhac.7](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.7.png)

    |
    
- **Bước 2**: Gửi chương trình sau vào Yolo UNO:
![nhac.8](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/nhac.8.png)


> **Ghi chú:** **Giải thích chương trình:**

Sau khi gửi chương trình xuống Yolo UNO, bài nhạc số 1 sẽ được phát ra mỗi khi ấn nút Boot trên mạch, âm lượng bạn có thể tùy chỉnh từ 0-30.
