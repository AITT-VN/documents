11. Bài 9: Điốt 
==================

Giới thiệu
--------
-----------

- **Đi-ốt bán dẫn** (Diode) là một loại linh kiện chỉ cho phép dòng điện đi qua nó theo một chiều mà không theo chiều ngược lại. Cực dương của Đi-ốt được gọi là **Anode** và cực âm là **Cathode**.

    .. image:: images/9.1.png
        :width: 400px
        :align: center 
    |
- Dòng điện sẽ được thông qua nếu nối đúng nguồn điện dương vào **Anode** và nguồn điện âm vào **Cathode**. Nếu nối ngược lại thì cần nguồn điện lên đến 1000 V mới có thể phá vỡ quy tắc của Đi-ốt. 

- Đi-ốt được áp dụng để bảo vệ mạch tránh các tình trạng mạch cấp nguồn ngược, phổ biến ở các dạng mạch có pin, mạch chỉnh lưu, tách sóng,...


Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Nguồn điện 3V.
    - Điện trở R1 100 Ω. 
    - Đi-ốt D1.
    - Động cơ M1.

- **Sơ đồ mạch điện**

    .. image:: images/bai_9.1.png
        :width: 500px
        :align: center 
    
*Mạch điện này gần giống như mạch điện trong bài trước về động cơ, tuy nhiên ta thêm vào một Đi-ốt D1 ở trước động cơ.*


- **Nguyên lý hoạt động:**

    Chân P1 được nối với nút nhấn và sẽ đọc trạng thái của nút nhấn để ra lệnh cho P0 bật hay tắt động cơ.


Kết nối mạch điện 
-----------
-------------

Hãy kết nối mạch điện như hình minh họa: 

    .. image:: images/bai_9.2.png
        :width: 500px
        :align: center 
    |

Chương trình
---------
-----------------

Trong chương trình ta sẽ liên tục đọc giá trị của P1.

    - Nếu P1 bị tắt (nút nhấn đang được nhấn và nối xuống Ground) thì ta sẽ bật chân P0 để bật động cơ. 
    - Và ngược lại, nếu chân P1 đang được bật (tức là nút nhấn được trả về trạng thái tắt ban đầu và P1 không được nối xuống Ground) thì ta sẽ tắt chân P0 để tắt động cơ. 

    .. image:: images/bai_9.3.png
        :width: 1000px
        :align: center 
    |

Kết quả
----------
---------------

Kết quả của chương trình: 

    .. image:: images/bai_9.4.png
        :width: 600px
        :align: center 
    |

Có thể bạn chưa biết?
---------
------------------

    .. image:: images/9.4.png
        :width: 200px
        :align: right
    |
Ngoài Đi-ốt thông thường và Đi-ốt phát quang, chúng ta còn nhiều loại Đi-ốt khác với các chức năng khác nhau rất hữu ích cho đời sống của con người, có thể kể đến:

    - Đi-ốt Laser: Tạo ra ánh sáng kết hợp (Laser).

    - Đi-ốt Quang: Chuyển ánh sáng thành năng lượng điện. Ứng dụng trong pin mặt trời.

    - Đi-ốt Barritt: Tạo ra các tín hiệu vi sóng đơn giản. Ứng dụng trong các báo động chống trộm.

    - Đi-ốt Gunn: Tạo ra tín hiệu sóng tần số cao. Ứng dụng trong các máy bắn tốc độ, cửa tự động,..



Chương trình mẫu
--------------
-------------------

- Điốt: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BvniLlgHLzWvdsHNHkLFUu2Yom>`_

.. image:: images/bai_9.5.png
    :width: 200px
    :align: center















