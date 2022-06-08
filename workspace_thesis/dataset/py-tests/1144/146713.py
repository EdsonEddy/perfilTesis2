import math


def prim(n):
    if n < 2:
        return False
    for i in range(2, (int(math.sqrt(n) + 1))):
        if n % i == 0:
            return False
    return True


cp = int(input())
for i in range(cp):
    x = int(input())
    xd = x+1
    xi = x-1
    su = 0
    while not prim(xd):
        xd += 1
    su += xd

    while not prim(xi):
        xi -= 1
    su += xi
    print(su)