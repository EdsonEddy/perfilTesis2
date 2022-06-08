n=int(input())
d=1
while d!=n+1:
    for i in range(1,n+1,1):
        print(str(d)+"/"+str(i))
        if i==n:
            d=d+1