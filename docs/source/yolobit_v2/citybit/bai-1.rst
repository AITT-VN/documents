<<<<<<< HEAD
4. Bài 1: Đèn công cộng thông minh
=================================
=======
3. Bài 1: Đèn công cộng thông minh
=================================

Mục tiêu:
------------
-----------------

Trong bài này, chúng ta sẽ cùng lập trình một chiếc đèn thông minh có thể tự sáng khi có người vào buổi tối. Các đèn này có thể gắn vào các khu vui chơi hoặc công viên tùy thích.


Kết nối 
----------
--------------

- Cảm biến ánh sáng (P0)

    .. image:: images/bai_1.1.1.png
        :width: 200px
        :align: center 
    |
- Cảm biến chuyển động PIR (P1)

    .. image:: images/bai_1.1.2.png
        :width: 200px
        :align: center 
    |
- Module LED (P2)

    .. image:: images/bai_1.1.3.png
        :width: 200px
        :align: center 
    |
**Kết nối**

    .. image:: images/bai_1.2.png
        :width: 800px
        :align: center 
    
Lắp ráp 
-----------
----------------

**Lắp ráp khung cho mạch mở rộng**

Đầu tiên, bạn cần lắp ráp một khung phù hợp với mạch mở rộng Yolo:Bit để sử dụng cho từng mô hình.

Thực hiện như sau:

    .. image:: images/bai_1.3.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_1.3.1.png
        :width: 1000px
        :align: center 
    |
**Lắp ráp mô hình**

    .. image:: images/bai_1.4.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_1.4.1.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_1.4.2.png
        :width: 1000px
        :align: center 
    | 
    .. image:: images/bai_1.4.3.png
        :width: 1000px
        :align: center 
    |

Giới thiệu khối lệnh
----------
----------------

    .. image:: images/bai_1.6.png
        :width: 1000px
        :align: center 
    |

Viết chương trình
------------
--------------------

1. Kéo khối lệnh điều kiện vào phần **lặp lại mãi**

    .. image:: images/bai_1.7.png
        :width: 300px
        :align: center 
    |
2. Cho khối lệnh toán tử **VÀ** vào phần nếu

    .. image:: images/bai_1.8.png
        :width: 400px
        :align: center 
    |
3. Tạo điều kiện: nếu trời tối (độ sáng < 30) và phát hiện có người

    .. image:: images/bai_1.9.png
        :width: 1000px
        :align: center 
    |
4. Bật đèn ở chân P2 trong 5 giây, sau đó tắt đèn

    .. image:: images/bai_1.10.png
        :width: 1000px
        :align: center 
    |

**Vấn đề xảy ra:** Thỉnh thoảng đèn vẫn không bật dù đang có người.

**Nguyên nhân:** Cảm biến hồng ngoại PIR không hoạt động liên tục nên chúng sẽ không phát hiện người kịp thời. Khi có người, cảm biến sẽ bật và hoạt động trong vòng 2 giây rồi tắt. Đến khi tiếp tục phát hiện có người thì cảm biến PIR mới bật lại nên sẽ có độ trễ nhất định.

**Giải pháp:** Sử dụng bộ đếm thời gian để đèn tự tắt nếu trong vòng 10 giây liên tục không có người xuất hiện


**Giới thiệu khối lệnh**

    .. image:: images/bai_1.11.png
        :width: 800px
        :align: center 
    |

**Sửa chương trình**

1. Nếu trời tối và cảm biến phát hiện có người thì bật đèn LED

    .. image:: images/bai_1.12.png
        :width: 800px
        :align: center 
    |
2. Sau khi bật đèn, reset bộ đếm để đếm lại từ đầu

    .. image:: images/bai_1.13.png
        :width: 800px
        :align: center 
    |
3. Nếu đếm được 10 giây (trong vòng 10 giây liên tiếp không có người xuất hiện) thì tắt đèn LED

    .. image:: images/bai_1.14.png
        :width: 1000px
        :align: center 
    |

Chương trình mẫu
------------
----------------

- Đèn công cộng thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Bq3zhPeIeRzldwwWE52H9gdAfT>`_

.. image:: images/bai_1.15.png
    :width: 200px
    :align: center 
>>>>>>> main
