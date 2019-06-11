def smart_divide(func):
    def inner(a,b):
        print('I am going divide', a, "and", b)
        if b == 0:
            print("Ops, can not divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a /b


print(divide(20, 5))
print(divide(20, 0))