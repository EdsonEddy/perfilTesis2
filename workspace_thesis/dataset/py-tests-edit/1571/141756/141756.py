import sys
for n in sys.stdin:
    n = int(n)
    v = list(map(int,input().split()))
    cont = 0
    for i in range(1,len(v)-1):
        if v[i-1]<v[i] and v[i+1]<v[i]:
            cont = cont+1
        elif v[i-1]>v[i] and v[i+1]>v[i]:
            cont = cont+1
        else:
            continue
    print(cont)
