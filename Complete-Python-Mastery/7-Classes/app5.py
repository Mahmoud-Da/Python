class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        # same as Point(0, 0)
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
# Point (1, 2)


point = Point(0, 0)
Point.zero()


# Point(0, 0, 1, "a")


zero_point = Point.zero()
zero_point.draw()
# Point (0, 0)
