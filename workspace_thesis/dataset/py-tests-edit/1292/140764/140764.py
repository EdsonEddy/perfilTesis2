from sys import stdin
for n in stdin:
    n = int(n)
    if n==0:
        break
    else:
        f = []
        c = input()
        c = c.split(" ")
        s = 0
        for i in range(n):
            f.append(int(c[i]))
            s = s+f[i]
        print(s)