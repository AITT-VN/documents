4. Bài 2: Nút nhấn
===================================


Giới thiệu
----------
----------------

- **Nút nhấn** là một linh kiện rất phổ biến, dùng để điều khiển các thiết bị điện. 

- **Đóng hoặc ngắt mạch điện nối vào 2 đầu của nút nhấn** là nguyên tắc hoạt động của nút nhấn.

- **Có 2 loại nút nhấn thường gặp:**

    - **Nhấn thả** (Push button): luôn ở trạng thái ngắt. Khi được nhấn thì sẽ đóng mạch điện. Nếu thả ra thì sẽ tự trả về lại trạng thái ngắt. Các nút nhấn trên các điều khiển TV, máy lạnh là loại này.

    .. image:: images/2_1.png
        :width: 300px
        :align: center 
    |
    - **Nhấn và giữ trạng thái đóng hoặc ngắt** (Lock button): mỗi khi được nhấn thì sẽ chuyển sang trạng thái ngược lại, ví dụ từ đóng (ON) thì sẽ chuyển sang ngắt (OFF) hoặc ngược lại. Các công tắc bật đèn quạt trong nhà thuộc loại này.

    .. image:: images/2_2.png
        :width: 300px
        :align: center 
    |

Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Đèn LED đỏ. 
    - Điện trở R1 100 Ω. 
    - Nút nhấn S1.

- **Sơ đồ mạch điện**

    .. image:: images/2.1.png
        :width: 600px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    - Khi nút nhấn S1 được nhấn, mạch điện ở hình 2 đóng và chân cắm P1 được nối với Ground (GND) nên bị tắt. Lúc này ta đọc được trạng thái của P1 là TẮT, dựa vào trạng thái này, ta điều khiển chân P0 bật để điều khiển LED.
    
    - Tương tự như bài 1, khi bật P0, đèn LED sẽ sáng. 


Kết nối mạch điện 
-----------
-------------

Nhấn S1 thì LED sáng, không nhấn S1 thì LED tắt!

    .. image:: images/2.2.png
        :width: 500px
        :align: center 
    |

Chương trình
---------
-----------------

- Thực hiện chương trình như sau:

    .. image:: images/2.3.png
        :width: 1000px
        :align: center 
    |
- **Lưu ý:** Khi dùng nút nhấn, cần cấu hình điện trở nội cho chân đang nối với nút nhấn để tránh gây ra **hiện tượng đoản mạch**

- Mỗi khối lệnh đều mang màu đặc trưng của mình tương ứng với nhóm khối lệnh. Hãy dựa theo màu của khối lệnh và hoàn thiện chương trình.


Kết quả
----------
---------------

Kết quả của chương trình như sau: 

    .. image:: images/2.4.png
        :width: 600px
        :align: center 
    |

Có thể bạn chưa biết? 
-----------
-------------

**Hiện tượng đoản mạch**

- Đoản mạch còn được gọi là ngắn mạch hay chập mạch. Hiện tượng này thường xảy ra khi cực dương và cực âm của nguồn điện tiếp xúc trực tiếp với nhau mà không đi qua điện trở hoặc thiết bị tiêu thụ điện nào.

- Khi xảy ra hiện tượng đoản mạch, cường độ dòng điện trong mạch rất lớn, có thể gây cháy hoặc hư hỏng thiết bị điện. Ngoài ra hiện tượng đoản mạch còn có thể xảy ra do sấm sét hoặc sụt áp.

    .. image:: images/2_6.png
        :width: 300px
        :align: center 
    |

Chương trình mẫu
--------------
-------------------

- Nút nhấn: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Bvc5bobpHD2DUBuUhfjg2xqOOQ>`_

.. image:: images/2.5.png
    :width: 200px
    :align: center 


