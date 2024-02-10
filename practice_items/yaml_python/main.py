import os, sys
import ruamel
import ruamel.yaml

args = sys.argv
if len(args) == 2:
    in_path = args[1]
else:
    print("Usage: python3 main.py <input file path yaml>")
    exit(1)

yaml = ruamel.yaml.YAML()

with open(in_path) as stream:
    data = yaml.load(stream)

out_path = in_path.replace("input/", "output/")
with open(out_path, "w") as stream:
    yaml.dump(data, stream=stream)

print(out_path)
print(data)

for k, v in data.items():
    print(k, v)
    