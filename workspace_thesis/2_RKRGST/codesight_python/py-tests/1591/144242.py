x=int(input())
for i in range(x):
    n=int(input())
    cad=""
    c=0
    l=len(str(n))
    while(n>0):
        d=n%10
        n=n//10
        if(d==2)or(d==3)or(d==5)or(d==7):
            s=str(d)
            cad=s+cad
        else:
            c=c+1
    if(c==l):
        print("-1")
    else:
        print(cad)