5. Bài 3: Thùng rác thông minh
==================================

Mục tiêu 
--------------
-------------

Một thùng rác thông minh với khả năng tự động mở nắp khi có người đến gần sẽ mang lại sự tiện lợi hơn rất nhiều, giúp thành phố xanh sạch đẹp hơn. Trong bài này, chúng ta hãy cùng lập trình một thùng rác có khả năng tự mở nắp khi có người và tự động báo hiệu khi thùng rác đầy nhé


Kết nối 
-----------
--------------

- Cảm biến vật cản (P0)

    .. image:: images/bai_3.1.png
        :width: 200px
        :align: center 
    |    
- Cảm biến chuyển động PIR (P1)

    .. image:: images/bai_3.2.png
        :width: 200px
        :align: center 
    |
- Động cơ Servo (P4)

    .. image:: images/bai_3.3.png
        :width: 200px
        :align: center 
    |
**Lưu ý:** Chỉnh góc Servo về 20o trước khi lắp ráp 

- **Kết nối**

    .. image:: images/bai_3.4.png
        :width: 600px
        :align: center 
    |

Lắp ráp mô hình 
-------------
---------------

    .. image:: images/bai_3.5.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_3.6.png
        :width: 1000px
        :align: center 
    |   
    .. image:: images/bai_3.7.png
        :width: 1000px
        :align: center 
    | 
    .. image:: images/bai_3.8.png
        :width: 1000px
        :align: center 
    | 
    .. image:: images/bai_3.9.png
        :width: 1000px
        :align: center 
    | 

Giới thiệu khối lệnh 
-------------------
-----------------------

    .. image:: images/bai_3.10.png
        :width: 1000px
        :align: center 
    | 
    .. image:: images/bai_3.11.png
        :width: 1000px
        :align: center 
    | 

Viết chương trình 
-------------
-------------------

1. Quay Servo chân P4 đến góc 20 độ (đóng nắp thùng rác)

    .. image:: images/bai_3.12.png
        :width: 800px
        :align: center 
    |
2. Tạo điều kiện: nếu cảm biến PIR phát hiện có người

    .. image:: images/bai_3.13.png
        :width: 800px
        :align: center 
    |
3.  Lồng điều kiện ghép vào bên trong: nếu thùng rác chưa đầy (cảm biến vật cản không phát hiện có rác trong thùng, khối lệnh có giá trị sai)

    .. image:: images/bai_3.14.png
        :width: 800px
        :align: center 
    |
4. Đổi màu đèn LED thành màu xanh và phát bài nhạc JUMP_UP để báo hiệu, sau đó quay Servo đến góc 90 để mở nắp thùng rác:

    .. image:: images/bai_3.15.png
        :width: 800px
        :align: center 
    |
5. Sau 3 giây, ta đóng nắp thùng rác (quay Servo về góc 20 độ)

    .. image:: images/bai_3.16.png
        :width: 800px
        :align: center 
    |
6.  Nếu cảm biến PIR phát hiện có người nhưng thùng rác đang đầy, hiển thị chữ Full lên màn hình:

    .. image:: images/bai_3.17.png
        :width: 800px
        :align: center 
    |
7. Tạm dừng chương trình trong khoảng 200 ms

    .. image:: images/bai_3.18.png
        :width: 800px
        :align: center 
    |
8. Nhấn nút A để mở, nhấn nút B để đóng thùng rác khi cần

    .. image:: images/bai_3.19.png
        :width: 800px
        :align: center 
    |

Chương trình mẫu 
---------------
-----------------

- Thùng rác thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Bs5g0o3KGfAHHN3lmBkIGuWmGA>`_

.. image:: images/bai_3.20.png
    :width: 200px
    :align: center 


