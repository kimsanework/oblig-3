def print_list(matretter):
    for mat in matretter:
        melding = f"{mat.title()} er godt!" # legger til en ekstra setning i utskrift
        print(melding)

favoritt_matretter = ['Hamburger','Lasagne','Pizza']
print_list(favoritt_matretter)

