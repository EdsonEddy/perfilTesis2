n=int(input())
for i in range(1,n+1,1):
    A=int(input())
    a=1
    b=0
    c=0
    if 1<=A<=200:
        for j in range(A):
            c=a+b
            a=b
            b=c
        print(c)
            
