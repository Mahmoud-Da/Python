values = []
for x in range(5):
    values.append(x * 2)

print(values)
# [0, 2, 4, 6, 8]

# [expression for item in items]
values = []
values = [x * 2 for x in range(5)]
values.append(values)
print(values)
# [0, 2, 4, 6, 8, []]

values = []  # This is an empty list
values = [x * 2 for x in range(5)]  # This creates a list [0, 2, 4, 6, 8]
# This appends the empty list values to original values which is empty array
values.append(values)
print(values)  # The output is [0, 2, 4, 6, 8, []]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
# [1, 2, 3, 4, 5, 6]

values = []
values = [x * 2 for x in range(5)]
values.extend(values)
print(values)
# [0, 2, 4, 6, 8]


values = {x * 2 for x in range(5)}
print(values)
# {0, 2, 4, 6, 8}

{1, 2, 3, 4}  # sets
{1: "a", 2: "b"}  # dictionaries


values = {x: x * 2 for x in range(5)}
print(values)
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

values = {}
for x in range(5):
    values[x] = x * 2
print(values)
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


values = (x * 2 for x in range(5))
print(values)
# <generator object <genexpr> at 0x10461ea80>
