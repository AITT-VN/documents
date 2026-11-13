# 3. Hướng dẫn kết nối và nạp chương trình cho Rio

Ngoài điều khiển bằng nút nhấn trực tiếp, Rio có thể được lập trình từ xa bằng các khối lệnh trực quan đầy màu sắc thông qua OhStem App!

## Thao tác kết nối

1. **Bật nguồn** khởi động Rio bằng nút đuôi.
2. Truy cập hệ thống lập trình tại trình duyệt: [https://app.ohstem.vn/](https://app.ohstem.vn/) (trên máy tính) hoặc sử dụng App Ohstem quét tải trên điện thoại/máy tính bảng.
3. Từ bảng điều khiển chính, chọn bảng thiết bị **Robot Rio** để vào giao diện lập trình kéo thả. Cụ thể, nhấn vào hình Rio khu vực này:

![](/wiki-assets/images/robot_rio/rio0.PNG)

   Giao diện lập trình hiển thị sẽ như thế này:

![](/wiki-assets/images/robot_rio/rio9.PNG)

4. Nhấn vào biểu tượng ghép nối ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZ2mwfA5N-jZ4ou4bfEgbgUt5qrnXXTXbrjQjW7TZCBJE-Jt6AK7SYOGAWKDC_qf-fBSeDM1eK9FpJafPXQk0oDF-8TDdFAByPJPqAffBSRN8V1_S5c1_LvdboKKqEfQ=s800?key=weG3yoGKu1BpTTNWOuLybJtY) sau đó chọn tên robot ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcFBJhJws3TDeZS5hgpON3kF5mGnz7ZvicGOpv_63qvN3oY5dRi-6hJJ9lQGISxiWH7VeYbmJbqtQfrJR7hdQi-PpN3aqlpCMDk7c8ieIbjneWms0z0fegUOsKe70YUb8A=s800?key=weG3yoGKu1BpTTNWOuLybJtY) và ấn Kết nối
5. Khi kết nối thành công, biểu tượng hình chú mèo/robot trên màn hình ở góc phải sẽ **đổi trạng thái màu sáng** ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcgCnkbDhYzhsZpZwm5mfmLpMUmbrE0cuTMi9pEyZh9hbdTiHFXxT6z2omSyr1ZuPwj1vTVSre_7VHkttuyDL1h6ng3zhB5LyGCAhfiZibR0OSvXZVWfaIJoHyW90uPX_0=s800?key=weG3yoGKu1BpTTNWOuLybJtY) để báo hiệu kết nối ổn định.

## Khởi chạy chương trình

Sau khi bạn đã sắp xếp, kéo thả thả các khối lệnh tạo thành một chuỗi lập trình...
- Để **nạp code và chạy thử**, nhấn vào biểu tượng Chạy (Play) ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcXETZMupgyYnoMSfwzAoa6b_9SkwvLUbYK-gFzD1PNWDqXMM7nF0VsFM6rHwsn_Zq441XAa5C5RUnTU_w0nacOEkDYL2A0pzwTEKc3R0TcxXI5sfsPjx0TBHpnXbG-qI8=s800?key=weG3yoGKu1BpTTNWOuLybJtY).
- Để **ngừng khẩn cấp** chương trình đang chạy, nhấn chuột vào biểu tượng nút Dừng (Stop) ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAEgOqyPfs7sTkfs_uOBjfgTDQ-RmpiAo33TPwRtGmEzM8-y7-ztAl1I41nw6Bn2Z5_9azVORM7Z3vtjRr_46kaZz5jhygkEFRDGicaeIrT236ukXppuphB1A_RbfEeg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) trên giao diện.

> 💡 **LƯU Ý:** Trong quá trình thiết kế lệnh, các khối lệnh thừa nằm rải rác ngoài màn hình (không móc chung vào chuỗi sự kiện chính) nên được dọn dẹp thường xuyên. Bạn có thể kéo chúng lên khu vực giỏ rác phía góc hoặc nhấp phải chọn Xoá.

## Giới thiệu các khối lệnh Rio

Dưới đây là một số khối lệnh di chuyển tương tác chính hỗ trợ riêng cho Rio trong thư viện:

