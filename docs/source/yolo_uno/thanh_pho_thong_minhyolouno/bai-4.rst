5. Bài 4: Hệ thống cảnh báo tốc độ
=================================

Mục tiêu 
----------
--------------

Trong thành phố, di chuyển vượt tốc độ là hành vi vi phạm. Vì vậy, thiết bị đo tốc độ rất cần thiết để kiểm tra tốc độ chạy của xe. Nếu tốc độ của xe vượt mức quy định, hệ thống sẽ hiển thị số lần vi phạm và giá trị vận tốc lớn nhất của xe lên màn hình LCD. 

Kết nối
----------
--------------

- Cảm biến khoảng cách (D9-D10)

    .. image:: images/cityuno4_1.png
        :scale: 90%
        :align: center 
    |
- Màn hình LCD OLED (I2C)

    .. image:: images/cityuno4_2.png
        :scale: 90%
        :align: center 
    |
- **Kết nối**

    .. image:: images/bai_5.3.png
        :scale: 90%
        :align: center 
    |


Lắp ráp mô hình 
-------------
---------------

    .. image:: images/bai_5.4.png
        :scale: 90%
        :align: center 
    |
    
Giới thiệu khối lệnh 
--------------
----------------

    .. image:: images/cityuno4_3.png
        :scale: 90%
        :align: center 
    |

Cách tính vận tốc 
----------
-------------

    .. image:: images/bai_5.7.png
        :scale: 90%
        :align: right

Để tính vận tốc xe, chúng ta sẽ sử dụng công thức sau:
 
    **v = S / t**

Trong đó:
    - v là vận tốc 
    - S là quãng đường
    - t là thời gian

Ta sẽ tiến hành đo khoảng cách đến xe trong 2 mốc thời gian khác nhau, từ đó tính ra quãng đường xe đi được:

    **S = Khoảng cách 1 - Khoảng cách 2**

    **Thời gian di chuyển = thời gian giữa 2 mốc thời gian**

    .. image:: images/bai_5.8.png
        :scale: 90%
        :align: center 


Viết chương trình 
----------
------------

1. Tạo 3 biến để chứa giá trị tốc độ, khoảng cách 1 và khoảng cách 2. Gán giá trị 0 cho các biến này

    .. image:: images/cityuno4_4.png
        :scale: 90%
        :align: center 
    |
2.  Nếu phát hiện có xe đến gần (khoảng cách < 40cm), tiến hành đo khoảng cách tại 2 thời điểm cách nhau 1 giây và lưu giá trị vào biến tương ứng:

    .. image:: images/cityuno4_5.png
        :scale: 90%
        :align: center 
    |
4. Lồng điều kiện nếu xe đang tiến lại gần (khoảng cách 2 < khoảng cách 1) vào bên trong Áp dụng công thức tính vận tốc vào và gán giá trị tính được vào biến tốc độ (thời gian là 1 giây):

    .. image:: images/cityuno4_6.png
        :scale: 90%
        :align: center 
    |

6. Nếu tốc độ quá hạn mức quy định (15), ta tiến hành bật đèn LED thành màu đỏ và xóa màn hình LCD:

    .. image:: images/cityuno4_7.png
        :scale: 90%
        :align: center 
    |
7. In dòng chữ “Speed Over - Slowdown!” :

    .. image:: images/cityuno4_8.png
        :scale: 90%
        :align: center 
    |

9. Nếu tốc độ không vượt mức 15, bật đèn LED thành màu xanh và hiển thị giá trị tốc độ lên màn hình LCD

    .. image:: images/cityuno4_9.png
        :scale: 90%
        :align: center 
    |

Chương trình mẫu 
---------------
-----------------

- Hệ thống cảnh báo tốc độ: 

.. image:: images/cityuno4_10.png
        :scale: 90%
        :align: center 
    |


























