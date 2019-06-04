#!/usr/bin/env python3
from numpy import *

# adicionando nova coluna

alunos = array([
    ['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95],
])

alunos = insert(alunos,[6], [[73], [80], [85]], axis=1)

# axis=1 coluna
print(alunos)