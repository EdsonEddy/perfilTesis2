n=int(input())
for i in range(n):
    x=input()
    c=0
    i=0
    while i>=0:
        b=x.find("96",i)
        if b<0:
            break
        c=c+1
        i=i+1
    if c>0:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")