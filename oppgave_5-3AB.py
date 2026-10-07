
filmer = [
    {"name": "Inception",
     "year": 2020, # legger årstall som et heltall, i tilfelle vi ønsker å bruke det senere
    "rating": 8.7,
     },
    {"name": "Inside Out",
     "year": 2015,
    "rating": 8.1,
     },
    {"name": "Con Air",
     "year": 1997,
     "rating": 6.9},
]

def legge_til_filmer(liste_med_filmer,navn_på_film, # bruker et beskrivende funksjonsnavn
                     år_på_film, rating_til_film = 5.0):
    ny_film = {
        "name" : navn_på_film,
        "year" : år_på_film,
        "rating" : rating_til_film
    }
    liste_med_filmer.append(ny_film)

legge_til_filmer(filmer,"The Iron Giant",
                 1999, 8.1)

legge_til_filmer(filmer,"The Dark Knight",
                 2008,9.1)

legge_til_filmer(filmer,"Django Unchained",
                 2012,8.5)

legge_til_filmer(filmer,"Mad Max: Fury Road",
                 2015,)

def print_ut_filmer(liste_med_filmer):
    for film in liste_med_filmer:
        print(f"{film["name"]} - {film["year"]} has a rating of {film["rating"]}")

print_ut_filmer(filmer)

print()

def gjennomsnittsrating_filmer(liste_med_filmer):
    total_score = 0
    for film in liste_med_filmer:
        total_score += film["rating"]
    gjennomsnitt = total_score / len(liste_med_filmer)
    return(gjennomsnitt)
print(round(gjennomsnittsrating_filmer(filmer),2))
print()

def filmer_etter_2009(liste_med_filmer):
    ny_filmliste = []
    for film in liste_med_filmer:
        if film["year"] > 2009:
            ny_filmliste.append(film)
    return(ny_filmliste)

ny_liste = filmer_etter_2009(filmer)
print_ut_filmer(ny_liste)
print()
#---------------------------------------------------------
# oppgave 5.3 A

filnavn = 'movies.txt'

def legg_til_i_text(liste_med_filmer,filnavn):
    with open('movies.txt','w') as fil: # 'w' - write, 'a' - append, 'r' - read
        for film in liste_med_filmer:
            fil.write(
                f"{film["name"]} - {film["year"]} has a rating of {film["rating"]}\n"
            )

# oppgave 5.3 B

legg_til_i_text(filmer,"movies.txt")

def legg_til_i_text(filnavn):
    with open(filnavn, "r") as fil:
        for linje in fil:
            print(linje, end="")

legg_til_i_text("movies.txt")