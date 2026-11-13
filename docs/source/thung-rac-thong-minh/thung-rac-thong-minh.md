# 4. Thực hiện dự án

## 1. Mục tiêu:
Trong bài này, chúng ta sẽ cùng lập trình một hệ thống phân loại rác thải qua camera AI.


## 2. Kết nối
- Module camera AI version 2 (Chân D9-D10)
![trash03](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash03.png)

    |
- Module SoundPlayer (D3-D4)
![trash04](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash04.png)

    |
- Màn hình LCD1602 (I2C)
![trash05](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash05.png)

    |
- 3 Servo 180 độ (D2-D11-D12)
![trash06](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash06.png)

    |
- **Kết nối:**
![trash07](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash07.png)


## 3. Thực hiện
- Trước khi lắp ráp, bạn cần căn chỉnh Servo về góc 0 (vị trí đóng nắp thùng rác) để hoạt động chính xác. Thực hiện như sau:

    1. Kết nối Servo vào chân D11 trên mạch Yolo UNO(thực hiện tương tự ở 3 chân servo còn lại)
    
    2. Kết nối Yolo UNO với Ohstem App và tiến hành lập trình.
    
    3. Tạo chương trình như hình minh họa
![trash08](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash08.png)


    4.  Nhấn nút chạy chương trình
    
    5. Ngắt kết nối Servo với nguồn điện (tránh vừa cắm điện vừa gắn làm quay Servo gây hư hại thiết bị)
    
    
## 4. Giới thiệu khối lệnh
- Khối lệnh điều khiển loa phát nhạc:
![trash10](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash10.png)


**Dự án này chúng ta sẽ thống nhất cách nhận kết quả phân loại rác qua IoT server OhStem**


## 5. Cấu hình cài đặt module camera AI/camera OhStem App:
- Bạn xem cách cấu hình/sử dụng tính năng camera AI ở hướng dẫn trước

## Viết chương trình
1. Đầu tiên sẽ cài đặt góc cho 4 servo về 0 độ (vị trí đóng nắp thùng)
![trash11](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash11.png)


2. Tạo 3 biến cho 3 loại rác thải, 3 biến này sẽ hiển thị trên màn hình lúc phân loại rác.
![trash12](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash12.png)


3. Khởi tạo Module phát nhạc tại chân D3-D4, mở âm lượng 30 (tối đa)
![trash13](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash13.png)


4. Kết nối wifi và server để nhận thông tin phân loại AI
![trash14](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash14.png)


5. Giả sử trong bước thiết lập cài đặt IoT của camera AI bạn gửi lên kênh V1. Vậy để thiết bị nhận thông tin điều khiển bạn cũng sẽ đăng ký kênh V1:
![trash15](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash15.png)


6. Chúng ta sẽ so sánh thông tin nhận được với loại rác mà mình đã đặt để phân loại, sử dụng câu lệnh Nếu:
![trash16](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash16.png)


7. Khi kết quả đúng, chúng ta sẽ cho servo quay đến góc mở (có thể là 90 hoặc 1 vị trí khác tùy theo vị trí bạn lắp servo đóng nắp) và phát bài nhạc theo thứ tự âm thanh đã lưu vào loa, âm thanh sẽ được phát ra khi nhận diện đúng loại rác
![trash17](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash17.png)


8. Chúng ta cũng có thể hiện lên số lần phân loại rác tương ứng  bằng cách cho biến cộng vào 1 khi phân loại đúng và in ra màn hình
![trash18](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash18.png)


9. Thực hiện tương tự với 3 loại rác còn lại
![trash19](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash19.png)
![trash20](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/trash20.png)


- Link chương trình mẫu: [https://app.ohstem.vn/#!/share/yolouno/35gNXQ1lHXaS4WeScnFTM1NRrWk](https://app.ohstem.vn/#!/share/yolouno/35gNXQ1lHXaS4WeScnFTM1NRrWk)


## 6. Nạp chương trình tham khảo:
Sau khi ấn vào đường liên kết của chương trình trên, sẽ xuất hiện 1 cửa sổ trang web có chương trình tham khảo hiển thị như hình:
![napcode 1](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/napcode_1.png)


Sau đó bạn ấn vào nút **IMPORT PROJECT** ở góc trên bên trái phần mềm lập trình như hình minh họa:
![napcode 2](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/napcode_2.png)


Thay đổi thông tin wifi để mạch Yolo UNO kết nối được Wifi (lưu ý cần đảm bảo kết nối vào mạng wifi băng tầng 2.4Ghz)
![napcode 3](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/napcode_3.png)


Sau đó bạn kết nối với máy tính và mạch Yolo UNO thông qua kết nối USB như hình minh họa:
![co ban 4](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/co_ban_4.png)


Chọn vào biểu tượng kết nối USB và kết nối vào thiết bị có tên **Espressif CDC Device (Com X)** với X là 1 số bất kỳ như hướng dẫn:
![napcode 4](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/napcode_4.png)
![co ban 5](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/co_ban_5.png)
![co ban 6](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/co_ban_6.png)


Sau đó chạy thử chương trình bằng cách ấn vào biểu tưởng nút tam giác Play như hình
![napcode 5](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/napcode_5.png)


Khi chương trình đã hoạt động, bạn cần lưu chương trình vào thiết bị, sau khi lưu xong chỉ cần khởi động hệ thống, cấp nguồn là hệ thống hoạt động
![co ban 10](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/co_ban_10.png)
