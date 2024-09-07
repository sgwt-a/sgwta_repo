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
