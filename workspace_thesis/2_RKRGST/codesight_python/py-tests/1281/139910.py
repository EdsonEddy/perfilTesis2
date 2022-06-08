from sys import stdin
for line in stdin:
    n = int(line)
    l = [1]
    if 1 <= n <= 10**9:
        if n == 1:
            print('Divisores de 1: 1')
        else:
            print('Divisores de ' + str(n) + ': 1 ', end='')
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(i, end=' ')
                l.append(i)
        ini = len(l)-2 if n ** 0.5 == int(n ** 0.5) else len(l) - 1
        for i in range(ini, 0, -1):
            print(n//l[i], end=' ')
        if n != 1:
            print(n)
