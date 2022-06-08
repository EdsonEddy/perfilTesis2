n=int(input())
while n>0:
    num=int(input())
    p=1
    num=num%6
    for i in range(num+1):
        p=p*2
        if p>=10:
            p=p%10+p//10
    print(p)
    n-=1