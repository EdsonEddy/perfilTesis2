f=int(input())
for g in range(f):
    e=input()
    a=input().split()
    d=0
    for b in a:
        b=int(b)
        c=b*2
        if c%3==0:
            d=d+c
    print("La suma es",d)