from pprint import pprint

sentence = "This is a common interview question"
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
# {'T': 1, 'h': 1, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1, 'w': 1, 'q': 1, 'u': 1}

pprint(char_frequency, width=1)
# {' ': 5,
#  'T': 1,
#  'a': 1,
#  'c': 1,
#  'e': 3,
#  'h': 1,
#  'i': 5,
#  'm': 2,
#  'n': 3,
#  'o': 3,
#  'q': 1,
#  'r': 1,
#  's': 3,
#  't': 2,
#  'u': 1,
#  'v': 1,
#  'w': 1}

pprint(sorted(char_frequency.items()))
# [(' ', 5),
#  ('T', 1),
#  ('a', 1),
#  ('c', 1),
#  ('e', 3),
#  ('h', 1),
#  ('i', 5),
#  ('m', 2),
#  ('n', 3),
#  ('o', 3),
#  ('q', 1),
#  ('r', 1),
#  ('s', 3),
#  ('t', 2),
#  ('u', 1),
#  ('v', 1),
#  ('w', 1)]

pprint(sorted(char_frequency.items(), key=lambda kv: kv[1]))
# [('T', 1),
#  ('h', 1),
#  ('a', 1),
#  ('c', 1),
#  ('r', 1),
#  ('v', 1),
#  ('w', 1),
#  ('q', 1),
#  ('u', 1),
#  ('m', 2),
#  ('t', 2),
#  ('s', 3),
#  ('o', 3),
#  ('n', 3),
#  ('e', 3),
#  ('i', 5),
#  (' ', 5)]

pprint(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
# [('i', 5),
#  (' ', 5),
#  ('s', 3),
#  ('o', 3),
#  ('n', 3),
#  ('e', 3),
#  ('m', 2),
#  ('t', 2),
#  ('T', 1),
#  ('h', 1),
#  ('a', 1),
#  ('c', 1),
#  ('r', 1),
#  ('v', 1),
#  ('w', 1),
#  ('q', 1),
#  ('u', 1)]

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])
# ('i', 5)
