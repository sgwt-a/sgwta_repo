from panda3d.core import Point3, PandaNode
from . import get_molecule_data, get_polar_angles_from_vec

class PlaceModel:
    def __init__(self, base):
        self.base = base
        self.base.used_element_symbols = []
        self.molecule_dict = {}




