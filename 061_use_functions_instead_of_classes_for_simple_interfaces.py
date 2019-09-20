# 単純なインターフェースにはクラスの代わりに関数を使う
from typing import List


def log_missing() -> int:
    print("Key added")
    return 0


if __name__ == "__main__":
    # List型のsortメソッドにのオプションとしてkey引数を取り、
    # keyフックとしてlambda式を与えてソートする
    names: List[str] = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    names.sort(key=lambda x: len(x))
    print(names)
    # >>> ['Plato', 'Socrates', 'Archimedes', 'Aristotle']
