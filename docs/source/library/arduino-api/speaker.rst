:mod:`speaker` --- Speaker
=============================================

.. module:: speaker
    :synopsis: Speaker

Chức năng chính và chức năng của ``speaker``

Function
----------------------

.. function:: speaker.stop()

    Dừng chơi nhạc.

.. function:: speaker.play(tune, wait=False, loop=False, duration=None)

    Phát 1 bài nhạc hoặc 1 nốt nhạc. Trong đó:
    
        - *tune* : Có thể là 1 trong các bài hát hoặc một tone nhạc nào đó:
        
            + *Bài hát* : ``BIRTHDAY, TWINKLE, JINGLE_BELLS, WHEEL_ON_BUS, FUR_ELISE,CHASE,JUMP_UP,jUMP_DOWN,POWER_UP,POWER_DOWN``
            + *Tone* : Đây là các nốt trong nhạc lý:

            .. image:: images/speaker.png

        - *wait* : Nếu bằng ``True`` thì sẽ phát hết bài hát mới kết thúc hàm. Mặc định nếu không ghi thì là ``False``.
        - *loop* :
        - *duration* : Thời gian kéo dài.

.. function:: speaker.pitch(frequency, time)

    Phát 1 âm thanh với tần số và độ dài truyền vào, trong đó:
    
        - *frequency* : Dữ liệu số, tần số âm thanh được phát và phạm vi giá trị của nó là ``0 ~ 5000``.
        - *time*: Tính theo ``giây``.


Sample Code
----------------------
Phát bài Happy Birthday khi nhấn giữ nút trên xController

.. code-block:: python

    while True:
        if btn_onboard.is_pressed():
            speaker.play(BIRTHDAY)
        else:
            speaker.stop()
