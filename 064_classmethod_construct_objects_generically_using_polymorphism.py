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


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


if __name__ == "__main__":
    pass
