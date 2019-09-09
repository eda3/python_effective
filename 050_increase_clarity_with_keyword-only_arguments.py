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
        if ignore_overflow:
            if ignore_zero_division:
                return float('inf')
            else:
                raise


if __name__ == '__main__':
    result: float = safe_division(1.0, 10 ** 500, True, False)
    print(result)  # 0
