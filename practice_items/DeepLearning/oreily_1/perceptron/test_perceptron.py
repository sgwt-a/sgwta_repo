import pytest
from perceptron import AND, NAND, OR, XOR


@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)])
def test_AND(a, b, expected):
    assert AND(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)])
def test_NAND(a, b, expected):
    assert NAND(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)])
def test_OR(a, b, expected):
    assert OR(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)])
def test_XOR(a, b, expected):
    assert XOR(a, b) == expected
