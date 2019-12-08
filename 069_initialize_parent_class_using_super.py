def main():
    tw = TimesTwo()
    print("tw.values", tw.value)

    pf = PlusFive()
    print("pf.value", pf.value)


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesTwo(object):
    value = 0

    def __init__(self):
        self.value *= 2


class PlusFive(object):
    value = 0

    def __init__(self):
        self.value += 5


if __name__ == "__main__":
    main()
