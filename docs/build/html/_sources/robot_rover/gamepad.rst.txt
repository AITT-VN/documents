**Tay cầm điều khiển robot**
===========

1. Giới thiệu
----
------------

Gamepad là một phụ kiện được sử dụng để mở rộng khả năng tương tác với các loại robot trong hệ sinh thái OhStem, bao gồm Robot xBot, Robot Rover và Maker Robot. Việc kết nối giữa Gamepad và robot được thực hiện thông qua module Gamepad Receiver ở cổng giao tiếp I2C có trên robot. Điều này cho phép người dùng dễ dàng kiểm soát và điều khiển robot một cách linh hoạt hơn, tăng tính năng tương tác và trải nghiệm với robot.

.. image:: images/gamepad.png
    :scale: 100%
    :align: center
|

Đặc biệt, Gamepad có 2 joystick và 12 nút nhấn có thể lập trình để tạo ra các tính năng tùy biến để người dùng điều khiển robot theo ý muốn. Các tính năng bao gồm di chuyển, nâng hạ, dò line,... sẽ giúp bạn khám phá tất cả các chức năng của robot và tạo ra những trải nghiệm mới mẻ.


**2. Link sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/tay-cam-dieu-khien-gamepad-v2
    :class: with-shadow
    :scale: 100%
    :align: center
|


3. Thông số kỹ thuật
----
-------

- **Thông số kỹ thuật của module Gamepad Receiver:**

.. image:: images/gamepad.1.png
    :scale: 70%
    :align: center
|

- **Thông số kỹ thuật của Gamepad:**

.. image:: images/gamepad.2.png
    :scale: 100%
    :align: center
|

4. Kết nối GamePad với Robot Rover
---------
--------- 

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/jkSBx4nnpJQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

|

- **Đối với Robot xBot và Maker Robot:** Kết nối module vào cổng I2C ở vị trí số 4. 

.. figure:: images/i2c_xbot.png
    :scale: 70%
    :align: center

    Các bước còn lại thực hiện tượng tự như Rover

|

5. Các nút nhấn có trên Gamepad: 
---------
---------

- **Mặt trước của Gamepad:**

.. image:: images/gamepad.3.png
    :scale: 70%
    :align: center
|

- **Mặt trên của Gamepad:**

.. image:: images/gamepad.4.png
    :scale: 70%
    :align: center
|

.. raw:: html

    <iframe width="640" height="360" src="https://www.youtube.com/embed/eqth_ATNAik" title="Hướng dẫn GamePad V2 với robot Rover - Ý nghĩa các nút nhấn - Phần 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

|


6. Chức năng của module Gamepad Receiver
-----
---------

Module Gamepad Receiver là thiết bị để kết nối robot với tay cầm điều khiển, trên module sẽ có các nút nhấn và đèn báo hiệu như sau: 

.. image:: images/gamepad.5.png
    :scale: 100%
    :align: center
|

1. **Đèn báo dung lượng pin trên Gamepad:**

    Khi gamepad đã được kết nối tới module, các đèn này sẽ hiển thị tình trạng pin của Gamepad như sau:
        
        + Pin < 20% hoặc Gamepad chưa được kết nối: 0 đèn sáng
        + Pin < 40%: 1 đèn sáng
        + Pin <60%: 2 đèn sáng
        + Pin <80%: 3 đèn sáng
        + Pin >80%: 4 đèn sáng


2. **Đèn báo trạng thái:**

    Đèn này sẽ báo cho bạn biết module đã kết nối thành công với Gamepad hay chưa. 

    **2.1. Đèn chớp tắt nhanh (0,2s):** Module đang tìm kiếm và cấp phép kết nối đến các gamepad mới.
    
    Sau đó, **nhấn giữ nút Nguồn và nút Share trên Gamepad cùng 1 lúc để Gamepad vào chế độ kết nối mới**. Khi đó đèn led trên Gamepad sẽ nháy trắng liên tục báo hiệu đã vào chế độ kết nối mới.

.. image:: images/gamepad.6.png
    :scale: 80%
    :align: center
|

    **2.2. Đèn chớp tắt chậm (1s):** Module đang tìm kiếm và kết nối các Gamepad đã được cho phép kết nối ở bước 2.1. 
    
    Đồng thời **nhấn nút nguồn Gamepad, đèn led trên Gamepad sẽ nháy trắng chậm báo hiệu đã vào chế độ tìm thiết bị đã kết nối.** Khi đèn trên GamePad và đèn báo trạng thái trên module Gamepad Receiver cùng hiện màu xanh thì đã kết nối thành công.

