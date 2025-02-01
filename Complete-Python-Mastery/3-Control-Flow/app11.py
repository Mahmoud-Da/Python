print(type(5))
# <class 'int'>
print(type(range(5)))
# <class 'range'>

# iterable
for x in range(5):
    print(x)
# 0
# 1
# 2
# 3
# 4

for x in "Python":
    print(x)

# P
# y
# t
# h
# o
# n


for x in ["Ali", "moody", 3, 4, 5]:
    print(x)

# Ali
# moody
# 3
# 4
# 5


shopping_cart = ["banana", "apple", "orange"]

for item in shopping_cart:
    print(item)
