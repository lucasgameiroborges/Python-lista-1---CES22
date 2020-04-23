import sys
import math

def teste_unitario(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():

    teste_unitario(is_prime(2))
    teste_unitario(is_prime(3))
    teste_unitario(is_prime(11))
    teste_unitario(not is_prime(1))
    teste_unitario(not is_prime(22))
    teste_unitario(not is_prime(20000316))

def is_prime(n):
    a = True
    if n == 1:
        a = False
    else:
        for i in range(2, math.floor(n ** 0.5)):
            if n % i == 0:
                a = False
    return a
testes()

""" usando o teorema do numero primo, aproximadamente 5 alunos dos 100 (?)
"""