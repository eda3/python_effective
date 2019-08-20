from typing import List, Dict


def sort_priority(values: List[int], group: Dict[int]) -> None:
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


numbers: List[int] = [8, 3, 1, 2, 5, 4, 7, 6]
group: Dict[int] = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers, '\n')


# [2, 3, 5, 7, 1, 4, 6, 8]


def sort_priority2(numbers: List[int], group: Dict[int]) -> bool:
    found: bool = False

    def helper(x):
        if x in group:
            found: bool = True  # Looks easy
            return 0, x
        return 1, 0

    numbers.sort(key=helper)
    return found


found: bool = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
