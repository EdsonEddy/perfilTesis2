a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
i=5-a
f=5-b
k=5-c
if x==i:
    if y==f:
        if z==k:
            print("Esta es la llave")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
else:
    print("Intenta con otra")