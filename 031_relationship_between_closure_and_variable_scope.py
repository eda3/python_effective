from typing import List, Set


def sort_priority(values: List[int], group: Set[int]) -> None:
    def helper(x: int):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


numbers: List[int] = [8, 3, 1, 2, 5, 4, 7, 6]
group: Set[int] = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers, '\n')


# [2, 3, 5, 7, 1, 4, 6, 8]


def sort_priority2(numbers: List[int], group: Set[int]) -> bool:
    found: bool = False

    def helper(x: int):
        if x in group:
            found: bool = True  # Looks easy
            return 0, x
        return 1, 0

    numbers.sort(key=helper)
    return found


found: bool = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
print('')


def sort_priority3(numbers: List[int], group: Set[int]) -> None:
    found: bool = False

    def helper(x: int):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x

    numbers.sort(key=helper)


found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