| Hình Ảnh Khối Lệnh | Diễn Giải Lệnh |
|---|---|
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd1mmY2YW3Zub4Qf3wxXLQwPKYQXMIBSz4D1WwQGwV_FDN-EteDzkEXW2eRz7gFzHLkkwszFifDQTYa_rkvgJr7scguLykh0zwjs4hfKv5XCMamQh9KCG0r5E3Ib3_kgMg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Tiến thẳng mãi mãi** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdmuZGdU8cEznhHyIJ7XpqMMiLZYHxR6pFnkMyc5NH-aOBGaGAqscxJ0JurT6OlPK0g6aDegx4pS4eU29P9SMdiWrY_I0czJwj19MX4AtXu57L2JCDSppHq7G3mRnu0XEs=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Lùi mãi mãi** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdmPc4cWw6Zij5lNCdnnLww7m-KCEghMZtQmhC9ZHOSun2ERq2rrIYhSXgfjYwfiyNRGtsiqyPWHfTx1D1IISHJZQJGTl94McyAGmX2v5eOCcrX1Ts8-O9YOYXQWQuezg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Xoay phải mãi mãi** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcWrQnPtG5e5BkLFT3hLfTsmNxVOo1yjMQrFtLq96wCymSHNIxIjHfxMDRBPc09Sg0GBkDats2g1ya-WqgGI8NlP9Zbds7H8hj94gJCiinBLf2bsKs8f39roLZF156HyBo=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Xoay trái mãi mãi** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf1f0Zsdp9Gg5EjvxN67EUQrDY19Tz2dYdYfJSvqSz8AK0eplqmd10GTRlE88bm9L2zhLLqpOBDuOl6xUq3ZzHXM8i-t-QYjYSup3UCss6Yy0JOC0cNkA1JEBMpZ6wLCNY=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Tiến thẳng 1s** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7DkaYN_1VBk1aKDqratDrBUPaQxGGamacnL-KdzpaTy0LoieHAehS_17udq0oCWPQpBp_Rz3BqBbaK7bxPTLBCqbpQ9C3HM9WRvwhbmNB8mwUz85zkFY8lCRfP1ilChs=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Đi lùi 1s** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXft2tysb3GWG22RaSzAIHjytK-YJRHDq_NRM1Xi1SIF96SbpWwb43EemIRnjbDjDx5uuk3i0r0dRK33lSWRtB_nAmex-ipmiyNdgwN_kh0A4B8m4ISW7zjwWFkkiM39Mw=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Quay trái 90 độ** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9zhvOgZcVgfh7gvzYwezoqB6b8yR8f1lyQpGk8qbvxecRz3DtHf3HxoSxmBs2ZWmQNo1OVeoMDSXtJm4UfsP_-VEw6Bdei9-DJGWXBxVQ2W8xyNuRUhwhSq6wL6DK_4g=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Quay phải 90 độ** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctbhTxUkSGC7ZZT8Rx3s6DqdC4k61psl16EgKFl90bye_D8jnqjNghDaf4PI8Jj7cu8vdwHav1ePDK-kxabUrT1EvQQ7o_plqvEKkhl2QIRF7bVYANk5U-ypdjvyF0KYg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Dừng xe** (Ngắt toàn bộ động cơ phanh lại) |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXexI78mCZzhf-L44CqY0Kw5QqtMSApS05aS69l8MSiZJ8lmn8Fns2tZh7IMovSQH35vaGxVwlduFxC41aEEfuhwS3ZEUfYYtQ2J8MrDHxTjHFw4uBwvdzIhL4Xp5C7yWA=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Dò line 1s** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeY3MzndpJZ4H9CLOPQ7x8e9PlnkrWGSiEkU7dx_cURD1eneTEYPV5oL5YYib3TPnPzHEkQ2u0UWj1p8w_wGxFUrFrcBiWZbpkg2eXJ404OkjZN2sTySTn7d7Veuq3bkg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Dò line đến vật cản** (Kích hoạt cảm biến) |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfkjz5gnTikM5Fcbv2UWFaKItmMUpfooFwjgA_S6zylVBKVJXuEphysFxbB0ME7iqq32g0UTvcQcyowSeHddSk7J1lW1Pncam33ckMFy-kVjvm-bNuZkP0cxBgBA3eLcl4=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Dò line vô hạn** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfbz-iNsMENp-8Pjt0TLbHBCbec8Ro0y6RTPsgIato1JxpM9IbB2WbgK8sdWEWpzQ-8mqN_M_B33DXTgUmYaWS2Mu-fZMrETziv0ppJPD-azc5i92Aw3F5Oi6J_YMGBiW4=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Phát loa cảnh báo** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdGQAhlpCNdKhkP4jKE8nlgim-7xzgQa1M7V_nSa94L-WtkP6yx4qE99VMJ8wvPuijD_qY6EZCtIPa6vqx72NYVJfs9mooeOYw8IL-P0nXQEJDFY2tuOLiSxuBoJavVv3M=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Phát nhạc theo bài chỉ định** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdEmwBTiIBinUKbdoZzYV7tWPFAnpTQi-TKdAFu4zviInnR-AAODvkP-4ZZ4FcejfyutP1XC_4Fw1r3EQTKvIkUlWNMGNFbomaLFiyjtj6I3Nr-zVVn9iV_PxEilgadUg=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Phát nốt nhạc** (Tự soạn dải giai điệu) |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAM2muPk1i16jzmOjDKuhzbNXFnYGUOKdxHPF3m6BH4lwRKXiuPE7mwQLOTsCqfNXji3aeK7_BBRQhr3aMs0k169fB_bHusof2LlRaNxKDwuG7xjalS0C_I7nNizZv1w=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Hàng đợi / Chờ 1s** (Tạm dừng trước khi đi tiếp) |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeIrCqH-jcPfo4wIyULaKApBnodmdu2sxBiTiPXBCKBCGYsiA_gMO3cBMp3VY9P8fgbAkfwzJp-nIfm8FrCxOHbql7AOgrd8YICp5odFwlSLxTsruVQ_qAs7F6f55g-p2s=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Vòng lặp theo số lần** |
| ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXflOb_gzEQd5DrAxXPx7d7p5VUWvzpbXqSXQI05T67tKOHiBAHhyymNfeknxMKt6s_Nn6VrCkG5mz5nPpiAXEeJ6dSXNhb6I_NDD7A8PZ9tivXFG-Sl8MYmnnVxobFYSQ=s800?key=weG3yoGKu1BpTTNWOuLybJtY) | **Lặp lại mãi mãi** |

