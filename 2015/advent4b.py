import hashlib

input = 'yzbqklnj'

number = 0

while True:
    key = input + str(number)
    if hashlib.md5(key.encode()).hexdigest().startswith('000000'):
        break
    number += 1

print(number)