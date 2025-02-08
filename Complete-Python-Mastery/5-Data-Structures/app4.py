letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
# a
# b
# c


for letter in enumerate(letters):
    print(letter)
# (0, 'a')
# (1, 'b')
# (2, 'c')

for letter in enumerate(letters):
    print(letter[0], letter[1])
# 0 a
# 1 b
# 2 c

items = [0, "a"]
index, letter = items

items = (0, "a")
index, letter = items

for index, letter in enumerate(letters):
    print(index, letter)
# 0 a
# 1 b
# 2 c
