# 単純なインターフェースにはクラスの代わりに関数を使う
from collections import defaultdict
from typing import Dict, Tuple
from typing import List


def log_missing() -> int:
    print("Key added")
    return 0


def use_log_missing():
    current: Dict[str, int] = {"green": 12, "blue": 3}
    increments: List[Tuple[str, int]] = [("red", 5), ("blue", 17), ("orange", 9)]
    result = defaultdict(log_missing, current)
    print("Before:", dict(result))

    # currentのdictについて、incrementsから一つひとつキーチェックする
    # キーにマッチするものがあればそれの値に修正
    # キーにマッチしないものがなければ(defaultdictならば)、
    # 新規にキーと値を追加する（そして"Key added"を出力"
    for key, amount in increments:  # type: str, int
        result[key] += amount
    print("After: ", dict(result))

    # >> Before: {'green': 12, 'blue': 3}
    # >> Key added
    # >> Key added
    # >> After:  {'green': 12, 'blue': 20, 'red': 5, 'orange': 9}


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self) -> int:
        print("Key added")
        self.added += 1
        return 0


def use_class_count_missing() -> None:
    current: Dict[str, int] = {"green": 12, "blue": 3}
    increments: List[Tuple[str, int]] = [("red", 5), ("blue", 17), ("orange", 9)]
    """
    ヘルパークラスを利用した例。counter内のメソッドmissing()が状態を持つ。
    しかしこの書き方だと、CountMissingクラスの目的が何であるかわからず、
    誰がmissingメソッドを呼ぶのか分からない
    """
    counter = CountMissing()
    result = defaultdict(counter.missing, current)

    print("Before:", dict(result))

    for key, amount in increments:
        result[key] += amount
    print("counter.added:", counter.added)
    print("After:", dict(result))

    # >>  Before: {'green':12, 'blue':3}
    # >>  Key
    # >>  added
    # >>  Key
    # >>  added
    # >>  counter.added: 2
    # >>  After: {'green':12, 'blue':20, 'red':5, 'orange':9}


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self) -> int:
        print("Key added")
        self.added += 1
        return 0


def use_class_better_count_missing() -> None:
    current: Dict[str, int] = {"green": 12, "blue": 3}
    increments: List[Tuple[str, int]] = [("red", 5), ("blue", 17), ("orange", 9)]
    """
    特殊メソッド__call__を使うことで、そのクラスが関数引数として使われるということを示唆する。
    また、クラスの目的が状態を持つ関数として動くであるという手がかりを与える

    """
    counter = BetterCountMissing()
    result = defaultdict(counter, current)

    print("Before:", dict(result))

    for key, amount in increments:
        result[key] += amount
    print("counter.added:", counter.added)
    print("After:", dict(result))

    # >>  Before: {'green':12, 'blue':3}
    # >>  Key
    # >>  added
    # >>  Key
    # >>  added
    # >>  counter.added: 2
    # >>  After: {'green':12, 'blue':20, 'red':5, 'orange':9}


if __name__ == "__main__":
    # List型のsortメソッドにのオプションとしてkey引数を取り、
    # keyフックとしてlambda式を与えてソートする
    names: List[str] = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    names.sort(key=lambda x: len(x))
    print(names)
    # >>> ['Plato', 'Socrates', 'Archimedes', 'Aristotle']

    print("---")

    # 関数log_missingを利用する
    use_log_missing()

    print("---")

    # クラスCountMissingを利用する
    use_class_count_missing()

    print("---")

    # クラスBetterCountMissingを利用する
    use_class_better_count_missing()
