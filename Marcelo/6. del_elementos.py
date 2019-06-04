from numpy import *

alunos = array([
    ['Roy', 80, 122, 85, 90, 95],
    ['Jonh', 80, 80, 75, 85, 100],
    ['Dave', 50, 80, 90, 95,100]
])

#  deletando linha
alunos = delete(alunos, [1], 0)  # axis

print(alunos)

print()

# deletando coluna
alunos = delete(alunos, [1], 1)  # axis

print(alunos)
