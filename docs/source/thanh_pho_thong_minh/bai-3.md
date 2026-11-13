# 4. Bài 3: Thùng rác thông minh

## 1. Mục tiêu
Một thùng rác thông minh với khả năng tự động mở nắp khi có người đến gần sẽ mang lại sự tiện lợi hơn rất nhiều, giúp thành phố xanh sạch đẹp hơn. Trong bài này, chúng ta hãy cùng lập trình một thùng rác có khả năng tự mở nắp khi có người.


## 2. Kết nối
- Cảm biến vật cản (D3-D4)
![cityuno3 1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_1.png)


- Động cơ Servo (D2)
![cityuno1 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_3.png)


**Lưu ý:** Chỉnh góc Servo về góc 20 trước khi lắp ráp

- **Kết nối**
![bai 3.4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_3.4.png)


## 3. Lắp ráp mô hình
![bai 3.5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_3.5.png)


## 4. Giới thiệu khối lệnh
- Khối lệnh xác định trạng thái cảm biến vật cản
![cityuno3 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_3.png)


## 5. Viết chương trình
1. Quay Servo chân D2 đến góc 20 độ (đóng nắp thùng rác)
![cityuno3 4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_4.png)


2. Tạo điều kiện: nếu cảm biến vật cản phát hiện có người phía trước cảm biến
![cityuno3 5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_5.png)


3. Sau 3 giây, ta đóng nắp thùng rác (quay Servo về góc 20 độ)
![cityuno3 6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_6.png)


## 6. Chương trình mẫu
- Thùng rác thông minh
![cityuno3 7](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_7.png)


Link chương trình: [https://app.ohstem.vn/#!/share/yolouno/2eIjitx56J35MpcX2K4P0NShqIF](https://app.ohstem.vn/#!/share/yolouno/2eIjitx56J35MpcX2K4P0NShqIF)