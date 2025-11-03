import random

def noppa(maksimi):
        summa = random.randint(1, maksimi)
        print(summa)
        return summa

maksimi = int(input("Anna heitettävän nopan tahkojen määrä: "))

silmaluku = noppa(maksimi)

while silmaluku != maksimi:
    print(silmaluku)
    silmaluku = noppa(maksimi)

else:
    print(f"{maksimi} tuli")