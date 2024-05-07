12. Vườn thông minh
========

1. Mục tiêu
---------
---------

Trong bài này, chúng ta làm một ứng dụng nhỏ đó là giám sát độ ẩm đất và bật tắt máy bơm tự động.

2. Kết nối 
-----
---------

Để sử dụng máy bơm mini bạn cần module 2 kênh USB để kích điện áp lên 5V và kết nối vào cổng D9-D10 của Yolo UNO và máy bơm mini vào cổng USB trên module này. 

Kết nối cảm biến độ ẩm đất vào cổng A1:

..  image:: images/vuon_thong_minh.png
    :scale: 80%
    :align: center 
|

3. Chương trình Arduino
------
-------

.. code-block:: arduino

    void setup() {

    }

    void loop() {
        if ((analogRead(A1)/10.24 > 60)) { // độ ẩm đất lớn hơn ngưỡng 60%
            analogWrite(D9, 0); // tắt máy bơm
        }

        if ((analogRead(A1)/10.24 < 20)) {
            analogWrite(D9, 250); // bật máy bơm
        }
    }
