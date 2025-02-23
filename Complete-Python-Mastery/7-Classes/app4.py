class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
# Point (1, 2)

point.z = 10


another = Point(3, 4)
another.draw()
# Point (3, 4)


print(point.default_color)
# red
print(another.default_color)
# red
print(Point.default_color)
# red


Point.default_color = "Yellow"
print(point.default_color)
# Yellow
print(another.default_color)
# Yellow
print(Point.default_color)
# Yellow
