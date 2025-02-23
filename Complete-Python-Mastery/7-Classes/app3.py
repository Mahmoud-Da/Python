class Point1:
    def draw(self):
        print("draw")


point = Point1()


class Point:
    def __init__(self, x, y):
        # self.x = 0
        self.x = x
        self.y = y

    def draw1(self):
        print("draw")

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
# 1

point.draw()
# Point (1, 2)

# point.draw(point)
