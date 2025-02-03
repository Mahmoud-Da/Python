def greet():
    message = "a"


print(message)
# NameError: name 'message' is not defined


def greet(name):
    message = "a"


print(name)
# NameError: name 'name' is not defined


def greet(name):
    message = "a"


def send_email(name):
    message = "b"


great("moody")
# a

message = "a"


def greet(name):
    print(message)


print(great("moody"))
# a


message = "a"


def greet(name):
    message = "b"


print(message)
# a


message = "a"


def greet(name):
    global message
    message = "b"


print(message)
# b
