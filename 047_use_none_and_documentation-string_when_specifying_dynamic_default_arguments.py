# 動的なデフォルト引数を指定するときにはNoneとドキュメンテーション文字列を使う

import time
from datetime import datetime as dt


def log(message: str, when: dt = dt.now()):
    print(type(when))
    print(f'{message}: {when}')


if __name__ == '__main__':
    # log()のdt.now()は関数定義の1度のみ評価されるため、
    # 二回呼び出した際のタイムスタンプは同一になる
    log('Hi there!')
    time.sleep(1)
    log('Hi again!')
    print('---')
