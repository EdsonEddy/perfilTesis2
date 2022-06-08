n=int(input())
for i in range(n):
    a=str(input())
    i=0
    c=0
    while i>=0:
        b=a.find("96",i)
        if b<0:
            break
        c=c+1
        i=b+1
    if c>=1:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")