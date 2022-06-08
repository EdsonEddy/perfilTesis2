n=int(input())
while n>0:
    x = int(input())
    a=x
    s=0
    b=0
    while x>0:
        f=(x//10)*10
        dig=x-f
        x=x//10
        cd=0
        d=1
        while d<=dig:
            if dig % d == 0:
                cd=cd+1
            d=d+1
        if cd == 2:
            s=s+(dig*10**b)
            b+=1
    if s==0:
        print("-1")
    else:
        print(s)