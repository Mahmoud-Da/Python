from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox1(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList1(UIControl):
    def draw(self):
        print("DropDownList")


def draw1(controls):
    for control in controls:
        control.draw()


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()
