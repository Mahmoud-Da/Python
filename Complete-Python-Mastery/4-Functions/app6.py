def multiply(x, y):
    return x * y


result = multiply(2, 3)
print(result)
# 6


def multiply2(*numbers):
    print(numbers)


multiply2(2, 3, 4, 5)
# (2, 3, 4, 5)

[1, 2, 3, 4, 5, 6]


def multiply3(*numbers):
    for number in numbers:
        print(number)


multiply3(2, 3, 4, 5)


def multiply4(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


final_result = multiply4(2, 3, 4, 5)
print(final_result)
