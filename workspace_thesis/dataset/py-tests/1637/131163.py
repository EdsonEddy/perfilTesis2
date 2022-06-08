a1,a2,a3=map(int,input().split())
l1,l2,l3=map(int,input().split())
i1=5-a1
i2=5-a2
i3=5-a3
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