10. Bài 8: Hệ thống phát hiện ngập nước
=====================================

Mục tiêu 
---------
--------------

- Tại các con đường ở vùng trũng trong thành phố thường xuất hiện tình trạng bị ngập nước. Do đó, chúng ta hãy cùng làm một hệ thống theo dõi và báo động tình trạng ngập nước nhé. 


- Khi bị ngập nước, đèn LED ở 2 bên đường sẽ báo động để các xe đang lưu thông biết và né tránh các đoạn đường này.


Kết nối 
--------
--------------

- Cảm biến mực nước (P1)

    .. image:: images/bai_8.1.png
        :width: 200px
        :align: center 
    |

- **Kết nối**

    .. image:: images/bai_8.2.png
        :width: 400px
        :align: center 
    |

Lắp ráp mô hình 
------------
---------------

Sử dụng lại mô hình trạm theo dõi thời tiết và chất lượng không khí. Nối thêm module cảm biến mực nước để hoàn thiện.
   
    .. image:: images/bai_8.3.png
        :width: 400px
        :align: center 
    |

Giới thiệu khối lệnh 
----------
-----------------

    .. image:: images/bai_8.4.png
        :width: 900px
        :align: center 
    |

Viết chương trình 
----------
-----------------

1. Tạo điều kiện **nếu đọc bộ đếm thời gian ≥ 3000 ms**

    .. image:: images/bai_8.5.png
        :width: 600px
        :align: center 
    |
2. Đặt điều kiện: nếu đọc cảm biến ngập nước > 40%

    .. image:: images/bai_8.6.png
        :width: 600px
        :align: center 
    |
3. Nếu điều kiện:

    - Đúng: đổi các LED thành màu đỏ

    - Sai: Đổi các LED thành màu xanh lá

    .. image:: images/bai_8.7.png
        :width: 600px
        :align: center 
    |
4. Reset bộ đếm thời gian ở cuối điều kiện

    .. image:: images/bai_8.8.png
        :width: 600px
        :align: center 
    |

Chương trình mẫu 
-----------------
-------------------

- Hệ thống phát hiện ngập nước: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BsdmIJRmcZklka5PEUlx9A2dqG>`_

.. image:: images/bai_8.9.png
    :width: 200px
    :align: center 
























