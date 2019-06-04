from numpy import *

a = array([
    ['Roy', 80, 75, 85, 90, 95],
    ['John', 17, 180, 175, 16, 199],
    ['Dave', 80, 80, 80, 90, 95]])


print(type(a))

print(a[:3,[0,1]])  #  :3 le as 3 linhas , depois da virgula [0,1] colunas

print(max(a[1,1:6]))
print(sorted(a[1,1:6]))

print(type(a[:3, [1,1]]))