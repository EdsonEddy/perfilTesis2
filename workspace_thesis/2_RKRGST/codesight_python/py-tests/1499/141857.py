import sys
for n in sys.stdin:
    n = int(n)
    v = list(map(int,input().split()))
    rel = []
    rel.append(-1)
    s = 'SI'
    for i in range(1,len(v)):
        if v[i-1]<v[i]:
            rel.append(-1)
        elif v[i-1]==v[i]:
            rel.append(0)
        else:
             rel.append(1)
        if rel[i-1]>rel[i]:
            s = 'NO'
            break
    print(s)