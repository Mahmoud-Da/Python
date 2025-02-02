def greet(name):
    print(f"Hi {name}")


print(round(1.9))
# 2


def get_greeting(name):
    return f"Hi {name}"


get_greeting("Moody")

print(get_greeting("Moody"))
# Hi Moody

message = get_greeting("Moody")
print(message)
# Hi Moody


# file = open("content.txt", "w")
# file.write(message)

print(greet("Moody"))
# Hi Moody
# None


def test(name):
    # print(f"Hi {name}")
    return "...."
