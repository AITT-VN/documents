# 2. Bật/Tắt đèn với nút nhấn đôi

## 1. Mục tiêu
Trong nội dung này, bạn sẽ biết cách kết nối và lập trình để điều khiển **đèn 4 LED RGB** bằng **nút nhấn đôi** trên mạch Yolo UNO. Khi nhấn nút, đèn sẽ bật/tắt theo yêu cầu, giúp bạn hiểu rõ hơn về cách xử lý tín hiệu từ nút nhấn và điều khiển thiết bị đầu ra. Đây là bước quan trọng để xây dựng các hệ thống điều khiển trong mô hình nhà thông minh.


## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Module led RGB kèm dây tín hiệu:
![tiny rgb](/wiki-assets/images/yolo_uno/smart_home_uno/images/tiny_rgb.png)


- Module nút nhấn đôi kèm dây tín hiệu:
![nut nhan doi](/wiki-assets/images/yolo_uno/smart_home_uno/images/nut_nhan_doi.png)


## 3. Kết nối phần cứng
- Kết nối module Led RGB vào chân D9 - D10 của Yolo UNO

- Kết nối module Nút nhấn đôi vào chân D5 - D6 của Yolo UNO
![2.2](/wiki-assets/images/yolo_uno/smart_home_uno/images/2.2.png)


## 4. Chương trình lập trình
- Câu lệnh dùng để làm việc với nút nhấn đôi, nằm trong mục **CẢM BIẾN**
![2.5](/wiki-assets/images/yolo_uno/smart_home_uno/images/2.5.png)


- Câu lệnh dùng để làm việc với đèn 4 LED RGB, nằm trong mục **HIỂN THỊ**
![2.3](/wiki-assets/images/yolo_uno/smart_home_uno/images/2.3.png)


- **Chương trình lập trình:**
![2.4](/wiki-assets/images/yolo_uno/smart_home_uno/images/2.4.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vFUcMKB8BO7kvw6DJJOlYPskQr](https://app.ohstem.vn/#!/share/yolouno/2vFUcMKB8BO7kvw6DJJOlYPskQr)
    
- **Giải thích chương trình:**  Sau khi thực hiện gửi chương trình lên Yolo UNO, đèn LED trên Yolo UNO sẽ chuyển sang đèn xanh. Khi nhấn nút A, đèn LED RGB sẽ chuyển sang màu đỏ. Khi nhấn nút B, đèn RGB tắt đèn.
