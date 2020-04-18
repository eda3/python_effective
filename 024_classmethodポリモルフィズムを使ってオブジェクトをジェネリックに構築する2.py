# @classmethodポリモルフィズムを使ってオブジェクトをジェネリックに構築する

# 特定のディレクトリ配下のテキストファイルの合計行数を出す処理

import os
from tempfile import TemporaryDirectory
from threading import Thread
from typing import List, Dict


class GenericInputData(object):
    """
    ジェネリックな入力データを表す共通クラス
    """

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    """
    入力データオープンクラス
    """

    def __init__(self, path: str):
        super().__init__()
        self.path: str = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config: Dict[str]) -> str:
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    """
    ジェネリックな行数カウント用共通クラス
    """

    def __init__(self, input_data: str):
        self.input_data: str = input_data
        self.result: int = 0

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(
        cls, input_class: PathInputData, config: Dict[str]
    ) -> List["GenericWorker"]:
        """ 入力データに対する操作を行うインスタンスworkerを作成する

        Args:
            input_class (PathInputData):
            config (Dict[str]):

        Returns:
            workers (List["GenericWorker"]):

        """
        workers: List[GenericWorker] = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    """
    行数カウントクラス
    """

    def map(self):
        data = self.input_data.read()
        self.result: int = data.count("\n")

    def reduce(self, other):
        self.result += other.result


def execute(workers: List[LineCountWorker]) -> int:
    """
    Args:
        workers (List[LineCountWorker]):

    Returns:
        first.result (int):

    """
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first: LineCountWorker = workers[0]
    rest: List[LineCountWorker] = workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def reduce_map(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


def write_test_files(tmpdir: str):
    """試験用のファイルを作成する

    Args:
        tmpdir (str):

    Returns:
        None
    """
    with open(os.path.join(tmpdir, "test.txt"), "w") as f:
        f.write("aaaaaa\nbbbbbbbb\nccccccccc\n")

    with open(os.path.join(tmpdir, "test2.txt"), "w") as f:
        f.write("AAAAA\nBBBBBBBB\nCCCCCC\n")


def main():
    with TemporaryDirectory() as tmpdir:
        write_test_files(tmpdir)
        config: Dict[str] = {"data_dir": tmpdir}

        result: int = reduce_map(LineCountWorker, PathInputData, config)
        print("result: ", result)


if __name__ == "__main__":
    main()
