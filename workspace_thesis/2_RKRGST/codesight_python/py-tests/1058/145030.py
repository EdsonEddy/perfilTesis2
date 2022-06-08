a=int(input())
for b in range (1,a+1):
    c=int(input())
    d=input().split()
    f=[]
    h=[]
    for e in d:
        f.append(int(e))
    f.sort()
    for g in f:
        h.append(str(g))
    print(" ".join(h))