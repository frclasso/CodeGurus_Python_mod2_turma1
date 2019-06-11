#!/usr/bin/env python3


import re

# testando a origem de dados

# with open('atv02_ex01.txt', 'r') as file:
#     leitor  = file.readlines()
#     for linha in leitor:
        #print(linha, end='')


# comentem a parte de cima

padrao = re.compile(r'\d\d\/(01)\/\d{4}')  # corresponde a questão "a"

with open('atv02_ex01.txt', 'r', encoding='utf-8') as f:
    leitor = f.read()
    matches = padrao.finditer(leitor)
    for match in matches:
        print(match)

