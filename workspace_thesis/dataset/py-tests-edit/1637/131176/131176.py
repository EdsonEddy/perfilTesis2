a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
i=5-a
x=5-b
k=5-c
if d==i:
    if e==x:
        if f==k:
            print("Esta es la llave")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
else:
    print("Intenta con otra")
