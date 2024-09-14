#!/usr/bin/env bash
set -e

pwd

# git config
.devcontainer/setting_git_config.sh

# python: requirements.txtで指定したバージョンがインストールできないケースが多発したためコメントアウト。必要最低限のもののみDockerfileでインストールすることにした。
# pip3 install -r .devcontainer/requirements.txt

# pre-commit
## 上記のgit config設定をしないとpre-commitがエラーになる
pre-commit install
