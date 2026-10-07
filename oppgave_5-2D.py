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
print()

#-------- Copilot -----------

# Liste med filmer
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# Funksjon for å legge til film
def legg_til_film(filmliste, name, year, rating=5.0):
    film = {
        "name": name,
        "year": year,
        "rating": rating
    }
    filmliste.append(film)

# Legg til noen filmer
legg_til_film(filmer, "Interstellar", 2014, 8.6)
legg_til_film(filmer, "The Dark Knight", 2008, 9.0)
legg_til_film(filmer, "Avatar", 2009, 7.9)
legg_til_film(filmer, "Frozen", 2013)  # Får rating 5.0

# A) Skriv ut alle filmer
def print_filmer(filmliste):
    for film in filmliste:
        print(f"{film['name']} - {film['year']} has a rating of {film['rating']}")

print("Alle filmer:")
print_filmer(filmer)

# B) Beregn gjennomsnittsrating
def gjennomsnitt_rating(filmliste):
    total = 0
    for film in filmliste:
        total += film["rating"]
    return total / len(filmliste)

snitt = gjennomsnitt_rating(filmer)
print(f"\nGjennomsnittsrating: {snitt:.2f}")

# C) Finn filmer fra og med et gitt år
def filmer_fra_aar(filmliste, aar):
    ny_liste = []

    for film in filmliste:
        if film["year"] >= aar:
            ny_liste.append(film)

    return ny_liste

filmer_2010 = filmer_fra_aar(filmer, 2010)

print("\nFilmer fra og med 2010:")
print_filmer(filmer_2010)