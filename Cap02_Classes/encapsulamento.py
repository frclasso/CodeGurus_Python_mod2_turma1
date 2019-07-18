

class Computer:
    """Exemplo de encaosulamento"""

    def __init__(self):
        self.precoPublico =500  # publico
        self._precoProtect = 900 # protegido
        self.__maxprice = 1000  # protegido Private

    def valorDeVenda_1(self):
        print('Valor de venda do produto: {}'.format(self.precoPublico))


    def valorDeVenda_2(self):
        print('Valor de venda do produto: {}'.format(self._precoProtect))


    def valorDeVenda_3(self):
        print('Valor de venda do produto: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price




dell = Computer()
dell.valorDeVenda_1()
dell.precoPublico = 800
dell.valorDeVenda_1()

ibm = Computer()
ibm.valorDeVenda_2()
ibm.precoProtect = 950
ibm.valorDeVenda_2()

macbook = Computer()

macbook.valorDeVenda_3()
macbook.__maxprice = 3000
macbook.valorDeVenda_3()
