16. Game: Bắn máy bay
=========================


**Giới thiệu**

Bán máy bay là thể loại game rất phổ biến. Với GameKit bạn có thể tạo ra trò chơi này theo quy luật của chính bạn.

Hãy tạo ra chiến hạm riêng cho mình và bắt đầu tiêu diệt các máy bay quân thù, đừng quên việc khéo léo né tránh để đạt điểm cao nhé!

    .. image:: images/bai_4.gif
        :width: 400px
        :align: center 
    |

Link chương trình mẫu: `Tại đây <https://makecode.com/_7DyR89eCLDHt>`_

Xem hướng dẫn online bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/YykbRLzF91k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**

Tìm và lấy khối ``set mySprite to sprite of kind player`` đặt vào ``on start``. nhấp vào biến ``mySprite``, chọn ``Rename variable…``, và đổi tên thành ``spacePlane``.

    .. image:: images/bai_4.1.png
        :width: 600px
        :align: center 
    |
Nhấp vào ô hình xám để mở trình chỉnh sửa ảnh. Tự vẽ cho mình một chiến hạm thật đặc biệt.

    .. image:: images/bai_4.2.jpg
        :width: 400px
        :align: center 
    |
**Bước 2**

Chọn khối ``set mySprite stay in screen`` đặt vào sau khối ``set mySprite to sprite of kind player``. Thay ``mySprite`` thành ``spacePlane``. Nhấp vào switch ``OFF`` để chuyển chế độ thành ``ON``.

Chọn mục ``Info``, lấy khối ``set life to``, thiết lập lại giá trị là **3**.

    .. image:: images/bai_4.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Bây giờ, hãy thêm một số hành động cho nút nhấn. Trong ``Controller`` chọn khối ``move mySprite with buttons``. Như trước, ta thay đổi ``mySprite`` thành ``spacePlane``. Nhấp vào biểu tượng **(+)** để mở rộng khối, thay đổi **vx** và **vy** thành **200**.

Tiếp theo, lấy khối ``on A button pressed`` từ ``Controller`` và đặt nó vào màn hình làm việc.

    .. image:: images/bai_4.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Quay lại ``Sprites``, tìm khối ``set projectile to projectile from mySprite`` và đặt nó vào trong ``on A button pressed``. Click vào biến ``projectile`` chọn ``Rename variable…``, và đổi tên thành ``dart``. Chuyển biến ``mySprite`` thành ``spacePlane``, đặt **vx** thành **200**, đặt **vy** thành **0**.

    .. image:: images/bai_4.5.png
        :width: 600px
        :align: center 
    |
Nhấp vào biểu tượng ô màu xám và vẽ một chiếc máy bay địch.

    .. image:: images/bai_4.6.jpg
        :width: 400px
        :align: center 
    |
**Bước 5**

Từ ``Sprites`` lấy khối ``on sprite of kind Player overlaps``. Chuyển giá trị ``kind`` thứ hai thành ``Enemy``.

Sau đó, kéo khối ``destroy mySprite``  vào và chọn biến ``otherSprite`` để thế vào ``mySprite``.

Tiếp theo, chọn khối ``change life by`` từ từ mục ``Info`` và thả nó vào sau ``destroy otherSprite``. Thiết lập giá trị bằng **-1**.

    .. image:: images/bai_4.7.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Tạo một bản sao ``on sprite of kind Player overlaps`` bằng cách nhấp chuột trái vào nó và chọn **Duplicate**. Trong khối mới đó, thay đổi ``Player`` thành ``projectile``. Và thay đổi giá trị trong ``change life by`` bằng **1**.

    .. image:: images/bai_4.8.png
        :width: 600px
        :align: center 
    |
**Bước 7**

Nhân bản thêm một ``destroy otherSprite`` và đặt liền kề, kéo biến ``sprite`` thế vào chỗ ``otherSprite``. Sau đó, nhấp vào biểu tượng **(+)** và chọn hiệu ứng **fire** và đặt thời gian hiệu ứng bằng **100 ms**.

    .. image:: images/bai_4.9.png
        :width: 600px
        :align: center 
    |
**Bước 8**

Vào mục ``Game`` lấy khối ``on game update every`` và đặt nó vào vùng kéo thả. Lấy khối ``set mySprite to sprite of kind player`` đặt vào trong ``on update interval``, đổi tên biến thành ``bogey``. Sau đó thay biến ``kind`` từ ``Player`` thành ``Enemy``. Nhấp vào hình ảnh sprite trống để mở trình chỉnh sửa hình ảnh. Vẽ một hình ảnh của một máy bay địch.

    .. image:: images/bai_4.10.png
        :width: 600px
        :align: center 
    |
**Bước 9**

Tìm ``set mySprite velocity to`` và đặt nó vào sau khối vừa tạo. Thay đổi biến thành ``bogey``. Sau đó, đặt **vx** thành **-100** và  **vy** thành **0**. Thêm một khối ``set mySprite position to``.

Như cũ, thay biến thành ``bogey``. Đặt biến **x** thành **180**. Trong ``Math``, lấy khối ``pick random`` thả vào vị trí giá trị **y**.

    .. image:: images/bai_4.11.png
        :width: 600px
        :align: center 
    |
Trong ``pick random``, đặt biến đầu là **8** và biến thứ hai là **112**.

    .. image:: images/bai_4.12.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Sau khi hoàn tất các khối, tiến hành tải chương trình vào GameKit và bắt đầu trải nghiệm trò chơi của chính mỉnh.

    .. image:: images/bai_4.13.gif
        :width: 400px
        :align: center 
    |




























