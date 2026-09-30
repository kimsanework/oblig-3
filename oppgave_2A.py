import random
# Oppgave 2.A – Funksjon - Tallgenerering

def gi_et_tilfeldig_tall():
    tilfeldig_tall = random.randrange(0,100)
    return tilfeldig_tall

gi_et_tilfeldig_tall()

print("********")
print(f"***{gi_et_tilfeldig_tall()}***")
print("********")
print()
print("********")
print(f"***{gi_et_tilfeldig_tall()}***")
print("********")
print()
print("********")
print(f"***{gi_et_tilfeldig_tall()}***")
print("********")


#
#  Oppgave 2.B
#
# Løs nå oppgaven over med hjelp fra KI. Filen med denne skal leveres
# ved siden av din egen. I teoridokumentet skriver du litt om forskjellene
# mellom din egenproduserte løsning og den KI-genererte løsningen. Nevn hvilken KI-løsning
# du brukte og hvilke instruksjoner/spørsmål du ga den.
#
# Tenk over: Klarte den å løse det på første forsøk (var koden kjørbar og virket det som forventet?)