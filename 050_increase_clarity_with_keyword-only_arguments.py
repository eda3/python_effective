# キーワード専用引数で明確さを高める


def safe_division(number: float, divisor: int, ignore_overflow: bool, ignore_zero_division: bool) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def safe_division_b(number: float, divisor: int,
                    ignore_overflow: bool = False, ignore_zero_division: bool = False) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def safe_division_c(number: float, divisor: int, *,
                    ignore_overflow: bool = False, ignore_zero_division: bool = False) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


if __name__ == '__main__':
    # 割り算でのfloatのオーバーフローが無視され、0が返される
    result: float = safe_division(1.0, 10 ** 500, True, False)
    print(result)  # 0

    result: float = safe_division(1.0, 0, False, True)
    print(result)  # inf

    print('---')

    # しかし、safe_division()の場合論理演算子を取り違う可能性がある
    # safe_division_b()の場合、キーワード引数を利用している
    # よりオプション利用性が増している
    result: float = safe_division_b(1.0, 10 ** 500, ignore_overflow=True)
    print(result)  # 0

    result: float = safe_division_b(1.0, 0, ignore_zero_division=True)
    print(result)  # inf
    print('---')

    # safe_division_b()の場合、以下のような位置引数を用いた呼び出しが使用可能となる
    print('位置引数を用いた古い呼び出し:safe_division_b')
    result: float = safe_division_b(1.0, 0, True, True)
    print(result)  # inf

    # save_division_c()のようにキーワード専用引数を使うことで、
    # 上記のような利用を使えないようにすることができる

    # この書き方だと、エラーになる
    # result: float = safe_division_c(1.0, 0, True, True)
    # エラー内容：TypeErrorTypeError: safe_division_c() takes 2 positional arguments but 4 were given

    # safe_division_cの場合、キーワード引数を指定する必要がある
    result: float = safe_division_c(1.0, 0, ignore_zero_division=True)
    print(result)
