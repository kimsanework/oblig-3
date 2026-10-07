# A) Oppretter en liste med filmer

filmer = [
    {
        "name": "Inception",
        "year": 2010,
        "rating": 8.7
    },
    {
        "name": "Inside Out",
        "year": 2015,
        "rating": 8.1
    },
    {
        "name": "Con Air",
        "year": 1997,
        "rating": 6.9
    }
]


# B og C) Funksjon som legger til en film
# rating har default-verdi 5.0

def add_movie(filmliste, name, year, rating=5.0):
    film = {
        "name": name,
        "year": year,
        "rating": rating
    }

    filmliste.append(film)


# B) Legger til 3 filmer med rating
add_movie(filmer, "The Dark Knight", 2008, 9.0)
add_movie(filmer, "Interstellar", 2014, 8.7)
add_movie(filmer, "The Matrix", 1999, 8.7)


# C) Legger til en film uten å oppgi rating
add_movie(filmer, "Titanic", 1997)


# Skriver ut filmene
print(filmer)