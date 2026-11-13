# 6. Bài 5: Đèn giao thông

## 1. Mục tiêu
Trong bài học này, chúng ta sẽ cùng làm một hệ thống mô phỏng đèn giao thông thực tế.


## 2. Kết nối
- Đèn 4 LED RGB (chân D5)
![cityuno5 1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_1.png)


- LED 4 kí số (chân D3-D4)
![cityuno5 2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_2.png)


- **Kết nối:**
![bai 6.2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_6.2.png)


## 3. Lắp ráp mô hình
![bai 6.3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_6.3.png)


## 4. Giới thiệu khối lệnh
- Vào thư mục **Mở rộng**, tải thư viện **LED 7 đoạn**:
![cityuno5 12](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_12.jpg)


- Câu lệnh khởi tạo LED 4 ký số:
![cityuno5 13](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_13.png)


- Câu lệnh sự kiện lập lịch:
![cityuno5 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_3.png)


## 5. Viết chương trình
1. Gửi ra thông điệp 1 kích hoạt khối lệnh đèn giao thông:
![cityuno5 5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_5.png)


2. Khi nhận được thông điệp 1 sẽ kích hoạt trạng thái đèn đỏ:
![cityuno5 6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_6.png)


3. Tạo 1 vòng lặp đếm ngược từ 5 về 0 và hiện giá trị lên màn hình 4 số:
![cityuno5 7](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_7.png)


4. Sau đó gửi tiếp thông điệp 2 để sang trạng thái đèn xanh:
![cityuno5 8](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_8.png)


5. Thực hiện tương tự trang thái đèn đỏ cho trạng thái đèn xanh:
![cityuno5 9](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_9.png)


6. Sau đó sẽ gửi thông điệp 3 để chuyển sang màu vàng (đèn vàng 3 giây):
![cityuno5 10](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_10.png)


7. Sau khi đèn vàng 3 giây sẽ gửi thông điệp về thông điệp 1.


## 6. Chương trình mẫu
- Đèn giao thông:
![cityuno5 11](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno5_11.png)


- Link chương trình mẫu: [https://app.ohstem.vn/#!/share/yolouno/2eIg8FXRMVHlsP7SxRLTgwywNfW](https://app.ohstem.vn/#!/share/yolouno/2eIg8FXRMVHlsP7SxRLTgwywNfW)