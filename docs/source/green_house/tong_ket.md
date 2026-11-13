# 8. Tổng hợp dự án

Tổng hợp lại các tính năng cơ bản của mô hình ta có:

- Bật/tắt quạt tự động dựa trên cảm biến nhiệt độ độ ẩm DHT20
- Bật tắt đèn thông tự động dựa trên cảm biến ánh sáng VEML 6040
- Bật tắt máy bơm dựa trên cảm biến độ ẩm đất điện dung

## **1. Hướng dẫn kết nối phần cứng cho dự án**
- Kết nối các module với Yolo UNO:


    :widths: 10, 20, 15
    
    1, "Relay 4 kênh", "I2C1"
    2, "Cảm biến ánh sáng VEML6040", "I2C2"
    3, "Màn hình LCD 1602", "I2C3"
    4, "Cảm biến DHT20", "I2C4"
    5, "Cảm biến độ ẩm đất điện dung", "A0"
    
    
- Kết nối các thiết bị với đầu ra của Relay:


    :widths: 10, 20, 15
    
    1, "Đèn", "Relay số 2"
    2, "Quạt", "Relay số 3"
    3, "Máy bơm", "Relay số 4"
    
    
## 2. Chương trình tổng
![tong ket](/wiki-assets/images/yolo_uno/green_house/images/tong_ket.png)


    Link chương trình [https://app.ohstem.vn/#!/share/yolouno/2vsqZvNfyWykyVhJrs0XWdOaFVU](https://app.ohstem.vn/#!/share/yolouno/2vsqZvNfyWykyVhJrs0XWdOaFVU)
    
    
## 3. Nạp chương trình tham khảo:
Sau khi ấn vào đường liên kết của chương trình trên, sẽ xuất hiện 1 cửa sổ trang web có chương trình tham khảo hiển thị như hình:
![napcode 1](/wiki-assets/images/yolo_uno/green_house/images/napcode_1.png)


Sau đó bạn ấn vào nút **IMPORT PROJECT** ở góc trên bên trái phần mềm lập trình như hình minh họa:
![napcode 2](/wiki-assets/images/yolo_uno/green_house/images/napcode_2.png)


Sau đó bạn kết nối với máy tính và mạch Yolo UNO thông qua kết nối USB như hình minh họa:
![co ban 4](/wiki-assets/images/yolo_uno/green_house/images/co_ban_4.png)


Chọn vào biểu tượng kết nối USB và kết nối vào thiết bị có tên **Espressif CDC Device (Com X)** với X là 1 số bất kỳ như hướng dẫn:
![napcode 4](/wiki-assets/images/yolo_uno/green_house/images/napcode_4.png)
![co ban 5](/wiki-assets/images/yolo_uno/green_house/images/co_ban_5.png)
![co ban 6](/wiki-assets/images/yolo_uno/green_house/images/co_ban_6.png)


Sau đó chạy thử chương trình bằng cách ấn vào biểu tưởng nút tam giác Play như hình
![napcode 5](/wiki-assets/images/yolo_uno/green_house/images/napcode_5.png)


Khi chương trình đã hoạt động, bạn cần lưu chương trình vào thiết bị, sau khi lưu xong chỉ cần khởi động hệ thống, cấp nguồn là hệ thống hoạt động
![co ban 10](/wiki-assets/images/yolo_uno/green_house/images/co_ban_10.png)
