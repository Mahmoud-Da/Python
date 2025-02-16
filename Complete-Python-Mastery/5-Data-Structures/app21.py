from sys import getsizeof
values = [x * 2 for x in range(10)]

for x in values:
    print(x)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

values = (x * 2 for x in range(10))
print(values)
# <generator object <genexpr> at 0x10429ea80>
for x in values:
    print(x)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18


values = (x * 2 for x in range(1000))
print(values)
# <generator object <genexpr> at 0x10429ea80>

print(getsizeof(values))
# 200
# 200 byte of memory


values = (x * 2 for x in range(1000000))
print(values)
# <generator object <genexpr> at 0x10429ea80>

print(getsizeof(values))
# 200

values = [x * 2 for x in range(1000000)]
print(values)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, ....]

print(getsizeof(values))
# 8448728
# 8448728 byte of memory


# values = (x * 2 for x in range(1000))
# print(values.len())
# AttributeError: 'generator' object has no attribute 'len'
