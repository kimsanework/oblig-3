import random

#ChatGPT
def skriv_tilfeldig_tall():
    tall = random.randrange(0, 101)

    print("*********")
    print("***" + str(tall) + "***")
    print("*********")


skriv_tilfeldig_tall()
skriv_tilfeldig_tall()
skriv_tilfeldig_tall()

#Copilot
def skriv_tilfeldig_tall():
    tall = random.randrange(0, 101)  # Tall mellom 0 og 100
    print("*********")
    print(f"***{tall}***")
    print("*********")

# Kall funksjonen flere ganger
skriv_tilfeldig_tall()
skriv_tilfeldig_tall()
skriv_tilfeldig_tall()
