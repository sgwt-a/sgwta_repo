# pytest

## 導入
```bash
pip install pytest
```

## 実行方法（サンプル）
- 全ファイル実行
    ```bash
    pytest
    ```
- 特定ファイル実行
    ```bash
    pytest test/test_calc.py
    ```
- 特定関数実行
    ```bash
    pytest test/test_calc.py::test_sum
    ```
- オプション
   - 詳細結果：`-v`
   - 最初にエラーとなったテストで中断する：`-x`

## パラメータ設定

```python
# import calc_sum
import pytest

def test_sum():
    assert calc_sum(3, 4) == 7

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (0, 0, 0)
])    
def test_sum_param(a, b, expected):
    assert calc_sum(a, b) == expected
```
