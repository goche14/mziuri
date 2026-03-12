movie = {
    "name": "La Haine",
    "director": "Mathieu Kassovitz",
    "year": 1995,
    "genres": ("crime-drama","social thriler"),
    "actors": ["vincent cassel","hubert kounde","said taghamoui"]   
}

print(len(movie))
director = movie.get("director")
print(director)

del movie["year"]
print(movie)

movie.clear()

print(movie)