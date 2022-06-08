n=int(input())
c=0
for i in range(1,n+1,1):
    b=int(input())
    for j in range(1,b+1):
        a=input()
        if a=='porque':
            c=j-1
    print(c)
