import math

def mult_table(n):
    l = range(n+1)
    for i in range(n+1):
        if i == 0:
            print(" ")
        elif i == 1:
            print("         1", end="")
        else:
            print("{0:4}".format(l[i]), end="")
    print("")
    lineBreaker = "    :-----"
    for i in range(1,n):
        lineBreaker = lineBreaker + "----"

    print(lineBreaker)

    for b in range(1, n+1):
        l = range(0, b*n + b, b)
        for i in range(n + 1):
            if i == 0:
                print("{0:4}:".format(b), end = "")
            elif i == 1:
                print("{0:5}".format(l[i]), end="")
            else:
                print("{0:4}".format(l[i]), end="")
        print("")



mult_table(12)