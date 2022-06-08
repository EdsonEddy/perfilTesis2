A=int(input())
while A>0:
    x=int(input())
    p=1
    x=x%6
    for i in range(x+1):
        p=p*2
        if p>=10:
            p=p%10+p//10
    print(p)
    A-=1