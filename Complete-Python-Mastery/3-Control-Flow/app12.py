number = 100
while number > 0:
    print(number)
    number //= 2

# 100
# 50
# 25
# 12
# 6
# 3
# 1

command = ""

while command != "exit":
    command = input(">")
    print("ECHO", command)


command = ""

while command != "exit" and command != "EXIT":
    command = input(">")
    print("ECHO", command)


command = ""

while command.lower() != "exit":
    command = input(">")
    print("ECHO", command)
