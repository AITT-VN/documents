12. Bài 9: Lần theo dấu vết
=======================================

*Vết tích mà Rover tìm được dường như đang dẫn đến nơi nào đó. Rover quyết định đi theo để tìm lại những vật bị mất*

Mục tiêu
--------------
--------------------

- Ứng dụng cảm biến dò đường để Rover tự động đi theo line


Viết chương trình
--------------
--------------------

1.  Rover sẽ chạy theo vạch đen trên bản đồ nhờ 4 mắt đọc, cơ chế hoạt động sẽ như sau:

    - **Đi thẳng**: S1 và S4 không đọc được vạch đen
        .. image:: images/bai_9.1.png
            :width: 300px
            :align: center 


    - **Rẽ trái:**  S1 đọc được vạch đen, S4 thì không 
  
        .. image:: images/bai_9.2.png
            :width: 300px
            :align: center 


    - **Rẽ phải:** S4 đọc được vạch đen, S1 thì không 

        .. image:: images/bai_9.3.png
            :width: 300px
            :align: center 
|
2. Viết thuật toán

    .. image:: images/bai_9.4.png
        :width: 800px
        :align: center   
|
3. Viết chương trình: Tạo điều kiện thứ nhất, nếu mắt S1 đọc được vạch đen thì rẽ trái

    .. image:: images/bai_9.5.png
        :width: 900px
        :align: center   
|
4. Tạo điều kiện tiếp theo, nếu mắt S4 đọc được vạch đen thì rẽ phải. Nếu cả 2 điều kiện không đúng, đi thẳng

    .. image:: images/bai_9.6.png
        :width: 900px
        :align: center 


Chương trình mẫu
--------------
-------------------

- Lần theo dấu vết: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeWoF7zQjV3kSvA350Ch1sPc1f>`_

.. image:: images/bai_9.7.png
    :width: 200px
    :align: center 