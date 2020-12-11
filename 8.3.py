import random


def calc_pi(n):
    k = 0
    i = 1

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            k = k+1
        else:
            i = i+1

    p = 4*k / n

    return p


pi = calc_pi(n=1000)
print(pi)
