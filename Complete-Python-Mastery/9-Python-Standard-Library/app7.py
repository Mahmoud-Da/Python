import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]
data = json. dumps(movies)
print(data)

# [{"id": 1, "title": "Terminator", "year": 1989},
# {"id": 2, "title": "Kindergarten Cop", "year": 1993}]

Path("movies.json").write_text(data)


data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
# [{'id': 1, 'title': 'Terminator', 'year': 1989},
#  {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}]

print(movies[0])
# {'id': 1, 'title': 'Terminator', 'year': 1989}

print(movies[0]["title"])
# Terminator
