n=int(input())
for i in range (n):
    n2=int(input())
    x=input().split()
    s=0
    for j in x:
        d=int(j)
        if (d*2)%3==0:
            s=s+(d*2)
    print('La suma es',s)
