class Animal1:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal1(Animal1):
    def __init__(self):
        self.wight = 2

    def walk(self):
        print("walk")


m = Mammal1()
# print(m.age)
# AttributeError: 'Mammal' object has no attribute 'age'
print(m.wight)
# 2


class Animal2:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal2(Animal2):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.wight = 2

    def walk(self):
        print("walk")


m = Mammal2()
print(m.age)
print(m.wight)
# Animal Constructor
# Mammal Constructor
# 1
# 2


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.wight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.wight)
# Mammal Constructor
# Animal Constructor
# 1
# 2
