# 7. Bài 6: Hệ thống theo dõi chất lượng không khí và tiếng ồn

## 1. Mục tiêu
Ở thành phố, chất lượng không khí là mối quan tâm hàng đầu.Tương tự, ô nhiễm tiếng ồn cũng là mối quan tâm hàng đầu cho sức khỏe người dân. Để đo lường và đưa ra giải pháp tương ứng, chúng ta hãy cùng lập trình một hệ thống để theo dõi chất lượng không khí và thời tiết nhé! Các giá trị này sẽ được hiển thị trên màn hình LCD.


## 2. Kết nối
- Cảm biến nhiệt độ độ ẩm DHT20 (I2C2)
![bai 7.1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.1.png)


- Cảm biến chất lượng không khí MQ-135 (A0)
![bai 7.2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.2.png)


- Cảm biến cường độ âm thanh (A1)
![cityuno6 1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_1.png)


**Lưu ý:** Cảm biến chất lượng không khí sẽ ấm lên khi được cấp điện, đây là đặc tính đốt nóng không khí của thiết bị.

- Màn hình LCD OLED (I2C1)
![bai 7.3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.3.png)


- **Kết nối:**
![bai 7.4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.4.png)


## 3. Lắp ráp mô hình
![bai 7.5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.5.png)
![bai 7.6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_7.6.png)


## 4. Giới thiệu khối lệnh
- Vào mục **Mở rộng**, tải 2 thư viện **OLED I2C** và **Cảm biến MQx**:
![cityuno6 9](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_9.jpg)


- Khối lệnh đọc nhiệt độ, độ ẩm từ cảm biến DHT20:
![cityuno6 2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_2.png)


- Khối lệnh đọc cường độ âm thanh:
![cityuno6 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_3.png)


- Khối lệnh khởi tạo cảm biến MQ135:
![cityuno6 4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_4.png)


- Khối lệnh đọc giá trị cảm biến MQ135:
![cityuno6 8](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_8.jpg)


## 5. Viết chương trình
1. Sử dụng câu lệnh **sau mỗi 5 giây thực hiện**.
![cityuno6 5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_5.png)

    |
2. Xóa màn hình LCD trước đó và in ra giá trị nhiệt độ, độ ẩm, chất lượng không khí (PPM), mức độ âm thanh lên màn hình LCD tại vị trí 3 hàng khác nhau:
![cityuno6 6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_6.png)

    |
    
## Chương trình mẫu
- Hệ thống theo dõi thời tiết và chất lượng không khí:
![cityuno6 7](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno6_7.png)


- Link chương trình mẫu: [https://app.ohstem.vn/#!/share/yolouno/2eIhjgbTjsU5k53Lf3nqIP8k5bW](https://app.ohstem.vn/#!/share/yolouno/2eIhjgbTjsU5k53Lf3nqIP8k5bW)