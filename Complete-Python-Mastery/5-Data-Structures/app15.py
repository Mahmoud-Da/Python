point = (1, 2)
print(type(point))
# <class 'tuple'>

point = 1, 2
print(type(point))
# <class 'tuple'>

point = 1,
print(type(point))
# <class 'tuple'>

point = 1
print(type(point))
# <class 'int' >


point = ()
print(type(point))
# <class 'tuple' >


point = (1, 2) + (3,  4)
print(point)
# (1, 2, 3, 4)

point = (1, 2) * 3
print(point)
# (1, 2, 1, 2, 1, 2)


point = tuple([1, 2])
print(point)
# (1, 2)

point = tuple("Hello World")
print(point)
# ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')


point = (1, 2, 3)
print(point[0])
# 1

point = (1, 2, 3)
print(point[0:2])
# (1, 2)

point = (1, 2, 3)
x, y, z = point

point = (1, 2, 3)
if 10 in point:
    print("exist")

point = (1, 2, 3)
# point[0] = 10
# TypeError: 'tuple' object does not support item assignment
