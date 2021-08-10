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
        - *tune* : Có thể là 1 trong các bài hát hoặc một tone nhjac nào đó:
            + *Bài hát* : ``BIRTHDAY, TWINKLE, JINGLE_BELLS, WHEEL_ON_BUS, FUR_ELISE,CHASE,JUMP_UP,jUMP_DOWN,POWER_UP,POWER_DOWN``
            + *Tone* : 
                ['C4', '4'], ['C4', '2'], ['C4', '1'], ['C4', '0.5'], ['C4', '0.25'], 
                ['B3', '4'], ['B3', '2'], ['B3', '1'], ['B3', '0.5'], ['B3', '0.25'],
                ['BB3', '4'], ['BB3', '2'], ['BB3', '1'], ['BB3', '0.5'], ['BB3', '0.25'],
                ['A3', '4'], ['A3', '2'], ['A3', '1'], ['A3', '0.5'], ['A3', '0.25'],
                ['AB3', '4'], ['AB3', '2'], ['AB3', '1'], ['AB3', '0.5'], ['AB3', '0.25'],
                ['G3', '4'], ['G3', '2'], ['G3', '1'], ['G3', '0.5'], ['G3', '0.25'],
                ['GB3', '4'], ['GB3', '2'], ['GB3', '1'], ['GB3', '0.5'], ['GB3', '0.25'],
                ['F3', '4'], ['F3', '2'], ['F3', '1'], ['F3', '0.5'], ['F3', '0.25'],
                ['E3', '4'], ['E3', '2'], ['E3', '1'], ['E3', '0.5'], ['E3', '0.25'],
                ['EB3', '4'], ['EB3', '2'], ['EB3', '1'], ['EB3', '0.5'], ['EB3', '0.25'],
                ['D3', '4'], ['D3', '2'], ['D3', '1'], ['D3', '0.5'], ['D3', '0.25'],
                ['DB3', '4'], ['DB3', '2'], ['DB3', '1'], ['DB3', '0.5'], ['DB3', '0.25'],
                ['C3', '4'], ['C3', '2'], ['C3', '1'],  ['C3', '0.5'], ['C3', '0.25'], 
        - *wait* : Nếu bằng ``True`` thì sẽ phát hết bài hát mới kết thúc hàm. Mặc định nếu không ghi thì là ``False``.
        - *loop* :
        - *duration* :

.. function:: speaker.pitch(frequency, time)
    Phát 1 âm thanh với tần số và độ dài truyền vào, trong đó:
        - *frequency* : Dữ liệu số, tần số âm thanh được phát và phạm vi giá trị của nó là ``0 ~ 5000``.
        - *time*: Tính theo ``giây``.


Sample Code：
----------------------
Phát bài Happy Birthday khi nhấn giữ nút trên xController

.. code-block:: python

    while True:
        if btn_onboard.is_pressed():
            speaker.play(BIRTHDAY)
        else:
            speaker.stop()
