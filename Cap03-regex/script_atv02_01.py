"""
24/12/2018 		R$ 95.000,00
25/12/2018		R$10.000,00
28/12/2018		R$ 10.000,00
02/01/2018		R$ 5.000,00
03/01/2018		R$ 20.000,00
10/01/2018		R$ 25.000,00
14/01/2018		R$ 3.000,00
01/02/2019		R$ 47.000,00

12/24/2018 		US$ 95,000.00
12/24/2018		US$10,000.00
12/28/2018		US$ 10,000.00
01/02/2018		US$ 5,000.00
01/03/2018		US$ 20,000.00
01/10/2018		US$ 25,000.00
01/14/2018		US$ 3,000.00
02/01/2019		US$ 47,000.00
"""

import re

#padrao = re.compile(r'\d\d\/(01)\/\d{4}')   ## dias do mes de janeiro BR

#padrao = re.compile(r'(01)\/\d{2}\/\d{4}')  # janeiro em formato US

padrao = re.compile(r'\d(2|4|8|0)\/(1|0)(1|2)\/(2018)')  # dias pares BR

# dias  pares em US
# dias pares em BR exceto dia 10 - negação
# dias pares em US exceto dia 10
# todos os valores
# valores em Reais
# valores em dolar


with open('atv02_ex01.txt','r') as f:
    leitor = f.read()
    matches = padrao.finditer(leitor)
    for match in matches:
        print(match)