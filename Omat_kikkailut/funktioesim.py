def terve(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return

def yhteenlasku(_luku1, _luku2, _luku3):
    _summa = _luku1 + _luku2 + _luku3
    return _summa


luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

summa = yhteenlasku(luku1, luku2, luku3)

print("Lukujen summa on ", summa)