n=int(input())
while n!=0:
    x=input().split()
    s=0
    for i in range(n):
        s=s+int(x[i])
    print(s)
    n=int(input())