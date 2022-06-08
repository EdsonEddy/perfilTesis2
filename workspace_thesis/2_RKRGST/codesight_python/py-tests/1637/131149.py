c1,c2,c3=map(int,input().split())
l1,l2,l3=map(int,input().split())
altura=5
i=altura-c1
j=altura-c2
k=altura-c3
if l1==i:
    if l2==j:
        if l3==k:
            print("Esta es la llave")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
else:
    print("Intenta con otra")