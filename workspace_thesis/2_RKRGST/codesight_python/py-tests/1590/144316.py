from sys import stdin
def separar(n):
    sd = 0
    while n > 0:
        en = n % 10
        n = n // 10
        sd = sd + en
    return sd


v = [0] * 10010
for i in range(1, 10010 - 1):
    v[i] = separar(i)
for x in stdin:
    n, a, b = map(int, x.split())
    s = 0
    for i in range(1, n + 1):
        if a <= v[i] <= b:
            s += i
    print(s)