# shell command

## シーン１：txtファイルを複数生成し、そのtxtファイルの拡張子をcsvに変換する

### txtファイルを複数生成する
inputディレクトリを生成し、sample_000.txt~sample_100.txtを生成する。
```bash
mkdir -p input && for i in $(seq -w 0 100); do touch "input/sample_${i}.txt"; done
```
### txtファイルの拡張子をcsvに変換する
コマンド１
```bash
for file in input/*.txt; do mv "$file" "${file%.txt}.csv"; done
```
- `"${file%.txt}.csv"`は、${file}の末尾の.txtを削除して.csvに置き換えた新しいファイル名を生成します。

コマンド２
```bash
find input -type f -name "*.txt" | xargs -I {} bash -c 'mv "$1" "${1%.txt}.csv"' _ {}
```
コマンドの説明
1. find input -type f -name "*.txt":
   - inputディレクトリ内のすべての.txtファイルを検索します。
   - -type fはファイルのみを対象にします。
1. |:
    - 前のコマンドの出力を次のコマンドの入力に渡します。
1. xargs -I {} bash -c 'mv "$1" "${1%.txt}.csv"' _ {}:
   - xargsを使って、findで見つかったファイルを1つずつ処理します。
   - -I {}: プレースホルダ{}を指定して、findの出力を個別の引数として渡します。
1. bash -c 'mv "$1" "${1%.txt}.csv"' _ {}:
   - bash -cでコマンドを実行します。
   - "$1"には現在のファイル名（{}）が渡され、.txtを.csvに変更します。
   - "_ {}"はbash -cコマンドの引数。第一引数が"_"で第二引数が"{}"。第一引数はスクリプト名だが処理に不要なためダミーとして"_"を記載している。
