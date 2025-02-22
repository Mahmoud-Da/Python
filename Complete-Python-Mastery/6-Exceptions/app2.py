try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")

# Age: 10
# Age: a
# You didn't enter a valid age


try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")
print("Execution continue")

# Age: a
# You didn't enter a valid age
# Execution continue


try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("Execution continue")

# Age: 10
# No exception were thrown
# Execution continue

# Age: a
# You didn't enter a valid age
# Execution continue


try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("No exception were thrown")
print("Execution continue")

# Age: a
# You didn't enter a valid age
# invalid literal for int() with base 10: 'a'
# <class 'ValueError'>
# Execution continue
