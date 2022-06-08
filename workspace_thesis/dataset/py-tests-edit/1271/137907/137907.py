casos=int(input())
for j in range(casos):
    n=int(input())
    t=n
    s=0
    while(n>0):
        a=n%10
        n=n//10
        i=1
        f=1
        while(i<=a):
            f=f*i
            i=i+1
        s=s+f
    if(s==t):
        print("Y")
    else:
        print("N")