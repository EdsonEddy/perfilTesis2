x,y,z=map(int,input().split())
a,b,c=map(int,input().split())
h=5-x
i=5-y
j=5-z
if a==h:
    if b==i:
        if c==j:
            print("Esta es la llave")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
else:
    print("Intenta con otra")

