sentit = float(input("Anna tuumiksi muutettava senttimäärä: "))
while sentit > 0:
    tuumat = sentit / 2.54
    print(f"{tuumat}.")
    sentit = float(input("Anna tuumiksi muutettava senttimäärä: "))

if sentit <= 0:
    print(f"Hyvästi.")
