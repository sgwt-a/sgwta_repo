# 上位ディレクトリのファイルの関数をimportするには下記のようにパスを追加する必要がある。
import sys, os

# 親ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import calc_sum, calc_diff
import pytest


def test_sum():
    assert calc_sum(3, 4) == 7


@pytest.mark.parametrize("a, b, expected", [(3, 5, 8), (-1, 1, 0), (0, 0, 0)])
def test_sum_param(a, b, expected):
    assert calc_sum(a, b) == expected


def test_diff():
    assert calc_diff(3, 4) == -1


@pytest.mark.parametrize("a, b, expected", [(3, 5, -2), (-1, 1, -2), (0, 0, 0)])
def test_diff_param(a, b, expected):
    assert calc_diff(a, b) == expected
