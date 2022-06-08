n=int(input())
while n>0:
    Z,a,b=map(int,input().split())
    m = input().split()
    list(m)
    sumaa=0
    geg=m[a:b+1]
    for i in geg:
        sumaa= sumaa+int(i)
    print(sumaa)
    n-=1