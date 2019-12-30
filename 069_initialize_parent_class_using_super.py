def main():
    tw = TimesTwo()
    print("tw.values", tw.value)

    pf = PlusFive()
    print("pf.value", pf.value)

    foo = OneWay(5)
    print("First ordering is ( 5 * 2 ) + 5 = ", foo.value)

    bar = AnotherWay(5)
    print("Second ordering still is", bar.value)

    print("")
    tf = TimesFive(5)
    print("tf.value", tf.value)

    pt = PlusTwo(2)
    print("pt.value", pt.value)

    print("")

    tw = ThisWay(5)
    print("# ダイヤモンド継承しているため、27と出てほしいところが7になってしまう")
    print("Should be ( 5 * 5) + 2 = 27 but is", tw.value)
    # >>> Should be ( 5 * 5) + 2 = 27 but is 7


class MyBaseClass(object):
    value = 0

    def __init__(self, value):
        print("MyBaseClass() before", self.value)
        self.value = value
        print("MyBaseClass() after", self.value)


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


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        print("TimesFive() before", self.value)
        self.value *= 5
        print("TimesFive() after", self.value)


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        print("PlusTwo() before", self.value)
        self.value += 2
        print("PlusTwo() after", self.value)


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


if __name__ == "__main__":
    main()
