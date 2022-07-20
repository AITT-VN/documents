17. Game: Phá giải mê cung
==========================

**Giới thiệu**

Bằng sự thông minh và khéo léo của mình hãy giúp cho nhân vật chính của chúng ta phá giải mê cung bí ẩn này thôi nào.
  
    .. image:: images/bai_5.gif
        :width: 500px
        :align: center 
    |

Link chương trình mẫu: `Tại đây <https://makecode.com/_bFR2490LcgyA>`_

Xem hướng dẫn online bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WIvDYSVpqsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**

Đầu tiên ta cần tạo một player. Tìm khối ``set mySprite to`` trong ``Sprites``. Kéo vào khối ``on start``.

    .. image:: images/bai_5.1.png
        :width: 600px
        :align: center 
    |
Nhấp vào hộp màu xám của ``set mySprite to`` và tạo cho mình một nhân vật mà bạn thích.

    .. image:: images/bai_5.2.gif
        :width: 500px
        :align: center 
    
    .. image:: images/bai_5.10.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Bây giờ, hãy làm cho hình nhân vật của chúng ta di chuyển bằng các phím mũi tên của bộ điều khiển. Lấy một ``move mySprite with buttons`` từ ``Controller`` và cho nó vào dưới khối ``set mySprite to``.

    .. image:: images/bai_5.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tiếp theo, tạo một mê cung theo ý định của bạn. Kéo ``set tilemap to ``từ ``Scene`` vào ``on start``. Nhấp vào hộp màu xám để mở một mê cung, chọn gạch và sử dụng các công cụ để vẽ mê cung của riêng bạn.

Hãy chắc chắn để lại một đường dẫn từ đầu đến cuối, để người chơi có thể thoát ra.

    .. image:: images/bai-5.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Chọn khối ``place mySprite on top of random`` trong ``Scene``, kéo thả vào khối ``on start`` đặt vào phía sau ``set tilemap to``. Điều này sẽ di chuyển nhân vật bạn đã tạo lên trên một trong các ô đã chọn; nhấp vào ô rô và chọn ô bạn chọn làm điểm bắt đầu cho trình phát.

    .. image:: images/bai_5.5.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Tìm khối ``camera follow sprite mySprite`` trong ``Scene``, kéo thả vào khối ``on start``. Điều này sẽ giúp theo dõi nhân vật người chơi khi nó di chuyển xung quanh màn hình.

    .. image:: images/bai_5.6.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Chọn khối ``on sprite of kind player overlaps at location`` trong ``Scene``. Sự kiện này sẽ xảy ra bất cứ khi nào người chơi tới cuối mê cung.

Tìm ``game over lose`` trong ``Game``, kéo vào trong khối ``on sprite of kind player overlaps at location``. Nhấp vào **LOSE** để chuyển thành  **WIN**. Điều này có nghĩa là khi bạn bước đến điểm cuối cùng (có hình các bậc thang) bạn sẽ thắng.

    .. image:: images/bai_5.7.png
        :width: 600px
        :align: center 
    |
**Bước 7**

Tìm ``start countdown 10 (s)`` trong ``Info``, bỏ nó vào trong khối ``on start``.

    .. image:: images/bai_5.8.png
        :width: 600px
        :align: center 
    |
**Bước 8**

Bây giờ bạn có một trò chơi với một mục tiêu, và thời gian chơi nhưng người chơi có thể di chuyển qua tất cả các bức tường! Mở lại trình chỉnh sửa tilemap và sử dụng **Draw wallscông** cụ để vẽ các bức tường có thể chặn các nhân vật trong tilemap, để chúng không thể di chuyển qua chúng.

    .. image:: images/bai_5.9.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Hãy tải chương trình của mình xuống GameKit và bắt đầu tận hưởng trò chơi xem mình có thể ra khỏi mê cung trong thời gian quy định không nhé.



















