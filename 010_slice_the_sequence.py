a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle tow:', a[3:-3])

print('---')

b = a
print('Before:a=', a)
print('Before:b=', b)
a[:] = [101, 102, 103]
assert a is b
print('After:a=', a)
print('After:b=', b)
