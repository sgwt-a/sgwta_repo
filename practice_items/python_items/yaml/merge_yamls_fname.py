import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True  # ダブルクォーテーションを保持（インデントは保持されない）


def merge_yaml(file1_path, file2_path, output_path):
    # YAMLファイルを読み込む
    with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
        data1 = yaml.load(f1)
        data2 = yaml.load(f2)

    # `DefineInterface.UpdateSignals` を統合
    update_signals1 = data1.get("DefineInterface", {}).get("UpdateSignals", [])
    update_signals2 = data2.get("DefineInterface", {}).get("UpdateSignals", [])

    # fnameをキーとしてマージ
    merged_signals = {}

    # デバッグ出力
    print(update_signals1)
    print(update_signals2)
    print(update_signals1 + update_signals2)

    for signal in update_signals1 + update_signals2:
        print(signal)
        fname = signal["fname"]
        if fname not in merged_signals:
            merged_signals[fname] = {"fname": fname, "signals": []}
        merged_signals[fname]["signals"].extend(signal["signals"])

    # 結果をリストに変換
    merged_signals_list = list(merged_signals.values())

    # デバッグ出力
    print("merged_signals ", merged_signals)
    print("merged_signals.values() ", merged_signals.values())
    print("merged_signals_list ", merged_signals_list)

    # data1の内容にマージ結果を反映
    data1["DefineInterface"]["UpdateSignals"] = merged_signals_list

    # 結果を新しいファイルに保存
    with open(output_path, "w") as output_file:
        yaml.dump(data1, output_file)


# 使用例
args = sys.argv
file1 = args[1]
file2 = args[2]
output_file = args[3]
merge_yaml(file1, file2, output_file)
