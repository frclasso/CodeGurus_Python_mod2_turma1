
class Gerentes:
    """Exemplo de polimorfismo"""
    def encargos(self):
        print('Responsavel pela gerencia da loja')

    def horario(self):
        print("trabalha em horario comercial")


class Developers:
    def encargos(self):
        print('Responsavel pela desenvolvimento do codigo')

    def horario(self):
        print("trabalha em horario livre")

class Designers:
    def encargos(self):
        print('Responsavel pela aparencia do objeto')

    def horario(self):
        print("trabalha em horario dio-noturno")


# teste de interface comuns

def encargos_test(pessoa):
    pessoa.encargos()

def horario_test(pessoa):
    pessoa.horario()


lazaro = Gerentes()
encargos_test(lazaro)
horario_test(lazaro)

marcelo = Developers()
encargos_test(marcelo)
horario_test(marcelo)


cris = Designers()
encargos_test(cris)
horario_test(cris)