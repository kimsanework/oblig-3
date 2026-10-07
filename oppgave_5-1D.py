# Oppgave 5.1 A
filmer = [
    {'name_1':'Inception','year_1': 2010,'rating_1': 8.7,
     'name_2':'Inside Out','year_2': 2015,'rating_2': 8.1,
     'name_3':'Con Air','year_3': 1997,'rating_3': 6.9}
]

print(filmer)
# Oppgave 5.1 B

def legg_til(filmliste,name, year, rating):
    film = {"name": name, "year": year, "rating": rating}
    filmliste.append(film)

legg_til(filmer,"The Iron Giant", 1999, 8.1)
legg_til(filmer,"The Dark Knight",2008,9.1)
legg_til(filmer,"Django Unchained", 2012,8.5)

print(filmer)
# Oppgave 5.1 C

#def add_movie(filmliste, name, year, rating=5.0):