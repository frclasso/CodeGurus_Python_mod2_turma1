#!/usr/bin/env python3

# special methods

class Empregados:

    num_emps = 0

    aumento = 1.04

    def __init__(self, nome, sobrenome, salario, empresa):  # construtor
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.empresa = empresa
        self.email_pro = nome.lower() + '.' + sobrenome.lower() + '@' + empresa + '.com.br'

        Empregados.num_emps += 1

    @property
    def email(self):
        nome = self.nome.lower()
        sobrenome = self.sobrenome.lower()
        empresa  = self.empresa.lower()
        return '{}.{}@{}.com.br'.format(nome, sobrenome, empresa)

    @property
    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    @nome_completo.setter
    def nome_completo(self, nome):
        nome, sobrenome = nome.split()
        self.nome = nome
        self.sobrenome = sobrenome

    @nome_completo.deleter
    def nome_completo(self):
        print('Deletando nomes')
        self.nome = None
        self.sobrenome = None


    def aumento_salario(self):
        self.salario = int(self.salario * Empregados.aumento)

    @classmethod
    def set_novo_aum(cls, aumento):
        cls.aumento = aumento

    def __repr__(self):
        """Representacao - saida"""
        return "Empregado(Nome:{} {}, email:{}, R$ {}, empresa:{})".format(self.nome,
                                                      self.sobrenome,
                                                      self.email,
                                                      self.salario,
                                                      self.empresa)

    def __str__(self):
        return '{} {}'.format(self.nome_completo(), self.email_pro)


emp1 = Empregados('Fabio','Classo', 5000, 'CodeGurus')
# print(emp1.__repr__())
# print(emp1)
# print()
# print(repr(emp1))
# print(str(emp1))

print()
emp2 = Empregados('Peter', 'Parker', 2000, 'PlanetDaily')
# print(str(emp2))
# print(emp2.__str__())
#
# emp1.nome = 'Roger'
# print(emp1.nome_completo())

emp1.nome = 'Jose'
emp1.sobrenome = 'Wagner'
print(emp1.nome)
print(emp1.sobrenome)
print(emp1.email)
print(emp1.nome_completo)

emp1.nome_completo = 'Fabio Classo'
print(emp1.nome)
print(emp1.sobrenome)
