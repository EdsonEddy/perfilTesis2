n=int(input())
for i in range(n):
    x=int(input())
    s=0
    l=list(map(int,input().split()))
    for j in l:
        if j%3==0:
            s=s+j*2

    print('La suma es',s)
