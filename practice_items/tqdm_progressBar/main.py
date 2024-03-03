from tqdm import tqdm
from time import sleep

## range
for i in tqdm(range(10000000)):
    pass

## list
str = "sagawa"
for i in tqdm(str, desc="[list]", postfix="postfix"):
    #print(i)    # "s", "a", "g", "a", "w", "a"
    sleep(0.3)

## enumerate
with tqdm(str) as pbar:
    for i, word in enumerate(pbar):
        #print(i, word)    # "0 s", "1 a", "2 g", "3 a", "4 w", "5 a"
        pbar.set_description("[enumerate]")    # with tqdm(str) as pbar: でやらないと上手く表示されない
        pbar.set_postfix({"i":i, "word":word})
        sleep(0.3)

## 自分で新ty北を設定
pbar = tqdm(total=100)
for i in range(100):
    pbar.update(1)
    sleep(0.1)



## 複数のバーを表示
# きれいに表示できない
import random
from multiprocessing import Pool, freeze_support, RLock

L = 8

def long_time_process(p):
    info = f'#{p:>2} '  # 進捗バーの左側に表示される文字列
    for _ in tqdm(range(20), desc=info, position=p+1):
        sleep(random.random())
    return p * 2

if __name__ == '__main__':
    freeze_support()  # Windows のみ必要
    with Pool(L,
             # Windows のみ必要
             initializer=tqdm.set_lock, initargs=(RLock(),)) as p:
             result = p.map(long_time_process, range(L))
    print("\n" * L)  # tqdm終了後のカーソル位置を最下部に持ってくる
    print(result)