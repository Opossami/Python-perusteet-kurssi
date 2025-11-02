tunnus = input("Anna käyttäjätunnus: \n")
salasana = input("Anna salasana: \n")
raja = 1
while raja <= 4:
    if tunnus != "python" or salasana != "rules":
        tunnus = input("Anna käyttäjätunnus: \n")
        salasana = input("Anna salasana: \n")
        raja = raja + 1
    if tunnus == "python" and salasana == "rules":
       print("Tervetuloa!")
       break
if raja >= 5:
    print("Pääsy evätty!")