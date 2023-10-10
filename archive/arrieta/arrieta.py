import requests, os, time
import bs4
import lxml
from openpyxl import Workbook, load_workbook
from data.lines import lines

tienda = 'Sanitarios Arrieta'

def get_page(brand):
    base_url = 'https://www.sanitariosarieta.com.ar/'
    urls = []
    prod_data = [
    ['Tienda', 'Marca', 'Linea', 'Nombre', 'Precio', 'Link', 'Cuotas' ],
    ]

    for web_page in range(0,36):
        if web_page == 0:
            urls.append(f'{base_url}{brand}_Desde_1_NoIndex_True')
            continue
        urls.append(f'{base_url}{brand}_Desde_{web_page*50+1}_NoIndex_True')   

    for page in urls:       
        try:
            response = requests.get(page)
            print(f'descargando desde {page}')
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            break
        print('parsing html')
        s = bs4.BeautifulSoup(response.text, 'lxml')
        if s.find_all('a') == []:
            print(f'end of {brand} pages')
            break
        prod_data += parse_page(s, brand)
    return prod_data
    

def parse_page(s, brand):
    page_data = []   
    for item in s.find_all(
            'div', class_='ui-search-result__content-wrapper shops__result-content-wrapper'):
        prod_link = item.find('a', href=True)
        prod_name = item.find('h2', class_='ui-search-item__title')
        prod_price = item.find(
            'span', class_='andes-money-amount__fraction')
        prod_cuotas = item.find('span', class_="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN")
         
        def line_type(name):
            for n in lines[brand]:
                if n.lower() in name.lower():
                    return n
        def get_cuotas(prod):
            if prod is None:
                return 0
            else:
                return prod.text.strip()
                     
        page_data.append([tienda, brand, line_type(prod_name.text.strip()), prod_name.text.strip(), 
                          int(prod_price.text.replace('.','').strip()), prod_link["href"], get_cuotas(prod_cuotas)])
    return page_data
    
# saving to excel file
def save_xls():

    brands = ['ferrum', 'fv', 'hidromet', 'peirano', 'vite', 'cerro', 'ilva', 'tendenza', 'alberdi', ]
    
    for brand in brands:
        data = get_page(brand)

        if 'Sanitarios Arrieta.xlsx' in os.listdir('.'):
            wb = load_workbook(filename='Sanitarios Arrieta.xlsx')
            ws = wb.active
            for row in data[1:]:
                ws.append(row)
            print('loading file...')
            print('saving to file...')
            wb.save('Sanitarios Arrieta.xlsx')
                
        else:        
            wb = Workbook()
            ws = wb.active
            ws.title = 'Sanitarios Arrieta'
            for row in data:
                ws.append(row)
            print('creating...')
            print('saving to file...')
            wb.save('Sanitarios Arrieta.xlsx')
        print('next page download in 5 seconds...')
        time.sleep(5)
  
    
save_xls()
