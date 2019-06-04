keys = ['a', 'b', 'c', 'd', 'e']

values = [100,200,300,400,500]

# Usando funcoes dict e zip
myDict = dict(zip(keys, values))
print(myDict)


# Dict comprehension
myDict2 = {k:v for(k,v) in zip(keys, values)}
print(myDict2)
