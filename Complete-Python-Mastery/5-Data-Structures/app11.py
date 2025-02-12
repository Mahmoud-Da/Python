items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)
# [10, 9, 12]

# [expression for item in items]
prices = [item[1] for item in items]
print(prices)
# [10, 9, 12]


# [expression for item in items if statement]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# [('Product1', 10), ('Product3', 12)]


filtered = [item for item in items if item[1] >= 10]
print(filtered)
# [('Product1', 10), ('Product3', 12)]
