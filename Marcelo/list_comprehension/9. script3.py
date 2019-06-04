# loop alinhado

lista = []
for i in range(3):
    for j in range(3):
        lista.append((i, j))

print(lista)

# list comprehension

lista2 = [(i, j) for i in range(3) for j in range(3)]

print(lista2)

print('-' * 70)

numList = []
for x in [10, 20, 30]:
    for j in [2, 4, 6]:
        numList.append(x * j)

print(numList)

numList2 = [(x * j) for x in [10, 20, 30] for j in [2, 4, 6]]
print(numList2)