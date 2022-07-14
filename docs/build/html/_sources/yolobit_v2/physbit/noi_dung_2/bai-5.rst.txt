5. Bài 5: Biến trở  (Potentiometer)
=================================

Giới thiệu
-----------
-----------

- **Biến trở**, là một điện trở có thể thay đổi giá trị có đơn vị là Ohm (Ω). Biến trở được ứng dụng trong việc điều chỉnh cường độ dòng điện hoặc điện áp trong mạch.

- Chúng ta có thể thấy biến trở ở rất nhiều thiết bị điện quanh ta như các nút vặn điều chỉnh của quạt, loa hay lò vi sóng, v.v.

- Trên bộ kit **Phys:Bit** có sẵn một **Biến trở xoay** (Potentiometer) có giá trị 10kΩ. 

    .. image:: images/5.1.png
        :width: 300px
        :align: center 
    |
- Một biến trở thường có 3 chân. Trong đó, 2 chân cố định ở đầu của điện trở. 

- Chân còn lại có thể được di chuyển, thường được gọi là núm xoay hay cần gạt. Vị trí của chân này sẽ quyết định giá trị của biến trở. 

- Bằng cách di chuyển chân này chúng ta có thể điều chỉnh giá trị điện trở để kiểm soát dòng điện và điện áp và thay đổi cách mạch điện hoạt động.

Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Nguồn điện 3V.
    - Biển trở xoay R1. 

- **Sơ đồ mạch điện**

    .. image:: images/bai_5.1.png
        :width: 600px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    Trong mạch điện trên, 2 chân của biến trở sẽ nối với 2 đầu nguồn điện và chân còn lại nối với chân P0 của **Yolo:Bit**. Khi biến trở được xoay qua trái hoặc phải thì biến trở sẽ thay đổi từ đó điện áp của dòng điện sẽ thay đổi theo. Nếu ta đọc giá trị analog đo được của chân P0 sẽ thấy sự thay đổi đó.


Kết nối mạch điện 
-----------
-------------

**Núm xoay** đấy dùng để điều chỉnh giá trị của biến trở

    .. image:: images/bai_5.2.png
        :width: 600px
        :align: center 
    |

Chương trình
---------
-----------------

- Chúng ta sẽ thực hiện chương trình đọc giá trị analog của chân P0 và vẽ biểu đồ lên màn hình LED. Chân P0 đọc được giá trị càng cao thì càng nhiều LED sáng, và ngược lại. 

    .. image:: images/bai_5.3.png
        :width: 1000px
        :align: center 
    |
- Hãy điều chỉnh biến trở và quan sát kết quả nhé.

Kết quả
----------
---------------

Kết quả của chương trình như sau: 

    .. image:: images/bai_5.4.png
        :width: 600px
        :align: center 
    |


Có thể bạn chưa biết?
-----------
-------------------

Có nhiều loại biến trở khác nhau và ứng với mỗi cách kết nối sơ đồ mạch điện, ý nghĩa của biến trở trong mạch điện sẽ khác nhau nên tùy vào mục đích sử dụng, người thiết kế mạch điện sẽ lựa chọn loại biến trở thích hợp để sử dụng. Biến trở có trên bộ Phys:Bit là biến trở xoay, thường được sử dụng cho mục đích chiết áp (điều chỉnh điện áp). Dưới đây là một số biến trở thông dụng:

- Biến trở con chạy: 

    .. image:: images/5.4.png
        :width: 300px
        :align: center 
    |
- Biến trở dây quấn:

    .. image:: images/5.5.png
        :width: 300px
        :align: center 
    |

Chương trình mẫu
--------------
-------------------

- Biến trở: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BvgwGfcj12malovc4ctXHdTFCP>`_

.. image:: images/bai_5.5.png
    :width: 200px
    :align: center 

