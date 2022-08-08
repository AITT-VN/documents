<<<<<<< HEAD
10. Bài 7: Hệ thống theo dõi thời tiết và chất lượng không khí
========================================
=======
9. Bài 7: Hệ thống theo dõi thời tiết và chất lượng không khí
========================================

Mục tiêu
------------
------------------

- Ở thành phố, chất lượng không khí là mối quan tâm hàng đầu. Để đo lường và đưa ra giải pháp tương ứng, chúng ta hãy cùng lập trình một hệ thống để theo dõi chất lượng không khí và thời tiết nhé! Các giá trị này sẽ được hiển thị trên màn hình LCD.


- Nếu chất lượng không khí xuống thấp, hệ thống sẽ báo động bằng màn hình LED 5 x 5 trên Yolo:Bit.


Kết nối 
--------
--------------

- Cảm biến nhiệt độ độ ẩm DHT20 (I2C2)

    .. image:: images/bai_7.1.png
        :width: 200px
        :align: center 
    |
- Cảm biến chất lượng không khí MQ-135 (P0)

    .. image:: images/bai_7.2.png
        :width: 200px
        :align: center 

**Lưu ý:** Cảm biến chất lượng không khí sẽ ấm lên khi được cấp điện, đây là đặc tính đốt nóng không khí của thiết bị.

- Màn hình LCD OLED (I2C1)

    .. image:: images/bai_7.3.png
        :width: 200px
        :align: center 
    |
- **Kết nối**

    .. image:: images/bai_7.4.png
        :width: 200px
        :align: center 
    |


Lắp ráp mô hình 
------------
---------------

    .. image:: images/bai_7.5.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_7.6.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_7.7.png
        :width: 1000px
        :align: center 
    |

Giới thiệu khối lệnh 
----------
-----------------

    .. image:: images/bai_7.8.png
        :width: 1000px
        :align: center 
    |

Viết chương trình 
----------
-----------------

1. Reset bộ đếm thời gian và đặt điều kiện **nếu đọc bộ đếm thời gian > 3000 ms**.

    .. image:: images/bai_7.9.png
        :width: 600px
        :align: center 
    |
2. Khởi tạo màn hình LCD. Xóa màn hình LCD trước đó và in ra giá trị nhiệt độ, độ ẩm, chất lượng không khí (PPM) lên màn hình LCD tại vị trí 3 hàng khác nhau:

    .. image:: images/bai_7.10.png
        :width: 600px
        :align: center 
    |
3. Tạo điều kiện để báo động về chất lượng không khí: Nếu chất lượng không khí > 1000 (Đạt mức độ đáng báo động)

    .. image:: images/bai_7.11.png
        :width: 800px
        :align: center 
    |
4.  Nếu điều kiện đúng: Hiện đèn màu đỏ và thông báo “Khong khi: Xau” lên màn hình LCD
    
    Nếu không: đổi màu đèn LED thành màu xanh và hiển thị dòng chữ “TKhong khi: Tot” lên màn hình LCD

    .. image:: images/bai_7.12.png
        :width: 800px
        :align: center 
    |
5. Reset bộ đếm thời gian ở cuối điều kiện chính

    .. image:: images/bai_7.13.png
        :width: 800px
        :align: center 
    |

Chương trình mẫu 
-----------------
-------------------

- Hệ thống theo dõi thời tiết và chất lượng không khí: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BsZMk5w3M7jC7a3AXSgWQtA3iu>`_

.. image:: images/bai_7.14.png
    :width: 200px
    :align: center 





















>>>>>>> main
