11. Thao tác với nút nhấn 
=========================

    .. image:: images/8.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Ở bài này mình sẽ hướng dẫn các bạn sử dụng nút nhấn trên GameKit để điều khiển trò chơi.

Link chương trình mẫu: `Tại đây <https://makecode.com/_2zaheeg8VC2T>`_

**Bước 1**

Tìm khối ``set score to 0`` trong ``Info``, kéo thả vào khối ``on start``.

Lúc này  điểm ban đầu của trò chơi là 0; quan sát màn hình mô phỏng bạn sẽ thấy điểm số xuất hiện ở góc trên bên phải màn hình.

    .. image:: images/8.2.png
        :width: 400px
        :align: center 
    |
**Bước 2**

Tìm ``set life to 3`` trong ``Info``, kéo thả vào khối ``on start``. Thay đổi giá trị 3 thành 5.

Điều này giúp đặt số lượt chơi mà người chơi sẽ có khi bắt đầu. Lượt chơi xuất hiện ở góc trên cùng bên trái của màn hình và nếu người chơi hết lượt, trò chơi sẽ kết thúc.

    .. image:: images/8.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tìm start ``countdown 10 (s)`` trong ``Info,`` kéo thả vào khối ``on start``.

Với mỗi lượt chơi bạn sẽ có 10s. Khi hết thời gian bạn sẽ mất một lượt chơi.

    .. image:: images/8.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Tìm ``on A button pressed`` trong ``Controller`` và kéo thả vào màn hình làm việc. Tìm khối ``change score by 1`` trong ``Info``, kéo thả vào khối ``on A button pressed``.

Điều này sẽ làm cho nó bất cứ khi nào nhấn nút ``A``, điểm của người chơi sẽ tăng thêm một. Hãy thử nhấn nút nhiều lần và xem bạn có thể đạt được điểm cao như thế nào.

    .. image:: images/8.5.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Lấy thêm một khối ``on any button pressed``, đưa vào cùng kéo thả và thay đổi ``any`` thành ``B``.

Tìm khối ``change life by -1`` trong ``Info``, thả vào on ``B button pressed``.

Điều này sẽ làm cho người chơi mất lượt khi họ nhấn nút ``B``.

    .. image:: images/8.6.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Tải chương trình của bạn xuống kit và sử dụng 2 nút nhấn A, B và xem thử chương trình hoạt động như thế nào nhé

































