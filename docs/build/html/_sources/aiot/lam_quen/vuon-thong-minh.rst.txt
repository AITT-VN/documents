12. Vườn thông minh
====================================

1. Mục tiêu 
----------
---------------

Trong dự án này, chúng ta sẽ thực hiện một hệ thống vườn thông minh, có thể tưới nước tự động dựa trên độ ẩm đất nhé!

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Cảm biến độ ẩm đất

.. image:: images/12.1.jpg
    :scale: 40 %
    :align: center
|

- Module đóng ngắt 2 kênh

.. image:: images/12.2.jpg
    :scale: 40 %
    :align: center
|

- Máy bơm mini

.. image:: images/12.3.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối cảm biến độ ẩm đất vào cổng P0
- Kết nối module đóng ngắt 2 kênh vào cổng P14/15. Trong đó, đầu kết nối usb của máy bơm nối vào output 1 của module 2 kênh như hình: 

.. image:: images/12.4.png
    :width: 450px
    :align: center
| 

4. Lập trình 
-------
----------

- **Giới thiệu khối lệnh**

Để sử dụng cảm biến độ ẩm đất, bạn hãy sử dụng khối lệnh sau: 

    - Khối lệnh này sẽ giúp bạn đọc phần trăm độ ẩm đất của khu vực mà bạn cắm cảm biến vào. 

.. image:: images/12.5.png
    :scale: 100 %
    :align: center
|

    - Ngoài ra, để điều khiển máy bơm qua mô đun đóng ngắt 2 kênh usb, bạn dùng khối lệnh sau:

.. image:: images/12.6.png
    :scale: 100 %
    :align: center
|

- **Lập trình**

Với sự kết hợp của 2 khối lệnh này, chúng ta có thể lập trình 1 hệ thống tưới nước tự động theo độ ẩm đất, với yêu cầu như sau:

    - Khi độ ẩm đất dưới 30% thì bật máy bơm với 70% công suất
    
    - Khi độ ẩm lớn hơn 70% thì tắt máy bơm (tương ứng với 0%)

Chúng ta sẽ sử dụng câu lệnh điều kiện nếu … thực hiện … để viết chương trình như sau:

.. image:: images/12.7.png
    :scale: 100 %
    :align: center
|

Sau khi đã thực hiện bật tắt máy bơm tự động, chúng ta sẽ cho hiển thị độ ẩm đất lên màn hình để quan sát. Với khối lệnh hiển thị lên màn hình LCD như các dự án trước, khối lệnh hiển thị ở dự án này sẽ như sau:

.. image:: images/12.8.png
    :scale: 100 %
    :align: center
|

Kết hợp các khối lệnh với nhau, ta sẽ có chương trình hoàn chỉnh về vườn thông minh, với tính năng tự đo độ ẩm đất và tưới nước, hiển thị phần trăm độ ẩm đất lên màn hình LCD1602

.. image:: images/12.9.png
    :scale: 80 %
    :align: center
|

5. Chương trình mẫu 
-------
------------

- Vườn thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWYdCrfrWrKnDBlb6fpUtxsOqk>`_

.. image:: images/12.10.png
    :width: 200px
    :align: center 