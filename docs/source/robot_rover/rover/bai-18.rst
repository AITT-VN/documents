21. Bài 18: Điều khiển và giám sát robot qua IoT
========================================

Mục tiêu:
--------------
-------------------

1. Làm quen với khái niệm Internet vạn vật (IoT), WiFi và MQTT
2. Thực hành lập trình có thể điều khiển và giám sát các hoạt động và trạng thái của robot qua Internet 

    .. image:: images/bai_18.1.png
        :width: 300px
        :align: center     
    |

Giới thiệu về công nghệ IoT, WiFi và MQTT  
--------------
-----------------

- **Công nghệ IoT:** IoT (Internet vạn vật) là mạng kết nối hàng tỷ thiết bị trên khắp thế giới qua Internet
     
    - Xây dựng thành phố thông minh:

    .. image:: images/bai_18.2.png
        :width: 200px
        :align: center     
    |
    - Internet công nghiệp:

    .. image:: images/bai_18.3.png
        :width: 200px
        :align: center     
    |
    - Hỗ trợ nông nghiệp và nhiều ứng dụng khác 

    .. image:: images/bai_18.3.1.png
        :width: 200px
        :align: center     
    |    

- **Kết nối WiFi trong IoT:** Có vai trò cực kỳ quan trọng trong IoT, là công nghệ chính để truyền dữ liệu trong hệ thống IoT

    .. image:: images/bai_18.5.png
        :width: 300px
        :align: center     
    |

- **Giao thức MQTT:** Là giao thức truyền thông tin nhẹ và nhanh giữa các thiết bị, phù hợp cho các thiết bị IoT

    - Gồm 2 phần chính: Broker (Server) và các Clients (thiết bị hay máy tính)

    - Client có thể publish các message lên một topic cụ thể hoặc subscribe một topic nào đó để nhận message từ topic này

    .. image:: images/bai_18.6.png
        :width: 900px
        :align: center     
    |


Giới thiệu khối lệnh
--------------
---------------------

- Tải thư viện lập trình MQTT trên OhStem App:

    1. Trong danh mục khối lệnh, chọn vào khối **MỞ RỘNG** để mở các thư viện mở rộng, như minh họa ở hình dưới:

    .. image:: images/bai_18.7.png
        :width: 600px
        :align: center     
    |
    2. Nhập từ khóa MQTT vào ô tìm kiếm, sau đó nhấn Enter. Kết quả của việc tìm kiếm sẽ xuất hiện như hình:

    .. image:: images/bai_18.8.png
        :width: 400px
        :align: center     
    |
    3. Nhấn vào MQTT để thêm thư viện. Khi thông báo sau đây xuất hiện, bạn chọn OK.

    .. image:: images/bai_18.9.png
        :width: 300px
        :align: center     
    | 
    Phần mềm sẽ yêu cầu bạn kết nối với mạch Yolo:Bit, tuy nhiên, bạn có thể bỏ qua bước này. Sau đó, chúng ta sẽ có một nhóm khối lệnh mới như hình:

    .. image:: images/bai_18.10.png
        :width: 600px
        :align: center     
    | 

- **Các khối lệnh trong MQTT**:

    - Khối lệnh kết nối vào mạng WiFi (bạn cần nhập tên và mật khẩu WiFi)

    .. image:: images/bai_18.11.png
        :width: 800px
        :align: center     
    |
    - Khối lệnh kết nối đến chương trình điều khiển với username và key đã đặt ở bảng giám sát

    .. image:: images/bai_18.12.png
        :width: 800px
        :align: center     
    |
    - Khối lệnh đăng ký nhận thông tin gửi vào chủ đề (thường là nhận lệnh từ bảng điều khiển Dashboard)

    .. image:: images/bai_18.13.png
        :width: 800px
        :align: center     
    |   


Tạo bảng điều khiển IoT (Dashboard)
-------------
------------------

1. Tại giao diện chính của OhStem App, chọn **Bảng điều khiển IoT**

    .. image:: images/bai_18.14.png
        :width: 800px
        :align: center     
    |  
2. Chọn **Tạo mới**

    .. image:: images/bai_18.15.png
        :width: 300px
        :align: center     
    |
3. Kéo thả và sắp xếp các công cụ điều khiển (widget) theo ý muốn

    .. image:: images/bai_18.16.png
        :width: 300px
        :align: center     
    |

**Giao diện cấu hình bảng điều khiển IoT**

    .. image:: images/bai_18.17.png
        :width: 900px
        :align: center     
    |


