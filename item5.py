import sys

def teste_unitario(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():

    teste_unitario(conta(["john"]) == 1)
    teste_unitario(conta(["john", "sam"]) == 2)
    teste_unitario(conta(["john", "kevin", "sam", "mark", "sam"]) == 3)
    teste_unitario(conta(["sam"]) == 1)
    teste_unitario(conta([]) == 0)
    teste_unitario(conta(["sam", "sam", "sam"]) == 1)

def conta(l):
    count = 0
    flag = True
    while flag and count < len(l):
        if l[count] == "sam":
            flag = False
        count += 1
    return count

testes()

""" Quando nao sam, a funcao conta todos os elementos da lista
"""