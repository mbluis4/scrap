from openpyxl import load_workbook

data = [['prueba', 'prueba','prueba', 'prueba',],
        ['prueba', 'prueba','prueba', 'prueba',],
        ['prueba', 'prueba','prueba', 'prueba',],
        ['prueba', 'prueba','prueba', 'prueba',]
        ]

wb = load_workbook(filename='1.xlsx')

ws = wb['fv']

for row in data:
    ws.append(row)
    print('saving..')

wb.save('2.xlsx')
