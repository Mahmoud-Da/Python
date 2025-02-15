point = {}

point = {"x": 1, "y": 2}
print(point)
# {'x': 1, 'y': 2}

list()
tuple()
set()
dict()

point = dict(x=1, y=2)
print(point)
# {'x': 1, 'y': 2}

print(point["x"])
# 1

# print(point[0])
# KeyError: 0


point["z"] = 20
print(point)
# {'x': 1, 'y': 2, 'z': 20}


# print(point["a"])
# KeyError: 'a'


if "a" in point:
    print(point["a"])


print(point.get("a"))
# None


print(point.get("a", 0))
# 0


del point["x"]
print(point)
# {'y': 2, 'z': 20}


for x in point:
    print(x)
# y
# z


for key in point:
    print(key, point[key])
# y 2
# z 20


for x in point.items():
    print(x)
# ('y', 2)
# ('z', 20)


for key, value in point.items():
    print(key, value)
# y 2
# z 20
