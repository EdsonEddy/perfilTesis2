n=int(input())
c=1
while c!=(n+1):
    for j in range(1,n+1,1):
        print(str(c)+"/"+str(j) )
        if j==n:
            c=c+1