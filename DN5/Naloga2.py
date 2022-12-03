import requests #knjižnica requests

def get_api_data(url): 
    # dodajte kodo po zgornjih navodilih
# preizkusite na primerih

    koda = requests.get(url)
    if koda.status_code == 200: #ce je status koda enaka 200 vrni stran v json
        page = koda.json()

    else:
        page = 'false' #ce ni vrni false
    return page

data = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
print(data)

#https://jsonplaceholder.typicode.com/nedala/nedala vrne false