class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other = Point(1, 2)

print(point + other)
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'


print(point + other)
# <__main__.Point object at 0x100bea520>


combined = point + other
print(combined.x)
# 2
