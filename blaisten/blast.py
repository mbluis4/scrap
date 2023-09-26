import requests
import bs4
from openpyxl import Workbook

blais_ferrum_1 = 'https://www.blaisten.com.ar/buscapagina?fq=B%3a30&PS=150&sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&cc=25&sm=0&PageNumber=1'


blaisten_prices = [
    ['Descripción', 'Precio', 'Link']
]


response = requests.get(blais_ferrum_1)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
prod_name = soup.select('.product-name')
prod_price = soup.select('.final-price')
prod_link = soup.find('a', )


for name, price in zip(prod_name, prod_price):
    blaisten_prices.append([name.getText(), price.getText()])


wb = Workbook()

ws = wb.create_sheet('ferrum')

for row in blaisten_prices:
    ws.append(row)

wb.save('blaisten.xlsx')
