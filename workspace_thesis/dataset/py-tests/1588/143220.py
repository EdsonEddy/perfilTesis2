x = int(input())
for j in range(x):
    p = int(input())
    n = [int(v) for v in input().split()]
    s = 0
    for i in range(p):
        m = n[i] * 2
        if m % 3 == 0:
            s = s + m
    print('La suma es', s)