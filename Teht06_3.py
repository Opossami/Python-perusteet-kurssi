def muunnin(gallonat):
    bensiini = gallonat * 3.785
    return float(bensiini)

gallonat = float(input("Anna litroiksi muutettava gallonamäärä: "))
bensiini = muunnin(gallonat)

while bensiini > 0:
    bensiini = muunnin(gallonat)
    print(bensiini)
    gallonat = float(input("Anna litroiksi muutettava gallonamäärä: "))
else:
    print("Adios!")
