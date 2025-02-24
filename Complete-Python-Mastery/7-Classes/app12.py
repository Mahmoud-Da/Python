class Mammal1:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish1:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")


# Animal: Parent, Base
# Mammal: Child, Sub

class Animal2:
    def eat(self):
        print("eat")


class Mammal2(Animal2):
    def walk(self):
        print("walk")


class Fish2(Animal2):
    def swim(self):
        print("swim")


m = Mammal2()
m.eat()
m.walk()
# eat
# walk


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
# 1
