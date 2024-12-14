# Supplementary Information

## 参考文献１

### URL
https://dev.classmethod.jp/articles/getting-started-with-pyyaml-and-ruamel-yaml/

### 要点
pythonでYAMLファイルを扱うには大きく`PyYAML`と`ruamel.yaml`の２つの選択肢がある。  
今回は仕事でも使う`ruamel.yaml`で勉強する。  

- 環境準備  
  1. LibYAML のインストール  
sudo yum install -y libyaml-devel
  1. ruamel.yaml のインストール  
pip install -U ruamel.yaml

<details><summary>pip install コマンドのオプション"-U"とは？</summary>

参考文献：https://www.task-notes.com/entry/20150810/1439175600  

"-U"オプションはパッケージのアップグレードを指定するオプション。    

その他、便利そうなオプション。  

```-r <file>``` でファイルに記載されたパッケージリストをまとめてインストールしてくれる。  
```bash
pip install -r requirements.txt
```
パッケージリストは下記のようにバージョン指定できる。  
```bash
numpy==1.9.2
pandas==0.16.2
python-dateutil==2.4.2
pytz==2015.4
scipy==0.16.0
six==1.9.0
```
下記コマンドでリストが生成できるらしい。  
freezeはインストール済みのパッケージを出力してくれるらしい。
```bash
pip freeze > requirements.txt
```
</details><br>

## ruamel.yaml と PyYAML の比較

| 特徴                       | ruamel.yaml                             | PyYAML                              |
|----------------------------|-----------------------------------------|-------------------------------------|
| **メンテナンス状況**        | 現在も積極的に開発・更新されている       | メンテナンスは限られている          |
| **YAMLバージョン対応**      | YAML 1.2 を完全サポート                 | YAML 1.1 に部分対応                 |
| **コメントの保持**          | 読み込んだファイルのコメントを保持可能   | コメントは保持されない              |
| **書式の柔軟性**            | インデントや引用符などを詳細に制御可能   | 書式の制御は限定的                  |
| **APIの使いやすさ**         | 柔軟だが、設定がやや複雑な場合がある     | シンプルで初心者に適している         |
| **パフォーマンス**          | 高機能である分、やや遅い場合がある       | 比較的高速                           |
| **インストール方法**        | `pip install ruamel.yaml`               | `pip install pyyaml`                |
| **ドキュメントの充実度**    | ドキュメントはあるが、分かりにくい場合がある | ドキュメントが簡潔で分かりやすい   |
| **主な用途**               | 設定ファイルの詳細制御やコメント保持が必要な場合 | シンプルなYAML操作が必要な場合   |
| **Unicode対応**            | 優れている                               | 十分に対応                          |
| **安全性**                 | 安全な読み込み（`safe_load`）対応        | 安全な読み込み（`safe_load`）対応   |
| **依存関係**               | 独立して動作                             | 独立して動作                         |

### 選択のポイント

#### ruamel.yaml が適している場合
- YAML 1.2 の完全サポートが必要。
- コメントや書式を保持しながらYAMLを編集したい。
- 書式や出力の柔軟なカスタマイズが必要。

#### PyYAML が適している場合
- 基本的なYAMLの読み書きだけで十分。
- 高速に処理したい。
- シンプルで学習コストが低いツールを使いたい。

### 具体例
下記のサンプルのYAMLファイルに対してload/dumpするケースで違いを記載する。  
```yaml
Description: sample1
IdDef: XXXXXXXXXX
# comment 1
InputPorts:
- Name: port1_in
  IdDef: AAAAAAAAAA
  Description: "port1"
  PortType:
    Path: InCompo1/Int
    Id: ZZZZZ
  ConnectedPort:
    Path: InCompo1/port1  # comment
    Id: QQQQQ
```
### ruamel.yaml

#### import等の準備
```python
import ruamel.yaml
yaml = ruamel.yaml.YAML()
```
### load/dump
```python
with open(in_path) as stream:
    data = yaml.load(stream)
out_path = in_path.replace("input/", "output/")
with open(out_path, "w") as stream:
    yaml.dump(data, stream=stream)
```
### 出力ファイル
ポイント
- `#`のコメント文が出力される
- 値のダブルクォーテーションは削除される
```yaml
Description: sample1
IdDef: XXXXXXXXXX
# comment 1
InputPorts:
- Name: port1_in
  IdDef: AAAAAAAAAA
  Description: port1
  PortType:
    Path: InCompo1/Int
    Id: ZZZZZ
  ConnectedPort:
    Path: InCompo1/port1  # comment
    Id: QQQQQ
```


### yaml

#### import等の準備
```python
import yaml
```
### load/dump
```python
with open(in_path) as stream:
    data = yaml.load(stream)
out_path = in_path.replace("input/", "output/")
with open(out_path, "w") as stream:
    yaml.dump(data, stream=stream)
```
### 出力ファイル
ポイント
- `#`のコメント文が出力されない
- 値のダブルクォーテーションは削除される
```yaml
Description: sample1
IdDef: XXXXXXXXXX
InputPorts:
- ConnectedPort:
    Id: QQQQQ
    Path: InCompo1/port1
  Description: port1
  IdDef: AAAAAAAAAA
  Name: port1_in
  PortType:
    Id: ZZZZZ
    Path: InCompo1/Int
```


## ruamel.yamlで出力時にインデントを指定する方法

`ruamel.yaml`では、`yaml.indent()`メソッドを使用して、YAMLの出力時のインデントをカスタマイズできます。

### インデントの設定例

以下は、マッピング（辞書）やシーケンス（リスト）のインデント幅を指定してYAMLを出力する例です。

```python
from ruamel.yaml import YAML

yaml = YAML()
yaml.indent(mapping=4, sequence=2, offset=2)  # インデントを設定

data = {
    'key1': 'value1',
    'key2': {
        'nested_key1': 'nested_value1',
        'nested_key2': ['item1', 'item2']
    }
}

# YAMLファイルに出力
with open('output.yaml', 'w') as file:
    yaml.dump(data, file)
```

### yaml.indent() メソッドの引数
- mapping: マッピング（辞書）のインデント幅を指定します（デフォルト: 2）。
- sequence: シーケンス（リスト）のインデント幅を指定します（デフォルト: 2）。
- offset: マッピングのキーと値の間のスペース幅を指定します（デフォルト: 0）。

### 出力例
上記のコードを実行すると、次のようなYAMLが生成されます。
```yaml
コードをコピーする
key1: value1
key2: 
    nested_key1: nested_value1
    nested_key2: 
      - item1
      - item2
```

## コメントの追加

### 新しいコメントをプログラムで追加する
```python
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

yaml = YAML()
data = CommentedMap()
data['key1'] = 'value1'
data['key2'] = 'value2'

# コメントを追加
data.yaml_set_comment_before_after_key('key1', before="これはkey1の説明コメント")
data.yaml_set_comment_before_after_key('key2', after="横のコメント")

# YAMLファイルに書き出し
with open('output.yaml', 'w') as file:
    yaml.dump(data, file)
```
### 出力結果
```yaml
# これはkey1の説明コメント
key1: value1
key2: value2  # 横のコメント
```
