luvut = []

luku = input("Anna luku: ")

while luku != "":
    luvut.append(luku)
    luku = input("Anna luku: ")

else:
    list(map(int, luvut))
    luvut.sort(reverse=True)
    print(luvut[:5])