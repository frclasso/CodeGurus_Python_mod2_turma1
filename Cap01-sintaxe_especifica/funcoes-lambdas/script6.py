

def make_increment(n):
    return lambda x: x + n

f = make_increment(45)
print(f(1))
print(f(2))
print(f(3))