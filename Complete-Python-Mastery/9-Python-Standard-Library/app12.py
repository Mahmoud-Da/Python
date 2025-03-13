import random
import string

print(random.random())
# 0.7764312619933015

print(random.randint(1, 10))
# 9

print(random.choice([1, 2, 3, 4]))
# 2

print(random.choices([1, 2, 3, 4], k=2))
# [4, 2]

print(random.choices("abcdefghi", k=4))
# ['i', 'c', 'i', 'd']

print("".join(random.choices("abcdefghi", k=4)))
# cddg

print(",".join(random.choices("abcdefghi", k=4)))
# c,b,c,b

print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

print(string.digits)
# 0123456789

print("".join(random.choices(string.ascii_lowercase + string.digits, k=9)))
# 9qd99f64n

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
# [3, 4, 2, 1]
