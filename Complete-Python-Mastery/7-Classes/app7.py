class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)
# before redefine the __eq__ magic method
print(point == other)
# False

# after redefine the __eq__ magic method
print(point == other)
# True

# before redefine the __gt__ magic method
print(point > other)
# TypeError: '>' not supported between instances of 'Point' and 'Point'

# after redefine the __gt__ magic method
point = Point(10, 20)
other = Point(1, 2)
print(point > other)
# True


print(point < other)
# False
