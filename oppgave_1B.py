#Oppgave 1.B

student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favourite course": "Programmering 1"
}

# 1. Skriv ut studentens fullstendige navn
print(student["first name"], student["last name"])

# 2. Endre favorittkurs med emnekode
student["favourite course"] = "ITF10219 Programmering 1"

# 3. Legg til alder
student["age"] = 20

print(student)