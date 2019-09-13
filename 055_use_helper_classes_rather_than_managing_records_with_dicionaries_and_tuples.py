# 辞書やタプルで記録管理するよりもヘルパークラスを使う

from typing import Dict, List


class SimpleGradebook(object):
    """成績記録クラス
    学生集団の成績を記録するクラス
    """

    def __init__(self) -> None:
        self._grades: Dict[str, List[int]] = {}

    def add_student(self, name: str) -> None:
        """学生名追加メソッド
        _gradesに引数で与えた学生名を追加する

        Args:
            name (str): 学生名

        Returns:
            None
        """
        self._grades[name]: List[int] = []

    def report_grade(self, name: str, score: int) -> None:
        """スコア追加メソッド
        既存の学生のスコアを追加する

        Args:
            name (str): スコア追加対象の学生名
            score (int): 追加するスコア

        Returns:
            None
        """
        self._grades[name].append(score)

    def average_grade(self, name: str) -> float:
        """平均スコア取得メソッド
        nameで指定した学生の平均スコアを計算する

        Args:
            name (str): 平均スコア計算対象の学生名

        Returns:
            float: 平均スコア

        """
        grades: List[int] = self._grades[name]
        return sum(grades) / len(grades)

    def get_grades(self) -> Dict[str, List[int]]:
        """成績データ取得メソッド
        記録した成績データを取得する

        Returns:
            Dict[str, List[int]]: 成績データ

        """

        return self._grades


class BySubjectGradebook(object):
    """科目別成績記録クラス
    学生集団の成績を科目別に記録する
    まだギリギリ、DictとListで管理出来るが、型ヒントを見ると複雑になっているのが分かる
    """

    def __init__(self) -> None:
        self._grades: Dict[str, Dict[str, List[int]]] = {}

    def add_student(self, name: str) -> None:
        """学生名追加メソッド

        Args:
            name (str): 学生名

        Returns:
            None
        """
        self._grades[name]: Dict[str, List[int]] = {}

    def report_grade(self, name: str, subject: str, grade: int) -> None:
        """科目別スコア追加メソッド

        Args:
            name (str): スコア追加対象の学生名
            subject (str): 科目名
            grade (int): 追加するスコア

        Returns:
            None
        """
        by_subject: Dict[str, List[int]] = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name: str) -> float:
        """平均スコア取得メソッド

        Args:
            name (str): 学生名

        Returns:
            float: 平均スコア


        """
        by_subject: Dict[str, List[int]] = self._grades[name]
        total: int = 0
        count: int = 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


if __name__ == '__main__':
    # 追加する学生の名前を設定
    student_name: str = 'Isaac Newton'
    book: SimpleGradebook = SimpleGradebook()

    # 学生に複数の成績スコアを与え、平均点を表示
    book.add_student(student_name)
    book.report_grade(student_name, 100)
    book.report_grade(student_name, 0)
    print(book.average_grade(student_name))
    # >>> 50.0
    print('---')

    # 追加する学生の名前を設定
    student_name: str = 'Albert Einstein'
    book2: BySubjectGradebook = BySubjectGradebook()
    book2.add_student(student_name)
    book2.add_student('eda')
    book2.report_grade(student_name, 'Math', 75)
    book2.report_grade(student_name, 'Math', 65)
    book2.report_grade(student_name, 'Gym', 90)
    book2.report_grade(student_name, 'Gym', 95)
    print(book2.average_grade(student_name))
    # >>> 81.25
    print('---')
