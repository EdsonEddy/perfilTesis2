from sys import stdin
for n in stdin:
    n = int(n)
    f = []
    c = input()
    c = c.split(" ")
    for i in range(n-1):
        f.append(int(c[i]))
    for j in range(1,n+1):
        if f.count(j)==0:
            print(j)
            break