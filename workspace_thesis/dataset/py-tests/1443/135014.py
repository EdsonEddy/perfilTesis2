import sys
for c in sys.stdin:
    s=0
    n=int(c)
    if(n>=1 and n<=100):
        for i in range(1,n):
            d=n%i
            if(d==0):
                s=s+i
        #print(s)
        if(s<n):
            print("Deficiente")
        elif(s==n):
            print("Perfecto")
        elif(s>n):
            print("Abundante")