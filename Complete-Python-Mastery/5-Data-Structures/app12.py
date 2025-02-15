list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(zip(list1, list2))
# <zip object at 0x10063fc40>

print(list(zip(list1, list2)))
# [(1, 10), (2, 20), (3, 30)]


print(list(zip("abc", list1, list2)))
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
