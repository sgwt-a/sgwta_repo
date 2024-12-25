import sys
import os
import ruamel.yaml
from jinja2 import Template, Environment, FileSystemLoader

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True  # ダブルクォーテーションを保持（インデントは保持されない）


def gen_input_data():
    # define input data
    ret = {
        "dump_path_list": [],
        "node_list": [],
        "compo_remap_list": [],
        "port_remap_list": [],
    }
    ret["dump_path_list"] = ["dump_setting.ini"]
    ret["node_list"] = [
        {"compo_name": "CompoA", "node_name": "NodeA"},
        {"compo_name": "CompoB", "node_name": "NodeB"},
    ]
    ret["compo_remap_list"] = [
        {"origin": "OriginCompoA", "remapped": "CompoA"},
        {"origin": "OriginCompoB", "remapped": "CompoB"},
    ]
    ret["port_remap_list"] = [{"target": "TargetCompo", "remapped": "CompoA"}]

    return ret


def gen_launch_from_template(temp_path, input_data, output_path):
    # load template yaml.j2
    with open(temp_path) as file:
        template = Template(file.read())
    # add input_data into template
    print(input_data)
    filled_yaml = template.render(input_data)
    # output yaml
    with open(output_path, "w") as file:
        file.write(filled_yaml)
    return


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        temp = args[1]
        output_path = args[2]
    else:
        exit(1)
    input_data = gen_input_data()
    gen_launch_from_template(temp, input_data, output_path)
