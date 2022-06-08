from sys import stdin
for n in stdin:
    n = int(n)
    for i in range(n):
        m,a,b = map(int,input().split(' '))
        c = input()
        c = c.split(" ")
        f = []
        for l in range(m):
            f.append(int(c[l]))
        print(sum(f[a:b+1]))