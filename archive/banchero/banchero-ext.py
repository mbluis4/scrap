import requests
import bs4
from pathlib import Path

ht = 'https://www.tienda.bancherosanitarios.com.ar/ferrum'

res = requests.get(ht)


with open('banchero-prueba.html', 'wb+') as b:
    b.write(res.content)
    print('page saved')
