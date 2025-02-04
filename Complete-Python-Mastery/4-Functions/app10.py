def fizz_buzz():
    for i in range(100):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        if i % 5 == 0:
            print("Buzz")
        if i % 3 == 0:
            print("Fizz")
        print(i)


fizz_buzz()


def fizz_buzz_without_loop(number):
    if int(number) % 5 == 0 and int(number) % 3 == 0:
        return "FizzBuzz"
    if int(number) % 5 == 0:
        return "Buzz"
    if int(number) % 3 == 0:
        return "Fizz"
    return int(number)


print(fizz_buzz_without_loop(3))
print(fizz_buzz_without_loop("3"))
print(fizz_buzz_without_loop(5))
print(fizz_buzz_without_loop("5"))
print(fizz_buzz_without_loop(15))
print(fizz_buzz_without_loop("15"))
print(fizz_buzz_without_loop(1))
print(fizz_buzz_without_loop("1"))

# Fizz
# Fizz
# Buzz
# Buzz
# FizzBuzz
# FizzBuzz
# 1
# 1
