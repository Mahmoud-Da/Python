numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]


first, second, third = numbers

# first, second = numbers
# ValueError: too many values to unpack (expected 2)


numbers2 = [1, 2, 3, 4, 4, 2, 1]
first, second, *other = numbers2
print(first, second)
# 1 2
print(other)
# [3, 4, 4, 2, 1]


def multiple(*args):
    return args


print(multiple(1, 2, 3, 4, 5))
# (1, 2, 3, 4, 5)


numbers3 = [1, 2, 3, 4, 4, 2, 9]
first, *other, last = numbers3
print(first, last)
# 1 9
print(other)
# [2, 3, 4, 4, 2]
