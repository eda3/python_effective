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


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


if __name__ == "__main__":
    main()
