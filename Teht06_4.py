def listajuttu(lista):
    funktiolista = []
    for item in lista:
        funktiolista.append(item)
    summa = 0
    for item in funktiolista:
        summa = summa + item
    return summa

lista =[]
muuttuja = input("Anna luku, käskyllä lopeta, jatketaan seuraavaan vaiheeseen:  ")

while muuttuja != "lopeta":
    numero = int(muuttuja)
    lista.append(numero)
    muuttuja = input("Anna luku, käskyllä lopeta, jatketaan seuraavaan vaiheeseen:  ")


if muuttuja == "lopeta":
    summa = listajuttu(lista)
    print(summa)
