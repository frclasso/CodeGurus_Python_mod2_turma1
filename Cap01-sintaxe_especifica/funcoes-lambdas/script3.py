

# usando as chaves de dicionario

key = 'quadratic'

print({
    'square':(lambda x:x **2),
    'cubic':(lambda x:x**3),
    'quadratic':(lambda x:x**4)}[key](10))

#
# l = lambda x:x**2
# l(10)