class TimesTwo(object):
    value = 0

    def __init__(self):
        self.value *= 2


def main():
    tw = TimesTwo()
    print("tw.values", tw.value)


if __name__ == "__main__":
    main()