.. image:: images/gamepad.7.png
    :scale: 80%
    :align: center
|

    **2.3. Đèn chuyển từ trạng thái luôn bật sang chớp tắt 3 lần rồi tắt hẳn:** Module đã xóa tất cả các kết nối đã cấp phép ở bước 2.1.

3. **Nút Reset:**

    Khởi động lại module, đồng thời ngắt kết nối với Gamepad đã kết nối.

4. **Nút Clear:** Nút này có chức năng sau:
    
    + Nhấn giữ nút Clear sau khi nhấn nút Reset: Lúc này đèn báo kết nối sẽ nhấp nháy nhanh như mô tả ở mục 2.2 để bắt đầu tìm kiếm thiết bị Gamepad mới.
    
    + Nhấn giữ nút Clear trong vòng 3 giây trong quá trình Gamepad đã kết nối thành công với module Gamepad Receiver thì module Gamepad Receiver sẽ xóa kết nối của Gamepad đã được cho phép. Để sử dụng kết nối lại, bạn cần thực hiện lại bước 2.1


7. Hướng dẫn lập trình cho Gamepad
-------
-------

7.1. **Thư viện**
-----------

1. Vào giao diện lập trình cho Yolo:Bit (hoặc xBot) trong OhStem App tại địa chỉ `<https://app.ohstem.vn/>`_ hoặc ứng dụng OhStem App trên mobile ( Tải trên Google Play / App Store với tên tìm kiếm là “OhStem App”)

.. image:: images/thu_vien.1.png
    :scale: 100%
    :align: center
|

2. Nhấn vào mục Mở Rộng ở danh sách bên trái: 

.. image:: images/thu_vien.2.png
    :scale: 100%
    :align: center
|

3. Chọn thư viện **Robocon** trong danh sách mục mở rộng có sẵn (hoặc nhập tên Robocon vào ô tìm kiếm nếu bạn không nhìn thấy): 

.. image:: images/robocon.png
    :scale: 80%
    :align: center
|

Chọn tải thư viện: 

.. image:: images/thu_vien.3.png
    :scale: 100%
    :align: center
|

4. Chọn thiết bị Yolo:Bit (hoặc xBot) để kết nối (nếu chưa kết nối) và phải đảm bảo đã cài đặt thư viện thành công (bên trái giao diện **xuất hiện danh mục Gamepad** như hình):

.. image:: images/robocon.2.png
    :scale: 60%
    :align: center
|


7.2. **Giới thiệu khối lệnh**
----------

Trong danh mục khối lệnh Gamepad sẽ có các khối lệnh với chức năng như sau: 

- **Khối lệnh khởi tạo Gamepad:** 
    
    Để lập trình cho Gamepad, trước tiên bạn cần khai báo chân kết nối của module Gamepad Receiver với robot bằng câu lệnh sau: 

.. image:: images/gamepad.8.png
    :scale: 100%
    :align: center
|

.. note:: Đối với xBot, bạn sử dụng câu lệnh sau để khai báo cổng kết nối module Gamepad Receiver với robot: 

    .. figure:: images/gamepad.27.png
        :scale: 100%
        :align: center

        Chỉ kết nối module với xBot ở cổng 4, 5 hoặc 6
|

- **Cài đặt chế độ điều khiển:**

    Bạn có thể đặt chế độ điều khiển mặc định của robot bằng câu lệnh:

.. image:: images/gamepad.9.png
    :scale: 100%
    :align: center
|

    Từng chế độ điều khiển trên Gamepad sẽ có chức năng và màu đèn tương ứng như sau: 

    + **Phím điều hướng dpad - đèn màu cam**: cho phép robot di chuyển theo 4 hướng tiến về trước, lùi lại, rẽ trái và rẽ phải. Bạn cũng có thể điều khiển **robot di chuyển theo đường cong** bằng cách nhấn **kết hợp 2 phím ↑ hoặc ↓ với ↶ hoặc ↷ cùng lúc đến khi thả nút nhấn**.
    
    + **Joystick trái - đèn xanh lá**: chỉ có thể điều khiển robot di chuyển đến các hướng bằng joystick ở bên trái Gamepad.  

    + **Joystick phải - đèn xanh dương**: tượng tự với joystick trái, chỉ có thể điều khiển robot đi đến các hướng bằng joystick ở bên phải Gamepad.  

    + **Kết hợp joystick trái và joystick phải - đèn tím**: bạn có thể điều khiển từng động cơ của robot, Joystick trái điều khiển động cơ bên trái, joystick phải điều khiển động cơ bên phải. 


