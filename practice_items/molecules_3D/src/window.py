from panda3d.core import WindowProperties
from . import DrawText

class Window:
    def __init__(self, base, title, screen_size, bottom_left_text):
        self.props = WindowProperties()
        self.props.setTitle(title)
        self.props.setSize(*screen_size)
        base.win.requestProperties(self.props)

        # get font
        self.font = base.loader.loadFont("/mnt/c/Windows/Fonts/msgothic.ttc")

        # 左下のテキストを表示
        self.bottom_left_text = DrawText(bottom_left_text, self.font, base.a2dBottomLeft, scale=0.12, pos=(0.05, 0.2))

        # 左上のテキストを表示
        how_to_use = ("左右矢印キー：カメラの水平回転\n"
                      "上下矢印キー：カメラの垂直回転\n"
                      "マウスホイール：カメラの遠近")
        self.top_left_text = DrawText(how_to_use, self.font, base.a2dTopLeft)

        # "ESC"キーでアプリが終了
        base.accept("escape", exit)

