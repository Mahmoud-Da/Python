class EmployeeA:
    pass


class PersonA:
    pass


class ManagerA(EmployeeA, PersonA):
    pass


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manger = Manager()
manger.greet()
# Employee Greet


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
