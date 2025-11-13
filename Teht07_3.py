lentokentät = {"EFKH":"Helsinki",
               "LHBP":"Budapest"}

def lisäys(icao, kaupunki):
    lentokentät[icao] = kaupunki
    print(f"Lisätty {icao} = {kaupunki}")
    return

def etsi(icao):
    print(lentokentät.get(icao, "Koodia ei löytynyt"))
    return

print("Haluatko hakea (haku) vai lisätä (lisätä) kentän ICAO koodilla vai haluatko lopettaa (lopeta)?")
vastaus = input().lower()

while vastaus != "lopeta":
    if vastaus == "lisätä":
        icao = input("Anna lisättävä ICAO koodi:")
        kaupunki = input("Anna lisättävä kaupunki: ")
        lisäys(icao, kaupunki)

    elif vastaus == "haku":
        icao = input("Anna haettava ICAO koodi?: ")
        etsi(icao)
    else:
        print("Tuntematon komento, käytä haku, lisätä tai lopeta.")
    vastaus = input("Haluatko hakea, lisätä vai lopettaa?: ").lower()


print("Hyvästi")