from pprint import pprint
import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Godfather", "release_year": 1972},
#     {"id": 1, "title": "Terminator", "release_year": 1984},
#     {"id": 1, "title": "Matrix", "release_year": 1999}
# ]

# data = json.dumps(movies)
# max_length = max(len(repr(d)) for d in movies) + 10
# pprint(data, width=max_length)

# For writing to a json file
# path = Path('./movies.json')
# path.write_text(data)

# To read from a json file
data = Path('./movies.json').open()
movies = json.loads(data.read())
print(movies)
data.close()

# Or
data = Path("./movies.json").read_text()
movies = json.loads(data)
print(movies)
