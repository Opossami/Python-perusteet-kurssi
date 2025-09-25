print("Anna käyttäjätunnus?")
tunnus = input("Käyttäjätunnus: \n")
print("Anna salasana?")
salasana = input("Salasana: \n")
raja = 0
while raja < 5:
    if tunnus != "python" or salasana != "rules":
        print(f"Anna käyttäjätunnus? {raja}")
        tunnus = input("Käyttäjätunnus: \n")
        print(f"Anna salasana?{raja}")
        salasana = input("Salasana: \n")
        raja = raja + 1
    if tunnus == "python" and salasana == "rules":
       print("Tervetuloa!")
       break


else:
    print("Pääsy evätty!")


