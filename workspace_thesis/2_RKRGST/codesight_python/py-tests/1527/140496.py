n=int(input())
for i in range(n):
    a=int(input())
    if 10**2<=a<=10**18:
        lis=str(a)
        lisd=lis.count("96")
        if int(lisd)>=1: 
            print("APLAZADO!") 
        else:
            print("TE SALVAS :D")