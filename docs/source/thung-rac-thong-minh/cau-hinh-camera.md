# 2. Cấu hình cho camera AI

## 1. Thiết lập Camera AI:
Để làm việc trực tiếp với camera AI V2, bạn cần thực hiện theo các bước sau đây:

    1. Kết nối wifi cho camera
    2. Huấn luyện mô hình AI
    3. Nhận dạng qua camera
    4. Lập trình thiết bị thực hiện nhiệm vụ theo mô hình đã huấn luyện
    
    
## **1.1 Kết nối wifi cho camera AI V2:**
1. Sau khi kết nối camera với thiết bị, hãy bật nguồn. Đèn báo trên camera sẽ sáng màu đỏ (báo hiệu camera chưa có kết nối internet).
![camera v2 2](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_2.png)


2. Lúc này, dùng điện thoại hoặc laptop vào biểu tượng kết nối wifi, tìm kiếm mạng wifi của camera là **ohstem-ai-camera- xxxxx (với x là id của camera)**.
![camera v2 3](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_3.png)


    *Chọn vào tên wifi, một trang web mới tự động mở ra như hình bên dưới (Nếu không tự mở lên bạn có thể nhập ip 192.168.4.1 vào thanh tìm kiếm của Google Chrome, Cốc cốc…):*
![camera v2 4](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_4.png)


3. Chọn tiếp vào **Configure WiFi**
![camera v2 5](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_5.png)


Ở giao diện này bạn sẽ chọn mạng wifi mà mình muốn camera kết nối, **nhập mật khẩu wifi vào ô Password và chọn Save**:
![camera v2 6](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_6.png)


4. Khi kết nối wifi thành công, đèn trên camera sẽ chuyển sang màu xanh lá như hình:

**Lưu ý:** Camera AI và laptop/ điện thoại phải kết nối chung 1 mạng wifi ở bước 3.
![camera v2 7](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_7.png)


    **Để xóa mạng wifi đang kết nối, bạn cần ấn giữ nút Boot trong 5 giây (ngay cạnh đèn led), khi đèn chuyển từ xanh qua đỏ là camera của bạn đã xóa mạng wifi đang kết nối thành công.**
![camera v2 8](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_8.png)


5. **Lấy địa chỉ IP của camera:** Bấm vào biểu tượng kết nối wifi trên laptop, bạn sẽ thấy 1 mạng wifi có tên là **192.168.x.xxx - cam - id** xuất hiện, đây chính là địa chỉ IP của camera (mỗi mạng wifi sẽ cho ra một địa chỉ IP khác nhau):
![camera v2 9](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_9.png)


**Lưu ý**: Không được kết nối vào mạng wifi của camera, chỉ xem để lấy địa chỉ IP truy cập.

6. **Truy cập vào địa chỉ IP của camera**: Vào trình duyệt Chrome/ Cốc cốc… gõ vào ô tìm kiếm địa chỉ ip của camera để truy cập vào Camera AI. Trang web sẽ hiển thị giao diện như sau:
![camera v2 10](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_10.png)


**Các thông tin chúng ta cần lưu ý là:**

    + **Mô hình AI:** để trống nếu như muốn sử dụng mô hình của mình tự huấn luyện. Hoặc chọn mô hình có sẵn.
    + **Link mô hình:** là đường liên kết mô hình của mình tự huấn luyện (hướng dẫn ở phần sau). Nếu sử dụng mô hình có sẵn thì hệ thống sẽ tự điền link.
    + **Độ chính xác:** từ 0-100 là mức độ chính xác mà kết quả nhận diện mà bạn mong muốn.
    
    
## **1.2 Huấn luyện mô hình - Tạo link mô hình**
Ở phần này, chúng ta sẽ cần dùng 1 công cụ tạo mô hình AI của Google:

1. Mở 1 tab mới trên trình duyệt và truy cập vào trang web: [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/)  và chọn **Get Started**:
![camera ai 7](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_ai_7.png)


2. Giao diện sẽ hiện ra như hình chọn vào **Image Project**:
![camera ai 8](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_ai_8.png)


3. Chọn tiếp vào **Standard image model**:
![camera ai 9](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_ai_9.png)


