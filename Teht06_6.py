import math
def pizzalaskuri(koko1, koko2, hinta1,  hinta2):
    voittaja = []
    Eka = hinta1 / ((koko1 / 2) ** 2 * math.pi)
    Toka = hinta2 / ((koko2 / 2) **  2 * math.pi)
    if Eka < Toka:
        voittaja.append("Eka")
        hinta = Eka
    else:
        voittaja.append("Toka")
        hinta = Toka
    return voittaja, hinta

hinta1 = float(input("Mitä maksaa ensimmäinen pizzavaihtoehto?: "))
koko1 = float(input("Kuinka iso on ensimmäinen pizzavaihtoehto?: "))
hinta2 = float(input("Mitä maksaa toinen pizzavaihtoehto?: "))
koko2 = float(input("Kuinka iso on toinen pizzavaihtoehto?: "))

voittaja, hinta = pizzalaskuri(koko1, koko2, hinta1, hinta2)
for item in voittaja:
    print(f"{item} pizza on halvempi, sillä se maksaa vain {hinta:.2f} neliöltä!")


