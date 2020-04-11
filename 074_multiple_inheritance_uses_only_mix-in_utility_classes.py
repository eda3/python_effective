# 多重継承はmix-inユーティリティクラスだけに使う

from typing import Dict


class ToDictMixin(object):
    """Pythonのオプジェクトをメモリ内の表現からシリアライズできる辞書表現に変換する

    """

    def to_dict(self):
        """辞書型に変換

        Returns:


        """
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict: Dict):
        """辞書型に変換

        Args:
            instance_dict (Dict):

        Returns:
            Dict: 変換後の辞書型オプジェクト

        """
        output: Dict = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key: object, value: object):
        """

        Args:
            key (object):
            value (object):

        Returns:

        """
        if isinstance(value, ToDictMixin):
            print("## is ToDictMixin")
            print("")
            return value.to_dict()
        elif isinstance(value, dict):
            print("## is dict")
            print("")
            return self._traverse_dict(value)
        elif isinstance(value, list):
            print("## is list")
            print("")
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            print("## is __dict__")
            print("")
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    """mix-inを使った二分木辞書表現を作るクラス

    """

    def __init__(self, value, left=None, right=None):
        """

        Args:
            value ():
            left ():
            right ():
        """
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent


def main():
    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(11)),
    )
    print(tree)
    # tree = BinaryTree(10, 2)
    print(tree.to_dict())


if __name__ == "__main__":
    main()
