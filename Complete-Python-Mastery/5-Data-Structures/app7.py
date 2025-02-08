numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
# [2, 3, 6, 8, 51]


numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)
# [51, 8, 6, 3, 2]


numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
# [2, 3, 6, 8, 51]

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers, reverse=True))
# [51, 8, 6, 3, 2]


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items. sort()
print(items)
# [('Product1', 10), ('Product2', 9), ('Product3', 12)]


# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]


# def sort_item(item):
#     return item[1]


# items. sort(sort_item)
# print(items)
# TypeError: sort() takes no positional arguments


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items. sort(key=sort_item)
print(items)
# [('Product2', 9), ('Product1', 10), ('Product3', 12)]
