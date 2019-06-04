from numpy import *

a = array([
    ['Roy', 80, 122, 85, 90, 95],
    ['Jonh', 80, 80, 75, 85, 100],
    ['Dave', 50, 80, 90, 95,100]])

print(type(a))

print(a)


print(a[:, [0, 1]])

print()
print(max(a[0,1:6]))

print(sort(a[0,1:6]))