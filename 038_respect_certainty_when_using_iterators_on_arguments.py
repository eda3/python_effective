# 引数に対してイテレータを使うときには確実さを尊ぶ

from typing import List


def normalize(numbers: List[int]) -> List[float]:
    """引数をパーセント割合に変換する

    :param numbers: 変換したいリスト
    :return: 変換後リスト
    """
    total: int = sum(numbers)
    result: List[float] = []
    for value in numbers:
        percent: float = 100 * value / total
        result.append(percent)
    return result


if __name__ == '__main__':
    # 訪問者数リスト
    visits: List[int] = [15, 35, 80]
    percentages: List[float] = normalize(visits)

    print(percentages)
