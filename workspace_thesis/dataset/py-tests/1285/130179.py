while(1>0):
    a=str(input())
    if(a==""):
        break
    b=0
    d=0
    e=0
    for c in a:
        b=b+1
        c=int(c)
        if(b%2==0):
            d=d+c
        else:
            e=e+c
    if(e==d):
        print("SI")
    else:
        print("NO")