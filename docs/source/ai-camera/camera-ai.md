# 1. Camera AI

## 1. Giới thiệu
![camera ai](/wiki-assets/images/module/ai-camera/images/camera_v2_1.png)


**Camera AI** (phiên bản V2) là module camera thông minh dùng để thu hình ảnh, video và chạy các mô hình trí tuệ nhân tạo được huấn luyện từ **Google Teachable Machine**. Module giúp robot và các dự án STEM có khả năng "nhìn thấy" và nhận biết được vật thể, khuôn mặt, màu sắc, loại rác… mà không cần lập trình phức tạp.

**Điểm nổi bật:**

- **Thiết kế mới, dễ lắp ráp:** kích thước module chuẩn của hệ sinh thái OhStem, có vỏ nhựa bảo vệ và các lỗ tương thích Lego để lắp ghép với những module khác.
- **Kết nối linh hoạt:** cổng USB Type-C để cấp nguồn và nạp firmware, cổng Grove để xuất kết quả nhận dạng trực tiếp cho mạch điều khiển mà **không cần đi qua server IoT** làm trung gian, giúp ứng dụng ổn định và chạy nhanh hơn.
- **Chip xử lý mới:** ESP32-S3 với tốc độ xử lý AI nhanh gấp đôi camera V1, hỗ trợ WiFi cả 2 băng tần 2.4GHz và 5GHz.

**Một số ứng dụng thường gặp:** hệ thống phân loại rác thải, nhà thông minh cảnh báo người lạ, robot nhận diện và bám theo vật thể, máy bán hàng tự động nhận diện sản phẩm…

**Chưa có module Camera AI?** Bạn vẫn có thể thử nghiệm mô hình AI bằng webcam của laptop/điện thoại với công cụ Camera AI có sẵn trên OhStem App — cách huấn luyện mô hình giống hệt hướng dẫn ở trang này, xem [2. Camera AI với OhStem App](/ai-camera/camera-ai-ohstem-app.md).

