# Denne koden består av to forsøk på å løse oppgave 4A.
# Forsøk 1 - jeg prøvde å løse koden helt alene
print("Regn ut volum av et tredimensjoanlt objekt! "
      "For å starte trenger vi noen inputs.")

def volum(lengde, bredde, høyde):
    return lengde * høyde * bredde

lengde = float(input("Skriv inn lengde: ")) # float, i tilfelle bruker ønsker desimaltall
bredde = float(input("Skriv inn bredde: "))
høyde = float(input("Skriv inn høyde: "))

resultat = volum(lengde, bredde, høyde)
print(f"Volumet av objektet er: {resultat}")

def volum_dobbel(lengde, bredde, høyde): # denne funksjonen regner ut dobbel størrelse
    return (lengde * høyde * bredde)*2
resultat_2 = volum_dobbel(lengde, bredde, høyde)
print(f'Fun fact: Et dobbelt så stort tredimensjonalt objekt ville vært: {resultat_2}')

def volum_halv(lengde, bredde, høyde):# denne funksjonen regner ut halvparten av volum
    return (lengde * høyde * bredde)/2
resultat_3 = volum_halv(lengde, bredde, høyde)
print(f'Fun fact: Et halvparten så lite tredimensjonalt objekt ville vært: {resultat_3}')
print()

# forsøk 2 - "kodeorkester" i mentortimen, hvor studentene sammen jobbet for å løse oppgaven
def volum (bredde, lengde, høyde):
    mål = lengde * bredde * høyde
    return "volum = " + str(mål) # typecasting

print(volum(3,4,5))
print(volum(6,7,8))
print(volum(9,10,11))
