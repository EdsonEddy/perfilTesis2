n=int(input())
for i in range(1,n+1):
    x=int(input())
    a=bin(x)
    c=a.count('11')
    print(c)
