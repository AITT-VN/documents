14. Game: Bông hoa hạnh phúc 
=====================


**Giới thiệu**

**Bông hoa hạnh phúc** là game tạo ra những chú ong bay ra ngẫu nhiên từ bông hoa. Có lẻ bạn nghĩ bài học này sẽ khá nhàm chán nhưng nó sẽ thích hợp để tạo khung cảnh, tăng cảnh quan sinh động trong game hơn là một trò chơi đơn lẻ.

    .. image:: images/bai_2.gif
        :width: 400px
        :align: center 
    |
Link chương trình mẫu: `Tại đây <https://makecode.com/_KfuXADLLyDyo>`_ 

Xem hướng dẫn bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7GA_V4WXcP4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**

Trong bộ công cụ ``scene`` chọn khối ``set background color to`` bỏ vào khối ``on start`` và chọn màu nền tùy thích.

Tìm khối ``set mySprite to`` trong ``Sprites``. Kéo thả vào khối ``on start``, sau khối ``set background color to``.

    .. image:: images/bai_2.1.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Tìm khối ``on update every 500 ms`` trong ``Game``, và thả nó vào màn hình làm việc. Thiết lập thời gian là **1000 ms**.

    .. image:: images/bai_2.2.png
        :width: 600px
        :align: center 
    |
Lấy khối ``set projectile to projectile from mySprite`` trong ``Sprites`` đặt vào trong ``on game update every 1000 ms``.

    .. image:: images/bai_2.3.png
        :width: 600px
        :align: center 
    |
Nhấp vào ô màu xám trên ``projectile`` và tìm chọn hình ảnh chú ong trong **Gallery**.

    .. image:: images/bai_2.4.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tìm chọn khối ``pick random 0 to 10``. Đặt nó vào vị trí ``vx`` của khối ``projectile`` và thay đổi **0** thành **-25**, **10** thành **25**.

    .. image:: images/bai_2.5.png
        :width: 600px
        :align: center 
    |
Nhân đôi khối ``pick random -25 to 25`` này và đặt vào ``vy`` của ``projectile``.

    .. image:: images/bai_2.6.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Tìm khối ``set mySprite x to 0`` trong ``Sprites``, đặt sau khối set ``projectile`` to và thay đổi ``mySprite`` thành ``projectile``. Thay đổi ``x`` thành ``lifespan`` và đặt **0** thành **3000**.

    .. image:: images/bai_2.7.gif
        :width: 600px
        :align: center 
    |
**Bước 5**

Cho đến bước 4, bạn sẽ thấy ở vùng mô phỏng có những chú ong bay bị ngược khi di chuyển về phía trái.

Giờ hãy thiết lập một điều kiện để khi chúng bay về bên trái sẽ đảo ngược lại nhé. Lấy một khối ``if then`` và đặt nó vào sau khối ``set projectile lifespan``. Thay đổi điều kiện ``true`` của khối ``if then`` thành khối ``0 < 0``. Tìm và đặt khối ``mySprite x`` vào vị trí **0**.

Thay đổi ``mySprite`` thành ``projectile`` và thay đổi ``x`` thành ``vx (velocity x)``.

    .. image:: images/bai_2.8.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Đi đến mục mở rộng **Advanced**. Trong ``Images`` tìm khối ``flip picture horizontally``. Đặt nó vào trong khối ``if then``. Giờ quay lại mục ``Sprites``, lấy khối ``mySprite image`` và đặt vào ``picture`` trong khối ``flip picture horzontally``. Thay đổi tên ``mySprite`` thành ``projectile``.

    .. image:: images/bai_2.9.gif
        :width: 600px
        :align: center 
    |
    .. image:: images/bai_2.10.png 
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Sau khi bạn làm xong các bước hãy nạp chương trình vào GameKit của mình và chạy thử xem kết quả của như thế nào nhé.














