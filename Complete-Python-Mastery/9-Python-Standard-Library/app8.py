import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)
# [{'id': 1, 'title': 'Terminator', 'year': 1989},
#  {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}]

# connection = sqlite3.connect("db.sqlite3")
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"

    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

# sqlite3.OperationalError: no such table: Movies

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)

    # (1, 'Terminator', 1989)
    # (2, 'Kindergarten Cop', 1993)

    movies = cursor.fetchall()
    print(movies)
    # [(1, 'Terminator', 1989), (2, 'Kindergarten Cop', 1993)]
