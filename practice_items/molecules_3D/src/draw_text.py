from direct.gui.DirectGui import OnscreenText
from panda3.core import TextNode

class DrawText(OnscreenText):
    # scale: 文字サイズ
    # pos: 位置
    # align: 文字詰め 左詰め=TextNode,ALeft, 中央ぞろえ=TextNode.ACenterなど
    # fg: テキスト色
    # bg: 背景色
    # mayChange: プログラム実行中にテキストを変更するときはTrue
    # wordwrap: 折り返し文字数
    def __init__(self, text, font, parent, scale=0.07, pos=(0.05, -0.1), align=TextNode.ALeft, fg=(1, 1, 1, 1), bg=(0, 0, 0, 0.1), mayChange=True, wordwrap=40):
        super().__init__(text=text, font=font, parent=parent, scale=scale, pos=pos, align=align, fg=fg, bg=bg, mayChange=mayChange, wordwrap=wordwrap)
    