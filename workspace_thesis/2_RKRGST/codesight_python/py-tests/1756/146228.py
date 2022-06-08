casos=int(input())
while casos>0:
    num=int(input())
    x=1
    num=num%6
    for i in range(num+1):
        x=x*2
        if x>=10:
            x=x%10+x//10
    print(x)
    casos-=1