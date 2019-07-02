#!/usr/bin/env python

# -*-coding:utf-8 -*-
class Empregados:

    aumento = 1.04
    numero_colaboradores = 0

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

    @classmethod
    def set_aumento(cls, aumento):  #cls => classe
        cls.aumento = aumento

    @classmethod
    def from_string(cls, emp_str):
        nome, sobrenome, salario,empresa = emp_str.split('-')
        return cls(nome, sobrenome, salario, empresa)


# Herança / Inheritance
class Developers(Empregados):
    pass


emp_1 = Empregados('Fabio','Classo', 5000, 'FloripaCodeGurus')
emp_2 = Empregados('Giovanna', 'Classo', 6000, 'FloripaCodeGurus')
print(Empregados.aumento)
print(emp_1.aumento)
print(emp_1.salario)
emp_1.aumento_sal()
print(emp_1.salario)
print()

Empregados.set_aumento(1.05)
print(Empregados.aumento)
print(emp_2.aumento)

print()
emp_str_3 = 'John-Doe-2000-testeempresa'
emp3 = Empregados.from_string(emp_str_3)
print(emp3.nome, emp3.sobrenome, emp3.salario, emp3.empresa)

emp_4 = Empregados('Jane', 'Doe', 4000, 'empresa')
emp_5 = Developers('Peter', 'Parker', 7000, 'Planet Diary')
print()
print(emp_4.nome_completo())
print(emp_5.nome_completo())
print(emp_5.salario)
emp_5.aumento_sal()
print(emp_5.salario)