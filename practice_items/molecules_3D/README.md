# 3D分子ビューアー

## 概要
日経ソフトウェア2024年9月号

## 環境準備

`pip install panda3d`

### 注意
Docker環境では本プログラムは動作しない。
ChatGPT：「Docker環境では物理デバイス（マウスやキーボード）が存在しないため、/dev/input に関連するエラーは無視するしかありません。」


## PDBj
タンパク質の結晶構造データベース

https://pdbj.org/?lang=ja

## 実行方法
draw_molecular_structure.pyの末尾にて表示させたいpdbファイルを選択し、コマンドで実行。  
`python3 draw_molecular_structure.py`
