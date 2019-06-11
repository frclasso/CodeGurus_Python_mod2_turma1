alunos = [
    ['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95],
]

b = [
    [['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95],

]]

print(type(alunos))
print(type(b))

print(alunos[0][0])
print(alunos[1][0])
print(alunos[2][0])
print(alunos[-1])
print(alunos[-1][-2])
print(alunos[-2][-3])

alunos[2] = ['Sam', 82, 79, 88, 97, 99]
print(alunos)

alunos [0][4]=95
print(alunos)