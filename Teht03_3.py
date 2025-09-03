print("Anna biologinen sukupuolesi ja hemoglobiinisi")
sukupuoli =input("Sukupuoli?").lower()
hemoglob =int(input("Hemoglobiini?"))

if sukupuoli == "nainen":
    if hemoglob >= 176:
        print("Hemoglobiinisi on korkealla!")
    elif hemoglob <= 175 and hemoglob >= 117:
        print("Hemoglobiinisi on raja-arvojen piirissä!")
    elif hemoglob <= 116:
        print("Hemoglobiinisi on matalalla!")


if sukupuoli == "mies":
    if hemoglob >= 196:
        print("Hemoglobiinisi on korkealla!")
    elif hemoglob <= 195 and hemoglob >= 134:
        print("Hemoglobiinisi on raja-arvojen piirissä!")
    elif hemoglob <= 133:
        print("Hemoglobiinisi on matalalla!")

