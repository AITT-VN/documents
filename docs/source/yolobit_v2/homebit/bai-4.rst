7. Bài 4: Quạt thông minh
=====================================

Mục tiêu
-------------------
-------------------

Trong bài học này, chúng ta sẽ cùng lập trình bật quạt thông minh tùy theo nhiệt độ phòng ở: nếu trời nóng (nhiệt độ ≥ 29) thì quạt tự động bật, ngược lại, nếu trời lạnh (nhiệt độ < 29) thì quạt tự tắt.

Thiết bị cần dùng
-------------------
-------------------

.. image:: images/homebit_51.png
    :width: 400px
    :align: center
|   
.. image:: images/homebit_39.png
    :width: 400px
    :align: center
|   
- Kết nối cảm biến DHT20 và màn hình LCD như bài 2

- Kết nối quạt mini vào cổng P10

Giới thiệu khối lệnh
-------------------
-------------------

.. image:: images/homebit_40.png
    :width: 400px
    :align: center
|   
Viết chương trình
--------------------
-------------------

1. Tạo điều kiện: Nếu đọc nhiệt độ ≥ 29, thực hiện bật quạt với tốc độ 50

.. image:: images/homebit_52.png
    :width: 600px
    :align: center
|   
2. Tương tự, nếu nhiệt độ dưới 29, quạt sẽ tự tắt (tốc độ 0%)

.. image:: images/homebit_53.png
    :width: 600px
    :align: center
|   
