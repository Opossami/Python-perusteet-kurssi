luku = int(input("Anna luku: "))

if luku == 0 or luku == 1:
    print("Luku ei ole alkuluku")
elif luku > 1:
    for i in range(2,luku):
        if luku % i == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku!")
else:
    print("Luku ei ole alkuluku")
