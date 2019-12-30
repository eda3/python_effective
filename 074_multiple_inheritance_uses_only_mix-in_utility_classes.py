# 多重継承はmix-inユーティリティクラスだけに使う


class ToDictMixin(object):
    """Pythonのオプジェクトをメモリ内の表現からシリアライズできる辞書表現に変換する

    """

    def to_dict(self):
        """辞書型に変換

        Returns:

        """
        return self._traverse_dict(self.__dict__)


def main():
    pass


if __name__ == "__main__":
    main()
