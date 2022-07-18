3. Quả chanh mọng nước 
===================

**Giới thiệu**

    .. image:: images/bai_3.gif
        :width: 400px
        :align: center 
    |
Nếu là người ưa thích sự nhanh nhẹn và khéo léo thì Quả chanh mọng nước là sự lựa chọn phù hợp giành cho bạn. Trong trò chơi bạn sẽ phải điều khiển quả chanh mọng nước khéo léo di chuyển vào những quả dâu tây vắt nước. Chạm vào càng nhiều dâu tây thì điểm số của bạn càng cao.

Link chương trình mẫu: `Tại đây <https://makecode.com/_DX0EoEYqPhxi>`_

Xem hướng dẫn bằng video tại:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/2r5Uu9dG4vw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|

**Bước 1**

Trong khối ``on start`` chọn khối ``set background color`` từ ``Scene``. Chọn màu nền cho trò chơi. Lấy tiếp khối ``set mySprite to`` từ ``Sprites``.

    .. image:: images/bai_3.1.png
        :width: 600px
        :align: center 
    |
Chọn hình ảnh quả chanh cho nhân vật từ **Gallery**. Trong ``Controller`` chọn khối ``move mySprite with buttons`` để điều khiển quả chanh.

    .. image:: images/bai_3.2.gif
        :width: 400px
        :align: center 
    |
**Bước 2**

Để giữ cho quả chanh của bạn không thoát ra khỏi màn hình, bạn chọn khối ``set mySprite stay in screen``. Chuyển sang chế độ ``ON``. Tìm khối ``start countdown`` và đặt vào cuối. Thay đổi thời gian từ **10** thành **30** giây.

    .. image:: images/bai_3.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Bây giờ, đặt khối ``on game update every`` từ ``Game``. Thiết lập thời gian là **1000 ms**. Từ ``Sprites``, kéo khối ``set projectile to`` ``projectile from side`` và thả nó vào trong ``on game update every``. Chọn hình ảnh quả dâu tây cho nhân vật từ **Gallery**.

    .. image:: images/bai_3.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Trong ``Math`` chọn khối ``pick random`` và đặt nó vào vị trí **vx**. Trong ``pick random`` thay đổi **0** đầu tiên thành **-50** và **10** thành **50**. Sao chép một khối tương tự và đặt nó vào vị trí **vy**.

    .. image:: images/bai_3.5.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Từ ``Sprites``, chọn khối ``on sprite of kind overlaps`` bỏ vào màn hình làm việc. Thiết lập tham số **otherSprite** thành **Projectile**. Tiếp từ ``Sprites``, kéo thêm khối ``mySprite start effect`` và thả vào khối ``overlaps``. Nhấp vào biểu tượng dấu **(+)** để mở rộng khối và thiết lập thời gian thành **200** ms.

    .. image:: images/bai_3.6.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Cuối cùng, để ghi điểm cho trò chơi, bạn kéo khối ``change score by`` từ ``Info`` thả vào sau khối ``mySprite start effect``.

    .. image:: images/bai_3.7.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Đến đây coi như mọi việc đã hoàn thành. Hãy tải chương trình vào Game Kit của bạn và thể hiện sự khéo léo của mình thôi nào.

    .. image:: images/bai_3.8.jpg
        :width: 400px
        :align: center 
    |

