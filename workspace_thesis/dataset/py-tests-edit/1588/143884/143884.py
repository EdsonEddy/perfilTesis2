n=int(input())
c=0
for i in range(1,n+1,1):
    a=int(input())
    h=list(map(int,input().split()))
    for k in h:
        if k%3==0:
            c=k*2+c
    print('La suma es',c)
    c=0
