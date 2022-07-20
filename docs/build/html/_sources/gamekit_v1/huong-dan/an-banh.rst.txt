1. Trò chơi ăn bánh 
=========================

**Giới thiệu**

    .. image:: images/bai_1.gif
        :width: 400px
        :align: center 
    |
Chase the Pizza là trò chơi điều khiển nhân vật đi ăn bánh, với mỗi bánh ăn bánh sẽ được tính một điểm. Thời gian quy định quy định cho một lượt chơi là 3s.

Link chương trình mẫu: `Tại đây <https://makecode.com/_b6tcFWRF94uo>`_

Hướng dẫn bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7GA_V4WXcP4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**

Mở công cụ ``Scene``, kéo và thả khối ``set background color`` vào khối ``on start`` . Trong khối ``set background color``, nhấp vào hình bầu dục màu xám để mở bảng màu và chọn màu nền tùy ý.

    .. image:: images/bai_1.1.jpg
        :width: 600px
        :align: center 
    |
**Bước 2**

Mở công cụ ``Sprites`` chọn khối ``set mySprite`` kéo thả vào khối ``on start`` trên màn hình làm việc. Điều này sẽ tạo một ``Player`` mới trong trò chơi của bạn.

    .. image:: images/bai_1.2.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tự tạo ``Player`` cho riêng mình bằng cách nhấp vào hình vuông màu xám trong khối set ``mySprite`` để mở chỉnh sửa Sprite. vẽ nhận vật tùy thích hoặc như hình minh họa dưới đây.

    .. image:: images/bai_1.3.gif
        :width: 400px
        :align: center 
    |
**Bước 4**

Mở hộp công cụ ``Controller`` chọn khối move ``mySprite with buttons`` kéo thả vào vị trí sau khối set ``mySprite``. Điều này sẽ cho phép bạn di chuyển nhân vật ``Player`` xung quanh màn hình bằng các phím mũi tên. Bạn có thề dùng thử trong phần mô phỏng trò chơi.

    .. image:: images/bai_1.4.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Mở công cụ ``Sprites``, chọn khối set ``mySprite2`` khác rồi kéo thả vào trong khối ``on start`` của không gian làm việc. Để tạo đối tượng pizza.

    .. image:: images/bai_1.5.png
        :width: 600px
        :align: center 
    |
Trong khố ``set mySprite2`` block, nhấp vào ``mySprite2`` để mở menu, chọn **Rename variable...** Đặt tên **pizza** cho nhân vật rồi chọn **Ok**.

    .. image:: images/bai_1.6.gif
        :width: 600px
        :align: center 
    |
Trong khối ``set pizza`` click vào ``Player`` để đổi loại hình nhân vật là ``Food``.

    .. image:: images/bai_1.7.jpg
        :width: 600px
        :align: center 
    |
Trong khối ``set pizza`` nhấp vào ô màu xám, sau đó vào **Gallery** tìm hình ảnh pizza và nhấn **Done** để lưu.

    .. image:: images/bai_1.8.gif
        :width: 400px
        :align: center 
    |
**Bước 6**

Mở công cụ ``Sprites`` chọn khối ``on sprite overlaps otherSprite`` kéo thả vào trong màn hình làm việc. Khối này sẽ giúp bạn thực hiện thay đổi trong game khi người chơi ăn được pizza.

Trong ``on sprite overlaps otherSprite`` click vào ``Player`` thứ 2 nằm phía sau ``otherSprite`` chọn sang nhân vật ``Food`` như hình.

    .. image:: images/bai_1.9.png
        :width: 600px
        :align: center 
    |
**Bước 7**

Mở công cụ ``Info`` chộn khối ``change score`` đặt vào trong ``on sprite overlaps otherSprite``. Nghĩa là khi ``Player`` ăn(chạm) vào ``pizza`` thì sẽ tăng điểm số.

    .. image:: images/bai_1.10.png
        :width: 600px
        :align: center 
    |
**Bước 8**

Sau khi bị ăn ta sẽ cho ``pizza`` xuất hiện lại ngẫu nhiên trên màn hình. Mở ``Sprites``  chọn khối ``set mySprite position`` đặt vào trong ``on sprite overlaps otherSprite``.

    .. image:: images/bai_1.11.png
        :width: 600px
        :align: center 
    |
Trong khối ``set mySprite position``, click vào ``mySprite`` chọn **Rename variable...** đổi tên lại thành ``pizza``.

    .. image:: images/bai_1.12.png
        :width: 600px
        :align: center 
    |
**Bước 9**

Mở hộp công cụ ``Math`` chọn 2 khối ``pick random`` đặt vào vị trí **x và y** của khối ``set pizza position``.

Trong khối ``pick random`` thay đổi giá trị từ **10** thành **160** của **x** và từ **10** thành **120** của **y** .

    .. image:: images/bai_1.13.png
        :width: 600px
        :align: center 
    |
**Bước 10**

Mỗi khi ăn được pizza ta sẽ cho khởi động lại bộ đếm thời gian. Mở công cụ ``Info`` chọn khối ``start countdown`` kéo vào khối ``on sprite overlaps otherSprite``.

    .. image:: images/bai_1.14.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Sau khi bạn hoàn thành sẽ có chương trình như sau. Bạn tiến hành **Download** chương trình vào Game Kit và trải nghiệm trò chơi xem như thế nào nhé.

    .. image:: images/bai_1.15.png
        :width: 600px
        :align: center 
    |




































