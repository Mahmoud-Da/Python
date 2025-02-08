letters = ["a", "b", "c", "d"]
print(letters[0])
# "a"

print(letters[-1])
# "d"


letters2 = ["a", "b", "c", "d"]
letters2[0] = "A"
print(letters2)
# ["A", "b", "c", "d"]


letters3 = ["A", "b", "c", "d"]
print(letters3[0:3])
# ['A', 'b', 'c']

print(letters3)
# ["A", "b", "c", "d"]

print(letters3[:3])
# ['A', 'b', 'c']

print(letters3[0:])
# ["A", "b", "c", "d"]

print(letters3[:])
# ["A", "b", "c", "d"]


print(letters3[::2])
# ['A', 'c']


numbers = list(range(10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])
# [0, 2, 4, 6, 8]

print(numbers[::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
