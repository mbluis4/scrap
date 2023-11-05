import re

a = 'Precio $200.000,00 m2'

reg = re.compile(r'(\d*\.?\d+|\d{1,3}(.\d{3})*(\,\d+)?)')
f = reg.search(a).group()
print(f)
