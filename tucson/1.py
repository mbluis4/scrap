
lineas = [
    'veneto',
    'bari',
    'andina',
    'marina',
    'espacio',
    'mayo',
    'trento',
    'hola soy'
]

prod_linea = ''
name1 = 'FERRUM ESPACIO ESPEJO INCLINABLE 60X80'
name2 = 'FERRUM MARINA INODORO CORTO'
name3 = 'hola soy luis alskdla aksdañlksd ñalskdñla'


def linea_tipo(name):
    for n in lineas:
        if n in name.lower():
            return n 
print(linea_tipo(name1))
print(linea_tipo(name2))
print(linea_tipo(name3))

