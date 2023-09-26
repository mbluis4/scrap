import requests
import bs4
from pathlib import Path

tucson_html = 'https://tienda.tucsonsa.com/sanitarios/?mpage=14'

res = requests.get(tucson_html)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(soup))
tucson_file = open('tucson.txt', 'wb')

for chunk in res.iter_content(100000):
    tucson_file.write(chunk)
tucson_file.close()
