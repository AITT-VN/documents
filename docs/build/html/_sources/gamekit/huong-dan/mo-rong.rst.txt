8. Sử dụng thêm tiện ích mở rộng trong trò chơi
============================



**Giới thiệu**

Các thư viện tiện ích mở rộng trong Arcade cho phép người dùng dễ dàng phát triển và chia sẻ các thư viện của mình với người khác. Trong hướng dẫn này, bạn sẽ sử dụng phần thư viện ``corgi`` để tạo một trò chơi đơn giản. Trong bài học này, thư viện mở rộng đã được tải sẵn. Bạn có thể tìm hiểu về các thư viện khác và sử dụng cho các dự án khác của mình.

    .. image:: images/bai_8.gif
        :width: 500px
        :align: center 
    |

Link chương trình mẫu: `Tại đây <https://makecode.com/_AXWTugikKbzi>`_

Xem hướng dẫn online bằng video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Ga5wLKnAhJc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|

**Bước 1**
Tìm ``set myCorg to`` trong ``Corgi``. kéo vào khối ``on start``.

    .. image:: images/bai_8.1.png
        :width: 500px
        :align: center 
    |
Thư viện tiện ích mở rộng trong MakeCode Arcade

**Bước 2**

Bây giờ, hãy làm cho nhân vật của chúng ta di chuyển  bằng các phím mũi tên của bộ điều khiển.Khối ``make myCorg move left and right with arrow keys`` giúp nhân vật di chuyển sang trái và phải, khối ``make myCorg jump if up arrow key is pressed`` sẽ giúp nhân vật bạn nhảy lên với phím mũi tên hướng lên.

    .. image:: images/bai_8.2.png
        :width: 500px
        :align: center 
    |
**Bước 3**

Bạn có muốn nhân vật của bạn chuyển động khi di chuyển? Khối ``change image when myCorg is moving`` sẽ giúp bạn thực hiện điều này.

    .. image:: images/bai_8.3.png
        :width: 500px
        :align: center 
    |
**Bước 4**

Tiếp theo chúng ta sẽ vẽ bản đồ và tường bằng khối ``set tilemap to`` , nhớ để vào khối ``on start`` nhé.

    .. image:: images/bai_8.4.png
        :width: 500px
        :align: center 
    |
Đặt kích thước của tilemap là 20 x 8, vẽ một số nền tảng cho corgi đứng và đặt chúng là ``Walls``.

    .. image:: images/bai_8.5.gif
        :width: 500px
        :align: center 
    |
**Bước 5**

Thiết lập quan sát nhân vật bằng khối ``make camera follow myCorg left and right`` từ ``Corgi`` và để vào khối ``on start``.

    .. image:: images/bai_8.6.png
        :width: 500px
        :align: center 
    |
**Bước 6**

Ở cuối bản đồ trò chơi, tạo một cột khác biệt với những cái khác. Điều này sẽ đại diện cho mục tiêu cho người chơi.

    .. image:: images/bai_8.7.png
        :width: 500px
        :align: center 
    |
    .. image:: images/bai_8.9.png
        :width: 500px
        :align: center 
    |
**Bước 7**
Thêm một khối ``on sprite of kind Player overlaps at location`` từ ``Scene``, sau đó nhấp vào ô rô để tìm ô bạn sử dụng làm mục tiêu. Bên trong sự kiện đó, thêm một ``game over lose``. Chuyển **LOSE** thành **WIN.**

    .. image:: images/bai_8.8.png
        :width: 500px
        :align: center 
    |
**Hoàn thành**

Sau khi hoàn tất chương trình hãy tải nó xuống GameKit của bạn.

Sử dụng các nút nhấn để điều khiển nhân vật vượt qua các vật cản để đi đến đích và giành chiến thắng.


















