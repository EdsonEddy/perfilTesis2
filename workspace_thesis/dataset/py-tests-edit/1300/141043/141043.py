from sys import stdin, stdout
c=0
for n in stdin:
    n=int(n)
    cad = input()
    v = cad.split(" ")
    for i in range(n):
        v[i]=int(v[i])
    for j in range(n):
        if v[j]==v[n-1]:
            c=c+1
    print(c)
    c=0