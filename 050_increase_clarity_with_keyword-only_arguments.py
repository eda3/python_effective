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
