

# class MyPoint

class Point:
    def draw(self):
        print("draw")


point = Point()
# point.

print(type(point))
# <class '__main__.Point'>

print(isinstance(point, Point))
# True

print(isinstance(point, int))
# False
