print("-----Tervetuloa käyttämään laskinta!-----")

while True:
    print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n"
          " C: Kertolasku \n D: Jakolasku")
    valinta = input("Valintasi: (A - D), Q lopettaa: ").upper()

    if valinta == "Q":
        print("Ohjelma lopetaan, kiitos hei!")
        break

    a = float(input("Anna esimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        print("Yhteenlasku:", a + b)
    elif valinta == "B":
        print("Vähennyslasku:", a - b)
    elif valinta == "C":
        print("Kertolasku:", a * b)
    elif valinta == "D":
        print("Desimaalijakolasku:", a / b)
    else:
        print("Valintasi oli virheellinen")
