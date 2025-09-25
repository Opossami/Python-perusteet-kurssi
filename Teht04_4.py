import random
arvattava = random.randint(1, 10)
print("Saatko arvattua arpomani numeron välillä 1-10?")
arvaus = int(input("Anna arvauksesi: "))
while arvaus != arvattava:
        if arvaus > arvattava:
            print("Liian suuri arvaus")
            arvaus = int(input("Arvaa uudestaan: "))
        if arvaus < arvattava:
            print("Liian pieni arvaus")
            arvaus = int(input("Arvaa uudestaan: "))
        if arvaus == arvattava:
            print("Oikein!")