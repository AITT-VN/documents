9. Bài 7: Còi báo
========================================

Giới thiệu
--------
-----------

- **Còi báo** (Buzzer) hay còn gọi là **còi chíp hoặc còi xung**, là một loại thiết bị có thể phát ra âm báo hay dùng trong các mạch điện tử. 

    .. image:: images/7.1.png
        :width: 300px
        :align: center 
    |
- **Giới thiệu về MOSFET**

    - **MOSFET** là một linh kiện đóng vai trò như một công tắc điện tử để bật tắt dòng điện. 3 chân của **MOSFET** gồm:

        - G (gate) gọi là cực cổng.
        - D (drain) gọi là cực máng.
        - S (source) gọi là cực nguồn.

    - Nguồn không đủ mạnh để buzzer phát ra âm thanh to và rõ nên nguồn được cấp cho buzzer là nguồn trực tiếp từ cực dương (3V) và cực âm (GND) của nguồn điện. **“Công tắc MOSFET”** được sử dụng giúp ta có thể điều khiển buzzer bật tắt tùy ý bằng cách bật hoặc tắt dòng điện đi qua buzzer.

    .. image:: images/7.2.png
        :width: 400px
        :align: center 
    |

Xây dụng mạch điện 
------------
-----------

- **Thành phần:**

    - Nguồn điện 3V.
    - Điện trở R1 100 Ω. 
    - Còi báo SG1.
    - MOSFET.

- **Sơ đồ mạch điện**

    .. image:: images/bai_7.1.png
        :width: 500px
        :align: center 
    |
- **Nguyên lý hoạt động:**

    MOSFET được điều khiển bởi chân P0. Khi P0 bật, MOSFET đóng, dòng điện đi từ 3V qua buzzer xuống GND, tạo thành mạch điện kín giúp buzzer phát ra âm thanh. Ngược lại khi P0 tắt, MOSFET mở, không có dòng điện chạy qua nên buzzer không hoạt động.


Kết nối mạch điện 
-----------
-------------

Hãy kết nối mạch điện như hình minh họa: 

    .. image:: images/bai_7.2.png
        :width: 500px
        :align: center 
    |

Chương trình
---------
-----------------

Thực hiện chương trình như sau: 

    .. image:: images/bai_7.5.png
        :width: 1000px
        :align: center 
    |

Kết quả
----------
---------------

Kết quả của chương trình: 

    .. image:: images/bai_7.6.png
        :width: 600px
        :align: center 
    |

Có thể bạn chưa biết?
-----------
-------------------

Có 2 loại buzzer là buzzer chủ động (active) và buzzer bị động (passive). Buzzer chủ động chỉ cần được cấp điện sẽ phát ra âm thanh. Khác với buzzer chủ động, nguồn cấp cho buzzer bị động phải là một tín hiệu xung. Ứng với xung có tần số khác nhau, buzzer bị động sẽ phát ra âm thanh có cao độ khác nhau, nhờ đặc điểm này, ta có thể điều khiển buzzer bị động phát ra các giai điệu nhạc bằng cách thay đổi tần số xung cấp cho buzzer. Buzzer có trên Phys:Bit là loại active.


Chương trình mẫu
--------------
-------------------

- Còi báo: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BvkOBTKhIH2f6MAYcLjNrcfEiH>`_

.. image:: images/bai_7.7.png
    :width: 200px
    :align: center 


