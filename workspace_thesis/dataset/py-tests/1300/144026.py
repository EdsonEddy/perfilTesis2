while 3>0:
    ls=int(input())
    a=input().split()
    b=a[ls-1]
    s=0
    for i in a:
        if i==b:
           s=s+1
    print(s)