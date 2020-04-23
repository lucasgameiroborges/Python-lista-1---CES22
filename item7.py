import sys

def teste_unitario(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():

    teste_unitario(sum_of_squares([2, 3, 4]) == 29)
    teste_unitario(sum_of_squares([-2, -3, 4]) == 29)
    teste_unitario(sum_of_squares([]) == 0)
    teste_unitario(sum_of_squares([0, 1]) == 1)

def sum_of_squares(l):
    a = 0
    for i in range(len(l)):
        a += l[i] ** 2

    return a

testes()

