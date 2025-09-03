kokonaisluku =int(input("Anna kokonaisluku?"))

if kokonaisluku % 3 == 0 and kokonaisluku % 5 == 0:
    print("BoomBuzz!")
elif kokonaisluku % 3 == 0:
    print("Boom!")
elif kokonaisluku % 5 == 0:
    print("Buzz")
