# coding: utf-8
import sys, os

sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, flatten=True, one_hot_label=False
    )
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


import time

start = time.time()

x, t = get_data()
network = init_network()
print(
    "sample_weight.pkl parameter: ", list(network.keys())
)  # ['b2', 'W1', 'b1', 'W2', 'W3', 'b3']

accuracy_cnt = 0
fail_data = []
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)  # 最も確率の高い要素のインデックスを取得
    if p == t[i]:
        accuracy_cnt += 1
    else:  # 判定失敗した画像を保存
        fail_data.append([i, x[i], t[i], p])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

end = time.time()
print(f"実行時間: {end - start:.4f} 秒")


# 判定失敗した画像を保存
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


for i, img, label, p in fail_data:
    # print(img, label)
    img = img.reshape(28, 28) * 255  # 値を 0〜255 にスケール
    # img_show(img)
    # print(np.uint8(img))
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.save("fail_data/fail_num_{}_label_{}_pred_{}.png".format(i, t[i], p))
