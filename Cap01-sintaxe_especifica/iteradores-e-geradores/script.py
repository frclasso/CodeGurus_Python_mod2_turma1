

my_list = [4,7,9,5,2]

# obtendo iterador
my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
#print(next(my_iter))  # Erro EOL StopIteration

print(my_iter.__next__())

while True:
    try:
        item = next(my_iter)
        print(f'Imprindo iteradores: {item}')
    except StopIteration:
        break