Điều khiển đổi màu Rover từ Internet
-------------------
--------------------

**Yêu cầu:** Cấu hình Color Picker để bật tắt đèn LED trên Rover

**Cấu hình bảng điều khiển IoT**

    1. Trong giao diện bảng điều khiển IoT, kéo thả Color Picker ra ngoài 

    .. image:: images/bai_18.18.png
        :width: 200px
        :align: center     
    |
    2. Nhấn vào Color Picker và cấu hình kênh là V1.

    .. image:: images/bai_18.19.png
        :width: 400px
        :align: center     
    |
    3. Nhấn nút Play để chuyển về chế độ điều khiển 

    .. image:: images/bai_18.20.png
        :width: 400px
        :align: center     
    |

**Lập trình và nạp vào robot Rover:**

    1. Kết nối vào mạng WiFi. Đây là bước đầu mà chúng ta cần làm để thiết bị có thể kết nối với Internet. Cũng giống như máy tính, việc kết nối với mạng WiFi bất kỳ chỉ cần được thực hiện một lần. Do đó, chúng ta sẽ lập trình tính năng này trong phần **bắt đầu** của chương trình.

    .. image:: images/bai_18.21.png
        :width: 700px
        :align: center     

    **Lưu ý:** Trong câu lệnh này, bạn cần cung cấp đúng 2 thông tin là tên và mật khẩu của WiFi cho Yolo:Bit.
    

    2. Sau khi kết nối với mạng WiFi, chúng ta sẽ lập trình để Yolo:Bit kết nối với server OhStem mà chúng ta đã tạo trước đó, thông qua 2 thông tin là Username và key sẽ bỏ trống.

        - Với Username lấy trong bảng điều khiển IoT
    
    .. image:: images/bai_18.22.png
        :width: 800px
        :align: center     
    |
    3. Cuối cùng cần đăng ký nhận thông tin gửi vào chủ đề - topic đã cấu hình trước đó. Ở đây cấu hình đã chọn cho Color Picker trước đó là V1. 

    **Lưu ý:** Cần ghi đúng chính xác tên của chủ đề. 

    .. image:: images/bai_18.23.png
        :width: 800px
        :align: center     

    Mỗi khi nút nhấn trên Dashboard được nhấn, dữ liệu sẽ được tự động lưu lại trong biến **thông tin**. Phần hướng dẫn này sẽ được trình bày ở các phần sau.
    

    4. Liên kết định kỳ đến Server.

    Sau các bước cấu hình ở trên, chúng ta cần phải tạo một liên kết định kì với Server. Việc này được thực hiện lặp đi lặp lại liên tục, nên chúng ta cần phải hiện thực nó trong khối **lặp lại mãi**, như sau:

    .. image:: images/bai_18.24.png
        :width: 800px
        :align: center     
    |
    Chu kì kiểm tra kết nối với Server mà chúng tôi đề xuất ở đây là 1 giây, tức là 1000ms (sử dụng câu lệnh tạm dừng trong mục CƠ BẢN). Thời gian dừng càng lớn thì việc nhận tín hiệu điều khiển khi nhấn nút sẽ chậm. Tuy nhiên, nếu thời gian dừng nhỏ thì chúng sẽ làm tốn tài nguyên của mạng Internet (do mạch Yolo:Bit phải thường xuyên truy cập và gửi dữ liệu lên Server Adafruit IO). 
    
    Trong các ứng dụng hiện tại, chúng ta nên sử dụng độ trễ 1 giây.
    

    5. Xử ký dữ liệu nhận được từ Server OhStem. Để xử lý dữ liệu nhận được (lưu trong biến thông tin), chúng ta cần phải lập trình trong phần **bắt đầu**.

    Chương trình hoàn chỉnh như sau:

    .. image:: images/bai_18.25.png
        :width: 800px
        :align: center 
    |


Định kỳ cập nhập thông tin lên Server IoT 
----------------
-----------------------

**Yêu cầu:** Định kỳ cập nhật thông tin nhiệt độ, ánh sáng từ Rover lên Server IoT (bảng điều khiển)

**Cấu hình bảng điều khiển IoT**
   
    1. Kéo Widget thông tin ra ngoài 

    .. image:: images/bai_18.26.png
        :width: 200px
        :align: center 
    |
    2. Đặt tên, cấu hình kênh V2 và chọn cách hiển thị

    .. image:: images/bai_18.27.png
        :width: 300px
        :align: center 
    |
    3. Thực hiện tương tự với ánh sáng (V3)

    .. image:: images/bai_18.28.png
        :width: 400px
        :align: center 
    |    

