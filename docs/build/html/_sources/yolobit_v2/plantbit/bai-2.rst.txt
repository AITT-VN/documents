5. Bài 2: Cảnh báo khi thiếu nước
===================================

Mục tiêu
---------------------
---------------------

Khi biết tình trạng độ ẩm, chúng ta có thể chăm sóc cây tốt hơn để tăng năng suất của cây trồng. Hãy cùng thực hành dự án đơn giản: hiển thị mặt vui khi đất đủ ẩm, ngược lại, hiển thị mặt buồn khi đất thiếu ẩm nhé!


Thiết bị cần dùng
--------------------
--------------------

- Cảm biến độ ẩm đất

.. image:: images/planbit_30.png
    :width: 200px
    :align: center
|
- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: images/planbit_31.png
    :width: 200px
    :align: center
|

Kết nối
---------------------
---------------------

- Kết nối **cảm biến độ ẩm đất** vào cổng P0

.. image:: images/planbit_32.png
    :width: 400px
    :align: center
|


Giới thiệu khối lệnh
------------------------
------------------------

.. image:: images/planbit_38.png
    :width: 700px
    :align: center  
|
.. image:: images/planbit_39.png
    :width: 700px
    :align: center 
|


Viết chương trình
-------------------------
-------------------------

1. Kéo thả **khối lệnh điều kiện** vào phần lặp lại mãi

.. image:: images/planbit_40.png
    :width: 200px
    :align: center
|
2. Kéo thả **khối lệnh so sánh** vào điều kiện nếu

.. image:: images/planbit_41.png
    :width: 300px
    :align: center
|
3. Đặt điều kiện nếu độ ẩm đất ≤ 30% như sau:

- Đặt **khối lệnh đọc độ ẩm đất** và **khối lệnh số vào khối lệnh so sánh**

- Chọn phép so sánh là ≤

-  Thay giá trị **khối lệnh số** là 30

.. image:: images/planbit_42.png
    :width: 600px
    :align: center
|
4. Nếu điều kiện đúng, hiện mặt buồn: Kéo thả **khối lệnh hiện hình ảnh SAD** vào phần thực hiện

Nếu không, hiện mặt vui: Kéo thả **khối lệnh hiện hình ảnh SMILE** vào phần nếu không

.. image:: images/planbit_43.png
    :width: 600px
    :align: center
|

Chương trình mẫu
---------------------
---------------------

- Cảnh báo khi thiếu nước: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CyjKX9K1Qmy8G2UvvjkrCUXAYO>`_

.. image:: images/planbit_44.png
    :width: 200px
    :align: center
|