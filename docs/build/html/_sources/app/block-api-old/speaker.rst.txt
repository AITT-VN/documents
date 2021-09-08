Loa tích hợp
=============================================

Chức năng chính của loa tích hợp

.. function:: speaker.play(BIRTHDAY)
----------------------

Phát một bài hát như được lựa chọn trong danh sách có sẵn.

.. image:: images/speaker-1.png
    :width: 480
    :align: center


.. function:: speaker.play(BIRTHDAY, wait=True)
----------------------

Phát một bài hát như được lựa chọn trong danh sách có sẵn và chờ đến khi bài hát kết thúc.

.. image:: images/speaker-2.png
    :width: 480
    :align: center


.. function:: speaker.play(['C3:1'], wait=True)
----------------------

Phát một nốt nhạc với độ dài nhất định theo nhạc lý.

.. image:: images/speaker-3.png
    :width: 480
    :align: center


.. function:: speaker.pitch(frequency, time)
----------------------

.. image:: images/speaker-4.png
    :width: 480
    :align: center

Phát 1 âm thanh với tần số và độ dài truyền vào, trong đó:
    
    - *frequency* : Dữ liệu số, tần số âm thanh được phát và phạm vi giá trị của nó là ``0 ~ 5000``.
    - *time*: Tính theo ``giây``.

.. function:: speaker.stop()
----------------------

.. image:: images/speaker-5.png
    :width: 480
    :align: center

Dừng chơi nhạc.

Ví dụ
----------------------
Phát bài Happy Birthday khi nhấn giữ nút trên xController

.. image:: images/speaker-6.png
    :width: 500
    :align: center
