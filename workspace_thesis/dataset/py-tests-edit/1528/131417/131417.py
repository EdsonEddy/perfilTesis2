e=int(input())
for f in range(1,e+1):
    a=int(input())
    if(a>9876543210):
        print("NO!")
    else:
        a=str(a)
        c=9999999999999999
        d=0
        for b in a:
            b=int(b)
            if (b>=c):
                print("NO!")
                d=1
                break
            c=b
        if(d==0):
            print("SI!")