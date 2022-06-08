from sys import stdin
for n in stdin:
    n = int(n)
    s = input()
    v = s.split(" ")
    cont = 0
    for i in range(len(v)):
        if v[i]==v[n-1]:
            cont=cont+1
    print(cont)