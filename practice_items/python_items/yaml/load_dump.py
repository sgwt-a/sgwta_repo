import os, sys

### モジュールのインポート
# import ruamel # 不要
import ruamel.yaml

yaml = ruamel.yaml.YAML()
# import yaml

"""
出力形式の設定
"""
yaml.indent(mapping=2, sequence=4, offset=2)  # インデントを設定
yaml.preserve_quotes = True  # ダブルクォーテーションを保持（インデントは保持されない）

"""
入力ファイルの引数設定
"""
args = sys.argv
if len(args) == 2:
    in_path = args[1]
else:
    print("Usage: python3 main.py <input file path yaml>")
    exit(1)

"""
YAMLファイルの読み込み
"""
with open(in_path) as stream:
    data = yaml.load(stream)  # type(data) = <class 'ruamel.yaml.comments.CommentedMap'>

"""
コメントの追加
"""
## 特定のキーの直前にコメントを追加
data.yaml_set_comment_before_after_key("InputPorts", before="これはInputPortsの直前のコメント")

## 特定のキーの直後にコメントを追加
data.yaml_set_comment_before_after_key("InputPorts", after="これはInputPortsの直後のコメント")

## 特定のキーの行末にコメントを追加
### key: value の行末にしかコメント追加できないため、InputPorts:の後ろには追加できなかった。
data.yaml_add_eol_comment("これはIdDefの行末のコメント", key="IdDef")

## 特定のキーの文末にコメントを追加 -> 上手く表示できない
# data["InputPorts"].yaml_add_eol_comment("これは要素0の文末のコメント", 1)

# 対象の場所にコメントを追加
for port in data["InputPorts"]:
    if port["Name"] == "port1_in":  # "port1_in"のエントリを特定
        port["PortType"].yaml_add_eol_comment(
            "This is a comment for Path of port1_in", key="Path"
        )

"""
YAMLファイルの出力
"""
out_path = in_path.replace("input/", "output/")
with open(out_path, "w") as stream:
    yaml.dump(data, stream=stream)


"""
デバッグ出力
"""
print(out_path)
print(data)
print(type(data))

for k, v in data.items():
    print(k, v)
