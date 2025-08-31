kanta = input("Antaisitko suorakulmion kannan?\n")
kanta = float(kanta)
korkeus = input("Antaisitko vielä suorakulmion korkeuden?\n")
korkeus = float(korkeus)

print (f"Suorakulmion piiri on {kanta * 2 + korkeus * 2}")
print (f"Suorakulmion pinta-ala on {kanta * korkeus:.2f}")