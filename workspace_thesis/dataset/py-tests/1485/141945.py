from sys import stdin

for x in stdin:
    n = int(x)
    cont = 0
    for i in range(n):
        num = int(input())
        nc = num
        nn = ''
        while num > 0:
            dig = num % 10
            nn = nn + str(dig)
            num = num // 10
        if nc == int(nn):
            cont = cont + 1
    print(cont)