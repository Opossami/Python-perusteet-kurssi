nimet = set()

nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimi = input("Anna nimi: ")
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
        nimi = input("Anna nimi: ")



else:
    for nimi in nimet:
        print(nimi)

