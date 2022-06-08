n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split(" "))
    if a>1 and a<=100000 and b>1 and b<100000:
        if a<=b:
            for j in range(1,a):
                if a%j==0 and b%j==0:
                    c=j
        else:
            for j in range(1,b):
                if b%j==0 and a%j==0:
                    c=j
    print(c)