data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

def najvecja_vrednost(data):
    najvecja_vrednost_prices = data["prices"] 
    a = max(najvecja_vrednost_prices) #shranimo najvecjo vrednost v a iz kljuca prices
    najvecja_vrednost_volume = data["volume"]
    b = max(najvecja_vrednost_volume)#shranimo najvecjo vrednost v b iz kljuca volume
    najvecja_vrednost = [a,b] #sharnimo v spremenlijvko list
    vrednosti = najvecja_vrednost
    print(vrednosti)
najvecja_vrednost(data)


