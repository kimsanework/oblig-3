#Oppgave 1.A - Dictionaries
student = {
    "fornavn" : "Kim",
    "etternavn" : "Brarud",
    "favorittfag" : "Programmering 1"
}

print(student['fornavn'], student['etternavn'])

student['favorittfag'] = 'ITF10219 Programmering 1' # endrer verdien til nøkkelen "favorittfag"
student['alder'] = 33 # legger til nytt "nøkkel-verdi"-par

