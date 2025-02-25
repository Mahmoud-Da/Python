from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# def draw(control):
#     control.draw()

ddl = DropDownList()
print(isinstance(ddl, UIControl))
# True

# draw(ddl)
# DropDownList

text_box = TextBox()
# draw(text_box)
# TextBox


def draw(controls):
    for control in controls:
        control.draw()


draw([ddl, text_box])
# DropDownList
# TextBox
