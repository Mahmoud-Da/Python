import pdb


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))

# Start
# 6


def multiplyError(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiplyError(1, 2, 3))
# Start
# 1


def multiplyFixed(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiplyFixed(1, 2, 3))
# Start
# 1


def multiplyError2(*numbers):
    pdb.set_trace()
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiplyError2(1, 2, 3))
# Start
# 1
