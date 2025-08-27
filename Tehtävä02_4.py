print("Jos kerrot minulle kolme kokonaislukua, lasken niistä sinulle summan, tulon ja keskiarvon!")
luku1 =input("Antaisitko ensimmäisen kokonaisluvun?:\n")
luku2 =input("Antaisitko toisen kokonaisluvun?:\n")
luku3 =input("Antaisitko kolmannen kokonaisluvun?:\n")

luku1 = int(luku1)
luku2 = int(luku2)
luku3 = int(luku3)

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"Lukujen summa on {summa}")
print(f"Tulo on {tulo}")
print(f"Keskiarvo on {keskiarvo}")