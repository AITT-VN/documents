8. Bài 5: Hiển thị thông tin
=================================

Mục tiêu
-------------------------
-------------------------

Trong bài này, chúng ta sẽ sử dụng cảm biến nhiệt độ độ ẩm DHT20 và cảm biến ánh sáng để đọc giá trị từ môi trường và hiển thị các giá trị đó lên màn hình LCD OLED. Đây là những thông tin quan trọng ảnh hưởng tới sự sinh trưởng của cây. Dựa trên thông tin này, ta có thể đưa ra các quyết định chăm sóc cây hợp lý hơn.

Thiết bị cần dùng
--------------------------
--------------------------

.. image:: images/planbit_52.png
    :scale: 100%
    :align: center
|
Kết nối
--------------------------
--------------------------

.. image:: images/planbit_53.png
    :scale: 100%
    :align: center
|
Giới thiệu khối lệnh
--------------------------
--------------------------

    .. image:: images/planbit_54.png
        :width: 900px
        :align: center  

    .. image:: images/planbit_55.png
        :width: 900px
        :align: center 

Viết chương trình
--------------------------
--------------------------

1. Khởi tạo màn hình LCD và Reset bộ đếm thời gian

.. image:: images/planbit_56.png
    :scale: 100%
    :align: center
|
2. Tạo điều kiện: Nếu bộ đếm thời gian ≥ 5000ms (5 giây). Điều kiện này giúp mỗi 5 giây chương trình sẽ thực hiện lệnh bên trong

.. image:: images/planbit_57.png
    :scale: 100%
    :align: center
|
3. Bắt đầu cập nhật cảm biến nhiệt độ và xóa màn hình LCD cũ sau mỗi 5 giây:

Kéo thả khối **cập nhật cảm biến DHT20** và **xóa màn hình LCD** vào phần thực hiện 

.. image:: images/planbit_58.png
    :scale: 100%
    :align: center
|
4. Tạo văn bản in ra LCD nội dung “nhiet do” lấy thông tin từ **khối lệnh đọc nhiệt độ** cho dòng 1 (tọa độ y=0)

.. image:: images/planbit_59.png
    :scale: 100%
    :align: center
|
5. Tương tự, tạo văn bản in ra 2 nội dung còn lại:

- Nội dung “do am” lấy thông tin từ **khối lệnh đọc độ ẩm** cho dòng 2 (y = 15)

- Nội dung “do sang” lấy thông tin từ **khối lệnh đọc độ sáng** cho dòng 3 (y = 30)

6. Reset bộ đếm để đếm lại sau mỗi 5 giây

.. image:: images/planbit_60.png
    :scale: 90%
    :align: center
|
