n=int(input())
o=str(8) #2
c=str(4) #1
for i in range(0,n,1):
        x=int(input())
        if 0<=x<=17:
            if x==1:
                print(0)
            elif x==0:
                print(1)
            elif x>1 and x>0:
                R=x%2
                r=x//2
                k=print((c*R)+(r*o))