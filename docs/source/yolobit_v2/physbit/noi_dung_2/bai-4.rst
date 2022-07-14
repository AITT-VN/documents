4. Bài 4: Đèn LED nhiều màu RGB
=====================================

Giới thiệu
----------
----------------

- **Đèn LED RGB**, có thể hiện ra nhiều màu từ 3 LED bên trong với 3 màu cơ bản là đỏ (Red), lục (Green) và lam (Blue). RGB là viết tắt của 3 màu cơ bản đó.

- Đèn LED RGB có 4 chân, 3 chân nối với 3 đèn LED bên trong và 1 chân chung cho cả 3 LED này. Có 2 loại đèn LED RGB: loại chân chung nối với nguồn âm (GND) và chân chung nối với nguồn dương (VCC). 

- LED RGB có trên bộ kit Phys:Bit là loại chân nối với GND.

    .. image:: images/4.1.png
        :width: 200px
        :align: center 
    |

Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Đèn LED RGB. 
    - 3 Điện trở 100 Ω. 

- **Sơ đồ mạch điện**

    .. image:: images/bai_4.1.png
        :width: 600px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    Theo sơ đồ trên, chân chung của đèn LED RGB sẽ được nối vào GND và 3 chân còn lại của 3 LED sẽ được điều khiển bật tắt bằng 3 chân cắm mở rộng của Yolo:Bit là P0, P1 và P2.

Kết nối mạch điện 
-----------
-------------

Hãy kết nối mạch điện như hình minh họa: 

    .. image:: images/bai_4.2.png
        :width: 600px
        :align: center 
    |

Chương trình
---------
-----------------

Ta sẽ lập trình cho **Yolo:Bit** hoạt động như sau:

    1. Nếu nút A được nhấn, ta cho đèn LED RGB hiện màu đỏ bằng cách bật chân P0 (nối với LED đỏ bên trong đèn LED RGB) và tắt 2 chân còn lại. 

    2. Nếu nút B được nhấn, ta cho hiện màu xanh lá bằng cách bật chân P1 (nối với LED xanh lá bên trong đèn LED RGB) và tắt 2 chân còn lại.

    3. Nếu cả 2 nút A và B được nhấn, ta cho đèn LED RGB hiện màu xanh dương bằng cách bật chân P2 (nối với LED xanh dương bên trong đèn LED RGB) và tắt 2 chân còn lại.

    .. image:: images/bai_4.3.png
        :width: 1000px
        :align: center 
    |

Kết quả
----------
---------------

Kết quả của chương trình như sau: 

    .. image:: images/bai_4.4.png
        :width: 600px
        :align: center 
    |


Bài tập mở rộng 
-----------
---------------

**Hãy thử làm**

    .. image:: images/4.4.png
        :width: 200px
        :align: right  
    
- Cho đèn LED đỏ và đèn LED lục cùng sáng

- Cho đèn LED lam và đèn LED đỏ cùng sáng

- Cho đèn LED lục và đèn LED lam cùng sáng

- Để 3 đèn LED cùng sáng


Chương trình mẫu
--------------
-------------------

- Đèn LED nhiều màu RGB: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Bvf46BGe5xCwR304j8G7L3mR8d>`_

.. image:: images/bai_4.5.png
    :width: 200px
    :align: center 
