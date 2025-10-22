luvut = []

syote = input("Anna luku: ")

while syote != " ":
    luku =int(syote)
    luvut.append(luku)
    luku = input("Anna luku: ")

else:
    luvut.sort(reverse=True)
    print(luvut[:5])