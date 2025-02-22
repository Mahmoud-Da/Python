try:
    file = open("app1.py")
    age = int(input("Age: "))
    x_factor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")


try:
    file = open("app1.py")
    age = int(input("Age: "))
    x_factor = 10 / age
    file.close()
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")


try:
    file = open("app1.py")
    age = int(input("Age: "))
    x_factor = 10 / age

except ValueError:
    print("You didn't enter a valid age")
    file.close()
else:
    print("No exception were thrown")


try:
    file = open("app1.py")
    age = int(input("Age: "))
    x_factor = 10 / age

except ValueError:
    print("You didn't enter a valid age")
    file.close()
else:
    print("No exception were thrown")
    file.close()


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
