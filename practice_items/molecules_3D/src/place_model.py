from panda3d.core import Point3, PandaNode
from . import get_molecule_data, get_polar_angles_from_vec

class PlaceModel:
    def __init__(self, base):
        self.base = base
        self.base.used_element_symbols = []
        self.molecule_dict = {}

    def display_molecular_structure(self, molecular_name, parent, is_count_atoms=False):
        # get atom position and bond
        if molecular_name not in self.molecule_dict:
            self.molecule_dict[molecular_name] = get_molecule_data(molecular_name)  # pdb info
        # dis play molecular structure
        self.display_atom_models(molecular_name, parent, is_count_atoms)
        self.display_joint_models(molecular_name, parent)

    def display_atom_models(self, molecular_name, parent, is_count_atoms):
        atoms = self.molecule_dict[molecular_name]["atoms"]
        for atom in atoms:
            x, y, z, element_symbol = atom
            placeholder = parent.attachNewNode(PandaNode("placeholder"))
            placeholder.setPos(Point3(z, y, x))
            if element_symbol in self.base.atom_models:
                atom_model = self.base.atom_models[element_symbol]
            else:
                atom_model = self.base.atom_models["Other"]
            atom_model.instanceTo(placeholder)
            # get the number of atoms
            if is_count_atoms:
                self.base.used_element_symbols.append(element_symbol)
    
    def display_joint_models(self, molecular_name, place):
        atoms = self.molecule_dict[molecular_name]["atoms"]
        joints = self.molecule_dict[molecular_name]["joints"]
        for joint in joints:
            start = joint[0]
            end = joint[1]
            if len(joint) == 2:   # ?
                joint_num = 1
            else:
                joint_num = joint[2]
            x1, y1, z1, _ = atoms[start-1]
            x2, y2, z2, _ = atoms[end-1]
            start_position = Point3(z1, y1, x1)
            end_position = Point3(z2, y2, x2)
            center_position = ( start_position + end_position ) / 2
            direction = end_position - start_position
            polar_angles = get_polar_angles_from_vec(direction)
            # display joint
            placeholder = place.attachNewNode(PandaNode("placeholder"))
            placeholder.setPos(center_position)
            placeholder.setHpr(polar_angles)
            if joint_num == 3:
                diff_positions = [ Point3(0, 0.16, 0), Point3(0.14, -0.08, 0), Point3(-0.14, -0.08, 0) ]
            elif joint_num == 2:
                diff_positions = [ Point3(0, 0.16, 0), Point3(0, -0.16, 0) ]
            else:
                diff_positions = [ Point3(0, 0, 0) ]
            for diff_positoin in diff_positions:
                sub_placeholder = place.attachNewNode(PandaNode("sub_placeholder"))
                sub_placeholder.setPos(diff_positoin)
                self.base.joint_model.instanceTo(sub_placeholder)

                


