def ver(n):
    while n>0:
        d=n%100
        n=n//10
        if d==96:
            return 1
    return 0


x=int(input())
for i in range(1,x+1):
    
    n=int(input())
    if ver(n)==1:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")
