n = int(input())
c=0
c2=0
d=0
N1=n
dN=0
if (n>=1 and n<=99999):


    while (n>0):
        c=c+1
        n=int(n/10)
        
    if (c%2==0):

        print("*")
    else:
        c=int(c/2)
        d=c+1

        while(c2<d):
            dN=N1%10
            N1=int(N1/10)
            c2=c2+1
        print(dN)    
        
