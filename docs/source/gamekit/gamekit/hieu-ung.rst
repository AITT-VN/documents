8. Tạo hiệu ứng tuyết rơi 
=============================

    .. image:: images/5.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Ở bài này chúng ta sẽ học cách tạo hiệu ứng tuyết rơi trên màn hình bằng bằng cách di chuyển ngẫu nhiên các sprite có hình dạng tuyết rơi.

Link chương trình mẫu: `Tại đây <https://makecode.com/_fd9VKqFHwAXg>`_


**Bước 1**

Trong bộ công cụ ``game`` chọn khối ``on game update`` kéo thả vào không gian làm việc.

Khác với khối ``on start`` chương trình chỉ chạy một lần, thì khối ``on game update`` sẽ liên tục cập nhật lại vị trí, vận tốc của các sprites.

    .. image:: images/5.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Tìm ``set projectile to`` trong ``Sprite`` khối có ``projectile from side`` bên trong nó.

Kéo bỏ vào khối ``on game update`` và thay đổi **vx** thành **0** và **vy** thành **100**.

    .. image:: images/5.3.png
        :width: 800px
        :align: center 
    |
**Bước 3**

Nhấp vào hộp màu xám bên cạnh **projectile** và tạo một pixel trắng duy nhất làm hình dạng tuyết.

    .. image:: images/5.4.png
        :width: 400px
        :align: center 
    
    .. image:: images/5.5.png
        :width: 800px
        :align: center 
    |    
**Bước 4**

Chọn ``pick random 0 to 10`` từ ``Math``  và đặt nó sau **vy** của ``projectile``, trong ``pick random 0 to 10`` thay đổi **0** và **100** thành **20** và **30**. Điều này nghĩa là hình ảnh hạt tuyết sẽ di chuyển tử trên màn hình xuống dưới với tốc độ ngẫu nhiên từ khoản 20 đến 30 pix/s (điểm ảnh trên giây)

    .. image:: images/5.6.png
        :width: 800px
        :align: center 
    |
**Bước 5**

Thiết lập hạt tuyết trên màn hình. Tìm ``set mySprite position to`` trong ``Sprites`` và đặt nó sau khối ``set projectile to``.

Thay đổi ``mySprite``  thành ``projectile``

    .. image:: images/5.7.png
        :width: 800px
        :align: center 
    |
**Bước 6**

Lấy một khối ``pick random 0 to 10`` và đặt nó vào giá trị x trong khối ``set projectile position to``. Tìm ``screen width`` (độ rộng màn hình) trong ``Screen`` và thay thế vào vị trí **10** trong ``pick random 0 to 10``. Điều này sẽ khiến hạt tuyết xuất hiện ngẫu nhiên bất kì vị trí nào ở  màn hình, và di chuyển xuống dưới giống như đang rơi.

    .. image:: images/5.8.png
        :width: 800px
        :align: center 
    |
**Bước 7**

Tại thời điểm này, sẽ có rất nhiều hạt tuyết xuất hiện. Để kiếm soát hoạt động của hiệu ứng tuyết rơi, chúng ta sẽ sử dụng khối lệnh điều kiện ``if then`` như hình minh họa

    .. image:: images/5.9.png
        :width: 800px
        :align: center 
    |
**Bước 8**

Lấy khối ``0 % chance`` từ ``Math`` và thay thế vào vị trí của **true** trong khối ``if then``. Thay đổi tỷ lệ phần trăm từ **0** sang **25**.

Lúc này, chương trình chỉ cho phép tạo ra khoảng 25% số lượng tuyết rơi so với lúc đầu. Bạn có thể thay đổi mật độ tuyết rơi theo số % này.

    .. image:: images/5.10.png
        :width: 800px
        :align: center 
    |
**Hoàn thành**

Tải chương trình của bạn vào GameKit và quan sát màn hình sẽ thấy có hiệu ứng giống như tuyết rơi.





























