# src/__init__.pyが存在する場合にimport可能
from src import calc_sum, calc_diff

# src/__init__.pyが存在しない場合でもimport可能
# from src.sum import calc_sum
# from src.diff import calc_diff


if __name__ == "__main__":
    x = calc_sum(1, 2)
    y = calc_sum(10, 100)
    answer = y - x
    print(answer)  # 107
