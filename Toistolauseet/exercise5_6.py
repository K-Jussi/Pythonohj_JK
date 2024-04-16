omadict = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Rikos, Draama",
    "duration": 154
}
print("{name}\n{year}\n{director}\n{genre}\n{duration}".format(*omadict, **omadict))
