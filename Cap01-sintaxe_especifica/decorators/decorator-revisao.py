import time

# Definir um decorator

def calcula_duracao(funcao):
    # calcular o tempo de execucao da funcao passada como argumento
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print("[{funcao}] - Tempo total de execucao: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total = str(tempo_final - tempo_inicial))
        )
    return wrapper

@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

import math

@calcula_duracao
def fatorial():
    # vamos começar 1 seg depois
    time.sleep(1)
    print(math.factorial(10))

main()
fatorial()