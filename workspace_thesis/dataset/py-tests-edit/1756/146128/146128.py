
veces=int(input())
while veces>0:
    x=int(input())
    y=1
    x=x%6
    for i in range(x+1):
        y=y*2
        if y>=10:
            y=y%10+y//10
    print(y)
    veces-=1