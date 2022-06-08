import sys
for l in sys.stdin:
    k,t=map(int,l.split())
    s=k
    c=1
    cont=1
    if s==t:
            print(cont)
    else:
        while s<t:
                c=c*2
                s=s+(k*c)

                cont=cont+1
        print(cont)


