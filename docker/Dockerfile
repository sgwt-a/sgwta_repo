# ベースイメージとして Ubuntu 20.04 を使用
FROM ubuntu:20.04

# 環境変数を設定して、ユーザー入力を無効化（インストール時の確認プロンプトを防ぐ）
ENV DEBIAN_FRONTEND=noninteractive

# 基本的な依存パッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    docker.io \
    gcc \
    g++ \
    git \
    git-lfs \
    python3 \
    python3-pip \
    python3-dev \
    sudo \
    unzip \
    wget \
    zip \
    ssh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python用の追加ライブラリをインストール（必要に応じて） ->  pip3 install 
RUN pip3 install \
    cpplint \
    gitpython \
    pre-commit \
    pyyaml==5.3.1 \
    pandas==1.5.3 \
    openpyxl==3.1.1 \
    jinja2 \
    ruamel.yaml==0.17.21 \
    panda3d \
    tqdm


# 作業ディレクトリの設定
WORKDIR /workspaces

# コンテナ起動時にbashを使用
#CMD [ "bash" ]
