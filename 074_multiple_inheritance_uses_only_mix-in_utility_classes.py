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

        Returns:

        """
        return self._traverse_dict(self.__dict__)

    def _traverse(self, key, value):
        """

        Args:
            key ():
            value ():

        Returns:

        """
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


def main():
    pass


if __name__ == "__main__":
    main()
