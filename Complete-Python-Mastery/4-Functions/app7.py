def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)
# {'id': 1, 'name': 'John', 'age': 22}


def save_user2(**user):
    print(user["id"])


save_user2(id=1, name="John", age=22)
# 1


def save_user3(**user):
    print(user["name"])


save_user3(id=1, name="John", age=22)
# John
