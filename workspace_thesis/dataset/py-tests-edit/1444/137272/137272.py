a=int(input())
for i in range(1,a+1):
    n=int(input())
    a=bin(n)
    c=a.count('11')
    print(c)