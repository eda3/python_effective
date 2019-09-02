# 動的なデフォルト引数を指定するときにはNoneとドキュメンテーション文字列を使う

import time
from datetime import datetime as dt


def log(message: str, when: dt = dt.now()) -> None:
    print(f'{message}: {when}')


def log2(message: str, when: dt = None) -> None:
    """ タイムスタンプを入れつつログメッセージを出力

    Args:
        message: 表示するログメッセージ
        when: メッセージが発生した日時。デフォルトは現在時刻

    Returns:

    """
    when = dt.now() if when is None else when
    print(f'{message}: {when}')


if __name__ == '__main__':
    # log()のdt.now()は関数定義の1度のみ評価されるため、
    # 二回呼び出した際のタイムスタンプは同一になる
    log('Hi there!')
    time.sleep(1)
    log('Hi again!')
    print('---')

    # デフォルト引数をNoneにしておき、1度目と2度目の呼び出しで挙動を変える
    log2('Hi there!')
    time.sleep(1)
    log2('Hi again!')
    print('---')
