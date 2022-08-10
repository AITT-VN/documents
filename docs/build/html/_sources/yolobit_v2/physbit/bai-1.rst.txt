3. Bài 1: Đèn LED
=================================

Giới thiệu
----------
----------------

**Bóng đèn LED** là một thiết bị rất phổ biến trong cuộc sống hiện nay. 
Với ưu điểm như độ bền cao và tiêu thụ điện thấp, đèn LED được ứng dụng vào hầu hết các thiết bị điện hiện có trên thị trường.


Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Đèn LED 

    - Điện trở R1 100 Ω. 

- **Sơ đồ mạch điện**

    .. image:: images/1.1.png
        :width: 600px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    - Lỗ cắm GND trên Phys:Bit là cực âm của nguồn điện, lỗ cắm 3V là cực dương của nguồn. Chân cắm P0 có thể đóng vai trò như cực âm khi chân P0 tắt và đóng vai trò như cực dương khi P0 bật.

    - Khi bật chân P0 (P0 đóng vai trò như cực dương của nguồn điện), mạch điện sẽ kín, dòng điện chạy từ cực dương sang cực âm và đèn LED sáng do có dòng điện chạy qua. 
    
    - Khi tắt chân P0 (P0 đóng vai trò như cực âm của nguồn điện), mạch điện sẽ hở, không có dòng điện chạy từ cực dương sang cực âm và đèn LED tắt do không có dòng điện chạy qua


Kết nối mạch điện 
-----------
-------------

Hãy kết nối mạch điện như hình minh họa: 

    .. image:: images/1.2.png
        :width: 500px
        :align: center 
    |

Chương trình
---------
-----------------

- Thực hiện chương trình như sau:

    .. image:: images/1.3.png
        :width: 1000px
        :align: center 
    |

- Bạn cũng có thể kết hợp bật và tắt LED sau mỗi 2 giây để tạo thành hiệu ứng LED chớp tắt như trên.

- Hãy kết nối với Yolo:Bit và chạy chương trình sau khi thực hiện các thao tác.

    .. image:: images/1.4.png
        :width: 400px
        :align: center 
    |

Kết quả
----------
---------------

Hãy bật công tắc của Phys:Bit.

    .. image:: images/1.5.png
        :width: 600px
        :align: center 
    |

Có thể bạn chưa biết? 
-----------
-------------

    .. image:: images/1_4.png
        :width: 200px
        :align: left 
    |
- Sử dụng đèn LED là một trong những giải pháp giúp việc sử dụng năng lượng trở nên hiệu quả hơn. Ngoài việc tiết kiệm năng lượng và có tuổi thọ cao lên đến hàng chục năm thì việc sử dụng đèn LED còn rất nhiều lợi ích cho sức khỏe và môi trường.

    .. image:: images/1_5.png
        :width: 200px
        :align: right
    |
- Ánh sáng từ đèn LED không gây ra triệu chứng đau đầu và cận thị như đèn huỳnh quang. Đèn LED cũng không bức xạ ra tia cực tím (nguyên nhân gây bệnh về da) như đèn sợi đốt.
|
- Đèn LED không tỏa nhiều nhiệt như các loại đèn truyền thống. Nếu thay thế đèn truyền thống bằng đèn LED thì môi trường sẽ không phải gánh chịu 258 triệu tấn khí thải carbon trong một năm. Điều đó giúp giảm thiểu hiệu ứng nhà kính, góp phần chống lại biến đổi khí hậu, ô nhiễm không khí, nguồn nước và ô nhiễm đất.”


Chương trình mẫu
--------------
-------------------

- Đèn LED: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BvXYmN5gD7iXbEf61CPlWBoTlK>`_

.. image:: images/1.6.png
    :width: 200px
    :align: center 

