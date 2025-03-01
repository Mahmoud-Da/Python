from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

# before __eq__
print(p1 == p2)
# False


print(id(p1))
# 4369148160

print(id(p2))
# 4370467408

# after __eq__
print(p1 == p2)
# True


Point1 = namedtuple("Point1", ["x", "y"])
new_p1 = Point1(1, 2)
new_p2 = Point1(1, 2)

new_p1 = Point1(x=1, y=2)
new_p2 = Point1(x=1, y=2)

print(new_p1 == new_p2)
# True

print(new_p1.x)
# 1

# new_p1.x = 10
# can't set attribute

new_p1 = Point1(x=1, y=2)
new_p1 = Point1(x=10, y=2)
