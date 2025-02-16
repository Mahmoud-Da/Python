numbers = [1, 2, 3]
print(numbers)
# [1, 2, 3]

print(1, 2, 3)
# 1 2 3

print(*numbers)
# 1 2 3

values = list(range(5))
print(values)
# [0, 1, 2, 3, 4]

values = [*range(5)]
print(values)
# [0, 1, 2, 3, 4]

values = [*"Hello"]
print(values)
# ['H', 'e', 'l', 'l', 'o']

first = [1, 2]
second = [3]
values = [*first, *second]
print(values)
# [1, 2, 3]

values = [*first, "a", *second, *"Hello"]
print(values)
# [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
# {'x': 10, 'y': 2, 'z': 1}
