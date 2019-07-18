#!/usr/bin/env python3

# Heranca

class Empregados: #definicao da classe

    num_emps = 0

    aumento = 1.04

    def __init__(self, nome, sobrenome, email, salario, empresa):  # construtor
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.salario = salario
        self.empresa = empresa
        self.email_pro = nome.lower() + '.' + sobrenome.lower() + '@' + empresa + '.com.br'

        Empregados.num_emps += 1

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def aumento_salario(self):
        self.salario = int(self.salario * Empregados.aumento)

    @classmethod
    def set_novo_aum(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def from_string(cls, emp_str):
        nome, sobrenome, email, salario, empresa = emp_str.split('-')
        return cls(nome, sobrenome, email,salario, empresa)


class Programadores(Empregados):  # herança / inheritance
    aumento = 1.10

    def __init__(self,  nome, sobrenome, email, salario, empresa, linguagem):
        super().__init__( nome, sobrenome, email, salario, empresa)
        self.linguagem_de_programacao = linguagem


class Gerente(Empregados):

    def __init__(self,  nome, sobrenome, email, salario, empresa, empregados=None):
        super().__init__(nome, sobrenome, email, salario, empresa)
        if empregados is None:
            self.empregados = []
        else:
            self.empregados = empregados

    def add_emp(self, emp):
        if emp not in self.empregados:
            self.empregados.append(emp)

    def exibe_funcionario(self):
        for emp in self.empregados:
            print(f'Funcionario sob minha gestao: {emp.nome_completo()}')


emp_1 = Empregados('Fabio', 'Classo', 'fabio@email.com', 6000, 'codegurus')
print(emp_1.email_pro)
emp_1.aumento_salario()
print(emp_1.salario)

dev_1 = Programadores('Peter', 'Parker', 'fabio@email.com', 6000, 'codegurus', 'Python')
print(dev_1.email_pro)
print(dev_1.linguagem_de_programacao)
print(dev_1.salario)
dev_1.aumento_salario()
print(dev_1.salario)

gen1 = Gerente('JJ', 'Jameson', 'jjm@planetdaily.com', 20000, 'Planet Daily',[dev_1])
print(gen1.email_pro)
print(gen1.exibe_funcionario())

print()
# verificar a origime , isntacia > classe
print(isinstance(gen1, Gerente))
print(isinstance(gen1, Programadores))
print(isinstance(gen1, Empregados))
print(isinstance(emp_1, Empregados))
print(isinstance(emp_1, Programadores))

# verificar a subclasse > classe
print(issubclass(Gerente, Empregados))  # correto ==> subclass, class
print(issubclass(Programadores, Empregados))
print(issubclass(Gerente, Programadores))
print(issubclass(Empregados, Gerente))
