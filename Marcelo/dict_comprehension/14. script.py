dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# dobrar valores

valorDobrado = {k:v *2 for (k, v) in dict1.items()}

print(valorDobrado)


chaveDobrada = {k * 2: v for (k, v) in dict1.items()}

print(chaveDobrada)


numbers = range(10)

new_dict_for = {}

for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2

print(new_dict_for)

# comprehension

new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}
print(new_dict_comp)