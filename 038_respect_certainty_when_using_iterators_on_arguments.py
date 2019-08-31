# 引数に対してイテレータを使うときには確実さを尊ぶ
import os
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


def read_visits(data_path: str) -> List[int]:
    """訪問者リストの取得

    :param data_path: 訪問者リストファイル格納パス
    :return: ジェネレータで１行ずつ返却
    """
    with open(data_path) as f:
        for line in f:
            yield int(line)


if __name__ == '__main__':
    # 訪問者数リスト
    visits: List[int] = [15, 35, 80]
    percentages: List[float] = normalize(visits)

    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]

    print('---')

    # ファイルから訪問者を読み込み、パーセント割合に変換する
    it = read_visits('data' + os.sep + '038_my_numbers.txt')
    percentages = normalize(it)

    # イテレータは結果を一つしか出力しないので、空リストになる
    print('percentages:', percentages)  # []
