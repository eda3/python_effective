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


def normalize_copy(numbers: List[int]) -> List[float]:
    """引数をパーセント割合に変換する

    :param numbers: 変換したいリスト
    :return: 変換後リスト
    """
    numbers = list(numbers)  # イテレータをコピー
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

    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]

    print('---')

    # ファイルから訪問者を読み込み、パーセント割合に変換する
    path: str = 'data' + os.sep + '038_my_numbers.txt'
    it = read_visits(path)
    percentages = normalize(it)

    # イテレータは結果を一つしか出力しないので、空リストになる
    print('percentages:', percentages)  # []

    print('---')

    # ファイルから訪問者を読み込み、パーセント割合に変換する
    it = read_visits(path)
    percentages = normalize_copy(it)  # イテレータのコピーを作る

    # 期待通りの動きになるが、訪問者リストファイルが巨大だった場合、
    # メモリがクラッシュする可能性がある
    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]

    print('---')
