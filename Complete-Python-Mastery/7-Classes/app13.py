# class Animal(object):
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
print(isinstance(m, Mammal))
# True

print(isinstance(m, Animal))
# True

print(isinstance(m, object))
# True

o = object()
# o.
# m.

print(issubclass(Mammal, Animal))
# True

print(issubclass(Animal, object))
# True
