**Camera AI**
=============

1. Giới thiệu
----------
----------

.. image:: images/camera_ai_1.png
    :scale: 100%
    :align: center
|  
Bộ kit Camera AI là một công cụ thú vị dùng để truyền hình ảnh và video từ camera. Bạn có thể sử dụng nó để xử lý thông tin và chạy các mô hình trí tuệ nhân tạo từ Google Teachable Machine. 

Bộ kit này thường được dùng trong các dự án STEM và Robotics để giúp robot nhận biết hình ảnh, nhận diện khuôn mặt và thực hiện nhiều công việc khác nhau. Ngoài ra, bạn cũng có thể ứng dụng bộ kit vào các sản phẩm sáng tạo như hệ thống phân loại rác, hoặc mô hình nhà thông minh cảnh báo khi có người lạ xuất hiện… Dưới đây là hướng dẫn cách sử dụng Camera AI.

..  image:: images/gio.png
    :alt: some image
    :target: https://shop.ohstem.vn/san-pham/esp32-camera/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**Các bước làm việc với Camera AI:**

1. Cài đặt phần mềm Esptouch để cấu hình wifi cho camera
2. Tạo các trường dữ liệu
3. Nhận dạng qua camera

2. Cài đặt phần mềm Esptouch cấu hình wifi cho camera
---------
-----

1. Cấp nguồn cho Camera

2. Truy cập vào Google Play hoặc App Store và cài đặt app **Esptouch** như hình: 

.. image:: images/camera_ai_2.png
    :scale: 100%
    :align: center
|  

3. Sau khi hoàn tất cài đặt, truy cập vào app và chọn EspTouch như hình: 

.. image:: images/camera_ai_3.png
    :scale: 80%
    :align: center
|  

4. Điền **mật khẩu wifi** như hình bên dưới và chọn **START** để hoàn tất việc cấu hình wifi cho camera. 
    
**Lưu ý**: 
    - Bạn cần bật vị trí và cho phép app truy cập vào vị trí của bạn.
    - Sử dụng wifi có băng tần 2.4G

.. image:: images/camera_ai_4.png
    :scale: 100%
    :align: center
|  

5. **Lấy địa chỉ camera**: 
    Sau khi đã gửi tín hiệu cấu hình đi, bạn vui lòng chờ trong giây lát, sẽ có 1 thông báo hiện ra như hình và ghi chú lại địa chỉ IP:
    (Nếu thay đổi mạng wifi, bạn cần thực hiện các thao tác trên)

.. image:: images/camera_ai_5.png
    :scale: 100%
    :align: center
| 

6.  Truy cập vào trình duyệt Google Chrome/ Microsoft Edge…  nhập địa chỉ của Camera vào thanh tìm kiếm, giao diện sau sẽ xuất hiện.:

    Các trường dữ liệu mà bạn cần quan tâm là:

    - Đường dẫn AI
    - Username
    - Kênh dữ liệu

.. image:: images/camera_ai_6.png
    :scale: 100%
    :align: center
| 

3. Tạo các trường dữ liệu:
---------
-----

**3.1. Tạo đường dẫn AI:**
---------

Ở phần đường dẫn AI này, chúng tra sẽ cần dùng 1 công cụ tạo mô hình AI của Google:

1. Truy cập vào trang web: `<https://teachablemachine.withgoogle.com/>`_ và chọn **Get Started**:

.. image:: images/camera_ai_7.png
    :scale: 100%
    :align: center
|

2. Giao diện sẽ hiện ra như hình chọn vào **Image Project**:

.. image:: images/camera_ai_8.png
    :scale: 100%
    :align: center
|

3. Chọn tiếp vào **Standard image model**: 

.. image:: images/camera_ai_9.png
    :scale: 100%
    :align: center
|

    Giao diện được hiển thị tương tự với giao diện Mô hình AI trên OhStem App

.. image:: images/camera_ai_10.png
    :scale: 100%
    :align: center
|   

4. **Huấn luyện mô hình AI**:

Chọn vào **Webcam** và nhấn **Hold to Record** để thu thập mẫu. Sau khi hoàn tất, chọn **Train Model**

.. image:: images/camera_ai_20.jpg
    :scale: 100%
    :align: center
| 

5. Chọn **Export Model** để xuất ra mô hình:

.. image:: images/camera_ai_11.png
    :scale: 100%
    :align: center
| 

6. Sau đó bạn ấn vào chọn **Upload my model**:

.. image:: images/camera_ai_12.png
    :scale: 100%
    :align: center
| 

7. Một đường link sẽ xuất hiện, hãy **sao chép và dán vào đường dẫn AI trên trang địa chỉ của camera**: 

.. image:: images/camera_ai_13.png
    :scale: 100%
    :align: center
| 

8. Kết quả như hình: 

.. image:: images/camera_ai_14.png
    :scale: 100%
    :align: center
| 

**3.2. Username và kênh dữ liệu:**
---------

1. **Tạo kênh dữ liệu:**

    Truy cập vào `<https://app.ohstem.vn/>`_, chọn Bảng điều khiển IoT và tạo một bảng điều mới, đặt lại Username và chọn kênh thông tin.  Đây là 2 thông tin quan trọng của server MQTT. 

.. image:: images/camera_ai_15.png
    :scale: 100%
    :align: center
| 

2. **Điền thông tin Username và kênh dữ liệu vào trang địa chỉ của camera**, kết quả như hình: 
    
    Username bạn cần đặt giống như username bạn cấu  hình trên bảng điều khiển thông  tin. Kênh dữ liệu sẽ gồm từ V1 đến V20 theo đúng như ta đã cấu hình trên bảng điều khiển IoT.
 
.. image:: images/camera_ai_16.png
    :scale: 100%
    :align: center
|


4. Bắt đầu nhận dạng qua camera
-------
-----------

Sau khi đã điền xong các thông tin, bạn ấn **Bắt đầu nhận dạng** 

.. image:: images/camera_ai_17.png
    :scale: 100%
    :align: center
|

Lúc này camera sẽ tiến hành khởi chạy, trong thời gian sử dụng camera, bạn không được ẩn Tab đi, luôn luôn phải được chạy trên trình duyệt (mẹo nhỏ: bạn có thể kéo trang camera làm 1  cửa sổ riêng và thu nhỏ  lại)

Camera nhận diện sẽ có các thông số như sau : 

.. image:: images/camera_ai_18.png
    :scale: 100%
    :align: center
|

Ở phần Result sẽ là kết quả mà  AI nhận dạng được và độ tin cậy của kết quả, kết quả sẽ được gửi lên trực tiếp server IoT của OhStem

.. image:: images/camera_ai_19.png
    :scale: 100%
    :align: center
|

Sau đó chúng ta chỉ cần xử lý chương trình nhận lệnh từ IoT là có thể hoàn thành.