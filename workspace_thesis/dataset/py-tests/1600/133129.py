#Curiosesco
z = []


def  fac():
    v = [0]
    acum = 1
    for i in range(1, 10):
        acum *= i
        v.append(acum)
    return v


def sumdig(n):
    if n // 10 == 0:
        return z[n]
    else:
        return sumdig(n // 10) + z[n % 10]


n = int(input())
z = fac()
for i in range(n):
    intent = int(input())
    if intent == sumdig(intent):
        print('SI')
    else:
        print('NO')
