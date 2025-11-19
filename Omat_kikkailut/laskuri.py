print("-----Tervetuloa käyttämään laskinta!-----")

def summa(num1, num2):
    print("Yhteenlaskun tulos on:", num1 + num2)
    return

def vahennys(num1, num2):
    print("Vähennyslaskun tulos on:", num1 - num2)
    return

def kertolasku(num1, num2):
    print("Kertolaskun tulos on:", num1 * num2)
    return

def jakolasku(num1, num2):
    if b != 0:
        print("Jakolaskun tulos on:", num1 / num2)
    else:
        print("Nollalla ei voi jakaa")

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
        summa(a, b)
    elif valinta == "B":
        vahennys(a, b)
    elif valinta == "C":
        kertolasku(a, b)
    elif valinta == "D":
        jakolasku(a, b)
    else:
        print("Valintasi oli virheellinen")
