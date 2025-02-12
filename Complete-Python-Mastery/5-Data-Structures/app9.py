items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []

for item in items:
    prices.append(item[1])

print(prices)
# [10, 9, 12]

x = map(lambda item: item[1], items)
print(x)

# <map object at 0x104f8b160>

x = map(lambda item: item[1], items)
for item in x:
    print(item)

# 10
# 9
# 12

x = list(map(lambda item: item[1], items))
print(x)
# [10, 9, 12]


prices = list(map(lambda item: item[1], items))
print(prices)
# [10, 9, 12]
