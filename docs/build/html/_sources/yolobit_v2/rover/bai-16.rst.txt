19. Bài 16: Lập trình AI - Điều khiển bằng giọng nói
==============================================

Mục tiêu
--------------
------------------------

1. Làm quen với khái niệm trí tuệ nhân tạo (AI) và công nghệ nhận dạng giọng nói
2. Ứng dụng lập trình nhận dạng giọng nói.

.. image:: images/bai_16.1.png
    :width: 300px
    :align: center   
|

Giới thiệu về AI
------------
--------------------

- Trí thông minh nhân tạo AI là công nghệ mô phỏng những suy nghĩ, quá trình tiếp thu kiến thức của con người cho máy móc 

.. image:: images/bai_16.2.png
    :width: 800px
    :align: center   
|
- Có khả năng nhận dạng và chuyển đổi giọng nói của con người thành văn bản để xử lý

.. image:: images/bai_16.3.png
    :width: 200px
    :align: center   
|
- Các ứng dụng của nhận dạng giọng nói:

.. image:: images/bai_16.4.png
    :width: 500px
    :align: center  
|

Môi trường lập trình trên OhStem App 
--------------
-------------------

- Trong giao diện chính của OhStem App, chúng ta chọn tiếp vào phần **Lập trình AI**, như hướng dẫn ở hình sau đây:

.. image:: images/bai_16.5.png
    :width: 800px
    :align: center  
|
- Giao diện lập trình kéo thả sau đây sẽ hiện ra, với khối lệnh đặt trưng **bắt đầu ...lặp mãi mãi** cho các ứng dụng của chúng ta.

.. image:: images/bai_16.6.png
    :width: 500px
    :align: center
|

Giới thiệu khối lệnh
------------
------------------------

- Khối lệnh nhận dạng giọng nói: Bật chức năng chuyển đổi giọng nói thành văn bản (Text to speech - TTS).

.. image:: images/bai_16.7.png
    :width: 500px
    :align: center
|
- Khối lệnh so sánh kết quả nhận nhận diện giọng nói với các từ được nhập vào

.. image:: images/bai_16.8.png
    :width: 500px
    :align: center
|
- Khối lệnh đọc kết quả nhận diện giọng nói

.. image:: images/bai_16.9.png
    :width: 500px
    :align: center
|

Nhận dạng giọng nói và in kết quả ra màn hình:
------------------------------------------------
------------------------------------

    .. image:: images/bai_16.10.png
        :width: 400px
        :align: center
    |
    - Tại giao diện **Lập trình AI**. Xây dựng chương trình hiển thị kết quả giọng nói.
 
        .. image:: images/bai_16.11.png
            :width: 800px
            :align: center

        - Câu lệnh **đổi màu hình nền** sang màu trắng, có tác dụng xóa xóa kết quả nhận dạng trước đó, để việc hiển thị kết quả tiếp theo không bị che mất. 
        |
        - Chạy chương trình và quan sát kết quả: 

        .. image:: images/bai_16.png
            :width: 300px
            :align: center
    |

Điều khiển robot bằng giọng nói 
-------------------
------------------------

**Phần 1: Gửi lệnh cho Robot**

*Lập trình để nhận dạng giọng nói và gửi lệnh đến robot*

    1. Xây dựng câu lệnh bắt từ khóa 

        .. image:: images/bai_16.12.png
            :width: 500px
            :align: center

        - Khi bắt được từ lệnh đi thẳng, chúng ta sẽ gửi một **mã lệnh** tới mạch Yolo:Bit đang kết nối, là số 1 cho đơn giản. Câu lệnh để bắt từ khóa (**kết quả có chứa**) nằm trong nhóm **GIỌNG NÓI**. Câu lệnh gửi **1 tới thiết bị đang kết nối** nằm trong nhóm **GIAO TIẾP**.
    |
    2. Hoàn thiện chương trình nhận dạng giọng nói

        - Tiếp tục nhân bản toàn bộ câu lệnh ở bước trên, và ghép nó vào vị trí thích hợp để hoàn thiện chương trình như sau:

        .. image:: images/bai_16.13.png
            :width: 800px
            :align: center
    |

**Phần 2: Robot nhận lệnh**

*Lập trình để robot hoạt động theo lệnh nhận được*

    1. Chuyển sang giao diện **Lập trình thiết bị**

        .. image:: images/bai_16.14.png
            :width: 800px
            :align: center
    |
    2. Bắt đầu với một vài hiệu ứng trước khi vào khối lặp lại mãi mãi, như sau:

        .. image:: images/bai_16.15.png
            :width: 300px
            :align: center 
    |
    3. Khai báo biến **Lệnh AI** để đọc và lưu lại lệnh được gửi tới robot.

        .. image:: images/bai_16.16.png
            :width: 300px
            :align: center 
    |   
    4. Đọc lệnh AI từ cửa sổ nhập lệnh. Liên tục đọc lệnh do chương trình AI gửi tới ở cửa sổ nhập lệnh  

        .. image:: images/bai_16.17.png
            :width: 1200px
            :align: center 
    |
    5. Xây dựng phép so sánh chuỗi 

    .. image:: images/bai_16.18.png
        :width: 400px
        :align: center    
    |
    6. Nhân bản câu lệnh so sánh chuỗi và ghép nối lại chương trình để có được cấu trúc chương trình như sau:

    .. image:: images/bai_16.19.png
        :width: 700px
        :align: center        
    |
    7. Hoàn thiện chương trình bằng ghép nối cái câu lệnh di chuyển tương ứng.

    .. image:: images/bai_16.20.png
        :width: 800px
        :align: center    
    |

Lưu chương trình vào Yolo:Bit 
-------------------
------------------------

Sau khi biên soạn chương trình xong, chương trình cần được lưu cố định vào Yolo:Bit. Điều này sẽ rất cần thiết cho việc kết nối ổn định giữa xBot và chương trình AI về sau. 

1. Lưu chương trình vào Yolo:Bit Rover

    .. image:: images/bai_16.21.png
        :width: 300px
        :align: center
    |
2. Reset lại Yolo:Bit

3. Mở chương trình AI, kết nối với Yolo:Bit Rover

4. Chạy chương trình AI


Chương trình mẫu
-------------------
------------------------

- Điều khiển robot bằng giọng nói: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BepIuCggBc71rsRElGOHpOq0DI>`_

.. image:: images/bai_16.22.png
    :width: 200px
    :align: center 