# Liste med filmer

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


# Funksjon som legger til en film

def add_movie(filmliste, name, year, rating=5.0):
    film = {
        "name": name,
        "year": year,
        "rating": rating
    }

    filmliste.append(film)


# Legger til flere filmer

add_movie(filmer, "The Dark Knight", 2008, 9.0)
add_movie(filmer, "Interstellar", 2014, 8.7)
add_movie(filmer, "The Matrix", 1999, 8.7)
add_movie(filmer, "Titanic", 1997)


# A) Funksjon som skriver ut alle filmer

def print_movies(filmliste):
    for film in filmliste:
        print(f"{film['name']} - {film['year']} has a rating of {film['rating']}")


print_movies(filmer)


# B) Funksjon som regner ut gjennomsnittsrating

def average_rating(filmliste):
    total = 0

    for film in filmliste:
        total += film["rating"]

    return total / len(filmliste)


gjennomsnitt = average_rating(filmer)

print("Gjennomsnittsrating:", gjennomsnitt)


# C) Funksjon som finner filmer fra og med et gitt år

def movies_from_year(filmliste, år):
    resultat = []

    for film in filmliste:
        if film["year"] >= år:
            resultat.append(film)

    return resultat


filmer_fra_2010 = movies_from_year(filmer, 2010)

print("Filmer fra og med 2010:")
print_movies(filmer_fra_2010)