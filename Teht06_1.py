import random

def noppa():
        summa = random.randint(1,6)
        print(summa)
        return summa

silmaluku = noppa()

while silmaluku != 6:
    print(silmaluku)
    silmaluku = noppa()

else:
    print("Kutonen tuli")

