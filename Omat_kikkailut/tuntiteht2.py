nimi =str(input("Moi, mikä on nimesi? ")).lower()


if nimi == "matti":
    print("Seuraava, kiitos!")

else:
    maara = float(input("Montako keittoannosta? "))
    hinta = maara * 5.9
    print(f"Kokonaishinta on {hinta:.2f}!")
