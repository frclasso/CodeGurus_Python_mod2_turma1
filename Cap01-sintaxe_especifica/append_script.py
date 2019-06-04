from numpy import *

alunos = array([
    ['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95],
])


alunos = append(alunos, [['Sam', 82,79,88,97,99]], axis=0)
print(alunos)

"""axis=0 , representa as dimensoes 0 (zero) siginifica linha (row)
axis=1, coluna(column)"""