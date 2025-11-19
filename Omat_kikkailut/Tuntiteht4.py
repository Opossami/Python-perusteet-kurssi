def osallistujat(sanakirja):
    kurssi = input("Anna kurssin nimi jonka osallistujamääräm haluat tietää: ")
    määrä = 0

    for nimi, kurssit in sanakirja.items():
        if kurssi in kurssit:
            määrä = määrä + 1

    return määrä



kurssilistat = {"Sami":["Matikan peruskurssi", "Liikunta", "Puukäsityöt"],
                "Antti":["Liikunta", "Suunnistus", "Puukäsityöt"],
                "Joonas":["Nepalin alkeet", "Pitkä puola", "Kahvinkeiton taito"],
                "Matias":["Maastavedon peruskurssi", "Pitkä lounas", "Kalenteroinnin taito"]}


nimi = input("Anna nimi: ")
kurssit = []

while True:
    kurssi = input("Anna seuraava kurssi: ")
    if kurssi == "":
        break
    kurssit.append(kurssi)

kurssilistat[nimi] = kurssit

oppilasmaara = osallistujat(kurssilistat)
print(f"Kurssille osallistuu {oppilasmaara} oppilasta.")

for nimi,kurssit in kurssilistat.items():
    print(nimi,"-", kurssit)