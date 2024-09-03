import collections

def get_molecules_data(file_name):
    with open(f'pdb_files/{file_name}', 'r') as f:
        molecule = { 
            "atoms":[],   # [x, y, z, element_symbol]
            "joints":[]   # 
        }

        for line in f:
            values = line.split()
            head_value = values[0]

            # get atom info: position (x, y, z) and atom name
            if head_value in ["HETATM", "ATOM"]:
                x, y, z = map(float, values[5:8])
                element_symbol = values[2][:1]
                molecule["atoms"].append([x, y, z, element_symbol])
            # get atom connectino info
            if head_value == "CONECT":
                target = int(values[1])  # 原子ID
                pairs = [ int(num) for num in values[2:] ]
                bond_count_dict = collections.Counter(pairs)
                for atom_id, bond_count in bond_count_dict.items():
                    sorted_pair = sorted([target, atom_id])
                    joint = sorted_pair + [bond_count]
                    if joint not in molecule["joints"]:  # 重複チェック
                        molecule["joints"].append(joint)
    return molecule

