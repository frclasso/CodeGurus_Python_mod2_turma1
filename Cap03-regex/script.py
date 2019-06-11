text_to_search="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha  HaHa

MetaCharacters (Need to be escaped \):
. ^ $ * + ? { } [ ] \ | ( )

codecla.com.br

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
"""

emails = """
FabioClasso@gmail.com
fabio.classo@codecla.edu
fabio-74-classo@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://codecla.com.br
"""

sentence = 'Start a sentence and then bring it to an end'
import  re
# print('Tab')
# print('\tTab')
# print(r'\tTab')
# padrao = re.compile(r'abc')
# ocorrencias = padrao.finditer(text_to_search)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)
#print(text_to_search[1:4])

# ponto(.)
# padrao = re.compile(r'.')

# \d - digitos[0-9]
# padrao = re.compile(r'\d')

# \w  - letras[a-zA-Z0-9]
#padrao = re.compile(r'\w')


# metacaracteres \
# padrao = re.compile(r'\$')
# ocorrencias = padrao.finditer(text_to_search)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

# qunatificadores
"""
    * 0 ou mais de um
    + 1 ou mais de um
    ? 0 ou 1
    {n} numero exato de ocorrencias
    {n, m} intervalo
"""

padrao = re.compile(r'\d{3}.\d{3}.\d{4}')
ocorrencias = padrao.finditer(text_to_search)
for ocorrencia in ocorrencias:
    print(ocorrencia)
print()

# grupos []

padrao = re.compile(r'[89]00.\d{3}.\d{4}')
ocorrencias = padrao.finditer(text_to_search)
for ocorrencia in ocorrencias:
    print(ocorrencia)

print()
"""FabioClasso@gmail.com
fabio.classo@codecla.edu
fabio-74-classo@my-work.net"""

# padrao = re.compile(r'[a-zA-Z0-9]+@[a-z0-9]+\.com')
#padrao = re.compile(r'[a-zA-Z0-9.]+@[a-z0-9]+\.(com|edu)')
padrao = re.compile(r'[a-zA-Z0-9.-]+@[a-z0-9-]+\.(com|edu|net)')
ocorrencias = padrao.finditer(emails)
for ocorrencia in ocorrencias:
    print(ocorrencia)