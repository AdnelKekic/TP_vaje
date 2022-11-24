#Vnesi vsa števila
a = input("Prvo število:")
b = input("Drugo število:")
c = input("Tretje število:")

#Izpiši vrednost a in njen tip
print("a = " +str(a))
print(type(a))

#Izpiši vrednost b in njen tip
print("b = " +str(b))
print(type(b))

#Izpiši vrednost c in njen tip
print("c = " +str(c))
print(type(c))

#Primerjaj vrednosti a in b ter vrednosti a in c
if b==a and c<=a:
    print ("Pravilno")
else:
    print ("Napačno")



