n=13
if (n>10):
    while (n!=1):
        p=n%10
        d=n//10
        n=p**2+d**2
        if (n==1):
            print (n)
            break
else:
    s = n * n
    while (s!=1):
        p=s%10
        d=s//10
        s=p**2+d**2
        if (s==1):
            print (s)
        else:
            print ("infeliz")
            break