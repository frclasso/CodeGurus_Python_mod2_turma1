

def action(x):
    return lambda newX: x + newX

a = action(99)
print(a)
print(a(100))

action2 = lambda y:(lambda newY: y + newY)
a2 = action2(99)
print(a2)
print(a2(100))