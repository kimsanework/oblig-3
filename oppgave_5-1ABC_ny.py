# oppgave 5.1. A

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

# oppgave 5.1. B
def legge_til_filmer(liste_med_filmer,navn_på_film, # bruker et beskrivende funksjonsnavn
                     år_på_film, rating_til_film = 5.0):
    ny_film = {
        "namn" : navn_på_film,
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

# oppgave 5.1. C

for film in filmer:
    print(film)

