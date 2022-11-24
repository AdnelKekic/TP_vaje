#definiramo l in u spremenljivke, kjer določimo najmanjšo in največjo vrednost
l = int(1)
u = int(50)

#funkcija za določanje glede na območje 1-50 in izpis praštevil
for num in range(l, u+1):
    if num > 1:

        for i in range(2, num):
            if num%i==0:
                break

        else:
            print(num)
