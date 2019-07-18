#!/usr/bin/env python3

# classes revisao


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
        self.salario = int(self.salario * self.aumento)

    @classmethod
    def set_novo_aum(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def from_string(cls, emp_str):
        nome, sobrenome, email, salario, empresa = emp_str.split('-')
        return cls(nome, sobrenome, email,salario, empresa)



# instaciar um objeto
#emp_1 = Empregados()
#emp_2 = Empregados()
# print(id(emp_1))
# print(id(emp_2))
# print()
#
# # atributos
# emp_1.nome = 'Fabio'
# emp_1.sobrenome = 'Classo'
# emp_1.email = 'fabioclasso@company.com'
# emp_1.salario = 5000
#
#
# emp_2.nome = 'Giovanna'
# emp_2.sobrenome = 'Classo'
# emp_2.email = 'giovannaclasso@company.com'
# emp_2.salario = 7000
#
# print(emp_1.email)
# print(emp_2.email)

emp_3 = Empregados('Peter', 'Parker','pparker@planetdaily.com', 3000, 'codegurus')
emp_4 = Empregados('Mary', 'Watson','mjwatson@planetdaily.com', 4000, 'codegurs')

print(emp_3.email)
print(emp_4.email)
print(emp_4.email_pro)
print(emp_4.nome_completo()) #acessando instancia
print(Empregados.nome_completo(emp_3))  # acessando via classe


# 3000 > 3120
# 4000 > 4160


print(Empregados.num_emps)
print(Empregados.aumento)
print(emp_4.aumento)
print(emp_3.aumento)

Empregados.set_novo_aum(1.05)
print(Empregados.aumento)
print(emp_4.aumento)
print(emp_3.aumento)

print(emp_3.salario)
emp_3.aumento_salario()
print(emp_3.salario)

print(emp_4.salario)
emp_4.aumento_salario()
print(emp_4.salario)

# verificar metodos e variaveis
#print(Empregados.__dict__)
#print(emp_4.__dict__)


# dados viessem desestruturados
emp_str_5 = 'John-Doe-jd@gmail.com-2000-Volvo'
emp_str_6 = 'Jane-Doe-jd@gmail.com-2000-Volvo'
emp_str_7 = 'Anna-Doe-Ad@gmail.com-2000-Volvo'
emp_str_8 = 'Mike-Doe-Md@gmail.com-2000-Volvo'


emp_5 = Empregados.from_string(emp_str_5)
emp_6 = Empregados.from_string(emp_str_6)
emp_7 = Empregados.from_string(emp_str_7)
emp_8 = Empregados.from_string(emp_str_8)

print(emp_5.email_pro)
print(emp_6.email_pro)
print(emp_7.email_pro)
print(emp_8.email_pro)
