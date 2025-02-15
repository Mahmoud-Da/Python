numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
# {1, 2, 3, 4}


second = {1, 2, 3, 4}
second.add(5)
print(second)
# {1, 2, 3, 4, 5}

second.remove(5)
print(second)
# {1, 2, 3, 4}

print(len(second))
# 4


numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)
# {1, 2, 3, 4, 5}

print(first & second)
# {1}

print(first - second)
# {2, 3, 4}

print(first ^ second)
# {2, 3, 4, 5}


# print(first[0])
# TypeError: 'set' object is not subscriptable


if 1 in first:
    print("yes")
# yes