Giao diện được hiển thị tương tự với giao diện Mô hình AI trên OhStem App
![camera ai 10](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_ai_10.png)


4. **Bắt đầu huấn luyện mô hình AI**:

Chọn vào **Webcam** và nhấn **Hold to Record** để thu thập mẫu. Sau khi hoàn tất, chọn **Train Model**
![camera v2 11](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_11.png)


5. Chọn **Export Model** để xuất ra mô hình:
![camera v2 12](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_12.png)


6. Sau đó bạn ấn vào chọn **Upload my model**:
![camera v2 13](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_13.png)


7. Một đường link sẽ xuất hiện, hãy **sao chép và dán vào đường dẫn AI trên trang địa chỉ của camera**:
![camera v2 14](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_14.png)


Kết quả như hình:
![camera v2 15](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_15.png)


**Mô hình mẫu:** ](https://teachablemachine.withgoogle.com/models/uUg-HVyPX/)

Mẫu vật tham khảo:
![sample](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/sample.png)


## **1.3 Nhận dạng qua camera**
Sau khi đã điền xong các thông tin, bạn ấn **Bật camera** để bắt đầu nhận dạng:
![camera v2 16](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_16.png)


Chờ khoảng 1 phút để hiện hình ảnh và kết quả nhận dạng sẽ được thể hiện trên màn hình, tương tự như hình sau:
![camera v2 17](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_17.png)


## 2. Chương trình nhận dạng qua sever IoT
Quy trình thực hiện:

    1. Kết nối wifi cho camera
    2. Huấn luyện mô hình AI
    3. Nhận dạng qua camera
    4. Tạo bảng điều khiển IoT
    5. Cấu hình camera gửi dữ liệu lên bảng điều khiển
    6. Viết chương trình cho thiết bị nhận dữ liệu từ bảng điều khiển
    
Các bước 1, 2, 3 thực hiện tương tự như mục 1.1, 1.2 và 1.3. Dưới đây sẽ hướng dẫn bạn cách thực hiện các bước còn lại.

## **2.1. Tạo bảng điều khiển IoT:**
Truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn **Bảng điều khiển IoT** và tạo một bảng điều mới.

Với bảng điều khiển mới, bạn cần thực hiện các thao tác sau:

    1. Đặt lại tên cho **Username** (đặt thêm ký tự hoặc số để không trùng với các username khác)
    2. Chọn **kênh thông tin**.  Đây là 2 thông tin quan trọng của server MQTT.
![camera v2 22](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_22.png)


## **2.2 Cấu hình camera gửi dữ liệu lên bảng điều khiển**
Trên trang địa chỉ IP của camera, ở phần **Cài đặt nâng cao (Cài đặt IoT)**, chúng ta cần chú ý các thông tin sau:
![camera v2 23](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_23.png)


- **Server**: bạn chọn vào server OhStem, nơi bạn sẽ gửi thông tin kết quả nhận dạng.
- **User**: điền tên username của bảng điều khiển IoT mà bạn đã tạo ở mục 5.1.
- **Kênh dữ liệu**: điền tên kênh thông tin đã chọn ở mục 5.2 (V1 … V20)
- **Tần suất gửi**: Với các mẫu giống nhau bạn có thể chọn tần suất gửi lâu hơn. Ví dụ, khi nhận diện 1 vật không thay đổi, tần suất gửi là 10s 1 lần, vậy cứ sau 10s thông tin về vật sẽ được gửi lên server nếu như vật đó không thay đổi.

Điền thông tin **Username** và **kênh dữ liệu** vào trang địa chỉ của camera, kết quả như hình:
![camera v2 24](/wiki-assets/images/yolo_uno/thung-rac-thong-minh-yolo-uno/images/camera_v2_24.png)


**Nhận diện:**

Bật cùng lúc 2 tab địa chỉ IP của camera và bảng điều khiển IoT, không được ẩn tab xử lý camera đi, kết quả nhận diện sẽ được hiển thị lên bảng điều khiển.

Ở phần Kết quả nhận dạng sẽ là kết quả mà camera AI nhận dạng được và độ tin cậy của kết quả, kết quả sẽ được gửi lên trực tiếp server IoT của OhStem.
