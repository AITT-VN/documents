3. Bài 2: Bãi đậu xe thông minh
===================================

1. Mục tiêu
----------
--------------

Trong bài này, chúng ta sẽ cùng lập trình một bãi đậu xe thông minh có thể tự động mở thanh chắn để xe vào (nếu chỗ đậu xe còn trống). Nếu bãi xe đầy, đèn LED trên Yolo UNO sẽ đổi thành màu đỏ để báo hiệu và hiển thị số lượng chỗ rống trên màn hình OLED.

2. Kết nối 
----------
------------

- Cảm biến vật cản (D9-D10)

.. image:: images/cityuno1_1.PNG
    :width: 150px
    :align: center 
|

- Cảm biến khoảng cách (D5-D6)

.. image:: images/cityuno1_2.PNG
    :width: 150px
    :align: center 
|

- Động cơ Servo (D11)

.. image:: images/cityuno1_3.PNG
    :scale: 80%
    :align: center 
|


- **Kết nối:**

.. image:: images/bai_2.4.png
    :scale: 80%
    :align: center 
|

3. Lắp ráp mô hình
----------
-------------

- Trước khi lắp ráp, bạn cần căn chỉnh Servo về góc 90 để hoạt động chính xác. Thực hiện như sau:

    1. Kết nối Servo vào chân D11 trên mạch Yolo UNO

    2. Kết nối Yolo UNO với Ohstem App và tiến hành lập trình.

    3. Tạo chương trình như hình minh họa

.. image:: images/cityuno1_4.PNG
    :scale: 100%
    :align: center 
|

    4.  Nhấn nút chạy chương trình 

    5. Ngắt kết nối Servo với nguồn điện (tránh vừa cắm điện vừa gắn làm quay Servo gây hư hại thiết bị)


- **Tiến hành lắp ráp**:

.. image:: images/bai_2.6.png
    :scale: 100%
    :align: center 
|
    

4. Giới thiệu khối lệnh 
-------------
----------------------

- Vào mục **Mở rộng**, tải thư viện **Màn hình OLED**: 

.. image:: images/cityuno4_11.PNG
    :scale: 80%
    :align: center 
|

- Khối lệnh kiểm tra khoảng cách:

.. image:: images/cityuno1_5.PNG
    :scale: 80%
    :align: center 
|

- Khối lệnh điều khiển chân servo 180 độ: 

.. image:: images/cityuno1_6.PNG
    :scale: 80%
    :align: center 
|


- Khối lệnh xác định trạng thái cảm biến vật cản

.. image:: images/cityuno3_3.PNG
    :scale: 90%
    :align: center 
| 

- Khối lệnh tạm dừng (chờ): 

.. image:: images/cityuno1_7.PNG
    :scale: 80%
    :align: center 
|


5.  Giới thiệu về biến 
--------
-------------

- Để kiểm tra số chỗ đỗ xe còn lại, chúng ta cần sử dụng đến biến. Có thể hiểu, biến như một chiếc hộp, nơi chứa giá trị mà ta cần sử dụng.

- Mỗi hộp chỉ có thể chứa duy nhất một giá trị (chữ, số, chuỗi, dữ liệu) tại một thời điểm. Trong trường hợp này, biến sẽ chứa giá  trị số, đại diện cho số chỗ đậu xe còn lại.

.. image:: images/bai_2.14.png
    :width: 400px
    :align: center 
|


**Cách tạo và sử dụng biến:**


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


6. Viết chương trình 
----------
--------------------

1. Tạo một biến mới tên **“Số chỗ đậu xe”** và gán giá trị 2 vào biến (đồng nghĩa với bãi xe vẫn còn 2 chỗ trống):

    .. image:: images/cityuno1_8.PNG
        :scale: 90%
        :align: center 
    |

2. Tạo điều kiện: nếu bãi xe còn trống (cảm biến vật cản không bị che đi), biến số chỗ đậu xe > 0

    .. figure:: images/cityuno1_9.PNG
        :scale: 80%
        :align: center 
    
        Khi bãi xe còn chỗ trống thì servo sẽ mở cánh barrier trong 3s để xe vào 
    |

3. Tạo thêm 1 điều kiện lồng ghép: nếu phát hiện có xe (khoảng cách đến xe < 5cm)

    .. image:: images/cityuno1_10.PNG
        :scale: 80%
        :align: center 
    |
    
    Trong trường hợp bãi xe còn chỗ trống (biến số chỗ đậu xe > 0): quay Servo đến góc 20 độ để mở thanh chắn, tạm dừng 500 mili giây:

4. Trong trường hợp bãi xe đã đầy chỗ (biến = 0): servo sẽ không mở barrier cho xe khác vào.

    .. image:: images/cityuno1_11.PNG
        :scale: 80%
        :align: center 
    |


5. Sử dụng khối lệnh sau mỗi 1 giây kiểm tra cảm biến vật cản. Nếu trạng thái chân D9 là bật, tức là không có vật cản. Nếu trạng thái chân là TẮT, tức là có vật cản phía trên cảm biến biến số chỗ đậu xe sẽ thay đổi như sau:
    
    .. image:: images/cityuno1_12.PNG
        :scale: 100%
        :align: center
    |

8. Chương trình mẫu 
------------
---------------

- Bãi đậu xe thông minh: 


.. image:: images/cityuno1_13.PNG
    :scale: 80%
    :align: center 
|

- Link chương trình: `<https://app.ohstem.vn/#!/share/yolouno/2eImTbJnX7OTcXuia2a6kNi2i7O>`_