**Thư viện sự kiện**

    1. Chọn Mở rộng trong giao diện lập trình thiết bị.

    .. image:: images/bai_18.29.png
        :width: 200px
        :align: center 
    |    
    2. Tải thư viện **SỰ KIỆN** 

    .. image:: images/bai_18.30.png
        :width: 300px
        :align: center 
    |
    3. Tải hoàn tất:

    .. image:: images/bai_18.31.png
        :width: 400px
        :align: center 
    |  

**Lập trình cho Rover như sau:**

    1. Viết chương trình sau mỗi 2 giây thông tin **nhiệt độ** và **mức độ sáng** sẽ được cập nhật lên bảng điều khiển. Chương trình như sau:

    .. image:: images/bai_18.32.png
        :width: 500px
        :align: center 
    | 
    2. Chương trình hoàn chỉnh để gửi thông tin lên bảng điều khiển.

    .. image:: images/bai_18.33.png
        :width: 800px
        :align: center 
    |    


Điều khiển robot qua Internet
--------------
-------------------

**Yêu cầu:** Điều khiển bật / tắt đèn pha 2 bên của robot Rover thông qua bảng điều khiển IoT

**Cấu hình bảng điều khiển IoT**
 
    1. Kéo Widget thông tin ra ngoài 

    .. image:: images/bai_18.34.png
        :width: 200px
        :align: center 
    |
    2. Đặt tên, cấu hình kênh V4.

    .. image:: images/bai_18.35.png
        :width: 200px
        :align: center 
    |
    3. Thực hiện tương tự cho đèn phải (V5)

    .. image:: images/bai_18.36.png
        :width: 400px
        :align: center 
    | 

**Lập trình cho Rover như sau:**

    1. Thêm 2 khối lệnh để đăng ký nhận thông tin từ chủ đề V4 (cho đèn LED bên trái) và V5 (cho đèn LED bên phải)

    .. image:: images/bai_18.37.png
        :width: 800px
        :align: center 
    |
    2. So sánh thông tin nhận được với giá trị kiểu chuỗi “1” và “0” bằng khối lệnh trong mục **Chữ viết**

    .. image:: images/bai_18.42.1.png
        :width: 400px
        :align: center 

    Chương trình hoàn chỉnh như sau:

    .. image:: images/bai_18.38.1.png
        :width: 600px
        :align: center 

    |


Điều khiển di chuyển qua Internet
---------------
----------------

**Yêu cầu:**  Điều khiển robot di chuyển theo các hướng thông qua bảng điều khiển IoT

**Cấu hình bảng điều khiển IoT**

    1. Kéo Widget Joystick ra ngoài

    .. image:: images/bai_18.39.png
        :width: 200px
        :align: center 
    |
    2. Chọn kênh thông tin V6

    .. image:: images/bai_18.40.png
        :width: 500px
        :align: center 
    |

**Lập trình cho Rover như sau:**

    1. Thêm khối lệnh đăng ký nhận thông tin từ chủ đề V6

    .. image:: images/bai_18.41.png
        :width: 700px
        :align: center 
    |
    2. So sánh thông tin nhận được và điều khiển robot tương ứng

    .. image:: images/bai_18.42.png
        :width: 600px
        :align: center 
    |


Chương trình mẫu
------------------
-----------------------

- Điều khiển đèn từ Internet: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BpjCK8aL6kHlNxUIb5GTlCz0Ph>`_

    .. image:: images/bai_18.1.1.png
        :width: 200px
        :align: center 
    |
- Định kỳ cập nhật thông tin lên Server IoT: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BpkqRmUtvGOpKkcMlfMTGBhREV>`_

    .. image:: images/bai_18.1.2.png
        :width: 200px
        :align: center 
    |
- Điều khiển bật / tắt đèn pha 2 bên của robot Rover thông qua bảng điều khiển IoT: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BpmypGiB30iHu4hcK7C9HN4iMr>`_

    .. image:: images/bai_18.1.3.png
        :width: 200px
        :align: center 
    |
- Điều khiển di chuyển qua Internet: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BpoDOSmODzxELqBDkCjHvLwirU>`_

    .. image:: images/bai_18.1.4.png
        :width: 200px
        :align: center 
    |
