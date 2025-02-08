letters = ["a", "b", "c"]
print(letters.index("a"))
# 0

# letters = ["a", "b", "c"]
# print(letters.index("d"))
# ValueError: 'd' is not in list


letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))


letters = ["a", "b", "c"]
print(letters.count("d"))
# 0
