import re


## ^ corresponde ao inicio da string
## $ corresponde ao final

sentence = 'Start a sentence and then bring it to an end'

padrao = re.compile(r'end$')
padrao = re.compile(r'^Start')  #  Start

matches = padrao.finditer(sentence)
for match in matches:
    print(match)