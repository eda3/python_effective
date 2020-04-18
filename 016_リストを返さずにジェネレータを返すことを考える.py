def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])
# >>> [0, 5, 11]
print('')


def index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])
# >>> [0, 5, 11]
print('')
