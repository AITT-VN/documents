:mod:`speaker` --- Speaker
=============================================

.. module:: speaker
    :synopsis: Speaker

Chức năng chính và chức năng của ``speaker``

Function
----------------------

speaker.stop()
     Dừng chơi nhạc.

speaker.play(tune, wait=False, loop=False, duration=None)
     Phát 1 bài nhạc hoặc 1 nốt nhạc. Trong đó:
         Danh sách bài hát: BIRTHDAY, TWINKLE, JINGLE_BELLS, WHEEL_ON_BUS, FUR_ELISE,CHASE,JUMP_UP,jUMP_DOWN,POWER_UP,POWER_DOWN.
         wait: Nếu bằng True thì sẽ phát hết bài hát mới kết thúc hàm.

speaker.pitch(frequency, time)
     Phát 1 âm thanh với tần số và độ dài truyền vào.


Sample Code：
----------------------
Phát bài Happy Birthday khi nhấn giữ nút trên xController

.. code-block:: python

    while True:
        if btn_onboard.is_pressed():
            speaker.play(BIRTHDAY)
        else:
            speaker.stop()
