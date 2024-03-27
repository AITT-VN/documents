6. Bài 5: Đèn giao thông
===================================

Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng làm một hệ thống mô phỏng đèn giao thông thực tế.



Kết nối 
--------------
--------------------

- Đèn 4 LED RGB (chân D5)

    .. image:: images/cityuno5_1.png
        :scale: 90%
        :align: center 
    |
- LED 4 kí số (chân D3-D4)

    .. image:: images/cityuno5_2.png
        :scale: 90%
        :align: center 
    |


- **Kết nối**

    .. image:: images/bai_6.2.png
        :scale: 90%
        :align: center 
    |

Lắp ráp mô hình 
------------
---------------

    .. image:: images/bai_6.3.png
        :scale: 90%
        :align: center 
    |

Giới thiệu khối lệnh 
----------
-----------------

    .. image:: images/cityuno5_3.png
        :scale: 90%
        :align: center 
    |
    .. image:: images/cityuno5_4.png
        :scale: 90%
        :align: center 
    |


Viết chương trình 
----------
-----------------

1. Gửi ra thông điệp 1 kích hoạt khối lệnh đèn giao thông:

    .. image:: images/cityuno5_5.png
        :scale: 90%
        :align: center 
    |
2. Khi nhận được thông điệp 1 sẽ kích hoạt trạng thái đèn đỏ:

    .. image:: images/cityuno5_6.png
        :scale: 90%
        :align: center 
    |
3. Tạo 1 vòng lặp đếm ngược từ 5 về 0 và hiện giá trị lên màn hình 4 số:

    .. image:: images/cityuno5_7.png
        :scale: 90%
        :align: center 
    |
4. Sau đó gửi tiếp thông điệp 2 để sang trạng thái đèn xanh:

    .. image:: images/cityuno5_8.png
        :scale: 90%
        :align: center 
    |
5. Thực hiện tương tự trang thái đèn đỏ cho trạng thái đèn xanh:

    .. image:: images/cityuno5_9.png
        :scale: 90%
        :align: center 
    |
6. Sau đó sẽ gửi thông điệp 3 để chuyển sang màu vàng (đèn vàng 3 giây):

    .. image:: images/cityuno5_10.png
        :scale: 90%
        :align: center 
    |
7. Sau khi đèn vàng 3 giây sẽ gửi thông điệp về thông điệp 1

Chương trình mẫu 
-----------------
-------------------

- Đèn giao thông: 

.. image:: images/cityuno5_11.png
    :scale: 90%
    :align: center 








