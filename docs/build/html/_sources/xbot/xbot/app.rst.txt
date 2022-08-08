3. Làm quen với phần mềm OhStem App
======================

**Mục tiêu:**

Biết cách sử dụng giao diện lập trình khối kéo thả của phần mềm OhStem App và viết một chương trình đơn giản để làm việc với đèn LED RGB có sẵn trên robot.


3.1 Các môi trường lập trình cho xBot
-----------------------------------
-----------------------------------

Chúng ta có thể sử dụng nhiều môi trường lập trình khác nhau để lập trình cho robot xBot, trong đó 3 môi trường phổ biến nhất là:

- **Phần mềm OhStem App**

Phần mềm này hỗ trợ **lập trình bằng giao diện kéo thả các khối lệnh**, phù hợp với các bạn nhỏ và người mới học lập trình.

OhStem App chạy được trên nhiều thiết bị khác nhau như máy tính, laptop, máy tính bảng, điện thoại (IOS và Android).

.. image:: images/xbot_3.1.png
    :width: 400px
    :align: center
|  

- **Phần mềm Arduino**

Arduino là môi trường **lập trình dạng chữ viết dựa trên ngôn ngữ C đã được chỉnh sửa**.

Arduino là phần mềm cực kỳ phổ biến và mạnh mẽ trong cộng đồng công nghê, phù hợp để lập trình các ứng dụng nâng cao và phức tạp hơn.

.. image:: images/xbot_3.2.png
    :width: 400px
    :align: center
|   

- **Lập trình bằng MicroPython**

Đây là ngôn ngữ được tạo ra dựa trên ngôn ngữ Python đã được rút gọn. Chúng phù hợp với các bộ xử lý nhỏ được sử dụng trong xBot, không có sức mạnh như máy tính của chúng ta.

Có rất nhiều phần mềm hỗ trợ lập trình MicroPython cho xBot: uPyCraft, Visual Studio Code,...

.. image:: images/xbot_3.3.png
    :width: 400px
    :align: center
|   


**Lưu ý**: *Cuốn sách này sẽ sử dụng OhStem App để hướng dẫn lập trình. Các môi trường lập trình còn lại sẽ được hướng dẫn trong các tài liệu khác.*

3.2 Download và cài đặt phần mềm OhStem App
---------------------------------------
---------------------------------------

- **Trên máy tính và laptop**

Trên máy tính hoặc laptop, bạn có thể truy cập vào trang web `<https://app.ohstem.vn >`_ để sử dụng phần mềm OhStem App mà không cần download và cài đặt gì khác. 

.. image:: images/xbot_3.4.png
    :width: 600px
    :align: center
|  

**Lưu ý**

    - Trình duyệt hỗ trợ OhStem App tốt nhất: Google Chrome, Microsoft Edge, Cốc Cốc
    - Trình duyệt không hỗ trợ: Firefox, Opera,...
    - Phải có kết nối Bluetooth


**Trên máy tính bảng và điện thoại**

Tìm và cài đặt ứng dụng **OhStem App** có trên Play Store của Android hoặc App Store của iOS.

.. image:: images/xbot_3.5.png
    :width: 400px
    :align: center
| 

3.3 Giao diện lập trình kéo thả của OhStem App
------------------------------------------
------------------------------------------

Chọn menu lập trình để vào giao diện lập trình cho xBot.

.. image:: images/xbot_3.6.png
    :width: 800px
    :align: center
|  

Các thành phần của giao diện lập trình này sẽ được giải thích chi tiết ở các phần tiếp theo.

    **3.3.1 Danh mục khối lệnh**

Đây là khu vực chứa các nhóm khối lệnh, với nhiều màu sắc khác nhau cho từng nhóm, giúp chúng ta dễ dàng tìm được khối lệnh cần sử dụng khi cần.

.. image:: images/xbot_3.7.png
    :width: 800px
    :align: center
   
.. image:: images/xbot_3.8.png
    :width: 800px
    :align: center

