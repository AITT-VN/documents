6. Bài 4: Hệ thống cảnh báo tiếng ồn
=====================================

Mục tiêu 
----------
--------------

Tại các khu vực cần sự yên tĩnh như trường học, bệnh viện, chúng ta sẽ thiết lập một hệ thống đo lường và cảnh báo khi tiếng ồn vượt hạn mức cho phép. Hệ thống sẽ lưu lại số lần vượt mức và hiển thị chúng lên màn hình LCD. 


Kết nối
----------
--------------

- Cảm biến âm thanh (P0)

    .. image:: images/bai_4.1.png
        :width: 200px
        :align: center 
    |   
- Màn hình LCD OLED (I2C1)

    .. image:: images/bai_4.2.png
        :width: 200px
        :align: center 
    | 
- **Kết nối**

    .. image:: images/bai_4.3.png
        :width: 400px
        :align: center 
    |

Lắp ráp mô hình 
-------------
---------------

    .. image:: images/bai_4.4.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_4.5.png
        :width: 1000px
        :align: center 
    |

Giới thiệu khối lệnh 
-------------------
-----------------------

    .. image:: images/bai_4.6.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_4.7.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_4.8.png
        :width: 1000px
        :align: center 
    |  


Giới thiệu về hàm 
-------------
----------------

- Với những chương trình dài có nhiều khối lệnh, chúng ta sẽ sử dụng **Hàm** để rút gọn những chương trình đó.

    .. image:: images/bai_4.9.png
        :width: 250px
        :align: center 
    |
- **Hàm** giống như việc bạn tạo thêm một loại khối lệnh mới để sử dụng, và khối lệnh này bao gồm các khối lệnh con bên trong

    .. image:: images/bai_4.10.png
        :width: 250px
        :align: center 
    |
**Cách tạo và sử dụng hàm**

1. Chọn mục **Nâng cao** >> **Hàm**: sử dụng khối lệnh hàm để làm gì để tạo hàm.

    .. image:: images/bai_4.11.png
        :width: 400px
        :align: center 
    |
2. Đưa các khối lệnh vào trong hàm, sau đó đặt tên cho hàm.

    .. image:: images/bai_4.12.png
        :width: 400px
        :align: center 
    |
3. Khối lệnh mới với tên vừa đặt sẽ xuất hiện trong mục **Hàm**.

    .. image:: images/bai_4.13.png
        :width: 400px
        :align: center 
    |

Viết chương trình 
-------------
--------------

1. Tạo một hàm để khởi động lại màn hình.

    • In ra nội dung “Vi pham: 0”, “Do on toi da: 0” tại dòng 15 và dòng 30

    .. image:: images/bai_4.14.png
        :width: 600px
        :align: center 
    |
2. Tạo 2 biến để chứa thông tin về số lần tiếng ồn vượt mức và giá trị tiếng ồn cao nhất, gán dữ liệu số cho 2 biến:

    .. image:: images/bai_4.15.png
        :width: 400px
        :align: center 
    |
3. Khởi tạo màn hình LCD và đổi màu tất cả đèn LED thành màu xanh lá, sau đó khởi động lại màn hình LCD

    .. image:: images/bai_4.16.png
        :width: 400px
        :align: center 
    |
4. Tạo biến độ ồn và gán giá trị nhận từ cảm biến âm thanh

    .. image:: images/bai_4.17.png
        :width: 800px
        :align: center 
    |
5. Nếu tiếng ồn lớn hơn mức 15, ta sẽ hiển thị giá trị tiếng ồn lên màn hình LED của Yolo:Bit dưới dạng biểu đồ phần trăm 

    .. image:: images/bai_4.18.png
        :width: 800px
        :align: center 
    |
6. Chương trình liên tục kiểm tra và lưu giá trị tiếng ồn cao nhất vào biến

    .. image:: images/bai_4.19.png
        :width: 800px
        :align: center 
    |
7. Nếu giá trị tiếng ồn lớn hơn 25:

    - Đổi tất cả LED thành màu đỏ

    - Cộng thêm 1 vào biến số lần vượt mức

    - Xóa màn hình LCD trước đó và hiển thị số lần vượt mức (dòng 15), giá trị tiếng ồn cao nhất (dòng 30) ra màn hình

    .. image:: images/bai_4.20.png
        :width: 800px
        :align: center 
    |
8.  Tạm dừng 50ms

    .. image:: images/bai_4.21.png
        :width: 800px
        :align: center 
    |
9. Nhấn nút A để đặt lại số liệu, bật đèn LED màu xanh để báo hiệu

    .. image:: images/bai_4.22.png
        :width: 400px
        :align: center 
    |

Chương trình mẫu 
---------------
-----------------

- Hệ thống cảnh báo tiếng ồn: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BsC7c89yhsN09u77mhXArcqx7Q>`_

.. image:: images/bai_4.24.png
    :width: 200px
    :align: center 

