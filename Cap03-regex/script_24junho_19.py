import re

#padrao = re.compile(r'.')  # ponto
#padrao = re.compile(r'\w') # \w word caracters [a-zA-Z0-9]
#padrao = re.compile(r'\W') # \W No word caracters
#padrao = re.compile(r'\s') # \s corresponde a espaços \t, \n \s
#padrao = re.compile(r'\S') # \S corresponde  não espaços
#padrao = re.compile(r'\d') # \d decimais, corresponde [0-9]
#padrao = re.compile(r'\bHa') # \b caracter de borda (boundary)
#padrao = re.compile(r'\BHa') # \b caracter de nao borda (not boundary)
#padrao = re.compile(r'\.')  # meta caracters "\"
#padrao = re.compile(r'[a-zA-Z]')  # intervalo/range []
#padrao = re.compile(r'[a-z]')  # Negação

#321-555-4321

"""
    * - 0 ou mais de uma correspondencia
    + - 1 ou mais...
    ?  - 0 ou 1(opcional)
    {n} - numero exato de correspondencia
    {n, m} - minimo e maximo
"""

# grupos [grupo]

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#padrao = re.compile(r'\d{3}.\d{3}.\d{4}')
#padrao = re.compile(r'\d{3}[*-.]\d{3}[*-.]\d{4}')
#padrao = re.compile(r'[89]00[*-.]\d{3}[*-.]\d{4}')


"""  Mr. Schafer
     Mr Smith
     Mrs. Robinson
     Ms Davis
     Mr. T    
"""
## ( ) grupo -  | "pipe" and

#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

"""
FabioClasso@gmail.com
fabio.classo@codecla.edu
fabio-74-classo@my-work.net 
"""


padrao = re.compile(r'')


with open('snippets1.txt', 'r') as f:
    leitor = f.read()
    matches = padrao.finditer(leitor)
    for match in matches:
        print(match)


