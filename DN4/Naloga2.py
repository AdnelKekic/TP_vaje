import math

n = int(input("Vnesi število elementov:"))#vnesemo število elementov
l = list() #naredimo list

for i in range(n):
    ele = int(input("Vnesi število:"))#vnesemo števila
    l.append(ele)

najmanjsi_element = min(l)
najvecji_element = max(l)

vsota_stevil = sum(l)#seštejemo vsa vpisana števila, da lahko potem izračunamo povprečje
povprecje = vsota_stevil/len(l) #računanje povprečja

def najblizje_stevilo(l,povprecje): #funkcija za iskanje števila najbližjega povprečju
    return l[min(range(len(l)), key = lambda i: abs(l[i]-povprecje))]


print ("Najmanjši element je:", najmanjsi_element)
print ("Največji element je:", najvecji_element)
print ("Povprečje števil je:", povprecje)
print ("Najbližje število povprečju je:", najblizje_stevilo(l,povprecje))


