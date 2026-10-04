# i dette programmet kan brukeren velge egne inputs:
print("Regn ut volum av et tredimensjoanlt objekt! "
      "For å starte trenger vi noen inputs.")

def volum(lengde, bredde, høyde):
    return lengde * høyde * bredde

lengde = float(input("Skriv inn lengde: ")) # float, i tilfelle bruker ønsker desimaltall
bredde = float(input("Skriv inn bredde: "))
høyde = float(input("Skriv inn høyde: "))

resultat = volum(lengde, bredde, høyde)
print(f"Volumet av objektet er: {resultat}")

def volum_2(lengde, bredde, høyde): # denne funksjonen regner ut dobbel størrelse
    return (lengde * høyde * bredde)*2
resultat_2 = volum_2(lengde, bredde, høyde)
print(f'Fun fact: Et dobbelt så stort tredimensjonalt objekt ville vært: {resultat_2}')

def volum_3(lengde, bredde, høyde):# denne funksjonen regner ut halvparten av volum
    return (lengde * høyde * bredde)/2
resultat_3 = volum_3(lengde, bredde, høyde)
print(f'Fun fact: Et halvparten så lite tredimensjonalt objekt ville vært: {resultat_3}')


#--------- jeg la til dette etter at jeg så hvordan KI-løste oppgaven ----------
print()

volum_2 = volum(1,2,3)
volum_3 = volum(4,5,6)
volum_4 = volum(7,8,9)

print(volum_2)
print(volum_3)
print(volum_4)
