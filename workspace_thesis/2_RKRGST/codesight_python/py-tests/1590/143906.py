from sys import stdin
for k in stdin:
    a,b,c=map(int,k.split())
    s=0
    for i in range(a+1):
        h=str(i)
        v=0
        for j in h:
            v=v+int(j)


        if v>=b and v<=c:
            s=s+i
    print(s)
