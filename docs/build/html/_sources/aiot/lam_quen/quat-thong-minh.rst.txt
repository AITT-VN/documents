9. Quạt thông minh
=============

1. Mục tiêu 
----------
---------------

Sau khi đã làm quen với cảm biến DHT20 và màn hình LCD, chúng ta sẽ cùng nâng cấp dự án lên 1 cấp độ phức tạp hơn, đó là quạt mini tự hoạt động dựa vào nhiệt độ của môi trường. Cụ thể, hệ thống sẽ hoạt động dựa vào nhiệt độ mà cảm biến DHT20 gửi về:

    - Nếu nhiệt độ lớn hơn 27 độ thì quạt sẽ bật
    - Nếu nhiệt độ nhỏ hơn 27 độ thì quạt sẽ tắt

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Màn hình LCD1602

.. image:: images/7.1.jpg
    :scale: 40 %
    :align: center
|
- Cảm biến nhiệt độ độ ẩm DHT20

.. image:: images/8.1.jpg
    :width: 30 %
    :align: center
| 
- Quạt mini

.. image:: images/6.3.jpg
    :scale: 40 %
    :align: center
|
3. Kết nối 
-------
------------

- Kết nối màn hình LCD1602 và cảm biến nhiệt độ độ ẩm DHT20 vào 2 cổng I2C
- Kết nối quạt mini vào cổng P10/P13

.. image:: images/9.1.png
    :width: 400px
    :align: center
| 

4. Lập trình 
-------
----------

Để điều khiển quạt mini, chúng ta sử dụng khối lệnh sau:

.. image:: images/9.2.png
    :scale: 100 %
    :align: center
|
Trước tiên, chúng ta hãy tạo điều kiện: Nếu nhiệt độ ≥ 27, quạt sẽ bật với tốc độ 50. Ngược lại, nếu nhiệt độ nhỏ hơn 27 độ thì quạt sẽ tắt (tương ứng với 0%):

.. image:: images/9.3.png
    :scale: 100 %
    :align: center
|
Đồng thời, bạn đừng quên dùng khối lệnh cập nhật cảm biến nhiệt độ & độ ẩm để theo dõi nhiệt độ thay đổi như thế nào nhé. Chương trình hoàn chỉnh sẽ như sau:

.. image:: images/9.4.png
    :scale: 100 %
    :align: center
|
5. Chương trình mẫu 
-------
------------

- Quạt thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWPTF1borEvQzh1t9UQAyUqBlG>`_

.. image:: images/9.5.png
    :width: 200px
    :align: center 