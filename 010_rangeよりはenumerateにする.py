from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= i << i

print(random_bits)

print('---')

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

print('---')

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')

print('---')

for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')

print('---')

for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
