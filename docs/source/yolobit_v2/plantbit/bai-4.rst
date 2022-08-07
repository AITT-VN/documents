7. Bài 4: Tưới nước tự động
=====================================

Mục tiêu
-----------------------
-----------------------

Chúng ta sẽ lập trình để máy bơm tự động tưới nước cho cây, dựa vào độ ẩm của đất. Việc này sẽ giúp tiết kiệm thời gian cho chúng ta, đồng thời cây trồng cũng được tưới một lượng nước thích hợp nhờ vào dữ liệu tính toán từ máy tính và thiết bị thông minh. 

Thiết bị cần dùng
-----------------------
-----------------------

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
-  Module đóng ngắt 2 kênh

.. image:: images/planbit_45.png
    :width: 200px
    :align: center
|
-  Động cơ bơm nước

.. image:: images/planbit_46.png
    :width: 200px
    :align: center
|


Kết nối
------------------------
------------------------

Kiểm tra lại kết nối tương tự như bài 2 và bài 3.

    - Bài 2: Kết nối cảm biến độ ẩm đất vào cổng P0

    - Bài 3: Kết nối Module đóng ngắt 2 kênh vào cổng P14/P15. Nối động cơ bơm nước vào cổng USB Output1.


Viết chương trình
------------------------
------------------------

1. Bắt đầu với chương trình cảu bài 2

.. image:: images/planbit_54.png
    :width: 550px
    :align: center
|
2. Khi đất thiếu nước, cần tưới nước cho cây: Kéo thả khối lệnh bật máy bơm với tốc độ 50% vào phần thực hiện.

.. image:: images/planbit_55.png
    :width: 600px
    :align: center
|
3. Bơm nước trong 3 giây, sau đó tắt máy bơm

.. image:: images/planbit_56.png
    :width: 600px
    :align: center
|


Chương trình mẫu
---------------------
---------------------

- Tưới nước tự động: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CynwjSnyeJMarOU7VUV38SRte1>`_

.. image:: images/planbit_57.png
    :width: 200px
    :align: center
|