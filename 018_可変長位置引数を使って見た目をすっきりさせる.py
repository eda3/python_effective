# 可変長位置引数を使って、見た目をすっきりさせる
from typing import List, Tuple


def log(message: str, values: List[int]) -> None:
    if not values:
        print(message)
    else:
        values_str: str = ', '.join((str(x) for x in values))
        print(f'{message}, {values_str}')


def log2(message: str, *values: Tuple[int]) -> None:
    if not values:
        print(message)
    else:
        values_str: str = ', '.join((str(x) for x in values))
        print(f'{message}, {values_str}')


if __name__ == '__main__':
    # スター引数を使わない場合、いちいち空リストを渡さないといけない
    print('# function log()')
    log('My number are', [1, 2])
    # これだとエラーになる
    # log('Hi there')
    log('Hi there', [])
    print('---')

    # 関数に可変長引数を用いることで、引数を省略することができる
    # 注意する点として、可変長引数を用いるとタプル型に変換される
    print('# function log2()')
    log2('My number are', 1, 2, 3)
    log2('Hi there')  # ずっと良い！
    print('---')

    # 可変長引数にリストを渡すときはスター演算子を使う
    favorites: List[int] = [7, 33, 99]
    log2('Favorite colors', *favorites)
