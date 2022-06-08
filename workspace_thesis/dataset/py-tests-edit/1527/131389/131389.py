y=int(input())
for z in range(1,y+1):
    a=input()
    c=0
    x=1
    for b in a:
        c=str(c)
        d=c+b
        d=int(d)
        if(d==96):
            print("APLAZADO!")
            x=0
            break
        c=b
    if(x==1):
        print("TE SALVAS :D")