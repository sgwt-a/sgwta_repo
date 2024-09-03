from direct.showbase.ShowBase import ShowBase  # ?
from panda3d.core import WindowProperties, Point3  # ?
from src import get_polar_angles_from_vec

class App(ShowBase):
    def __init__(self): # ?
        ShowBase.__init__(self) # ?

        # Set window
        self.props = WindowProperties()
        self.props.setTitle("2つのスフィアを繋ぐシリンダー")
        self.props.setSize(1200, 800)
        self.win.requestProperties(self.props)
        self.setBackgroundColor(0, 0, 0)

        # Display sphere
        positions = [ Point3(0, 20, 0), Point3(2, 23, 4) ]
        colors = [ (1, 0, 0), (0, 0, 1) ]
        for position, color in zip(positions, colors):
            sphere = self.loader.loadModel("models/smiley")
            sphere.reparentTo(self.render)  # モデルを配置するノードを指定
            sphere.setScale(1, 1, 1)
            sphere.setColor(*color)
            sphere.setTextureOff(1)  # モデルに貼り付けられたテクスチャを無効化
            sphere.setPos(position)  # モデルを配置する位置を指定

        # Display cylinder: 棒状の図形を表示できないので、球を引き伸ばして楕円で表現
        start_pos, end_pos = positions
        diff_position = end_pos - start_pos
        length = diff_position.length()
        polar_angles = get_polar_angles_from_vec(diff_position)
        center_position = (start_pos + end_pos) / 2
        cylinder = self.loader.loadModel("models/smiley")
        cylinder.reparentTo(self.render)
        cylinder.setScale(0.2, 0.2, length / 2)
        cylinder.setColor(0, 1, 0)
        cylinder.setTextureOff(1)
        cylinder.setPos(center_position)
        cylinder.setHpr(*polar_angles)

app = App()
app.run()

