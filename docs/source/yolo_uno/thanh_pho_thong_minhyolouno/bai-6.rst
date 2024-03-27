7. Bài : Hệ thống theo dõi chất lượng không khí và tiếng ồn
========================================

Mục tiêu
------------
------------------

- Ở thành phố, chất lượng không khí là mối quan tâm hàng đầu.Tương tự, ô nhiễm tiếng ồn cũng là mối quan tâm hàng đầu cho sức khỏe người dân. Để đo lường và đưa ra giải pháp tương ứng, chúng ta hãy cùng lập trình một hệ thống để theo dõi chất lượng không khí và thời tiết nhé! Các giá trị này sẽ được hiển thị trên màn hình LCD.



Kết nối 
--------
--------------

- Cảm biến nhiệt độ độ ẩm DHT20 (I2C2)

    .. image:: images/bai_7.1.png
        :scale: 90%
        :align: center 
    |
- Cảm biến chất lượng không khí MQ-135 (A0)

    .. image:: images/bai_7.2.png
        :scale: 90%
        :align: center 
    |

- Cảm biến cường độ âm thanh (A1)

    .. image:: images/cityuno6_1.png
        :scale: 90%
        :align: center 

**Lưu ý:** Cảm biến chất lượng không khí sẽ ấm lên khi được cấp điện, đây là đặc tính đốt nóng không khí của thiết bị.

- Màn hình LCD OLED (I2C1)

    .. image:: images/bai_7.3.png
        :scale: 90%
        :align: center 
    |
- **Kết nối**

    .. image:: images/bai_7.4.png
        :scale: 90%
        :align: center 
    |


Lắp ráp mô hình 
------------
---------------

    .. image:: images/bai_7.5.png
        :scale: 90%
        :align: center 
    |
    .. image:: images/bai_7.6.png
        :scale: 90%
        :align: center 
    |
    |

Giới thiệu khối lệnh 
----------
-----------------

    .. image:: images/cityuno6_2.png
        :scale: 90%
        :align: center 
    |
    .. image:: images/cityuno6_3.png
        :scale: 90%
        :align: center 
    |
    .. image:: images/cityuno6_4.png
        :scale: 90%
        :align: center 
    |

Viết chương trình 
----------
-----------------

1. Sử dụng câu lệnh **sau mỗi 5 giây thực hiện**.

    .. image:: images/cityuno6_5.png
        :scale: 90%
        :align: center 
    |
2. Xóa màn hình LCD trước đó và in ra giá trị nhiệt độ, độ ẩm, chất lượng không khí (PPM), mức độ âm thanh lên màn hình LCD tại vị trí 3 hàng khác nhau:

    .. image:: images/cityuno6_6.png
        :scale: 90%
        :align: center 
    |

Chương trình mẫu 
-----------------
-------------------

- Hệ thống theo dõi thời tiết và chất lượng không khí: 

.. image:: images/cityuno6_7.png
    :scale: 90%
    :align: center 





















