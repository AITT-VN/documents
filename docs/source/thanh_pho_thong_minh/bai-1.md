# 2. Bài 1: Đèn công cộng thông minh

## 1. Mục tiêu:
Trong bài này, chúng ta sẽ cùng lập trình một chiếc đèn thông minh có thể tự sáng vào buổi tối. Các đèn này có thể gắn vào các khu vui chơi hoặc công viên tùy thích.


## 2. Kết nối
- Cảm biến ánh sáng (A3)
![bai 1.1.3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_1.1.3.png)

    |
- Module 4 LED RGB (D7-D8)
![bai 1.1.1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_1.1.1.png)

    |
- **Kết nối:**
![bai 1.2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_1.2.png)


## 3. Lắp ráp
Các thao tác được thực hiện như sau:
![bai 1.4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_1.4.png)
![bai 1.4.1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_1.4.1.png)


## 4. Giới thiệu khối lệnh
- Khối lệnh của cảm biến ánh sáng
![cityuno01](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno01.png)


- Khối lệnh điều khiển đèn 4 LED RGB:
![cityuno02](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno02.png)


## Viết chương trình
1. Kéo khối lệnh điều kiện vào khối lệnh kiểm tra theo thời sau **Sau mỗi 1 giây thực hiện**
![cityuno03](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno03.png)


2. Tạo điều kiện: nếu trời tối (độ sáng < 15) thì sẽ bật đèn (đổi sang thành màu trắng)
![cityuno04](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno04.png)


3. Tạo điều kiện: nếu trời sáng (độ sáng > 35) thì sẽ tắt đèn (đổi sang thành màu đen)
![cityuno05](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno05.png)


- Chương trình hoàn thiện:
![cityuno06](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno06.png)


- Link chương trình mẫu: [https://app.ohstem.vn/#!/share/yolouno/2eImrFzleAHhhnxEm7l7IBnN7zU](https://app.ohstem.vn/#!/share/yolouno/2eImrFzleAHhhnxEm7l7IBnN7zU)