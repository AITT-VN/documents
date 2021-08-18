Giới thiệu
====================

Ở phần trước, bạn đã làm quen với các module và cách lập trình để làm việc với chúng một cách đơn giản. Trong phần này, để ứng dụng kiến thức đã học, chúng ta hãy cùng nhau xây dựng một dự án nhà thông minh hoàn chỉnh, bao gồm các chức năng sau:

  1. Đèn điều khiển từ xa

    ``Có thể bật tắt và điều chỉnh độ sáng tối đèn của ngôi nhà từ xa bằng remote``
  
  2.Quạt thông minh

    ``Tự động bật tắt quạt một cách thông minh dựa trên nhiệt độ và độ ẩm của ngôi nhà.``
  
  3. Đèn thông minh

    ``Tự động bật khi trời tối và khi phát hiện có người đến gần``
  
  4. Hệ thống chống trộm
    
    ``Phát âm thanh cảnh báo khi phát hiện có sự đột nhập (nếu chế độ bảo vệ được bật).``
  
  5. Cửa thông minh
    
    ``Có thể khóa và mở khóa cửa bằng mật mã (nhập mật mã bằng remote)``


Sơ đồ nối dây hoàn chỉnh của hệ thống như sau:
--------------

.. image:: images/intro-1.png
  :width: 600px
  :align: center

=============== ==========
 xController     Thiết bị 
 PORT 1          LCD 1602  
 PORT 2          DHT11  
 PORT 3          Quạt Mini  
 PORT 4          Cảm biến ánh sáng  
 PORT 5          Cảm biến PIR 
 PORT 6          Đèn LED
 S1              Servo 
 Jack pin        Pin 
=============== ==========

Chương trình mẫu
+++++++++++++++++

* :download:`Arduino Tutorial Code <https://github.com/AITT-VN/xbuild_creator_kit/tree/main/Arduino>`