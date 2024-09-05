from panda3d.core import PandaNode

class Camera:
    def __init__(self, base):
        self.base = base
        # マウス操作を禁止
        base.disableMouse()
        # カメラの設定
        self.camera_radius = 50  # 初期値の設定
        self.camera_theta = 0    # 初期値の設定
        self.camera_phi = 90     # 初期値の設定
        self.camera_node = base.render.attachNewNode(PandaNode("camera_node"))
        base.camera.reparentTo(self.camera_node)
        base.camera.setHpr(90, 0, 0)
        base.camera.setPos(self.camera_radius, 0, 0)
        self.update_camera_position()

        # キー操作でカメラを動かす
        base.accept("arrow_right", self.move_camera, [0, 0, 1])
        base.accept("arrow_left", self.move_camera, [0, 0, -1])
        base.accept("arrow_up", self.move_camera, [0, -1, 0])
        base.accept("arrow_down", self.move_camera, [0, 1, 0])
        base.accept("arrow_right-repeat", self.move_camera, [0, 0, 1])
        base.accept("arrow_left-repeat", self.move_camera, [0, 0, -1])
        base.accept("arrow_up-repeat", self.move_camera, [0, -1, 0])
        base.accept("arrow_down-repeat", self.move_camera, [0, 1, 0])
        base.accept("wheel_up", self.move_camera, [-1, 0, 0])
        base.accept("wheel_down", self.move_camera, [1, 0, 0])

    def update_camera_position(self):
        r = self.camera_radius
        print("camera:", r, self.camera_theta, self.camera_phi)
        self.base.camera.setPos(r, 0, 0)
        self.camera_node.setHpr(self.camera_phi, 0, self.camera_theta)

    def move_camera(self, diff_r, diff_theta, diff_phi):
        self.camera_radius += diff_r
        self.camera_theta += diff_theta
        self.camera_phi += diff_phi

        self.update_camera_position()
