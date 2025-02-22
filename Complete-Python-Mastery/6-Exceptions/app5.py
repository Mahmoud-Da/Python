file = None
try:
    file = open("app1.py")
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
finally:
    file.close()


try:
    with open("app1.py") as file:
        print("File opened")
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")


try:
    with open("app1.py") as file:
        print("File opened")
        file.__enter__
        file.__exit__
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")


try:
    with open("app1.py") as file, open("another.txt") as target:
        print("File opened")
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
