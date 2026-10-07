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


# Legger til tre filmer
add_movie(filmer, "The Dark Knight", 2008, 9.0)
add_movie(filmer, "Interstellar", 2014, 8.7)
add_movie(filmer, "The Matrix", 1999, 8.7)


# A) Skriver filmene til en fil
def write_movies_to_file(filmliste, filnavn):
    with open(filnavn, "w") as fil:
        for film in filmliste:
            fil.write(
                f"{film['name']} - {film['year']} has a rating of {film['rating']}\n"
            )


# B) Leser filen og skriver innholdet til terminalen
def read_movies_from_file(filnavn):
    with open(filnavn, "r") as fil:
        for linje in fil:
            print(linje, end="")


# Bruker funksjon A
write_movies_to_file(filmer, "movies.txt")

# Bruker funksjon B
read_movies_from_file("movies.txt")
print()

#------------ Copilot -------------

# Liste med filmer
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# A) Skriv filmer til fil
def skriv_filmer_til_fil(filmliste, filnavn):
    with open(filnavn, "w") as fil:
        for film in filmliste:
            linje = f"{film['name']} - {film['year']} has a rating of {film['rating']}\n"
            fil.write(linje)

# B) Les fra fil og skriv til terminal
def les_fil(filnavn):
    with open(filnavn, "r") as fil:
        innhold = fil.read()
        print(innhold)

# Test funksjonene
skriv_filmer_til_fil(filmer, "movies.txt")

print("Innholdet i movies.txt:")
les_fil("movies.txt")
