#Vnesi obe števili
Stevilo1 = float(input("Prvo število:"))
Stevilo2 = float(input("Drugo število:"))

#določitev funkcije za seštevanje
def add(s1,s2):
    sums = s1+s2
    return sums

Vsota = add(Stevilo1,Stevilo2)

#izpiši rešitev
print("Rešitev je:" +str(Vsota))
