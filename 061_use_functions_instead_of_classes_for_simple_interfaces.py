from collections import defaultdict
from typing import Dict, Tuple

# 単純なインターフェースにはクラスの代わりに関数を使う
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
