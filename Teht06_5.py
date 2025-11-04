def listajuttu(lista):
    funktiolista = []
    for item in lista:
        if item % 2 == 0:
            funktiolista.append(item)

    return funktiolista

lista =[]
muuttuja = input("Anna luku, käskyllä lopeta, jatketaan seuraavaan vaiheeseen:  ")

while muuttuja != "lopeta":
    numero = int(muuttuja)
    lista.append(numero)
    muuttuja = input("Anna luku, käskyllä lopeta, jatketaan seuraavaan vaiheeseen:  ")


if muuttuja == "lopeta":
    funktiolista = listajuttu(lista)
    print(lista)
    print(funktiolista)
