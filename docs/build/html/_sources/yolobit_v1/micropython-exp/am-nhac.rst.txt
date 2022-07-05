Âm nhạc
=============================================


MicroPython trên Yolo:Bit cung cấp đi kèm một thư viện rất thú vị để làm việc với loa có sẵn trên Yolo:Bit để phát ra âm nhạc.

Chúng ta hãy thử phát ra một bài nhạc nào:

.. code-block:: python

  import music

  music.play(music.NYAN)

Bạn để ý thấy để làm việc với âm nhạc, ta sử dụng thư viện music bằng câu lệnh import. Trong thư viện này, ta dùng hàm ``play()`` để chơi một bài nhạc. Sau đây là danh sách các bài nhạc có sẵn trong Yolo:Bit:

  - music.DADADADUM
  - music.ENTERTAINER
  - music.PRELUDE
  - music.ODE
  - music.NYAN
  - music.RINGTONE
  - music.FUNK
  - music.BLUES
  - music.BIRTHDAY
  - music.WEDDING
  - music.CHASE
  - music.JUMP_UP
  - music.JUMP_DOWN
  - music.POWER_UP
  - music.POWER_DOWN

Ngoài ra, bạn cũng có thể dễ dàng chơi các nốt nhạc để tạo thành một bản nhạc theo ý muốn. Các nốt nhạc được đặt tên theo ký tự như sau: C (Đồ), D (Rê), E (Mi), F (Fa), G (Son), A (La), B (Si).

Ngoài ra, mỗi nốt nhạc còn có quãng tám octave, chấp nhận các giá trị là từ 1 đến 8 và độ dài chấp nhận một trong các giá trị 0.25, 0.5, 1, 2, 4, 8.

Mỗi nốt nhạc được viết như sau: ``NOTE[octave]:[duration]``.

Ví dụ nốt nhạc “A4:4” là nốt La quãng trung có độ dài là 4. Dựa theo đó, bạn thử chạy chương trình này và đoán xem bài gì nhé:

.. code-block:: python

  import music

    tune = [“C4:4”, “D4:4”, “E4:4”, “C4:4”, “C4:4”, “D4:4”, “E4:4”, “C4:4”,

            “E4:4”, “F4:4”, “G4:8”, “E4:4”, “F4:4”, “G4:8”]

    music.play(tune)

**Hiệu ứng âm thanh**

Không chỉ phát ra các nốt nhạc, thư viện music của MicroPython trên Yolo:Bit còn có thể phát ra các âm thanh ở các tần số khác nhau, giúp chúng ta phát ra được những hiệu ứng âm thanh theo ý muốn.

Ví dụ nếu ta muốn phát ra âm thanh hú còi báo động giống của cảnh sát:

.. code-block:: python

  import music

    while True:

        for freq in range(880, 1760, 16):

            music.pitch(freq, 100)

        for freq in range(1760, 880, -16):

            music.pitch(freq, 100)

Hàm ``music.pitch()`` nhận đầu vào là tần số của âm thanh cần phát và độ dài. Nốt A (La) quãng trung có tần số khoảng 440.

Trong chương trình trên, ta dùng hàm ``range()`` của MicroPython để tạo ra một danh sách các tần số theo thông tin truyền vào. Hàm này nhận 3 thông tin truyền vào là số bắt đầu, số kết thúc và giá trị mỗi lần tăng hoặc giảm (nếu là số âm).

Câu lệnh ``range(880, 1760, 16)`` ý nghĩa là yêu cầu MicroPython tạo ra một dãy các số bắt đầu từ 880 và kết thúc ở 1760 với bước nhảy là 16.

Sau khi tạo ra dãy số, chúng ta dùng vòng lặp for để lặp qua từng con số trong dãy số được tạo ra và dùng hàm music.pitch để phát ra âm thanh có tần số bằng với số đang được lặp qua trong dãy số đó.

Làm việc với âm nhạc trong Yolo:Bit thật dễ dàng phải không các bạn.