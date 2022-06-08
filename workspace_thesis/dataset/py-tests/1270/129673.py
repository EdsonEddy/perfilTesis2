n=int(input())
for i in range(n):
    x=int(input())
    if 0<= x <= 17:
        if x == 0:
            print(1)
        else:
            if x == 1:
                print("0")
            else:
                y=0
                c=0
                z=x
                if z % 2 == 0:
                    while c < x:
                        c=c+2
                        y=(y*10)+8
                    print(y)
                else:
                    y=y+4
                    c=c+1
                    while c < x:
                        c=c+2
                        y=(y*10)+8
                    print(y) 