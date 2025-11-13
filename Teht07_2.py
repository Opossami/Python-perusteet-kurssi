nimet = set()

nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
        nimi = input("Anna nimi: ")

else:
    print(nimet)