- **Cài đặt tăng giảm tốc độ cho robot:**

    Câu lệnh giúp bạn tăng và giảm tốc độ của robot cho đến khi đạt yêu cầu:

.. image:: images/gamepad.10.png
    :scale: 80%
    :align: center
|

    Tốc độ mặc định của robot khi được điều khiển bằng Gamepad là 50. Bạn có thể chọn 2 nút nhấn bất kỳ trên Gamepad để tăng và giảm tốc độ bằng cách nhấn vào hình tam giác có trong câu lệnh. 
    
.. note:: Ngoài việc điều khiển các hướng di chuyển của robot, joystick trái và joystick phải còn có chức năng như một nút nhấn khi được nhấn.


- **Cài đặt điều khiển tay gắp của Robot:** 

    Câu lệnh có chức năng điều khiển tay gắp đóng và mở: 

.. image:: images/gamepad.11.png
    :scale: 80%
    :align: center
|
    Bạn cần **chọn đúng chân cắm servo của tay gắp** trong chương trình và nhấn vào hình tam giác có trong câu lệnh để chọn nút nhấn điều khiển tay gắp robot trên Gamepad. 


- **Cài đặt kit bắn bóng:**
    
    Câu lệnh có chức năng điều khiển kit bắn bóng, bật chế độ nạp đạn hoặc chế độ bắn:

.. image:: images/gamepad.12.png
    :scale: 80%
    :align: center
|

    Ở câu lệnh này bạn cần chọn đúng chân cắm của từng servo trên robot. Nhấn vào hình tam giác có trong câu lệnh để chọn nút nhấn điều khiển kit bắn bóng trên Gamepad.  
 
- **Đổi màu đèn trên Gamepad**
    
    Câu lệnh đổi màu đèn hiển thị trên Gamepad. Có thể chọn màu khác mà bạn muốn đổi. 

.. image:: images/gamepad.13.png
    :scale: 80%
    :align: center
|

    Vị trí đèn LED trên Gamepad: 

.. image:: images/gamepad.14.png
    :scale: 100%
    :align: center
|

- **Thay đổi mức độ rung của Gamepad:**

    Câu lệnh yêu cầu Gamepad rung để khi nó kết nối thành công với robot.
   
    Bạn có thể điều chỉnh độ rung trong khoảng từ 0 đến 100 và thời gian rung từ 0 đến 2000 mili giây (tương đương với 2 giây).

.. image:: images/gamepad.15.png
    :scale: 80%
    :align: center
|

- **Chuyển sang chế độ dò line:** 
    
    Câu lệnh này được sử dụng để bật chế độ dò line trên robot.  
   
    Nhấn giữ nút này để robot thực hiện việc dò line. Sau khi thả ra, chế độ dò line hết tác dụng trở về chế độ điều khiển trước đó. 

.. image:: images/gamepad.16.png
    :scale: 80%
    :align: center
|

    Tốc độ dò line có thể thay đổi trong khoảng từ 0 đến 100 và nhấn vào hình tam giác có trong câu lệnh để chọn nút nhấn  robot dò line trên Gamepad.
    
.. note:: Đối với xBot, bạn cần chọn đúng cổng kết nối của cảm biến dò line với robot khi thực hiện chương trình. 

    .. image:: images/gamepad.17.png
        :scale: 100%
        :align: center
    |


- **Nút tăng tốc:** 

    Câu lệnh này có chức năng giúp robot **tăng tốc lên tốc độ tối đa là 100 ngay lập tức**. 
    
    Nhấn giữ nút này trong khi sử dụng các chế độ di chuyển, sẽ giúp robot tăng tốc lên độ tối đa là 100. Khi thả nút, robot sẽ chuyển về tốc độ hoạt động trước đó của nó. 

.. image:: images/gamepad.18.png
    :scale: 100%
    :align: center
|

- **Đổi chế độ điều khiển:** 
    
    Câu lệnh có chức năng thay đổi chế độ điều khiển robot trên Gamepad. 

.. image:: images/gamepad.19.png
    :scale: 100%
    :align: center
