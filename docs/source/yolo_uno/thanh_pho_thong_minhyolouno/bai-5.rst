6. Bài 5: Đèn giao thông
===================================

1. Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng làm một hệ thống mô phỏng đèn giao thông thực tế.



2. Kết nối 
--------------
--------------------

- Đèn 4 LED RGB (chân D5)

.. image:: images/cityuno5_1.PNG
    :width: 150px
    :align: center 
|

- LED 4 kí số (chân D3-D4)

.. image:: images/cityuno5_2.PNG
    :width: 200px
    :align: center 
|


- **Kết nối:**

.. image:: images/bai_6.2.png
    :scale: 80%
    :align: center 
|

3. Lắp ráp mô hình 
------------
---------------

.. image:: images/bai_6.3.png
    :scale: 100%
    :align: center 
|

4. Giới thiệu khối lệnh 
----------
-----------------

- Vào thư mục **Mở rộng**, tải thư viện **LED 7 đoạn**:

.. image:: images/cityuno5_12.jpg
    :scale: 80%
    :align: center 
|

- Câu lệnh khởi tạo LED 4 ký số: 

.. image:: images/cityuno5_13.PNG
    :scale: 80%
    :align: center 
|

- Câu lệnh sự kiện lập lịch:

.. image:: images/cityuno5_3.PNG
    :scale: 80%
    :align: center 
|


5. Viết chương trình 
----------
-----------------

1. Gửi ra thông điệp 1 kích hoạt khối lệnh đèn giao thông:

.. image:: images/cityuno5_5.PNG
    :scale: 70%
    :align: center 
|

2. Khi nhận được thông điệp 1 sẽ kích hoạt trạng thái đèn đỏ:

.. image:: images/cityuno5_6.PNG
    :scale: 70%
    :align: center 
|

3. Tạo 1 vòng lặp đếm ngược từ 5 về 0 và hiện giá trị lên màn hình 4 số:

.. image:: images/cityuno5_7.PNG
    :scale: 70%
    :align: center 
|

4. Sau đó gửi tiếp thông điệp 2 để sang trạng thái đèn xanh:

.. image:: images/cityuno5_8.PNG
    :scale: 70%
    :align: center 
|

5. Thực hiện tương tự trang thái đèn đỏ cho trạng thái đèn xanh:

.. image:: images/cityuno5_9.PNG
    :scale: 70%
    :align: center 
|

6. Sau đó sẽ gửi thông điệp 3 để chuyển sang màu vàng (đèn vàng 3 giây):

.. image:: images/cityuno5_10.PNG
    :scale: 70%
    :align: center 
|

7. Sau khi đèn vàng 3 giây sẽ gửi thông điệp về thông điệp 1.


6. Chương trình mẫu 
-----------------
-------------------

- Đèn giao thông: 

.. image:: images/cityuno5_11.PNG
    :scale: 60%
    :align: center 
|

- Link chương trình mẫu: `<https://app.ohstem.vn/#!/share/yolouno/2eIg8FXRMVHlsP7SxRLTgwywNfW>`_






