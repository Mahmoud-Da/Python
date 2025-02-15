x = 10
y = 11


z = x
x = y
y = z

print("x: ", x)
print("y: ", y)
# x:  11
# y:  10


x = 10
y = 11


x, y = y, x
# x, y = (11, 10)

print("x: ", x)
print("y: ", y)
# x:  11
# y:  10


a, b = 1, 2
# unpacking the tuple = define the tuple