|
    Khi nhấn nút này, 4 chế độ điều khiển sẽ chuyển lần lượt từ: Phím điều hướng dpad -> Joystick trái -> Joystick phải -> Kết hợp Joystick trái và Joystick phải. Đồng thời đèn trên Gamepad sẽ đổi màu theo từng chế độ điều khiển. Giúp người dùng dễ dàng lựa chọn chế độ điều khiển phù hợp trong quá trình sử dụng.
    
    Nhấn vào hình tam giác có trong câu lệnh để chọn nút nhấn đổi chế độ điều khiển robot. 


- **Điều khiển servo:** 

    Câu lệnh này được sử dụng để điều khiển servo trên các bộ kit khác như đầu nâng, thùng xe... theo ý muốn của bạn. Bạn có thể thay đổi góc hoạt động của servo và thay đổi nút nhấn trên Gamepad bằng cách nhấn vào hình tam giác có trong câu lệnh .

.. image:: images/gamepad.20.png
    :scale: 70%
    :align: center
|

- **Cập nhật thông tin từ Gamepad:** 

    Câu lệnh này được sử dụng để cập nhật và xử lý thông tin từ Gamepad một cách liên tục. Do đó, trong chương trình lập trình, câu lệnh này thường được đặt trong vòng lặp lại mãi để luôn được cập nhật các tín hiệu mới nhất từ Gamepad.

.. image:: images/gamepad.21.png
    :scale: 100%
    :align: center
|

- **Câu lệnh đang kết nối:**

    Câu lệnh này giúp bạn nhận biết trạng thái kết nối của robot và Gamepad. 

.. image:: images/gamepad.22.png
    :scale: 100%
    :align: center
|

7.3 **Nạp chương trình**
-------

Để làm quen với Gamepad, chúng ta sẽ lập trình một chương trình đơn giản như sau: 

- **Robot Rover:** 

    + **Lưu ý:** **Trước khi lập trình cho Gamepad, bạn cần tải thêm thư viện Rover cho Yolo:Bit**, xem hướng dẫn `tại đây <https://docs.ohstem.vn/en/latest/robot_rover/rover/cai-dat-thu-vien.html>`_. 
    
    + **Chương trình mẫu** xem `tại đây <https://app.ohstem.vn/#!/share/yolobit/2NfZVqnzpS0VKgXP1Fma4PXz2Mi>`_. 

.. figure:: images/gamepad.23.png
    :scale: 100%
    :align: center

    Chương trình điều khiển Robot Rover bằng Gamepad
|    

    + **Giải thích chương trình:** 
    
     Khi nạp chương trình vào Yolo:Bit thành công, các câu lệnh trong phần lặp lại mãi sẽ giúp bạn nhận biết được robot đã kết nối thành công với thiết bị chưa. 
    
        * Nếu kết nối thành công, Robot Rover sáng đèn màu xanh lá. 
        * Ngược lại, nếu chưa kết nối, Robot chớp tắt đèn đỏ liên tục. 

.. image:: images/gamepad.24.png
    :scale: 100%
    :align: center
|

     Mỗi nút nhấn chỉ thực hiện một chức năng, do đó bạn hãy kiểm tra thật kỹ trong chương trình các nút nhấn được chọn có bị lặp lại hay không nhé!


- **Robot xBot / Maker Robot** sử dụng chương trình sau:

    + **Chương trình mẫu** xem `tại đây <https://app.ohstem.vn/#!/share/xbot/2Ne5ULhptT86actotKnyX8ENugX>`_.

.. figure:: images/gamepad.25.png
    :scale: 80%
    :align: center

    Chương trình điều khiển Robot xBot / Maker Robot bằng Gamepad
|

    + **Giải thích chương trình**: 
    
     Khi nạp chương trình vào xBot thành công, các câu lệnh trong phần lặp lại mãi sẽ giúp bạn nhận biết được robot đã kết nối thành công với thiết bị chưa. 
    
        * Nếu kết nối thành công, Robot sáng đèn màu xanh lá. 
        * Ngược lại, nếu chưa kết nối, Robot chớp tắt đèn đỏ liên tục. 

.. image:: images/gamepad.26.png
    :scale: 100%
    :align: center
|

     Mỗi nút nhấn chỉ thực hiện một chức năng, do đó bạn hãy kiểm tra thật kỹ trong chương trình các nút nhấn được chọn có bị lặp lại hay không nhé!




