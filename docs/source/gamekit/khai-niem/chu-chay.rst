9. Tạo hiệu ứng chữ chạy trên màn hình 
================================

    .. image:: images/9.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Sẽ thật tuyệt nếu như có một câu truyện mở đầu trò chơi hay một đoạn hướng dẫn cách chơi khi mới vào game. Điều dó sẽ làm người chơi thấy thích thù, hiểu hơn về nội dung của trò chơi.

Ở bài học này mình sẽ cung cấp cho các bạn một mẫu chương trình có sẵn để giới thiệu trò chơi theo cách cổ điển mà đa số các game 2D hiện nay đều có.

Các bạn có thể copy  đoạn code JavaScript bên dưới bỏ vào phần giao diện JavaScript để xây dựng chương trình.

Nếu bạn muốn thay đổi nội dung câu chuyện, cũng có thể viết lại bên trong đoạn **“storyLine“**.


.. code-block:: python

    namespace SpriteKind {
        export const Star = SpriteKind.create();
    }

    let ship: Sprite = null
    let hyper = false
    let star: Sprite = null
    let scroll = false
    let lineAdjust = 0
    let sagaSprite: Sprite = null
    let sagaImage: Image = null
    let storyLines = [
        "TALE OF TALAGRON",
        "",
        "Once upon a time,",
        "like really long ago,",
        "a peaceful people lived",
        "happily on Planet Talagron.",
        "",
        "They used the rare mineral",
        "Xelantium for energy to",
        "power their planet.",
        "",
        "Dobanites raided Talagron",
        "and took all the known",
        "Xelantium from them. Not",
        "nice! Ugh! Err!",
        "",
        "Your mission is to help",
        "protect Talagron from the",
        "greedy Dobanites. So, on",
        "your way now and good luck!"
    ]
    scroll = true
    sagaImage = image.create(scene.screenWidth(), 10 * storyLines.length)
    for (let i = 0; i <= storyLines.length - 1; i++) {
        sagaImage.printCenter(storyLines[i], i * 10, i > 0 ? 7 : 4)
    }
    sagaSprite = sprites.create(sagaImage, 0)
    sagaSprite.top = scene.screenHeight() - 1
    sagaSprite.setFlag(SpriteFlag.AutoDestroy, true)
    sagaSprite.vy = -10
    controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
        if (!hyper) {
            sagaSprite.vy = scroll ? 0 : -10
            scroll = !(scroll)
        }
    })

    controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
        if (!hyper) {
            sagaSprite.vy = 0
            scroll = false
            lineAdjust = (sagaSprite.bottom + 1) % 10
            sagaSprite.bottom -= (lineAdjust > 0) ? lineAdjust : 10
        }
    })
    controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
        if (!hyper) {
            sagaSprite.vy = 0
            scroll = false
            lineAdjust = (sagaSprite.top + 1) % 10
            sagaSprite.top += 10 - lineAdjust
        }
    })
    game.onUpdate(function () {
        if (sagaSprite.bottom < 0) {
            sagaSprite.destroy()
        }
        if (Math.percentChance(25) || hyper) {
            star = sprites.create(img`1`, SpriteKind.Star)
            star.setFlag(SpriteFlag.AutoDestroy, true)
            star.setFlag(SpriteFlag.Ghost, true)
            star.x = Math.randomRange(0, scene.screenWidth())
            star.y = Math.randomRange(0, scene.screenHeight())
            star.vx = (star.x < scene.screenWidth() / 2) ? -2 : 2
            star.vy = (star.y < scene.screenHeight() / 2) ? -1 : 1
            if (hyper) {
                star.ax = star.vx * 1000
                star.ay = star.vy * 1000
                if (Math.percentChance(15)) {
                    ship.x = Math.randomRange(scene.screenWidth() / 2 - 5, scene.screenWidth() / 2 + 5)
                    ship.y = Math.randomRange(scene.screenHeight() / 2 - 2, scene.screenHeight() / 2 + 2)
                }
            }
        }
    })
    sagaSprite.onDestroyed(function () {
        ship = sprites.create(img`
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . 7 4 . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . e e . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . e e . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . e e . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . e e . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . 4 e e 4 . . . . . . . . . . . . . .
        . . . . . . . . . . . . e e e e e e e e . . . . . . . . . . . .
        . . . . . . . . . . . e e e e e e e e e e . . . . . . . . . . .
        . . . . . . . . . . e e e e 5 3 3 5 e e e e . . . . . . . . . .
        . . . . . . . . . 4 e e e 5 3 5 2 2 5 e e e 4 . . . . . . . . .
        . . . . . . . 7 7 e e e e 5 2 2 5 5 2 e e e e 7 7 . . . . . . .
        . . . . . . 7 e e e e e e 2 2 5 2 3 3 e e e e e e 7 . . . . . .
        . . . . 7 e e e e e e e e 5 2 2 2 5 2 e e e e e e e e 7 . . . .
        . . e e e e e e e e e e e e 3 5 5 2 e e e e e e e e e e e e . .
        . e e e e e e . . . 7 e e e e e e e e e e 7 . . . e e e e e e .
        e e e e 7 . . . . . . . e e e e e e e e . . . . . . . 7 e e e e
        e 7 . . . . . . . . . . . e e e e e e . . . . . . . . . . . 7 e
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    `, SpriteKind.Player)
        ship.startEffect(effects.warmRadial)
        hyper = true
        for (let slowStar of sprites.allOfKind(SpriteKind.Star)) {
            slowStar.ax = slowStar.vx * 1000
            slowStar.ay = slowStar.vy * 1000
        }
    })














