class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())
# python

print(text.duplicate())
# PythonPython


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


custom_list = TrackableList()
custom_list.append("1")
# Append Called
