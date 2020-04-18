for i in range(3):
    print(f'Loop {i}')
else:
    print('Else block!')
# Loop 0
# Loop 1
# Loop 2
# Else block!

print('---')

for i in range(3):
    print(f'Loop {i}')
    if i == 1:
        break
else:
    print('Else block!')
# Loop 0
# Loop 1

print('---')

for x in []:
    print('Never runs')
else:
    print('For Else block!')
# For Else block!

print('---')

while False:
    print('Never runs')
else:
    print('While Else block!')
# While Else block!

print('---')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')
