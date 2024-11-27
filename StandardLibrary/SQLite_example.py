import sqlite3
import json
from pathlib import Path

movies: list[dict] = json.loads(Path("./movies.json").read_text())
print(movies)

# For writing to the database which already has a table called movies and 3 columns
# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
