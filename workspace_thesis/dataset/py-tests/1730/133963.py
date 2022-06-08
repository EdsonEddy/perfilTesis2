n=int(input())
if n>10:
    while n!=1:
        p=n%10
        d=n//10
        n=p**2+d**2
        if n==1:
            print ("1")
            break
            
