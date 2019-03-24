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
