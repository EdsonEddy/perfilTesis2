x=int(input())
while x>0:
    y=int(input())
    e=1
    y=y%6
    for i in range(y+1):
        e=e*2
        while e>=10:
            e=e%10+e//10
    print(e)
    x-=1