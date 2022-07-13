7. Bài 5: Hệ thống cảnh báo tốc độ
=================================

Mục tiêu 
----------
--------------

Trong thành phố, di chuyển vượt tốc độ là hành vi vi phạm. Vì vậy, thiết bị đo tốc độ rất cần thiết để kiểm tra tốc độ chạy của xe. Nếu tốc độ của xe vượt mức quy định, hệ thống sẽ hiển thị số lần vi phạm và giá trị vận tốc lớn nhất của xe lên màn hình LCD. 

Kết nối
----------
--------------

- Cảm biến khoảng cách (P10/P13)

    .. image:: images/bai_5.1.png
        :width: 200px
        :align: center 
    |
- Màn hình LCD OLED (I2C1)

    .. image:: images/bai_5.2.png
        :width: 200px
        :align: center 
    |
- **Kết nối**

    .. image:: images/bai_5.3.png
        :width: 400px
        :align: center 
    |


Lắp ráp mô hình 
-------------
---------------

    .. image:: images/bai_5.4.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_5.5.png
        :width: 1000px
        :align: center 
    |

Giới thiệu khối lệnh 
--------------
----------------

    .. image:: images/bai_5.6.png
        :width: 1000px
        :align: center 
    |

Cách tính vận tốc 
----------
-------------

    .. image:: images/bai_5.7.png
        :width: 400px
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
        :width: 600px
        :align: center 


Viết chương trình 
----------
------------

1. Tạo 3 biến để chứa giá trị tốc độ, khoảng cách 1 và khoảng cách 2. Gán giá trị 0 cho các biến này

    .. image:: images/bai_5.9.png
        :width: 400px
        :align: center 
    |
2. Khởi tạo cảm biến khoảng cách tại cổng P10/P13 và màn hình LCD:

    .. image:: images/bai_5.10.png
        :width: 800px
        :align: center 
    |
3.  Nếu phát hiện có xe đến gần (khoảng cách < 40cm), tiến hành đo khoảng cách tại 2 thời điểm cách nhau 1 giây và lưu giá trị vào biến tương ứng:

    .. image:: images/bai_5.11.png
        :width: 800px
        :align: center 
    |
4. Lồng điều kiện nếu xe đang tiến lại gần (khoảng cách 2 < khoảng cách 1) vào bên trong:

    .. image:: images/bai_5.12.png
        :width: 800px
        :align: center 
    |
5. Áp dụng công thức tính vận tốc vào và gán giá trị tính được vào biến tốc độ (thời gian là 1 giây):

    .. image:: images/bai_5.13.png
        :width: 800px
        :align: center 
    |
6. Nếu tốc độ quá hạn mức quy định (15), ta tiến hành bật đèn LED thành màu đỏ và xóa màn hình LCD:

    .. image:: images/bai_5.14.png
        :width: 800px
        :align: center 
    |
7. In dòng chữ “Vuot qua toc do” và giá trị tốc độ lên màn hình LCD (lấy thông tin từ biến tốc độ):

    .. image:: images/bai_5.15.png
        :width: 800px
        :align: center 
    |
8. Lặp lại 2 nốt nhạc A5 và E3 liên tục 3 lần để báo hiệu:

    .. image:: images/bai_5.16.png
        :width: 800px
        :align: center 
    |
9. Nếu tốc độ không vượt mức 15, bật đèn LED thành màu xanh và hiển thị giá trị tốc độ lên màn hình LCD

    .. image:: images/bai_5.17.png
        :width: 700px
        :align: center 
    |
10. Tạm dừng chương trình trong 2 giây để xe rời khỏi

    .. image:: images/bai_5.18.png
        :width: 700px
        :align: center 
    |
11. Tạm dừng toàn bộ chương trình trong 50ms ở cuối chương trình

    .. image:: images/bai_5.19.png
        :width: 700px
        :align: center 
    |

Chương trình mẫu 
---------------
-----------------

- Hệ thống cảnh báo tốc độ: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BsHSUZg4JGKkIpGDnjW8Vj86ya>`_

.. image:: images/bai_5.20.png
    :width: 200px
    :align: center 



























