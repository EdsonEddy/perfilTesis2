n=int(input())

for i in range(n):
    x=int(input())
    a=1
    b=0
    for j in range(x): 
        c=a+b
        a=b
        b=c
    print(c)