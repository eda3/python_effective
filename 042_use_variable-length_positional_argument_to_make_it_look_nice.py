from typing import List


def log(message: str, values: List[int]) -> None:
    if not values:
        print(message)
    else:
        values_str: str = ', '.join((str(x) for x in values))
        print(f'{message}, {values_str}')


if __name__ == '__main__':
    # スター引数を使わない場合、いちいち空リストを渡さないといけない
    print('# function log()')
    log('My number are', [1, 2])
    log('Hi there', [])
    print('---')
