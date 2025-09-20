vertailukohta = input("Antaisitko kokonaisluvun?: ")
pienin = vertailukohta
suurin = vertailukohta
luku = input("Antaisitko seuraavan kokonaisluvun?: ")
while luku != "":
    luku = input("Antaisitko seuraavan kokonaisluvun?: ")
    if pienin > luku:
        pienin = luku
    if suurin < luku:
        suurin = luku

if luku == "":
    print(f"{pienin}, {suurin}")