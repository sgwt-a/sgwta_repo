# Supplementary Information

## 要点
Pythonで何かしら時間のかかる処理をする際にプログレスバーを表示するのに便利なライブラリとして `tqdm`というものが存在します  

- 環境準備  
  1. tqdm のインストール  
pip install tqdm

- 基本的な使い方
```
from tqdm import tqdm

for i in tqdm(range(1000000)):
    pass
```
## 参考文献

### 基本的な使い方
https://qiita.com/SeeLog/items/73c054a37722890b17a2

### 複数のバーを同時表示（きれいに表示できない、、）
https://qiita.com/nkato_/items/9e2c75013d44050851ed
