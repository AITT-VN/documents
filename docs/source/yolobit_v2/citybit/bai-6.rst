<<<<<<< HEAD
9. Bài 6: Đèn giao thông
===================================
=======
8. Bài 6: Đèn giao thông
===================================

Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng làm một hệ thống mô phỏng đèn giao thông thực tế.

- Khi nhấn nút A: chế độ đèn giao thông bình thường

-  Khi nhấn nút B: chế độ ban đêm (đèn sẽ nhấp nháy đèn vàng)


Kết nối 
--------------
--------------------

- Đèn LED (số lương: 3)

    .. image:: images/bai_6.1.png
        :width: 200px
        :align: center 
    |
- Đèn LED Đỏ: P0

- Đèn LED Vàng: P1

- Đèn LED Xanh: P2


- **Kết nối**

    .. image:: images/bai_6.2.png
        :width: 400px
        :align: center 
    |

Lắp ráp mô hình 
------------
---------------

    .. image:: images/bai_6.3.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_6.4.png
        :width: 1000px
        :align: center 
    |

Giới thiệu khối lệnh 
----------
-----------------

    .. image:: images/bai_6.5.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_6.6.png
        :width: 400px
        :align: center 
    |


Viết chương trình 
----------
-----------------

1. Tạo một biến tên là chế độ và gán giá trị 0 vào biến:

    .. image:: images/bai_6.7.png
        :width: 400px
        :align: center 
    |
2. Khi nút A được nhấn, cho chế độ bằng 0

    .. image:: images/bai_6.8.png
        :width: 400px
        :align: center 
    |
3. Khi nút B được nhấn, cho chế độ bằng 1 và hiển thị hình dấu chấm than lên màn hình Yolo:Bit

    .. image:: images/bai_6.9.png
        :width: 400px
        :align: center 
    |
4. Trong chế độ đèn giao thông, cho bật đèn LED màu xanh (chân P2):

    .. image:: images/bai_6.10.png
        :width: 400px
        :align: center 
    |
5. Tạo hàm đếm 5 giây

    .. image:: images/bai_6.11.png
        :width: 400px
        :align: center 
    |
6. Tạo hàm đếm 3 giây

    .. image:: images/bai_6.12.png
        :width: 400px
        :align: center 
    |
7. Bật đèn xanh P2, gọi hàm đếm 5 giây, sau đó tắt đèn

    .. image:: images/bai_6.13.png
        :width: 400px
        :align: center 
    |
8. Bật đèn vàng P1, gọi hàm đếm 3 giây, sau đó tắt đèn

    .. image:: images/bai_6.14.png
        :width: 400px
        :align: center 
    |
9. Bật đèn đỏ P0, gọi hàm đếm 5 giây, sau đó tắt đèn

    .. image:: images/bai_6.15.png
        :width: 400px
        :align: center 
    |
10. Nếu chế độ = 1 (nút B được nhấn), ta tiến hành bật đèn vàng trong 1 giây và tắt đèn trong 0,5 giây liên tục

    .. image:: images/bai_6.16.png
        :width: 400px
        :align: center
    |

Chương trình mẫu 
-----------------
-------------------

- Đèn giao thông: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BsW3uYe2BBTDV3Oukf7uTGHmgY>`_

.. image:: images/bai_6.18.png
    :width: 200px
    :align: center 








>>>>>>> main
