from urllib import parse
my_values = parse.parse_qs('red=5&blue=0&green=', keep_blank_values=True)

print(my_values)
print(repr(my_values))

print('Red', my_values.get('red'))
print('Green', my_values.get('green'))
print('Opacity', my_values.get('opacity'))

print('================')

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print(f'Red    :   {red}')
print(f'Green  :   {green}')
print(f'Opasity:   {opacity}')

print('================')

# User helper function as it isn't easy to read on one line


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')

print(f'Red    :   {red}')
print(f'Green  :   {green}')
print(f'Opasity:   {opacity}')
