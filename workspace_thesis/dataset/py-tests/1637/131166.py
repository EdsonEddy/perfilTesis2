c1,c2,c3=map(int,input().split())
l1,l2,l3=map(int,input().split())
i1=5-c1
i2=5-c2
i3=5-c3
if l1==i1:
    if l2==i2:
        if l3==i3:
            print("Esta es la llave")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
else:
    print("Intenta con otra")