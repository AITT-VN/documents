4. Bài 3: Thùng rác thông minh
==================================

Mục tiêu 
--------------
-------------

Một thùng rác thông minh với khả năng tự động mở nắp khi có người đến gần sẽ mang lại sự tiện lợi hơn rất nhiều, giúp thành phố xanh sạch đẹp hơn. Trong bài này, chúng ta hãy cùng lập trình một thùng rác có khả năng tự mở nắp khi có người và tự động báo hiệu khi thùng rác đầy nhé


Kết nối 
-----------
--------------

- Cảm biến vật cản (D3-D4)

    .. image:: images/cityuno3_1.png
        :scale: 90%
        :align: center 
    |    

- Động cơ Servo (D2)

    .. image:: images/cityuno3_2.png
        :scale: 90%
        :align: center 
    |
**Lưu ý:** Chỉnh góc Servo về góc 20 trước khi lắp ráp 

- **Kết nối**

    .. image:: images/bai_3.4.png
        :scale: 90%
        :align: center 
    |

Lắp ráp mô hình 
-------------
---------------

    .. image:: images/bai_3.5.png
        :scale: 90%
        :align: center 
    |

Giới thiệu khối lệnh 
-------------------
-----------------------

    .. image:: images/cityuno3_3.png
        :scale: 90%
        :align: center 
    | 

Viết chương trình 
-------------
-------------------

1. Quay Servo chân D2 đến góc 20 độ (đóng nắp thùng rác)

    .. image:: images/cityuno3_4.png
        :scale: 90%
        :align: center 
    |
2. Tạo điều kiện: nếu cảm biến vật cản phát hiện có người phía trước cảm biến

    .. image:: images/cityuno3_5.png
        :scale: 90%
        :align: center 
    |

3. Sau 3 giây, ta đóng nắp thùng rác (quay Servo về góc 20 độ)

    .. image:: images/cityuno3_6.png
        :scale: 90%
        :align: center 
    |

Chương trình mẫu 
---------------
-----------------

- Thùng rác thông minh 

.. image:: images/cityuno3_7.png
    :scale: 90%
    :align: center 