.. image:: images/xbot_3.9.png
    :width: 800px
    :align: center

.. image:: images/xbot_3.10.png
    :width: 800px
    :align: center
|

Ngoài ra còn có một số khối lệnh nâng cao khác sẽ được nhắc đến trong bài sau.

.. image:: images/xbot_3.11.png
    :width: 400px
    :align: center
|   

    **3.3.2 Vùng viết chương trình**

Đây là **nơi chúng ta lắp ghép các khối lệnh với nhau** và tạo thành chương trình.

Bạn có thể kéo và di chuyển, phóng to, thu nhỏ các khối lệnh.

    **3.3.3 Chế độ lập trình**

OhStem App hỗ trợ 2  chế độ lập trình là: **lập trình kéo thả khối lệnh** và **lập trình bằng code** với ngôn ngữ MicroPython.

.. image:: images/xbot_3.12.png
    :width: 800px
    :align: center
|    

    **3.3.4 Các nút chức năng**

.. image:: images/xbot_3.13.png
    :width: 800px
    :align: center
|   

3.4 Thao tác làm việc với khối lệnh
-------------------------------
------------------------------

- **Kết nối các khối lệnh**

.. image:: images/xbot_3.14.png
    :width: 800px
    :align: center
| 
.. image:: images/xbot_3.15.png
    :width: 800px
    :align: center
| 

- **Xóa khối lệnh**

    + Trên máy tính, laptop

        1. Di chuyển chuột đến khối lệnh

        2. Nhấp chuột phải (hiển thị bảng tùy chọn)

        3. Chọn **Xóa mảnh này**

.. image:: images/xbot_3.16.png
    :width: 400px
    :align: center
|   
    + Xóa trên thiết bị di động

        1. Nhấn giữ khối lệnh để chờ bảng tùy chọn hiện ra.

        2. Chọn **Xóa mảnh này**

.. image:: images/xbot_3.17.png
    :width: 400px
    :align: center
|   

- **Xóa nhiều khối lệnh bằng khối lệnh cha**

    1. Để xóa được nhiều khối lệnh, các khối lệnh cần nằm trong khối lệnh cha

    2. Khi **xóa khối lệnh cha, các khối lệnh con sẽ bị xóa theo** (bảng tùy chọn sẽ hiển thị số mảnh sẽ bị xóa)

.. image:: images/xbot_3.18.png
    :width: 400px
    :align: center
|   
- **Xóa nhiều khối lệnh bằng cách kéo thả**

    1. Nhấp giữ nhóm khối lệnh và kéo vào danh mục khối lệnh

.. image:: images/xbot_3.19.png
    :width: 400px
    :align: center
| 

    2. Thả ra để xóa nhóm khối lệnh

.. image:: images/xbot_3.20.png
    :width: 400px
    :align: center
|   

- **Sao chép khối lệnh**

Để rút ngắn thời gian viết chương trình, bạn nên sử dụng **chức năng sao chép cho những khối lệnh cần lặp lại nhiều lần**.

Tương tự như xóa khối lệnh, bạn chọn khối lệnh và click chuột phải, chọn Tạo bản sao.

.. image:: images/xbot_3.21.png
    :width: 400px
    :align: center
|    
Bên cạnh đó, để tạo bản sao cho nhiều khối lệnh, các khối lệnh cần nằm trong khối lệnh cha, khi đó ta sao chếp khối lệnh cha sẽ sao chép luôn tất cả các khối lệnh con có trong đó:

.. image:: images/xbot_3.22.png
    :width: 400px
    :align: center
| 

- **Cách chạy và dùng chương trình**

Sau khi viết chương trình xong, bạn có thể gửi chương trình qua xBot để chạy bằng cách nhấn vào nút Chạy.

Khi chương trình đang chạy, nếu bạn muốn dừng lại hãy nhấn vào nút Dừng.

**Lưu ý:** Bạn cần kết nối với xBot trước khi chạy chương trình. Hướng dẫn ở bài tiếp theo.




















