11. Bài 8: Vết tích để lại 
=====================================

*Thủ phạm đã bị bắt, nhưng mọi chuyện chưa dừng ở đó. Rover cần khám nghiệm hiện trường để tìm lại những thứ đã mất. Phát hiện dấu vết là biệt tài của Rover.*


Mục tiêu
----------------
--------------------------------

- Làm quen cảm biến dò đường


Bộ phận điện tử
------------------
------------------------------------

- Cảm biến dò đường trên Rover gồm 4 mắt đọc nằm ở mặt dưới xe được đánh số từ S1 đến S4.


- Cảm biến này giúp Rover phát hiện vạch đen bên dưới để di chuyển, hoặc tránh né tùy theo mục đích lập trình

    .. image:: images/bai_8.1.png
        :width: 1000px
        :align: center   
|
- Cảm biến dò đường trên Rover hoạt động như thế nào?

    .. image:: images/bai_8.png
        :width: 300
        :align: center   

    - Mắt đọc dò đường sẽ phát ra và thu về hồng ngoại. Tùy theo mức độ hồng ngoại nhận lại mà xác định được bên dưới là vạch đen hay nền trắng.

        .. image:: images/bai_8.2.png
            :width: 300
            :align: center   

    - Phía trên Rover có các đèn báo hiệu tương ứng với từng mắt đọc:
    
        - Đọc được nền trắng: Đèn sáng
        - Đọc được nền đen: Đèn tắt

        .. image:: images/bai_8.3.png
            :width: 300
            :align: center   


Giới thiệu khối lệnh 
-----------------------
-----------------------

- Khối lệnh đọc line:

    .. image:: images/bai_8.4.png
        :width: 1000px
        :align: center   
|

Viết chương trình 
---------------------
--------------------------

1. Viết chương trình

    .. image:: images/bai_8.5.png
        :width: 800px
        :align: center   
|
2. Tạo điều kiện đầu tiên: **Nếu mắt S1 đọc được vạch đen, bật đèn số 1, 2, 3. Nếu không, tắt đèn**

    .. image:: images/bai_8.6.png
        :width: 800px
        :align: center   
|
3. Tạo điều kiện thứ 2: **Nếu mắt S4 đọc được vạch đen, bật đèn số 4, 5, 6. Nếu không, tắt đèn**

    .. image:: images/bai_8.7.png
        :width: 800px
        :align: center


Chương trình mẫu
--------------
-------------------

- Vết tích để lại: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeWXV0PSKrWqs4gdNub3l7LaW6>`_

.. image:: images/bai_8.8.png
    :width: 200px
    :align: center 


