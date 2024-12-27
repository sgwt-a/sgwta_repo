import os, sys

# 引数の取得
args = sys.argv
if len(args) == 2:
    # ファイル名
    file = args[1]
else:
    print("Error")
    exit(1)

# 挿入する字列
inserted_text = "AddString\n"

# 挿入位置 (例: 3行目の後に追記)
line_number = 3

# ファイルを読み込んで編集
with open(file, "r") as f:
    lines = f.readlines()

# debug
print(lines)

# 指定した行の後に文字列を追加
lines.insert(line_number, inserted_text)

# ファイルに書き戻す
with open(file, "w") as f:
    f.writelines(lines)

print(f"追記しました: {file}")
