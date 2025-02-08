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


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# lambda parameters: expression
items. sort(key=lambda item: item[1])
print(items)
# [('Product2', 9), ('Product1', 10), ('Product3', 12)]
