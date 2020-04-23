def sum(A, B):
    (x, y) = A
    (z, w) = B
    return (x + z, y + w)

X = (1, 2)
Y = (3, 4)

print("{0}".format(sum(X, Y)))