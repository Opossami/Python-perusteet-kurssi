lentokentät = {"EFKH":"Helsinki, Helsinki-Vantaa",
               "LHBP":"Budapest, Ferenc Liszt",
               "EGLL":"London, Heathrow",
                "KLAX":"Los Angeles international",
               "LTFM":"Istanbul Airport",
               "RJTT":"Tokyo, Haneda Airport",
               "ZSPD":"Shanghai, Pudong International Airport",
               "LFPG":"Charles de Gaulle Airport",
               "KJFK":"New York, JFK International Airport"}

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
        icao = input("Anna lisättävä ICAO koodi:").upper()
        kaupunki = input("Anna lisättävä kaupunki: ")
        lisäys(icao, kaupunki)

    elif vastaus == "haku":
        icao = input("Anna haettava ICAO koodi?: ")
        etsi(icao)
    else:
        print("Tuntematon komento, käytä haku, lisätä tai lopeta.")
    vastaus = input("Haluatko hakea, lisätä vai lopettaa?: ").lower()


print("Hyvästi")