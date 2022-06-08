t=0
c=3
n=int(input())
if 1<=n<=1000:
    if n==1:
        print(0)
    elif n!=0:
        r=n//3
        N=n%3
    if N==0:
        print(n)
    else:
        r=r+1
        for i in range(1,r,1):
            c=c*i
        print(c)