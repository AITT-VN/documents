8. Bài 5: Hiển thị thông tin
=================================

Mục tiêu
-------------------------
-------------------------

Trong bài này, chúng ta sẽ sử dụng cảm biến nhiệt độ độ ẩm DHT20 và cảm biến ánh sáng để đọc giá trị từ môi trường và hiển thị các giá trị đó lên màn hình LCD OLED. Đây là những thông tin quan trọng ảnh hưởng tới sự sinh trưởng của cây. Dựa trên thông tin này, ta có thể đưa ra các quyết định chăm sóc cây hợp lý hơn.

Thiết bị cần dùng
--------------------------
--------------------------

- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: Images/planbit_31.png
    :width: 200px
    :align: center
|
- Màn hình OLED LCD

.. image:: Images/planbit_58.png
    :width: 200px
    :align: center
|
- Cảm biến nhiệt độ, độ ẩm DHT20 

.. image:: Images/planbit_59.png
    :width: 200px
    :align: center
|
- Cảm biến ánh sáng

.. image:: Images/planbit_60.png
    :width: 200px
    :align: center
|


Kết nối
--------------------------
--------------------------

- Màn hình OLED LCD (I2C 1)
- Cảm biến nhiệt độ, độ ẩm DHT20 (I2C 2) 
- Cảm biến ánh sáng (P1)

.. image:: Images/planbit_61.png
    :width: 400px
    :align: center
|


Giới thiệu khối lệnh
--------------------------
--------------------------

.. image:: Images/planbit_62.png
    :width: 800px
    :align: center
|
.. image:: Images/planbit_63.png
    :width: 800px
    :align: center
|
.. image:: Images/planbit_64.png
    :width: 800px
    :align: center
|


Viết chương trình
--------------------------
--------------------------

1. Khởi tạo màn hình LCD và Reset bộ đếm thời gian

.. image:: Images/planbit_65.png
    :width: 250px
    :align: center
|
2. Tạo điều kiện: Nếu bộ đếm thời gian ≥ 5000ms (5 giây). Điều kiện này giúp mỗi 5 giây chương trình sẽ thực hiện lệnh bên trong

.. image:: Images/planbit_66.png
    :width: 500px
    :align: center
|
3. Bắt đầu cập nhật cảm biến nhiệt độ và xóa màn hình LCD cũ sau mỗi 5 giây:

Kéo thả khối **cập nhật cảm biến DHT20** và **xóa màn hình LCD** vào phần thực hiện 

.. image:: Images/planbit_67.png
    :width: 400px
    :align: center
|
4. Tạo văn bản in ra LCD nội dung “nhiet do” lấy thông tin từ **khối lệnh đọc nhiệt độ** cho dòng 1 (tọa độ y=0)

.. image:: Images/planbit_68.png
    :width: 800px
    :align: center
|
5. Tương tự, tạo văn bản in ra 2 nội dung còn lại:

- Nội dung “do am” lấy thông tin từ **khối lệnh đọc độ ẩm** cho dòng 2 (y = 15)

- Nội dung “do sang” lấy thông tin từ **khối lệnh đọc độ sáng** cho dòng 3 (y = 30)

- Reset bộ đếm để đếm lại sau mỗi 5 giây

.. image:: Images/planbit_69.png
    :width: 800px
    :align: center
|


Chương trình mẫu
---------------------
---------------------

- Hiển thị thông tin: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Cyq1mX3LGLTUl8N2IxLaYuKCyT>`_

.. image:: Images/planbit_70.png
    :width: 200px
    :align: center
|

