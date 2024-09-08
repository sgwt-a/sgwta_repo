# sgwta_repo

## リポジトリのクローン

`git clone https://github.com/sgwt-a/sgwta_repo.git`


## コードスタイル

### Python
- PEP8
- チェックツール：black
  - インストール：`pip install black`
  - 実行コマンド：`black {/path/to/.py src}`
    - 指定したパス以下のpythonファイルを自動整形する


## pre-commit
### 導入
- インストール
  - コマンド
    - `pip install pre-commit` ※WSL上ではこっちで実施
    - `brew install pre-commit`  ※Macbook上ではこっちで実施  
  - 確認  
  下記コマンドでバージョンが表示されればインストール成功  
`pre-commit --version`
- .pre-commit-config.yamlの作成  
ルートディレクトリ直下に配置すること
- 設定の反映  
`pre-commit install`  
下記ログが表示されたら成功  
`pre-commit installed at .git/hooks/pre-commit`
- 参考
    - https://qiita.com/shun198/items/7352a5c67bb3284583d1

### 手動でpre-commitを実行してテスト
`pre-commit run --all-files`
