def primo(n):
    i = 1
    x = 0
    sp = []
    while i <= n:
        x += 1
        cd = 0
        for j in range(1, x + 1):
            if x % j == 0:
                cd = cd + 1
        if cd == 2:
            sp.append(x)
            i = i + 1
    return sp


def fibo(n):
    a, b = 0, 1
    sf = []
    for i in range(n):
        a, b = b, a + b
        sf.append(a)
    return sf


# Metodo Principal
from sys import stdin

for n in stdin:
    tp, tx = map(int, n.split())
    nf = fibo(tp)
    np = primo(tp)
    s = 0
    for j in range(tp):
        s = s + nf[j] / (np[j] * tx)
    print('{:.2f}'.format(s))