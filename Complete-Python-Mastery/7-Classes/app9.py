class TagCloud:
    def __init__(self):
        self.tags = {}

    # def add(self, tag):
    #     self.tags[tag] = self.tags.get(tag, 0) + 1

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


# cloud = TagCloud()
# len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)

cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)
# {'python': 3}


# before we add lower method
cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)
# {'Python': 1, 'python': 2}


# after we add lower method
cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)
# {'python': 3}

print(cloud["python"])
# 3


cloud["python"] = 10
print(cloud.tags)
# {'python': 10}


print(len(cloud))
# 1

for tag in cloud:
    print(tag)

# python
