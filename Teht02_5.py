#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.
print("Antaisitko esineen massan keskiaikaisten mittojen mukaan niin muutan sen kiloiksi!")

leiviska = input("Kuinka monta leiviskää esine painaa?\n")
leiviska = int(leiviska)

naula = input("Kuinka monta naulaa esine painaa?\n")
naula = int(naula)

luoti = input("Kuinka monta luotia esine painaa?\n")
luoti = int(luoti)

aksiviel = leiviska * 20 * 32 * 13,3
aluan = naula * 32 * 13,3
ituol = luoti * 13,3

paino = ituol + aluan + aksiviel

print(f"Antamasi esine painaa kiloissa {paino} grammaa.")