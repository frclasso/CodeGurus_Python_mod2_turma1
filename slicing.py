from numpy import *

a = array([
    ['Roy', 80, 75, 85, 90, 60],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95]])

print(type(a))
print(a[0:3,[0,1]]) # :3 le as 3 linhas, depois da virgula[0,1] colunas

print(max(a[1,1:6]))



