from sys import stdin
for j in stdin:
    a,b=map(int,j.split())
    a=str(a)
    b=str(b)
    s=0
    for i in range(len(a)):
        c=a[i]
        d=b[i]
        if c!=d:
            s=s+1
    if s>1:
        print('lentes')
    else:
        print('feliz')