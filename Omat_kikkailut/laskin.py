# osaispa paremmin
print("anna numero")
numero =input()
from errno import ELOOP
print("Haluatko lisätä vai vähentää siitä?")
vastaus =input()
if  vastaus == "lisätä":
    print("Mitä haluat lisätä siihen?")
numero2 =input()
numero2 = float(numero2)
print(numero + numero2)
if vastaus == "vähentää":
    print("Mitä haluat siitä vähentää?")
numero3 =input()
numero3 = float(numero3)
print(numero - numero3)
elif vastaus == "lisätä" == "vähentää"
print("nyt en ymmärtänyt, voitko toistaa?")
ELOOP