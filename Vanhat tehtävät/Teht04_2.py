sentit = float(input("Anna tuumiksi muutettava senttimäärä: "))
while sentit > 0:
    tuumat = sentit / 2.54
    print(f"{tuumat}.")
    break

if sentit < 0:
    print(f"Hyvästi.")
