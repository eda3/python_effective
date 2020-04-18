# Bad writing
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x = 0
y = 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is a mistake!
