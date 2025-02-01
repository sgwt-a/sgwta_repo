import numpy as np

"""
パーセプトロンを用いてAND, NAND, ORが作れる。
XORは作れないが、それらを組み合わせることで作れる。→　パーセプトロンの階層を深くすれば非線形も表現できる。
"""


def perceptron(x1, x2, w1, w2, b):
    x = np.array([x1, x2])  # input
    w = np.array([w1, w2])  # weight
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    return perceptron(x1, x2, w1, w2, b)


def NAND(x1, x2):
    w1, w2, b = -0.5, -0.5, 0.7
    return perceptron(x1, x2, w1, w2, b)


def OR(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.3
    return perceptron(x1, x2, w1, w2, b)


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)
