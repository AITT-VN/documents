4. Bài 2: Bãi đậu xe thông minh
===================================

Mục tiêu
----------
--------------

Trong bài này, chúng ta sẽ cùng lập trình một bãi đậu xe thông minh có thể tự động mở thanh chắn để xe vào (nếu chỗ đậu xe còn trống). Nếu bãi xe đầy, đèn LED trên Yolo:Bit sẽ đổi thành màu đỏ để báo hiệu.

Kết nối 
----------
------------

- Cảm biến ánh sáng (P0)

    .. image:: images/bai_2.1.png
        :width: 200px
        :align: center 
    |
- Cảm biến khoảng cách (P10-P13)

    .. image:: images/bai_2.2.png
        :width: 200px
        :align: center 
    |
- Động cơ Servo (P4)

    .. image:: images/bai_2.3.png
        :width: 200px
        :align: center 
    |
**Kết nối**

    .. image:: images/bai_2.4.png
        :width: 600px
        :align: center 


Lắp ráp mô hình
----------
-------------

- Trước khi lắp ráp, bạn cần căn chỉnh Servo về góc 20 để hoạt động chính xác. Thực hiện như sau:

    1. Kết nối Servo vào chân P4 trên mạch mở rộng đã gắn Yolo:Bit

    2. Kết nối Yolo:Bit với Ohstem App và tiến hành lập trình.

    3. Tạo chương trình như hình minh họa

    .. image:: images/bai_2.5.png
        :width: 600px
        :align: center 
    |
    4.  Nhấn nút chạy chương trình 

    5. Ngắt kết nối Servo với nguồn điện (tránh vừa cắm điện vừa gắn làm quay Servo gây hư hại thiết bị)

- Tiến hành lắp ráp:

    .. image:: images/bai_2.6.png
        :width: 800px
        :align: center 
    |
    .. image:: images/bai_2.7.png
        :width: 800px
        :align: center 
    |    
    .. image:: images/bai_2.8.png
        :width: 800px
        :align: center 
    |
    Đặt cảm biến ánh sáng lên vị trí bãi đỗ nằm trên bản đồ như hình minh họa

    .. image:: images/bai_2.9.png
        :width: 400px
        :align: center 
    |

Giới thiệu khối lệnh 
-------------
----------------------

    .. image:: images/bai_2.10.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_2.11.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_2.12.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_2.13.png
        :width: 1000px
        :align: center 
    |

Giới thiệu về biến 
--------
-------------

- Để thay đổi độ sáng của đèn LED tương ứng với điều khiển từ remote, chúng ta cần sử dụng đến biến. Có thể hiểu, biến như một chiếc hộp, nơi chứa giá trị mà ta cần sử dụng.

- Mỗi hộp chỉ có thể chứa duy nhất một giá trị (chữ, số, chuỗi, dữ liệu) tại một thời điểm. Trong trường hợp này, biến sẽ chứa giá  trị số, đại diện cho mức độ sáng của đèn.

    .. image:: images/bai_2.14.png
        :width: 400px
        :align: center 
    |

**Cách tạo và sử dụng biến**

    1. Bạn cần vào mục Biến và chọn Tạo biến. Sau đó, điền tên cho biến mới để tạo.

    .. image:: images/bai_2.15.png
        :width: 400px
        :align: center 
    |
    2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.

    .. image:: images/bai_2.16.png
        :width: 400px
        :align: center 
    |

Viết chương trình 
----------
--------------------

1. Tạo một biến mới tên **“Bãi xe hết chỗ”** và gán giá trị sai vào biến (đồng nghĩa với bãi xe vẫn còn chỗ trống):

    .. image:: images/bai_2.26.png
        :width: 500px
        :align: center 
    |
2. Khởi tạo cảm biến khoảng cách P10/P13 và quay Servo đến góc 20 (để đóng thanh chắn):

    .. image:: images/bai_2.17.png
        :width: 800px
        :align: center 
    |
3. Tạo điều kiện: nếu bãi xe còn trống (cảm biến ánh sáng không phát hiện xe, độ sáng > 40), gán giá trị sai cho biến bãi xe hết chỗ, đồng thời bật đèn LED màu xanh để báo hiệu

    .. image:: images/bai_2.18.png
        :width: 800px
        :align: center 
    |
4. Nếu không, gán giá trị đúng cho biến và đổi màu đèn LED thành màu đỏ

    .. image:: images/bai_2.19.png
        :width: 800px
        :align: center 
    |
5. Tạo thêm 1 điều kiện lồng ghép: nếu phát hiện có xe (khoảng cách đến xe < 5cm)

    .. image:: images/bai_2.20.png
        :width: 800px
        :align: center 
    |
6. Trong trường hợp bãi xe còn chỗ trống (biến bãi xe hết chỗ có giá trị sai): quay Servo đến góc 20 độ để mở thanh chắn, tạm dừng 500 mili giây:

    .. image:: images/bai_2.21.png
        :width: 800px
        :align: center 
    |
7. Phát bài nhạc POWER_UP để báo hiệu, chờ 3 giây để xe di chuyển vào và bắt đầu đóng thanh chắn (quay Servo đến góc 110 độ):

    .. image:: images/bai_2.22.png
        :width: 800px
        :align: center 
    |
8. Trong trường hợp bãi xe đã đầy chỗ (biến có giá trị đúng): Phát bài nhạc POWER_DOWN để báo hiệu và tạm dừng chương trình trong 5 giây để xe rời khỏi bãi đậu, tránh trường hợp phát nhạc liên tục 

    .. image:: images/bai_2.23.png
        :width: 800px
        :align: center 
    |
9. Thêm tạm dừng 0.1 giây (100ms) vào cuối chương trình. Chương trình trong phần lặp lại mãi như sau:

    .. image:: images/bai_2.24.png
        :width: 800px
        :align: center 
    |

Chương trình mẫu 
------------
---------------

- Bãi đậu xe thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2FkI29lwsiyT25UIkISuO551cJE>`_

.. image:: images/bai_2.27.png
    :width: 200px
    :align: center 