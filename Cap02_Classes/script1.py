#!/usr/bin/env python

# -*-coding:utf-8 -*-

# Classes OOP
# definir classe - modelo
class Empregados:

    # variavel de classe
    aumento = 1.04
    numero_colaboradores = 0

    #construtor de classe
    def __init__(self, nome, sobrenome, salario, empresa):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.empresa = empresa
        self.email = nome.lower() + '.' + sobrenome.lower() + '@' + empresa.lower() + '.com'

        Empregados.numero_colaboradores += 1

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def aumento_sal(self):
        self.salario = int(self.salario * Empregados.aumento)

    def aumento2_sal(self):
        e = Empregados.aumento + 0.01
        self.salario = int(self.salario * e)


print(Empregados.numero_colaboradores)

# Instancia de classe(objeto)
emp_1 = Empregados('Fabio','Classo', 5000, 'FloripaCodeGurus')

emp_2 = Empregados('Giovanna', 'Classo', 6000, 'FloripaCodeGurus')

print(emp_1.nome)
print(emp_1.salario) # antes do aumento
emp_1.aumento_sal()
print(emp_1.salario) # depois do aumento
# print(emp_1.sobrenome)
# print(emp_1.empresa)
# print(emp_1.nome_completo())
#print(emp_1.__dict__)
print()

print(emp_2.nome)
print(emp_2.salario)
emp_2.aumento_sal()
print(emp_2.salario)
# print(emp_2.sobrenome)
# print(emp_2.salario)
# print(emp_2.empresa)
# print(emp_2.email)
#print(emp_2.nome_completo())
#print(Empregados.nome_completo(emp_2))

print()
emp_3 = Empregados('John', 'Doe', 8000, 'Eng Soft')
print(emp_3.nome)
print(emp_3.salario)
emp_3.aumento2_sal()
#print(emp_3.__dict__)
print(emp_3.salario)

print(Empregados.numero_colaboradores)