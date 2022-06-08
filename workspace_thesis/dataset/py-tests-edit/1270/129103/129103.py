x=int(input())
while x>0:
    n=int(input())
    s=""
    if n>1:
        if (n%2)==1:
            for i in range(1,n,2):
                s=s+str(8)
                i+=i
            print(str(4)+s)

        if (n%2)==0:
            for i in range(1,n,2):
                s=s+str(8)
                i+=i
            print(s)
    if n==1:
        print(0)
    if n==0:
        print(1)
    x-=1
