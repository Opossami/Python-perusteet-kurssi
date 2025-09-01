#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.
print("Antaisitko esineen massan keskiaikaisten mittojen mukaan niin muutan sen kiloiksi!")

leiviska = input("Kuinka monta leiviskää esine painaa?\n")
leiviska = float(leiviska)

naula = input("Kuinka monta naulaa esine painaa?\n")
naula = float(naula)

luoti = input("Kuinka monta luotia esine painaa?\n")
luoti = float(luoti)

#painot käännettyinä
aksiviel = float(leiviska * 20 * 32 * 13.3)
aluan = float(naula * 32 * 13.3)
ituol = float(luoti * 13.3)


gramma = ituol + aluan + aksiviel
kilo = gramma // 1000
grammat = gramma - kilo * 1000

print(f"No sehän painaa {kilo:3.0f} kiloa ja {grammat:3.0f} grammaa.")