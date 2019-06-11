def echo_funcname(func):
    def interna(*args, **kwargs):
        print("Chamando a funcao: {}".format(func.__name__))
        return func(*args, **kwargs)
    return interna

@echo_funcname
def dobro(x):
    return x * 2

@echo_funcname
def triplo(x):
    return x * 3

@echo_funcname
def quadruplo(x):
    return x * 4

print(dobro(10))
print(triplo(10))
print(quadruplo(10))


