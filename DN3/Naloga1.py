
from datetime import datetime
  
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

year = int(year)
month = int(month)

def emso_leta_preracun():
    emso = input("Vnesi emšo:")
    byear = emso[4:7] #izberemo stevilke od 4 do 7 elementa
    if byear[0] == '9': #ce je 0. element enak 9 postavi spredaj se 1 oziroma ce ni postavi 2
       byear = '1' + byear
    else:
       byear = '2' + byear

    a = int(byear)#pretvorimo str v int

    bmonth = emso[2:4]#mesec od 2. do 4. elementa  
    b = int(bmonth)

    if(a<year):  #funkcija za racunanje trenutnega leta in meseca od nase letnice
       if(b<=month):
        x = year - a
        y = month - b
        print(f"Star si {x} in {y} mesecev")

    else:
        x = (year - a)-1
        y = 12 -(b - month)
        print(f"Star si {x} in {y} mesecev")

emso_leta_preracun()



    





       



    










