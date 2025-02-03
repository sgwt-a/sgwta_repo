# coding: utf-8
import sys, os

sys.path.append(os.pardir)

import numpy as np
import time
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000
train_size = x_train.shape[0]  # 60,000
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)  # 600

start = time.time()

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 勾配
    # grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)

    # 更新
    for key in ("W1", "b1", "W2", "b2"):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)

end = time.time()
print(f"実行時間: {end - start:.4f} 秒")  # backpropagation: 実行時間: 0.3782 秒/epoch
# numerical diff: 実行時間: 31.7738 秒/epoch

# display accuracy
import matplotlib.pyplot as plt

n_epoch = len(test_acc_list)
x = np.arange(n_epoch)
y_train = train_acc_list
y_test = test_acc_list

fig, ax = plt.subplots()

c1, c2 = "blue", "green"  # 各プロットの色
l1, l2 = "train acc", "test acc"  # 各ラベル

ax.set_xlabel("epoch")  # x軸ラベル
ax.set_ylabel("accuracy")  # y軸ラベル
ax.set_title("")  # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()  # 罫線
ax.set_xlim([0, n_epoch])  # x方向の描画範囲を指定
ax.set_ylim([0, 1])  # y方向の描画範囲を指定
ax.plot(x, y_train, color=c1, label=l1)
ax.plot(x, y_test, color=c2, label=l2)
ax.legend(loc=0)  # 凡例
# fig.tight_layout()  # レイアウトの設定
# plt.savefig('acc_numerical.png') # 画像の保存
plt.savefig("acc_backpropagation_hidden100.png")  # 画像の保存
# plt.show()
