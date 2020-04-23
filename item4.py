import sys

def teste_unitario(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():

    teste_unitario(soma([3, 5, 8, 9, 10]) == 8)
    teste_unitario(soma([2, 5, 8, 9, 10]) == 0)
    teste_unitario(soma([3, 5, 7, 9, 1]) == 25)
    teste_unitario(soma([]) == 0)

def soma(l):
    s = 0
    count = 0
    flag = True
    while flag and count < len(l):
        if l[count] % 2 == 0:
            flag = False
        else:
            s += l[count]
        count += 1
    return s

testes()

""" Quando nao tem numero par, a funcao soma todos os elementos
"""