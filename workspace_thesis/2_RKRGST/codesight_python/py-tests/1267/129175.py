n=0
k=1
while 0<=n<=1000:
    n=int(input())
    if n!=0:
        if n<=1000:
            if n>0:
                for i in range(n):
                    k=k+2
                else:
                    print(k)
                    k=1
                    n=0
    else:
            print(1)