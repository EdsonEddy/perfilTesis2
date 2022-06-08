n=int(input())
while n>0:
    x=int(input())
    while x>0:
        d=x%10
        x=x//10
        if d==6:
            d=x%10
            if d==9:
                print("APLAZADO!")
                break
        if x==0:
             print ("TE SALVAS :D")
    n=n-1