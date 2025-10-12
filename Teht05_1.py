import random

nopat = int(input("Anna heitettävien noppien määrä: "))
summa = 0

for x in range(0, nopat):
    summa = summa + (random.randint(1,6))

print(summa)