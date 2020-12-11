import math


def heron(a, b, c):
    if a + b <= c:
        raise ValueError('Nie można stworzyć trójkąta z tych boków')

    p = (a + b + c) / 2

    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return S


P = heron(3, 3, 4)
print(P)
