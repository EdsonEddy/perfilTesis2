y=int(input())
while y >0:
    n=int(input())
    s=""
    if n > 1:
        if(n%2)==1:
            for i in range(1,n,2):
                s=s+str(8)
                i = i+1
            print(str(4)+s)
        if n%2==0:
            for i in range(1,n,2):
                s=s+str(8)
                i = i+1
            print(s)
    if n ==1 :
        print(0)
    if n == 0:
        print(1)
    y-=1