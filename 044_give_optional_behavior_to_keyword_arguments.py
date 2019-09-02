# キーワード引数にオプションの振る舞いを与える


def remainder(number, divisor):
    return number % divisor


if __name__ == '__main__':
    assert remainder(20, 7) == 6
    assert remainder(20, divisor=7) == 6  # OK
    assert remainder(number=20, divisor=7) == 6  # OK
    assert remainder(divisor=7, number=20) == 6  # OK

    # 各引数は一回ずつ指定できる。下の書き方だと、numberが2回使われているためNG
    # assert remainder(20, number=20) == 6  # NG TypeError: remainder() got multiple values for argument 'number'
