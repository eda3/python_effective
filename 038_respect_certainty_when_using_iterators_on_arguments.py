# 引数に対してイテレータを使うときには確実さを尊ぶ

from typing import List


def normalize(numbers: List[int]) -> List[float]:
    total: int = sum(numbers)
    result: List[float] = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits: List[int] = [15, 35, 80]
percentages: List[float] = normalize(visits)

print(percentages)
