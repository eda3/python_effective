# @classmethodポリモルフィズムを使ってオブジェクトをジェネリックに構築する


class InputData(object):
    """ 入力データを表す共通クラス

    """

    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


if __name__ == "__main__":
    pass