## 2. Mua sản phẩm
[![gio](/wiki-assets/images/module/ai-camera/images/gio.png)](https://shop.ohstem.vn/)


## 3. Thông số kỹ thuật

| Thông số | Giá trị |
|----------|---------|
| Chip xử lý | ESP32-S3 Xtensa dual-core 32-bit LX7, 240MHz, 4MB Flash, 8MB PSRAM |
| Cảm biến hình ảnh | Camera OV2640 2MP |
| Nguồn cấp | 5V qua cổng USB Type-C, 3.3V qua cổng Grove hoặc 3.7 – 6V qua cổng pin rời |
| Kết nối mạng | WiFi 2.4GHz và 5GHz |
| Giao tiếp với board | UART (cổng Grove 4 chân) |
| Mô hình AI | Google Teachable Machine (Image Project) |

## 4. Kết nối với board lập trình
Camera AI giao tiếp với board lập trình qua **UART**. Tùy vào board mà chân kết nối và khối lệnh khởi tạo sẽ khác nhau:

| Board lập trình | Chân kết nối | Khối lệnh khởi tạo | Mạch mở rộng |
|-----------------|--------------|--------------------|--------------|
| **Yolo:Bit** | P0 – P1 | `khởi tạo Camera AI chân RX P1 TX P0` | Cần Grove shield |
| **Yolo UNO** | D5 – D6 | `khởi tạo Camera AI chân RX D5 TX D6` | Không cần |

**Lưu ý:** Nếu bạn chỉ dùng camera để gửi kết quả lên **server IoT** (mục 7) thì không cần nối dây Grove giữa camera và board, chỉ cần cấp nguồn cho camera là đủ.

## **4.1 Kết nối với Yolo:Bit**
- **Bước 1:** Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![camera ai](/wiki-assets/images/module/ai-camera/images/camera_v2_1.png) | Camera AI (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/) |
| ![yolo](/wiki-assets/images/module/ai-camera/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/ai-camera/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |

- **Bước 2:** Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3:** Cấp nguồn cho camera bằng cáp USB Type-C
- **Bước 4:** Dùng dây Grove nối camera vào **cổng P0/P1** trên mạch mở rộng

## **4.2 Kết nối với Yolo UNO**
- **Bước 1:** Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![camera ai](/wiki-assets/images/module/ai-camera/images/camera_v2_1.png) | Camera AI (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/) |
| ![yolo uno](/wiki-assets/images/module/ai-camera/images/yolo_uno.png) | Mạch Yolo UNO | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/yolo-uno/) |

- **Bước 2:** Cấp nguồn cho camera bằng cáp USB Type-C
- **Bước 3:** Dùng dây Grove nối camera vào **cổng D5 – D6** trên Yolo UNO (Yolo UNO đã có sẵn cổng Grove nên không cần mạch mở rộng)
![noi camera yolo uno](/wiki-assets/images/module/ai-camera/images/camera_noi_yolo_uno.png)


## 5. Cấu hình và huấn luyện mô hình AI
Phần này **áp dụng chung cho mọi board** (Yolo:Bit, Yolo UNO…) vì toàn bộ thao tác được thực hiện trên camera và trên trình duyệt, chưa liên quan đến việc lập trình thiết bị.

Để làm việc với Camera AI, bạn cần thực hiện theo các bước sau đây:

1. Kết nối wifi cho camera
2. Huấn luyện mô hình AI
3. Nhận dạng qua camera
4. Lập trình thiết bị thực hiện nhiệm vụ theo mô hình đã huấn luyện (xem mục 6)

## **5.1 Kết nối wifi cho camera AI**
1. Sau khi kết nối camera với thiết bị, hãy bật nguồn. Đèn báo trên camera sẽ sáng màu đỏ (báo hiệu camera chưa có kết nối internet).
![camera v2 2](/wiki-assets/images/module/ai-camera/images/camera_v2_2.png)


2. Lúc này, dùng điện thoại hoặc laptop vào biểu tượng kết nối wifi, tìm kiếm mạng wifi của camera là **ohstem-ai-camera-xxxxx** (với x là id của camera).
![camera v2 3](/wiki-assets/images/module/ai-camera/images/camera_v2_3.png)


Chọn vào tên wifi, một trang web mới tự động mở ra như hình bên dưới (nếu không tự mở lên bạn có thể nhập ip **192.168.4.1** vào thanh tìm kiếm của Google Chrome, Cốc Cốc…):
![camera v2 4](/wiki-assets/images/module/ai-camera/images/camera_v2_4.png)


3. Chọn tiếp vào **Configure WiFi**
![camera v2 5](/wiki-assets/images/module/ai-camera/images/camera_v2_5.png)


Ở giao diện này bạn sẽ chọn mạng wifi mà mình muốn camera kết nối, **nhập mật khẩu wifi vào ô Password và chọn Save**:
![camera v2 6](/wiki-assets/images/module/ai-camera/images/camera_v2_6.png)


4. Khi kết nối wifi thành công, đèn trên camera sẽ chuyển sang màu xanh lá như hình:
![camera v2 7](/wiki-assets/images/module/ai-camera/images/camera_v2_7.png)


**Lưu ý:** Camera AI và laptop/điện thoại phải kết nối chung 1 mạng wifi ở bước 3.

Để **xóa mạng wifi đang kết nối**, bạn cần ấn giữ nút **Boot** trong 5 giây (ngay cạnh đèn led), khi đèn chuyển từ xanh qua đỏ là camera của bạn đã xóa mạng wifi đang kết nối thành công.
![camera v2 8](/wiki-assets/images/module/ai-camera/images/camera_v2_8.png)


5. **Lấy địa chỉ IP của camera:** Bấm vào biểu tượng kết nối wifi trên laptop, bạn sẽ thấy 1 mạng wifi có tên là **192.168.x.xxx - cam - id** xuất hiện, đây chính là địa chỉ IP của camera (mỗi mạng wifi sẽ cho ra một địa chỉ IP khác nhau):
![camera v2 9](/wiki-assets/images/module/ai-camera/images/camera_v2_9.png)


**Lưu ý:** Không được kết nối vào mạng wifi của camera, chỉ xem để lấy địa chỉ IP truy cập.

6. **Truy cập vào địa chỉ IP của camera:** Vào trình duyệt Chrome/Cốc Cốc… gõ vào ô tìm kiếm địa chỉ IP của camera để truy cập vào Camera AI. Trang web sẽ hiển thị giao diện như sau:
![camera v2 10](/wiki-assets/images/module/ai-camera/images/camera_v2_10.png)


**Các thông tin chúng ta cần lưu ý là:**

- **Mô hình AI:** để trống nếu như muốn sử dụng mô hình của mình tự huấn luyện. Hoặc chọn mô hình có sẵn.
- **Link mô hình:** là đường liên kết mô hình của mình tự huấn luyện (hướng dẫn ở phần sau). Nếu sử dụng mô hình có sẵn thì hệ thống sẽ tự điền link.
- **Độ chính xác:** từ 0 - 100 là mức độ chính xác mà kết quả nhận diện mà bạn mong muốn.

## **5.2 Huấn luyện mô hình - Tạo link mô hình**
Ở phần này, chúng ta sẽ cần dùng 1 công cụ tạo mô hình AI của Google:

1. Mở 1 tab mới trên trình duyệt và truy cập vào trang web [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/) và chọn **Get Started**:
![camera ai 7](/wiki-assets/images/module/ai-camera/images/camera_ai_7.png)


2. Giao diện sẽ hiện ra như hình, chọn vào **Image Project**:
![camera ai 8](/wiki-assets/images/module/ai-camera/images/camera_ai_8.png)


3. Chọn tiếp vào **Standard image model**:
![camera ai 9](/wiki-assets/images/module/ai-camera/images/camera_ai_9.png)


Giao diện được hiển thị tương tự với giao diện Mô hình AI trên OhStem App:
![camera ai 10](/wiki-assets/images/module/ai-camera/images/camera_ai_10.png)


4. **Bắt đầu huấn luyện mô hình AI:** Chọn vào **Webcam** và nhấn **Hold to Record** để thu thập mẫu. Sau khi hoàn tất, chọn **Train Model**
![camera v2 11](/wiki-assets/images/module/ai-camera/images/camera_v2_11.png)


**Lưu ý:** Hãy đặt tên các lớp (class) bằng tiếng Anh không dấu, ví dụ `Masked`, `NoMask`, `Nobody`. Tên này sẽ được dùng lại trong khối lệnh **camera nhận dạng được là** ở mục 6.

5. Chọn **Export Model** để xuất ra mô hình:
![camera v2 12](/wiki-assets/images/module/ai-camera/images/camera_v2_12.png)


6. Sau đó bạn ấn vào chọn **Upload my model**:
![camera v2 13](/wiki-assets/images/module/ai-camera/images/camera_v2_13.png)


7. Một đường link sẽ xuất hiện, hãy **sao chép và dán vào ô Link mô hình trên trang địa chỉ IP của camera**:
![camera v2 14](/wiki-assets/images/module/ai-camera/images/camera_v2_14.png)


Kết quả như hình:
![camera v2 15](/wiki-assets/images/module/ai-camera/images/camera_v2_15.png)


**Mô hình mẫu:** [https://teachablemachine.withgoogle.com/models/uUg-HVyPX/](https://teachablemachine.withgoogle.com/models/uUg-HVyPX/)

Mẫu vật tham khảo của mô hình mẫu:
![sample](/wiki-assets/images/module/ai-camera/images/camera_sample.png)


## **5.3 Nhận dạng qua camera**
Sau khi đã điền xong các thông tin, bạn ấn **Bật camera** để bắt đầu nhận dạng:
![camera v2 16](/wiki-assets/images/module/ai-camera/images/camera_v2_16.png)


Chờ khoảng 1 phút để hiện hình ảnh, kết quả nhận dạng sẽ được thể hiện trên màn hình tương tự như hình sau:
![camera v2 17](/wiki-assets/images/module/ai-camera/images/camera_v2_17.png)


## 6. Lập trình thiết bị đọc kết quả qua UART
Sau khi mô hình đã nhận dạng được (mục 5), bạn lập trình cho board đọc kết quả trực tiếp từ camera qua dây Grove. Cách này **không cần server IoT**, độ trễ thấp nên phù hợp với robot và các dự án cần phản hồi nhanh.

Bên dưới là hướng dẫn riêng cho từng board: **Yolo:Bit ở mục 6.1** và **Yolo UNO ở mục 6.2**. Bạn chỉ cần đọc phần tương ứng với board mình đang dùng.

## **6.1 Lập trình với Yolo:Bit**
1. Truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn lập trình thiết bị **Yolo:Bit**.
![camera v2 18](/wiki-assets/images/module/ai-camera/images/camera_v2_18.png)


2. Trong mục **Mở rộng**, tải thư viện **AI Camera** để thiết bị đọc kết quả trực tiếp từ module Camera AI.

**Link thư viện:** [https://github.com/AITT-VN/yolobit_extension_ai_camera.git](https://github.com/AITT-VN/yolobit_extension_ai_camera.git)
![camera v2 19](/wiki-assets/images/module/ai-camera/images/camera_v2_19.png)


3. Sau khi tải xong, danh mục **AI CAMERA** sẽ xuất hiện với các khối lệnh sau:
![camera v2 20](/wiki-assets/images/module/ai-camera/images/camera_v2_20.png)


| Khối lệnh | Chức năng |
|-----------|-----------|
| `khởi tạo Camera AI chân RX ... TX ...` | Khai báo cổng UART nối với camera (Yolo:Bit dùng RX **P1**, TX **P0**) |
| `camera cập nhật nhận dạng` | Đọc dữ liệu mới nhất từ camera, cần gọi trước khi so sánh kết quả |
| `camera nhận dạng được là "..." độ tin cậy > ...` | Trả về đúng/sai khi kết quả nhận dạng trùng tên lớp và vượt ngưỡng tin cậy |
| `đọc kết quả nhận dạng` | Trả về tên lớp mà camera đang nhận dạng được |
| `đọc độ tin cậy` | Trả về độ tin cậy (0 - 100) của kết quả hiện tại |

4. Gửi chương trình cơ bản sau lên Yolo:Bit:
![camera v2 21](/wiki-assets/images/module/ai-camera/images/camera_v2_21.png)


**Link chương trình mẫu:** [https://app.ohstem.vn/#!/share/yolobit/2af4ex5ZvT1H6uh2rrWNMEFt4Ql](https://app.ohstem.vn/#!/share/yolobit/2af4ex5ZvT1H6uh2rrWNMEFt4Ql)

**Giải thích chương trình:** Đầu tiên chúng ta khởi tạo kết nối của Camera AI với Yolo:Bit qua cổng **RX P1 / TX P0**. Tiếp theo, trong vòng **lặp lại mãi**, sau mỗi 1000 milli giây chương trình sẽ **cập nhật nhận dạng** từ camera và so sánh với mô hình đã huấn luyện: nếu nhận dạng được lớp `Masked` với độ tin cậy lớn hơn 70 thì bật đèn LED RGB màu trắng, ngược lại thì tắt đèn.

## **6.2 Lập trình với Yolo UNO**
1. Truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn lập trình thiết bị **Yolo UNO**.

2. Vào mục **Mở rộng** của Yolo UNO, tìm và tải thư viện **Camera AI**:
![thu vien camera uno](/wiki-assets/images/module/ai-camera/images/camera_uno_thuvien.png)


3. Sau khi tải xong, danh mục **AI CAMERA** sẽ xuất hiện với các khối lệnh sau:
![khoi lenh camera uno](/wiki-assets/images/module/ai-camera/images/camera_uno_khoilenh.png)


| Khối lệnh | Chức năng |
|-----------|-----------|
| `khởi tạo Camera AI chân RX ... TX ...` | Khai báo cổng UART nối với camera (Yolo UNO dùng RX **D5**, TX **D6**) |
| `khởi tạo Camera AI dùng OhStem App` | Dùng khi nhận dạng bằng **Mô hình AI trên OhStem App** thay cho module camera |
| `camera cập nhật nhận dạng` | Đọc dữ liệu mới nhất từ camera, cần gọi trước khi so sánh kết quả |
| `camera nhận dạng được là "..." độ tin cậy > ...` | Trả về đúng/sai khi kết quả nhận dạng trùng tên lớp và vượt ngưỡng tin cậy |
| `đọc kết quả nhận dạng` | Trả về tên lớp mà camera đang nhận dạng được |
| `đọc độ tin cậy` | Trả về độ tin cậy (0 - 100) của kết quả hiện tại |

4. Bạn có thể mở nhanh chương trình mẫu **Nhận diện hình ảnh bằng Camera AI** theo các thao tác sau: chọn biểu tượng **Project mẫu**, vào nhóm **4. Dự án AI**:
![mo chuong trinh uno](/wiki-assets/images/module/ai-camera/images/camera_uno_mo_chuongtrinh.png)


Chương trình hiển thị như sau:
![chuong trinh uno](/wiki-assets/images/module/ai-camera/images/camera_uno_chuongtrinh.png)


**Giải thích chương trình:** Khi Yolo UNO khởi động sẽ khởi tạo Camera AI ở chân **RX D5 / TX D6**. Sau đó, cứ mỗi 0.1 giây chương trình **cập nhật nhận dạng** từ camera và xử lý:

- Nếu camera nhận dạng được `Masked` (có đeo khẩu trang) thì đổi đèn LED trên board thành **màu xanh**
- Nếu camera nhận dạng được `NoMask` (không đeo khẩu trang) thì đổi đèn LED thành **màu đỏ**
- Nếu camera nhận dạng được `Nobody` (không có người) thì **tắt đèn**

## 7. Nâng cao - Nhận dạng qua server IoT
Ngoài cách đọc kết quả qua UART, bạn có thể cho camera gửi kết quả nhận dạng lên **server IoT của OhStem**, rồi để thiết bị đọc kết quả từ bảng điều khiển IoT. Cách này phù hợp khi camera và thiết bị đặt ở 2 vị trí xa nhau.

So sánh 2 cách để bạn dễ chọn:

| | Qua UART (mục 6) | Qua server IoT (mục 7) |
|---|---|---|
| Dây nối camera – board | Cần dây Grove | Không cần |
| Khoảng cách | Camera đặt cạnh board | Camera và board có thể ở xa nhau |
| Độ trễ | Thấp, phản hồi nhanh | Cao hơn, phụ thuộc mạng |
| Thư viện cần tải | AI Camera | MQTT |

Quy trình thực hiện:

1. Kết nối wifi cho camera
2. Huấn luyện mô hình AI
3. Nhận dạng qua camera
4. Tạo bảng điều khiển IoT
5. Cấu hình camera gửi dữ liệu lên bảng điều khiển
6. Viết chương trình cho thiết bị nhận dữ liệu từ bảng điều khiển

Các bước 1, 2, 3 thực hiện tương tự như mục 5.1, 5.2 và 5.3. Dưới đây sẽ hướng dẫn bạn cách thực hiện các bước còn lại.

## **7.1 Tạo bảng điều khiển IoT**
Truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn **Bảng điều khiển IoT** và tạo một bảng điều khiển mới.

Với bảng điều khiển mới, bạn cần thực hiện các thao tác sau:

1. Đặt lại tên cho **Username** (đặt thêm ký tự hoặc số để không trùng với các username khác)
2. Chọn **kênh thông tin**

Đây là 2 thông tin quan trọng của server MQTT.
![camera v2 22](/wiki-assets/images/module/ai-camera/images/camera_v2_22.png)


## **7.2 Cấu hình camera gửi dữ liệu lên bảng điều khiển**
Trên trang địa chỉ IP của camera, ở phần **Cài đặt nâng cao (Cài đặt IoT)**, chúng ta cần chú ý các thông tin sau:
![camera v2 23](/wiki-assets/images/module/ai-camera/images/camera_v2_23.png)


- **Server:** bạn chọn vào server OhStem, nơi bạn sẽ gửi thông tin kết quả nhận dạng.
- **User:** điền tên username của bảng điều khiển IoT mà bạn đã tạo ở mục 7.1.
- **Kênh dữ liệu:** điền tên kênh thông tin đã chọn ở mục 7.1 (V1 … V20).
- **Tần suất gửi:** với các mẫu giống nhau bạn có thể chọn tần suất gửi lâu hơn. Ví dụ, khi nhận diện 1 vật không thay đổi, tần suất gửi là 10s 1 lần, vậy cứ sau 10s thông tin về vật sẽ được gửi lên server nếu như vật đó không thay đổi.

Điền thông tin **Username** và **kênh dữ liệu** vào trang địa chỉ IP của camera, kết quả như hình:
![camera v2 24](/wiki-assets/images/module/ai-camera/images/camera_v2_24.png)


**Kết quả nhận diện:**

Bật cùng lúc 2 tab địa chỉ IP của camera và bảng điều khiển IoT, **không được ẩn tab xử lý camera đi**, kết quả nhận diện sẽ được hiển thị lên bảng điều khiển:
![camera v2 25](/wiki-assets/images/module/ai-camera/images/camera_v2_25.png)


Ở phần **Kết quả nhận dạng** sẽ là kết quả mà Camera AI nhận dạng được và độ tin cậy của kết quả, kết quả sẽ được gửi lên trực tiếp server IoT của OhStem.

## **7.3 Viết chương trình cho thiết bị nhận dữ liệu từ bảng điều khiển**
Ví dụ dưới đây dùng **Yolo:Bit**. Với **Yolo UNO** bạn thực hiện tương tự, chỉ khác ở bước chọn thiết bị lập trình là **Yolo UNO** — các khối lệnh MQTT là giống nhau trên cả 2 board.

Mở tab mới, truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn **lập trình thiết bị Yolo:Bit**, trong mục **Mở rộng** tìm kiếm và tải thư viện **MQTT**:
![camera v2 26](/wiki-assets/images/module/ai-camera/images/camera_v2_26.png)


Cuối cùng, gửi chương trình sau vào Yolo:Bit:
![camera v2 27](/wiki-assets/images/module/ai-camera/images/camera_v2_27.png)


**Link chương trình mẫu:** [https://app.ohstem.vn/#!/share/yolobit/2af4I5bvMQKIS5uUTxvzoy3ptf4](https://app.ohstem.vn/#!/share/yolobit/2af4I5bvMQKIS5uUTxvzoy3ptf4)

**Giải thích chương trình:**

Để nhận được thông tin từ bảng điều khiển, thiết bị cần được kết nối với wifi và kết nối với bảng điều khiển mà bạn đã tạo trước đó. Do đó, bạn cần nhập đúng thông tin wifi và username của bảng điều khiển vào 2 khối lệnh:
![camera v2 28](/wiki-assets/images/module/ai-camera/images/camera_v2_28.png)


Tiếp theo, đăng ký nhận thông tin từ kênh dữ liệu (từ V1 … V20) để so sánh kết quả và thực hiện nhiệm vụ:
![camera v2 29](/wiki-assets/images/module/ai-camera/images/camera_v2_29.png)


Sử dụng thêm khối lệnh **tạm dừng 1000 milli giây** và **cập nhật thông tin từ server** để thiết bị luôn nhận được thông tin mới nhất.

## 8. Một số lưu ý khi sử dụng

| Tình huống | Cách xử lý |
|------------|------------|
| Đèn camera sáng đỏ | Camera chưa kết nối được internet, hãy cấu hình lại wifi theo mục 5.1 |
| Đèn camera sáng xanh lá | Camera đã kết nối wifi thành công |
| Cần đổi sang mạng wifi khác | Ấn giữ nút **Boot** 5 giây cho tới khi đèn chuyển từ xanh sang đỏ, sau đó cấu hình lại wifi |
| Không truy cập được địa chỉ IP của camera | Kiểm tra laptop/điện thoại và camera có đang dùng **chung 1 mạng wifi** hay không |
| Kết quả nhận dạng không cập nhật | Không được ẩn (minimize) hoặc đóng tab xử lý camera trong lúc nhận dạng |
| Thiết bị không đọc được kết quả qua UART | Kiểm tra lại chân khởi tạo trong chương trình: Yolo:Bit là **RX P1 / TX P0**, Yolo UNO là **RX D5 / TX D6** |
| Nhận dạng sai nhiều | Thu thập thêm mẫu ảnh khi huấn luyện, huấn luyện lại mô hình, hoặc giảm giá trị **Độ chính xác** |
