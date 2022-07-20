18. Game: Bóng rổ
====================

**Giới thiệu** 

Nếu bạn là một người đam mê thể thao thì trò **bóng rổ** là một sự lựa chọn tuyệt vời. Bạn cần phải phán đoán chính xác cách di chuyển của nhân vật để có thể ném bóng vào rổ, ghi điểm cho mình.

    .. image:: images/bai_6.gif
        :width: 400px
        :align: center 
    |

Link chương trình mẫu: `Tại đây <https://makecode.com/_eWAa1fMH5H46>`_

Xem hướng dẫn online bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GYYELg0ZLMI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1 – Thiết lập hình nền trò chơi**

Từ công cụ ``Scene`` bạn chọn khối ``set background image`` bỏ vào trong màn hình làm việc, bên trong khối ``on start``. Trong khối ``set background image`` bạn chọn một màu ưa thích làm nền cho trò chơi.

    .. image:: images/bai_6.1.png
        :width: 600px
        :align: center 
    |
**Bước 2 – Tạo nhân vật người chơi**

Từ ``Sprites`` chọn khối ``set mySprite`` thả vào sau khối ``set background image``. Nhấp vào ô xám rồi chọn nhân vật bất kì từ **Gallery**.

    .. image:: images/bai_6.2.png
        :width: 600px
        :align: center 
    |
**Bước 3 – Định vị nhân vật Player ở cuối màn hình**

Từ ``Sprites`` kéo khối ``set sprite position`` thả vào sau khối ``set sprite``. Trong khối ``set mySprite position``, nhấp vào tọa độ **x** và sử dụng bộ chọn tọa độ, chọn một vị trí ở cuối màn hình như ảnh.

    .. image:: images/bai_6.3.png
        :width: 600px
        :align: center 
    |
**Bước 4 – Đặt tốc độ (chuyển động) của người chơi**

Từ ``Sprites`` kéo khối ``set mySprite velocity`` thả vào sau khối ``set mySprite position``. Để player chỉ di chuyển theo chiều ngang, đặt giá trị **vy** thành **0** .

    .. image:: images/bai_6.4.png
        :width: 600px
        :align: center 
    |
**Bước 5 – Làm player bật ra khi gặp tường (cạnh màn hình)**

Nếu bạn sử dụng trình mô phỏng ở bước 4 sẽ thấy nhân vật player di chuyển ra khỏi màn hình, đây không phải là điều chúng ta muốn, ta cần phải làm cho nhân vật bật ra lại khi gặp cạnh màn hình. Từ ``Sprites`` chọn khối ``set mySprite stay`` trong ``screen`` đặt nó vào sau ``mySprite velocity``. trong ``set mySprite stay`` trong ``screen``, hãy sử dụng menu thả xuống để chọn thuộc tính **bounce on wall**, thay đổi giá trị thành **true**.

    .. image:: images/bai_6.5.png
        :width: 600px
        :align: center 
    |
**Bước 6 – Tạo bóng rổ**

Trong mục ``Sprites`` chọn tiếp khối ``set mySprite`` thứ hai và tạo hình ảnh cho nhân vật này là một chiếc rổ (các bạn cố gẵng vẽ đẹp hơn mình nhé!)

    .. image:: images/bai_6.6.png
        :width: 600px
        :align: center 
    |
Trong ``set mySprite2`` nhấp vào ``Player`` từ menu thả xuống, chọn **Add a new kind**, chọn **Hoop**.

    .. image:: images/bai_6.7.png
        :width: 600px
        :align: center 
    |
**Bước 7 – Đặt vị trí của rổ lên trên cùng của màn hình**

Từ ``Sprites`` chọn tiếp khối ``set mySprite position`` thả vào sau khối ``set mySprite2``. Trong ``set mySprite position`` nhấp vào ``mySprite`` chọn ``mySprite2``. Sau đó nhấp vào tọa độ **x** và sử dụng bộ chọn tọa độ, chọn một vị trí ở giữa trên cùng của màn hình.

    .. image:: images/bai_6.8.png
        :width: 600px
        :align: center 
    |
**Bước 8 – Sử dụng một phím để bắn bóng rổ**

Từ bộ công cụ ``controller`` Tkéo khối ``on button pressed``bỏ vào màn hình làm việc. Nhấp vào menu thả xuống A để chọn bất kỳ nút nào.

    .. image:: images/bai_6.9.png
        :width: 600px
        :align: center 
    |
**Bước 9 – Ném bóng đi**

Từ ``Sprites`` kéo khối các khối ``set projectile to projectile from mySprite`` bỏ vào trong ``on button pressed``. Nhấp vào hình màu xám để mở trình chỉnh sửa hình ảnh sprite và vẽ hình ảnh của một quả bóng rổ (bạn thử sử dụng công cụ hình tròn trong trình chỉnh sửa hình ảnh).

    .. image:: images/bai_6.10.png
        :width: 600px
        :align: center 
    |
**Bước 10 – Thiết lập vận tốc (chuyển động) của quả bóng**

Chúng tôi muốn những quả bóng rổ di chuyển từ nhân vật Người chơi của chúng tôi theo chiều dọc lên trên. Trong khối ``set projectile`` đặt giá trị **vx** thành **0** và đặt giá trị **vy** thành **-100**.

    .. image:: images/bai_6.11.png
        :width: 600px
        :align: center 
    |
**Bước 11 – Tạo sự kiện và chiến thắng khi bóng vào rổ**

Từ ``Sprites`` kéo khối ``on mySprite overlaps`` thả vào màn hình làm việc. nhấp vào ``Player`` và thay đổi thành ``Hoop``.

Từ ``Game`` kéo khối ``game over`` thả vào khối ``on sprite overlaps`` và thay đổi biến thành **WIN**.

    .. image:: images/bai_6.12.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Sau khi hoành thành tất cả các khối trong chương trình như  trên, bạn tiến hành tải chương trình vào GameKit của mình và thử nhấn phím bất kì để ném bóng đi.