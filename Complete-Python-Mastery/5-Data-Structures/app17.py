from array import array

[1, 2, 3]

numbers = array("i", [1, 2, 3])
print(numbers)
# array('i', [1, 2, 3])

numbers.append(4)
print(numbers)
# array('i', [1, 2, 3, 4])

numbers.insert(1, 9)
print(numbers)
# array('i', [1, 9, 2, 3, 4])

numbers.remove(9)
print(numbers)
# array('i', [1, 2, 3, 4])

numbers.pop()
print(numbers)
# array('i', [1, 2, 3])


# numbers[0] = 1.0
# TypeError: 'float' object cannot be interpreted as an integer
