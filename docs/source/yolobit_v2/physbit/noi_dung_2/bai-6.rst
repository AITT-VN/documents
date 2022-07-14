6. Bài 6: Cảm biến ánh sáng
===================================

Giới thiệu
-----------
---------------

- **Cảm biến ánh sáng** hay còn gọi là **quang trở**. Đây cũng là một loại biến trở, nhưng khác với biến trở Potentiometer. Giá trị điện trở của cảm biến ánh sáng thay đổi theo mức độ ánh sáng nhận được.

- Càng có nhiều ánh sáng chiếu vào thì điện trở của quang trở càng thấp và quang trở sẽ dẫn điện tốt hơn. Khi ánh sáng ít hoặc trời tối thì điện trở của quang trở tăng cao và hạn chế dòng điện đi qua

    .. image:: images/6.1.png
        :width: 300px
        :align: center 
    |

Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Nguồn điện 3V.
    - Điện trở R1 10 KΩ. 
    -Quang trở P1.

- **Sơ đồ mạch điện**

    .. image:: images/bai_6.1.png
        :width: 600px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    - Theo sơ đồ trên, khi cảm biến P1 nhận được nhiều ánh sáng thì điện trở sẽ ở mức thấp và dòng điện sẽ chạy từ 3V qua chân P0 nhiều hơn, từ đó kết quả analog đọc được sẽ ở mức cao.
    - Ngược lại, khi P1 nhận được ít ánh sáng, điện trở của P1 sẽ tăng lên cao và chân P0 sẽ không có hoặc có ít dòng điện chạy qua, kết quả đọc được sẽ nhỏ hoặc bằng 0.


Kết nối mạch điện 
-----------
-------------

Dựa vào độ sáng từ môi trường mà cảm biến ánh sáng đọc được, chúng ta cùng điều chỉnh độ sáng của màn hình LED. Trời càng tối, màn hình càng sáng và ngược lại.

    .. image:: images/bai_6.2.png
        :width: 600px
        :align: center 
    |

Chương trình
---------
-----------------

- Giá trị analog đọc từ cảm biến ánh sáng là một số nằm trong khoảng từ 0 đến 4095. Tuy nhiên giá trị dùng để điều chỉnh độ sáng của đèn là một số trong khoảng 0 đến 100. Vì vậy ta cần dùng block đổi số để quy đổi độ sáng thành một số cũng nằm trong khoảng từ 0 đến 100.

- **Cách tạo biến: **

    1. Bạn cần vào mục Biến và chọn Tạo biến. Sau đó, điền tên cho biến mới để tạo

    .. image:: images/bai_7.3.png
        :width: 400px
        :align: center 
    

    2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.

    .. image:: images/bai_7.4.png
        :width: 400px
        :align: center 

- Chương trình được thực hiện như sau:

    .. image:: images/bai_6.3.png
        :width: 1000px
        :align: center 
    |

Kết quả
----------
---------------

Kết quả của chương trình như sau: 

    .. image:: images/bai_6.4.png
        :width: 500px
        :align: center 
    |

Có thể bạn chưa biết?
-----------
-------------------

- Nhờ nguyên lý hoạt động đơn giản và dễ sử dụng, cảm biến ánh sáng ngày càng được ứng dụng rộng rãi trong đời sống.

- Một số ứng dụng phổ biến thường thấy chính là các hệ thống đèn thông minh tự động bật khi trời tối và tự động tắt khi trời sáng để tránh lãng phí năng lượng điện. Các ứng dụng này cũng giúp cho đời sống của con người trở nên tiện nghi và thú vị hơn.


Chương trình mẫu
--------------
-------------------

- Cảm biến ánh sáng: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Bvj7i0nZRgJpXcZY4cYA5kZ4en>`_

.. image:: images/bai_6.5.png
    :width: 200px
    :align: center 

