19. Game: Nhảy thùng
===================


**Giới thiệu**

Nhảy thùng là trò chơi thuộc mô tiếp phản ứng nhanh, Người chơi cần khéo léo điều khiển nhân vật vượt qua những vật cản dưới đất, mội lần vượt qua một vật cản bạn sẽ ghi được 1 điểm

    .. image:: images/bai_7.gif
        :width: 400px
        :align: center 
    |
Link chương trình mẫu: `Tại đây <https://makecode.com/_V7q8XtHqvXKP>`_

Xem hướng dẫn online bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/KT9o-0yEuJU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**

Lấy khối ``set tilemap to`` thả vào ``on start``. Nhấp vào hộp màu xám để mở ``tilemap editor``. Ở góc dưới bên trái, đặt kích thước của tilemap thành **10x8** và vẽ một thanh ngang dài ở hai hàng dưới cùng của tilemap làm nền.

    .. image:: images/bai_7.1.gif
        :width: 500px
        :align: center 
    |
    .. image:: images/bai_7.2.png
        :width: 500px
        :align: center 
    |
**Bước 2**

Tìm khối ``set mySprite to`` trong ``Sprites``. thả vào khối ``on start`` và tạo một nhân vật người chơi.

    .. image:: images/bai_7.3.png
        :width: 500px
        :align: center 
    |
**Bước 3**

Mở trình chỉnh sửa tilemap và tìm vị trí ô vuông nơi bạn muốn đặt vị trí của mình. Bạn có thể thấy vị trí ở phía dưới bên trái của trình chỉnh sửa. Sử dụng ``place mySprite on top of tilemap col row`` để định vị vị trí.

    .. image:: images/bai_7.4.png
        :width: 500px
        :align: center 
    |
**Bước 4**

Hãy cho phép sprite có khả năng nhảy khi chúng ta nhấn nút. Ta chọn khối ``on any button pressed`` thả vào màn hình làm việc.

    .. image:: images/bai_7.5.png
        :width: 500px
        :align: center 
    |
**Bước 5**

Kéo khối ``set mySprite x`` vào ``on start``, nhấp vào menu thả xuống và chọn ``ay (acceleration y)``. Đặt giá trị thành **500** sao cho nhân vật bị kéo xuống bởi trọng lực hấp dẫn.

    .. image:: images/bai_7.6.png
        :width: 500px
        :align: center 
    |
**Bước 6**

Tạo sự kiện nhân vật bật nhảy khi nhấn nút. Kéo khối ``if then`` thả vào khối ``on A button pressed``. Thay **true** thành khối ``is mySprite hitting wall`` và đổi **left** thành **bottom**. Cuối cùng đặt khối ``set mySprite x`` và chọn ``vy (velocity y)`` đặt giá trị biến thành **-200**.

    .. image:: images/bai_7.7.png
        :width: 500px
        :align: center 
    |
**Bước 7**

Tạo vật cản di chuyển với tốc độ ngẫu nhiên. Làm cho chúng bắt đầu từ phía bên phải của màn hình và bay về phía người chơi. Di chuyển ``on game update every`` lên trình chỉnh sửa và đặt thời gian cách nhau thành **2000** mili giây. Kéo một ``projectile from side`` vào nó và vẽ một chiếc thùng làm vật cản.

    .. image:: images/bai_7.8.gif
        :width: 500px
        :align: center 
    |
    .. image:: images/bai_7.13.png
        :width: 500px
        :align: center 
    |
**Bước 8**

Kéo khối ``pick random`` vào vị trí **vx** và đặt phạm vi từ **-100** đến **-80**.

    .. image:: images/bai_7.9.png
        :width: 500px
        :align: center 
    |
**Bước 9**

Tìm khối ``place mySprite on top of tilemap col row`` và kéo khối ``on game update interval`` thả vào sau ``set projectile to``. Đặt giá trị ``col`` thành **9** và ``row`` thành **5**, đó là ô ở bên phải màn hình ngay phía trên tường. Thay ``mySprite`` thành ``projectile``.

    .. image:: images/bai_7.10.png
        :width: 500px
        :align: center 
    |
**Bước 10**

Mỗi khi một cái thùng bắt đầu di chuyển, chúng tôi muốn tăng điểm. Lấy khối ``change score by`` và nó vào trong ``on game update every``.

    .. image:: images/bai_7.11.png
        :width: 500px
        :align: center 
    |
**Bước 11**

Nếu cái thùng chạm vào người chơi thì trò chơi sẽ kết thúc. Kéo khối ``on sprite overlaps`` vào màn hình làm việc thay đổi ``otherSprite`` thành ``Projectile``. Đặt khối ``game over`` vào trong.

    .. image:: images/bai_7.12.png
        :width: 500px
        :align: center 
    |
**Hoàn thành**

Như vậy ta đã có một trò chơi như ý muốn. Điều cuối cùng bạn cần làm là tải trò chơi về Kít của mình và trải nghiệm hoạt động trong trò chơi.



