items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


filtered = []
for item in items:
    if item[1] >= 10:
        filtered.append(item)

print(filtered)
# [('Productl', 10), ('Product3', 12)]

x = filter(lambda item: item[1] >= 10, items)
print(x)
# <filter object at 0x10317b1c0>


x = list(filter(lambda item: item[1] >= 10, items))
print(x)
# [('Product1', 10), ('Product3', 12)]
