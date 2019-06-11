

my_list = [1,3,6,10]

l = [x**2 for x in my_list]
print(l)


a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# print(lambda x: [x**2 for x in my_list])
