casos=int(input())
for i in range(casos):
    n=list(input().split(" "))
    nn=[]
    h=""
    for j in range(len(n)):
        d=n[j]
        s=""
        for x in d:
            s=x+s
        h=s+" "+h
        g=h[:-1]
    print(g)