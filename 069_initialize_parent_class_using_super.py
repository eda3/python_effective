def main():
    tw = TimesTwo()
    print("tw.values", tw.value)

    pf = PlusFive()
    print("pf.value", pf.value)

    foo = OneWay(5)
    print("First ordering is ( 5 * 2 ) + 5 = ", foo.value)


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


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


if __name__ == "__main__":
    main()
