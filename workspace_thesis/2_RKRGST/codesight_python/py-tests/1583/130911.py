a=int(input())
for b in range(1,a+1):
    c=int(input())
    if c==1:
        d=int(input())
        print(d)
    elif c==2:
        d,e = map(int,input().split())
        x=0
        y=d
        z=e
        while (1>0):
            x=x+1
            d=d-1
            e=e-1
            if e==0 and d==0:
                print(x)
                break
            elif e==0 and d!=0:
                e=z
            elif d==0 and e!=0:
                d=y
    elif c==3:
        d,e,f=map(int,input().split())
        x=1
        while 1>0:
            if d%2==0 or e%2==0 or f%2==0:
                x=x*2
                if d%2==0:
                    d=d//2
                if e%2==0:
                    e=e//2
                if f%2==0:
                    f=f//2
            elif d%3==0 or e%3==0 or f%3==0:
                x=x*3
                if d%3==0:
                    d=d//3
                if e%3==0:
                    e=e//3
                if f%3==0:
                    f=f//3
            elif d%5 ==0 or e%5==0 or f%5==0:
                x=x*5
                if d%5==0:
                    d=d//5
                if e %5==0:
                    e=e//5
                if f%5==0:
                    f=f//5
            elif d%7 ==0 or e%7==0 or f%7==0:
                x=x*7
                if d%7==0:
                    d=d//7
                if e%7==0:
                    e=e//7
                if f%7==0:
                    f=f//7
            elif d%11 ==0 or e%11==0 or f%11==0:
                x=x*11
                if d%11==0:
                    d=d//11
                if e%11==0:
                    e=e//11
                if f%11==0:
                    f=f//11
            elif d%13 ==0 or e%13==0 or f%13==0:
                x=x*13
                if d%13==0:
                    d=d//13
                if e%13==0:
                    e=e//13
                if f%13==0:
                    f=f//13
            elif d%17 ==0 or e%17==0 or f%17==0:
                x=x*17
                if d%17==0:
                    d=d//17
                if e%17==0:
                    e=e//17
                if f%17==0:
                    f=f//17
            elif d%7 ==0 or e%7==0 or f%7==0:
                x=x*7
                if d%7==0:
                    d=d//7
                if e%7==0:
                    e=e//7
                if f%7==0:
                    f=f//7
            elif d%19 ==0 or e%19==0 or f%19==0:
                x=x*19
                if d%19==0:
                    d=d//19
                if e%19==0:
                    e=e//19
                if f%19==0:
                    f=f//19
            else:
                print(x*d*e*f)
                break
