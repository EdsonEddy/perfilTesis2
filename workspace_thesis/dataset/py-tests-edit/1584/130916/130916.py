n=0
while n!="":
    n=int(input())
    x=list(range(1,n))
    d=input().split()
    men=100000000
    may=0
    for i in d:
        k=int(i)
        if k<int(men):
            men=int(i)
        if k>int(may):
            may=int(i)
    r=int(may)-int(men)
    print(r)