from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode
from src import Window, Camera, MakeModel, PlaceModel


class DrawMolecularStructure(ShowBase):  # ShowBaseクラスを継承してDrawMolecularStructureクラスを定義
    def __init__(self, pdb_name, display_name, window_title):
        # ShowBaseの初期化
        # ShowBase.__init__(self)
        super().__init__(self)

        # 基本的なウィンドウをカメラの設定
        self.window = Window(
            self, window_title, (1200, 800), display_name
        )  # Windowsクラスをインスタンス化
        Camera(self)  # Cameraクラスをインスタンス化

        # 分子の配置に関する処理
        MakeModel(self)  # MakeModelクラスをインスタンス化
        self.place_model = PlaceModel(self)  # PlaceModelクラスをインスタンス化

        # 分子モデルを表示
        self.molecule_node = self.render.attachNewNode(PandaNode("molecule_node"))
        self.place_model.display_molecular_structure(
            pdb_name, self.molecule_node
        )  # place_modelインスタンスのdisplay_molecular_structureメソッドをコール


# app = DrawMolecularStructure("OCT.pdb", "オクタン", "分子構造模型")
app = DrawMolecularStructure("BNZ.pdb", "ベンゼン", "分子構造模型")
# app = DrawMolecularStructure("6fs4.pdb", "6fs4", "分子構造模型")
app.run()
