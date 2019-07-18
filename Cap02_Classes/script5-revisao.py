

class Passaros:
    # variaveis de classes
    species = "birds"
    size = 'big'

    # construtor de classe
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # metodos de classe
    def sing(self, song):
        return "{}, sings: {}".format(self.name, song)

    def dance(self):
        return '{} is  now dancing'.format(self.name)


class marinhos(Passaros): # herança simples
    def __init__(self, name, age, oceano):
        super().__init__(name, age)
        self.oceano = oceano


class terrestres(Passaros):
    def __init__(self, name, age, velocidade):
        super().__init__(name, age)
        self.velocidade = velocidade


class duck(marinhos, terrestres):
    def __init__(self,name, age, oceano, velocidade):
        super().__init__(name, age, oceano)
        terrestres.__init__(velocidade=30)


print(help(duck))
d = duck('Donald', 30, 'Atalntico', '30km')



blue = Passaros('Blue', 10)
print(blue.sing("Oh Happy Day"))

woo = Passaros('Zé Carioca', 15)
print(woo.species)
print(woo.size)
print(woo.sing('Alo alo marciano'))
print(blue.dance())
print(woo.dance())
print(f'Blue tem {blue.age} anos de idade')
print(f'Ze Carioca tem {woo.age} anos de idade')

pinguim = marinhos('Pinguim', 20, 'Atlantico')
print(pinguim.name, pinguim.size, pinguim.species)
print(pinguim.oceano)

ema = terrestres('Ema', 12, '32km/h')
print(ema.name)
print(ema.velocidade)