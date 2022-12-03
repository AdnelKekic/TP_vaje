import requests #knjiznica requests


def get_html(url):
    # dodajte kodo po zgornjih navodilih
    # preizkusite na primerih
    koda = requests.get(url)
    if koda.status_code == 200: #ce je status koda enaka 200 vrni stran v html
        page = koda.text

    else:
        page = 'false' #ce ni vrni false
    return page

page = get_html("https://www.youtube.com/")
print(page)