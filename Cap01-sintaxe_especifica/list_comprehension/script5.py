import timeit

numbers = range(10)
new_list = []


def power_two(numbers):
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n ** 2)
    return new_list

print('Utilizando um Loop For')
print(timeit.timeit('power_two(numbers)', globals=globals(), number=10000))

print('Utilizando uma List Comprehension')
print(timeit.timeit('[n**2 for n in range(10) if n % 2 == 0]', number=10000))