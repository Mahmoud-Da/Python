class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud["PYTHON"])
# 3

# print(cloud.tags["PYTHON"])
# KeyError: 'PYTHON'


# print(cloud.__tags)
# AttributeError: 'TagCloud' object has no attribute 'tags'


print(cloud.__dict__)
# {'_TagCloud__tags': {'python': 3}}


print(cloud._TagCloud__tags)
# {'python': 3}
