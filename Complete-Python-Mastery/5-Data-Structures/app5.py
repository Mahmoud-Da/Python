letters = ["a", "b", "c"]

letters.append("d")
print(letters)
# ['a', 'b', 'c', 'd']

letters.insert(0, "-")
print(letters)
# ['-', 'a', 'b', 'c', 'd']

letters = ['-', 'a', 'b', 'c', 'd']
letters.pop()
print(letters)
# ['-', 'a', 'b', 'c', 'd']

letters = ['-', 'a', 'b', 'c', 'd']
letters.pop(0)
print(letters)
# ['a', 'b', 'c', 'd']

letters = ['-', 'a', 'b', 'c', 'd']
letters.remove("b")
print(letters)
# ['-', 'a', 'c', 'd']

letters = ['-', 'a', 'b', 'c', 'd']
del letters[0]
print(letters)
# ['a', 'b', 'c', 'd']


letters = ['-', 'a', 'b', 'c', 'd']
del letters[0:3]
print(letters)
# ['c', 'd']

letters = ['-', 'a', 'b', 'c', 'd']
letters.clear()
print(letters)
# []
