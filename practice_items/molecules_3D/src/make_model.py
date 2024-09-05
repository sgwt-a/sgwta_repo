class MakeModel:
    CYLINDER_RADIUS = 0.05
    CYLINDER_LENGTH = 1.3     # 結合長（単結合も2重結合も同じ長さと仮定）

    def __init__(self, base):
        self.base = base
        self.base.atom_models = self.make_atom_models()
        self.base.joint_model = self.make_joint_model()

    def make_atom_models(self):
        atom_data = {
            "H": {"color": [1, 1, 1], "radius": 0.31},
            "C": {"color": [0, 1, 0], "radius": 0.77},
            "N": {"color": [0, 0, 1], "radius": 0.70},
            "O": {"color": [1, 0, 0], "radius": 0.66},
            "Other": {"color": [0.14, 0.23, 0.42], "radius": 1}
        }

        atom_models = {}
        for element_symbol, data in atom_data.items():
            atom_model = self.base.loader.loadModel("models/smiley")
            atom_model.setScale( data["radius"] / 2, data["radius"] / 2, data["radius"] / 2 )
            atom_model.setColor(*data["color"])
            atom_model.setTextureOff(1)
            atom_models[element_symbol] = atom_model
        
        return atom_models
    
    def make_joint_model(self):
        joint_model = self.base.loader.loadModel("models/smiley")
        joint_model.setScale( self.CYLINDER_RADIUS, self.CYLINDER_RADIUS, self.CYLINDER_LENGTH / 2 )
        joint_model.setColor(0.5, 0.5, 0.5)
        joint_model.setTextureOff(1)
        return joint_model