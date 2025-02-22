try:
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("Execution continue")

# Age: 0
# Traceback(most recent call last):
#     File "app3.py", line 3, in <module >
#     x_factor = 10 / age
#     ~~~ ^ ~~~~
# ZeroDivisionError: division by zero


try:
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exception were thrown")
print("Execution continue")

# Age: 0
# Age cannot be 0
# Execution continue


try:
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("Execution continue")


try:
    age = int(input("Age: "))
    x_factor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("Execution continue")

# Age: 0
# You didn't enter a valid age
# Execution continue


try:
    age = int(input("Age: "))
    x_factor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("Execution continue")

# Age: 0
# You didn't enter a valid age
# Execution continue
