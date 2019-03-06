import os
# with open('random.bin', 'w') as f:
#     f.write(os.urandom(10))

# >>>
# TypeError: must be str, not bytes

with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
