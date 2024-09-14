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


## Docker環境
### Dockerのインストール WSL(Windows)
- インストール
\\wsl$\Ubuntu-20.04\home\{username}にインストール用のシェルスクリプトを用意済み。  
下記コマンドを実行。  
./install_docker.sh
- 確認  
  - インストールされたことの確認  
    ```bash
    source ~/.bashrc
    sudo docker run hello-world
    ```
    次のようなメッセージが表示されれば成功
    ```bash
    Hello from Docker!
    This message shows that your installation appears to be working correctly.
    ～略～
    For more examples and ideas, visit:
    https://docs.docker.com/get-started/
    ```
  - バージョンの確認
    ```bash
    docker version
    ```

### Dockerのインストール Ubuntu(Macbook)
1. Dockerのインストール
下記リンク先を見てインストールする。  
https://docs.docker.com/engine/install/ubuntu/
1. sudoなしでdockerコマンドを実行できるようにするために、インストール後にManage Docker as a non-root userの手順を実施する。  
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
1. git LFSのインストール
    ```bash
    sudo apt update
    sudo apt install git-lfs
    git lfs install
    ```
### VSCode拡張機能
WSL上で下記をインストールする。  
→　コンテナ上で自動でインストールするようにdevcontainer.jsonに設定済み。
- Dev Container
- Bazel
- Git Graph
- Git History
