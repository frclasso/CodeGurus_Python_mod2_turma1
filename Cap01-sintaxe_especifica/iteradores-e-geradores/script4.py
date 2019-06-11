

# generator
def my_gen():
    n = 1
    print("Primeira ocorrencia")
    yield n

    n += 1
    print("Segunda ocorrencia")
    yield n

    n += 1
    print("Terceira ocorrencia")
    yield n

    n += 1
    print("Quarta ocorrencia")
    yield n


a = my_gen()
#print(next(a))
#print(next(a))
# print(next(a))
# print(next(a))

for n in my_gen():
    print(n)