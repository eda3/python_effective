# 引数に対してイテレータを使うときには確実さを尊ぶ
import os
from typing import List, Callable, NewType


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


def normalize_func(get_iter: Callable) -> List[float]:
    """引数をパーセント割合に変換する

    :param get_iter: 変換したいリスト
    :return: 変換後リスト
    """
    total: int = sum(get_iter())
    result: List[float] = []
    for value in get_iter():
        percent: float = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):
    def __init__(self, data_path: str) -> None:
        self.data_path: str = data_path

    def __iter__(self) -> List[int]:
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers: ReadVisits):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')  # イテレータなので良くない！コンテナ型にするべし
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

    print('normalize(visits)')
    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]
    print('---')

    # ファイルから訪問者を読み込み、パーセント割合に変換する
    path: str = 'data' + os.sep + '038_my_numbers.txt'
    it = read_visits(path)
    percentages = normalize(it)

    # イテレータは結果を一つしか出力しないので、空リストになる
    print('normalize(it)')
    print('percentages:', percentages)  # []
    print('---')

    # ファイルから訪問者を読み込み、パーセント割合に変換する
    it = read_visits(path)
    percentages = normalize_copy(it)  # イテレータのコピーを作る

    # 期待通りの動きになるが、訪問者リストファイルが巨大だった場合、
    # メモリがクラッシュする可能性がある
    print('normalize_copy(it)')
    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]
    print('---')

    # 期待通りの動きになるが、訪問者リストファイルが巨大だった場合、
    # 呼ばれるたびに新たなイテレータを返す関数を渡してあげれば、
    # 巨大なファイル読み込み問題は回避できる
    # しかし、引数にlambda式を入れ込むのはめんどい
    percentages = normalize_func(lambda: read_visits(path))
    print('normalize_func(it)')
    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]
    print('---')

    # イテレータプロトコルを実装したコンテナクラスを利用することで、
    # normalize()を修正しなくても期待通りの動きになる
    # ReadVisits = NewType('ReadVisits', List[int])
    visits_rv: ReadVisits = ReadVisits(path)
    percentages = normalize_defensive(visits_rv)
    print('class ReadVisits')
    print('percentages:', percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]
    print('---')
