6. Lập trình di chuyển theo tọa độ ORZ
=================================

Mục tiêu
---------------------
---------------------

- Giới thiệu về tọa độ ORZ
- hướng dẫn sử dụng câu lệnh để di chuyển đầu gắp đến vị trí theo ORZ.


Hệ tọa trụ ORZ
---------------
-------------------------

Hệ tọa độ hình trụ là hệ tọa độ ba chiều, chỉ định vị trí điểm theo khoảng cách từ trục tham chiếu đã chọn, hướng từ trục so với hướng tham chiếu đã chọn và khoảng cách từ mặt phẳng tham chiếu đã chọn vuông góc với trục. Khoảng cách sau được cho là số dương hoặc âm tùy thuộc vào phía nào của mặt phẳng tham chiếu đối diện với điểm.

Nguồn gốc của hệ thống là điểm mà cả ba tọa độ có thể được cho là 0. Đây là giao điểm giữa mặt phẳng tham chiếu và trục.

Trục này được gọi khác nhau là trục hình trụ hoặc trục dọc , để phân biệt nó với trục cực , là tia nằm trong mặt phẳng tham chiếu, bắt đầu từ điểm gốc và chỉ theo hướng tham chiếu.

Khoảng cách từ trục có thể được gọi là khoảng cách xuyên tâm hoặc bán kính , trong khi tọa độ góc đôi khi được gọi là vị trí góc hoặc là góc phương vị . Bán kính và góc phương vị được gọi là tọa độ cực , vì chúng tương ứng với hai hệ tọa độ cực chiều trong mặt phẳng qua điểm, song song với mặt phẳng tham chiếu. Tọa độ thứ ba có thể được gọi là chiều cao hoặc độ cao (nếu mặt phẳng tham chiếu được coi là nằm ngang), vị trí dọc hoặc vị trí trục .

- O là tọa đội góc (vị trí góc hoặc góc phương vị).
- R là bán kính (khoảng cách xuyên tâm).
- Z là độ cao (vị trí theo chiều dọc).

.. image:: images/bai-1-1.png
    :width: 400px
    :align: center
|

Giới thiệu khối lệnh
---------------------------
----------------------

- Khối lệnh bắt đầu chương trình:

.. image:: images/bai_1.6.png
    :width: 400px
    :align: center
| 
- Khối lệnh lặp lại số lần:

.. image:: images/bai_1.7.png
    :width: 400px
    :align: center
|   
- Khối lệnh di chuyển:

 .. image:: images/bai_1.8.png
    :width: 1200px
    :align: center
|    


Viết chương trình
---------------------
--------------------------

**Chương trình đơn giản:** Đây là chương trình điều khiển Rover đi tới và lùi, giúp bạn làm quen với lập trình điều khiển Rover di chuyển

    1.  Gắn khối lệnh di chuyển vào lệnh lặp lại mãi

    .. image:: images/bai_1.9.png
        :width: 800px
        :align: center  
    |
    2. Chọn hướng di chuyển và chỉnh tốc độ mong muốn

        - Có 4 hướng di chuyển: tiến tới, lùi lại, rẽ trái, rẽ phải tương ứng với hình dạng mũi tên.

        - Tốc độ của động cơ có giá trị từ 0 (đứng yên) đến 100 (tối đa).

    .. image:: images/bai_1.10.png
        :width: 400px
        :align: center
    |
    3. Thêm khối tạm dừng 1 giây (1000ms)

    .. image:: images/bai_1.11.png
        :width: 700px
        :align: center
    |
    4. Làm tương tự để tạo thêm lệnh đi lùi trong 1 giây

    .. image:: images/bai_1.12.png
        :width: 400px
        :align: center
    |
    5. Chạy chương trình

    .. image:: images/bai_1.13.png
        :width: 700px
        :align: center 
    |
    6.  Bạn có thể nhấn nút tạm dừng để dừng chương trình lại

    .. image:: images/bai_1.14.png
        :width: 70px
        :align: center 
    


**Chương trình di chuyển với thời gian:**  Chương trình này sẽ giúp Rover đi theo hình vuông

    1.  Gắn khối lệnh lặp số lần vào lệnh bắt đầu

    .. image:: images/bai_1.15.png
        :width: 700px
        :align: center 
    |  
    2. Sử dụng các khối lệnh di chuyển để hoàn thiện chương trình như hình minh họa (để ý các thông số)

    .. image:: images/bai_1.16.png
        :width: 600px
        :align: center 
    |


Chương trình mẫu
--------------
-------------------

- Nhấp vào chữ **tại đây** để xem chương trình mẫu, hoặc quét mã QR bên dưới để xem chương trình.

- Robot di chuyển tới lui: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeTmtVhptwmDZJMtzCrBz2Hc5n>`_

.. image:: images/bai_1.17.png
    :width: 200px
    :align: center 
| 
- Robot di chuyển hình vuông: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeTxamvWwDappzIrPkZx9j7xl3>`_

.. image:: images/bai_1.18.png
    :width: 200px
    :align: center 
