import sys

def teste_unitario(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():

    teste_unitario(is_palindrome("abba"))
    teste_unitario(not is_palindrome("abab"))
    teste_unitario(is_palindrome("aaa"))
    teste_unitario(is_palindrome(""))
    teste_unitario(not is_palindrome("ab"))

def is_palindrome(str):
    l = list(str)
    a = []
    for i in range(len(l)):
        a.append(l[i])
    l.reverse()
    if a == l:
        return True
    else:
        return False

testes()