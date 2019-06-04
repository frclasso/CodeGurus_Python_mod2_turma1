from numpy import *

alunos = array([
    ['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 88, 80, 90, 95],
])



# deletando linha
alunos = delete(alunos, [1], 0)  # axis=0
print(alunos)

# deletando coluna
alunos = delete(alunos, s_[1::2], axis=1)
print(alunos)