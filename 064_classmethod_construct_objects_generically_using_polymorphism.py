# @classmethodポリモルフィズムを使ってオブジェクトをジェネリックに構築する

# 特定のディレクトリ配下のテキストファイルの合計行数を出す処理

import os
from tempfile import TemporaryDirectory
from threading import Thread
from typing import List


class InputData(object):
    """
    入力データを表す共通クラス
    """

    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    """
    入力データオープンクラス
    """

    def __init__(self, path: str):
        super().__init__()
        self.path: str = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    """
    行数カウント用共通クラス
    """

    def __init__(self, input_data: str):
        self.input_data: str = input_data
        self.result: int = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    """
    行数カウントクラス
    """

    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir: str) -> PathInputData:
    """ インプット用のファイルパスを返却する

    Args:
        data_dir (str):

    Returns:
        PathInputData
    """

    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list: PathInputData) -> List[LineCountWorker]:
    """行数を持つworkerリストを作成する

    Args:
        input_list (List[str]):

    Returns:
        workers (List[LineCountWorker]):
    """
    workers: List[LineCountWorker] = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


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
    rest: LineCountWorker = workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def reduce_map(data_dir: str):
    inputs: PathInputData = generate_inputs(data_dir)
    workers = create_workers(inputs)
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
        result: int = reduce_map(tmpdir)
        print("result: ", result)


if __name__ == "__main__":
    main()
